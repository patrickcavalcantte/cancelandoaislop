#!/usr/bin/env python3
"""Gera o podcast da página com Edge TTS.

Lê roteiro.json (exportado da própria página), sintetiza cada linha com a voz
indicada e junta tudo em podcast.mp3. Também grava linhas.json, com o instante
de início de cada linha, que a página usa para destacar o trecho em reprodução.

Uso (na pasta podcast/):
    pip install edge-tts mutagen
    python gerar_podcast.py

Precisa de internet, porque o Edge TTS usa o serviço de voz da Microsoft.
Linhas já sintetizadas ficam em .cache/, então dá para rodar de novo sem refazer tudo.
Se o texto da página mudar, exporte o roteiro de novo (veja o README) e rode outra vez.
"""
import argparse
import asyncio
import hashlib
import json
import pathlib
import sys

import edge_tts
from mutagen.mp3 import MP3

AQUI = pathlib.Path(__file__).resolve().parent
VOZES = {"A": "pt-BR-FranciscaNeural", "B": "pt-BR-AntonioNeural"}


def fnv1a(texto: str) -> str:
    """Mesmo hash da página, para ela recusar um mp3 de outra versão do texto."""
    h = 0x811C9DC5
    for byte in texto.encode("utf-8"):
        h ^= byte
        h = (h * 0x01000193) & 0xFFFFFFFF
    return format(h, "x")


async def sintetizar(linha: dict, cache: pathlib.Path, velocidade: str, sem: asyncio.Semaphore) -> pathlib.Path:
    voz = VOZES.get(linha["voice"], VOZES["A"])
    chave = hashlib.sha1(f"{voz}|{velocidade}|{linha['text']}".encode("utf-8")).hexdigest()
    destino = cache / f"{chave}.mp3"
    if destino.exists() and destino.stat().st_size > 0:
        return destino
    async with sem:
        for tentativa in range(1, 5):
            try:
                tmp = destino.with_suffix(".tmp")
                await edge_tts.Communicate(linha["text"], voz, rate=velocidade).save(str(tmp))
                if tmp.stat().st_size == 0:
                    raise RuntimeError("áudio vazio")
                tmp.replace(destino)
                return destino
            except Exception as erro:  # rede instável é o caso comum
                if tentativa == 4:
                    raise RuntimeError(f"linha {linha['id']}: {erro}") from erro
                await asyncio.sleep(2 * tentativa)
    raise AssertionError("inalcançável")


async def principal(args) -> None:
    roteiro = json.loads((AQUI / "roteiro.json").read_text(encoding="utf-8"))
    linhas = roteiro["linhas"]
    if args.limite:
        linhas = linhas[: args.limite]
    esperado = fnv1a("\n".join(f"{l['voice']}|{l['text']}" for l in roteiro["linhas"]))
    if esperado != roteiro["hash"]:
        sys.exit("roteiro.json foi editado à mão ou está corrompido (hash não confere).")

    cache = AQUI / ".cache"
    cache.mkdir(exist_ok=True)
    sem = asyncio.Semaphore(args.paralelo)
    partes = await asyncio.gather(*(sintetizar(l, cache, args.velocidade, sem) for l in linhas))

    inicios, t = [], 0.0
    with open(AQUI / "podcast.mp3", "wb") as saida:
        for arquivo in partes:
            inicios.append(round(t, 3))
            t += MP3(str(arquivo)).info.length
            saida.write(arquivo.read_bytes())

    meta = {"duration": round(t, 2), "starts": inicios, "hash": roteiro["hash"]}
    (AQUI / "linhas.json").write_text(json.dumps(meta), encoding="utf-8")
    print(f"{len(linhas)} linhas, {t/60:.1f} min. Gerado: podcast.mp3 e linhas.json")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--velocidade", default="+0%", help='ritmo da voz, por exemplo "+10%%" ou "-5%%"')
    ap.add_argument("--paralelo", type=int, default=4, help="sínteses simultâneas")
    ap.add_argument("--limite", type=int, default=0, help="só as N primeiras linhas, para teste")
    asyncio.run(principal(ap.parse_args()))
