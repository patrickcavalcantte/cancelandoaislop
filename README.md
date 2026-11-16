# cancelandoaislop

Guia para evitar AI slop em interfaces, imagens e textos em português gerados por IA.

## Arquivos

- `index.html`: a página "Como evitar AI SLOP", com os erros organizados por severidade e exemplos lado a lado.
- `NIELSEN.md`: as 10 heurísticas de Nielsen como regras para o agente. Vai na raiz do projeto.
- `ANTIPADROES.md`: 48 antipadrões, cada um com sinal e regra de correção.
- `PORTUGUES.md`: regras de português do Brasil e checklist de revisão.

## Como usar

Copie os arquivos `.md` para a raiz do seu projeto e importe no `CLAUDE.md`:

```
## Design
Antes de criar ou alterar qualquer interface,
leia @NIELSEN.md e @DESIGN.md.
Antes de entregar, revise contra @ANTIPADROES.md.

## Texto
Ao escrever qualquer texto em português,
siga @PORTUGUES.md.
```

Os exemplos e as severidades são julgamento do autor, sem medição. Confira nas suas saídas.
