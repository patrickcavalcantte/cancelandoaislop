# Podcast da página

A página toca `podcast.mp3` quando ele existe ao lado do `index.html`, na pasta `podcast/`. Sem o arquivo, ela usa a voz sintética do navegador.

## Gerar o mp3 com Edge TTS

Na pasta `podcast/`:

```
pip install edge-tts mutagen
python gerar_podcast.py
```

O script lê `roteiro.json`, sintetiza cada linha (voz feminina para o texto, masculina para as aberturas de seção e para os "Evite") e grava `podcast.mp3` e `linhas.json`. O `linhas.json` guarda o instante em que cada linha começa, e a página usa isso para destacar o trecho que está tocando e acompanhar no menu.

Precisa de internet, porque o Edge TTS usa o serviço de voz da Microsoft. Linhas já sintetizadas ficam em `.cache/`, então rodar de novo é rápido. Opções: `--velocidade "+10%"`, `--paralelo 4`.

## Se o texto da página mudar

`roteiro.json` guarda um hash do texto. Se a página mudar, a página recusa o mp3 antigo e volta para a voz do navegador. Para atualizar, exporte o roteiro de novo (abra a página e, no console, rode `copy(JSON.stringify({hash: window.__roteiroHash, linhas: window.__roteiro}, null, 1))`, cole em `roteiro.json`) e gere o mp3 outra vez.

Coloque `.cache/` no `.gitignore`. O `podcast.mp3` pode ir para o repositório, com cerca de 15 MB para 30 minutos.
