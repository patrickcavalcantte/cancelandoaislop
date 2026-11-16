# Heurísticas de Nielsen: regras para o agente

Use este arquivo ao criar ou revisar qualquer interface.
Antes de entregar, responda cada pergunta e corrija o que falhar.

## 1. Visibilidade do estado do sistema
- Todo carregamento, envio e conclusão tem feedback visível.
- A tela mostra onde o usuário está (item ativo, passo X de Y).
- Pergunta: o usuário sabe o que está acontecendo agora?

## 2. Correspondência com o mundo real
- Use o vocabulário do domínio e do usuário, nunca o da equipe.
- Pergunta: algum rótulo exigiria explicação para quem usa?

## 3. Controle e liberdade do usuário
- Toda ação tem saída: cancelar, voltar ou desfazer.
- Pergunta: dá para se arrepender sem perder trabalho?

## 4. Consistência e padrões
- Mesma ação, mesmo nome, mesmo lugar, mesmo visual.
- Cores, espaços e raios vêm de tokens (DESIGN.md).
- Pergunta: existe valor visual escrito direto no componente?

## 5. Prevenção de erros
- Confirmação ou desfazer em ação destrutiva.
- Valide junto ao campo e limite entradas impossíveis.
- Pergunta: o que o usuário pode errar aqui e como o impedimos?

## 6. Reconhecimento em vez de memorização
- Opções e contexto visíveis. Label sempre visível, nunca só placeholder.
- Pergunta: o usuário precisa lembrar algo da tela anterior?

## 7. Flexibilidade e eficiência
- Atalhos, busca e valores padrão sensatos para quem repete a tarefa.
- Pergunta: quantos cliques tem a tarefa mais frequente?

## 8. Estética e design minimalista
- Cada elemento ajuda a tarefa. Sem decoração que compita com o conteúdo.
- Um foco principal por tela.
- Pergunta: o que posso remover sem perder função?

## 9. Ajudar a reconhecer, diagnosticar e corrigir erros
- A mensagem diz o que aconteceu, por quê e o que fazer.
- Sem códigos crus nem "algo deu errado".
- Pergunta: quem lê sabe como resolver?

## 10. Ajuda e documentação
- Dica no ponto de uso, curta e específica.
- Pergunta: a primeira vez de um usuário novo funciona sem manual?

## Estados obrigatórios por componente
padrão, vazio, carregando, erro, sucesso, desabilitado, foco.

## Proibido
- Gradiente roxo para azul e efeito de vidro por padrão.
- Emoji como ícone ou marcador.
- Texto de exemplo, métricas inventadas, depoimentos fictícios.
- Elemento clicável que não seja button ou a.
- Cor literal fora de :root.
- Imagem gerada com brilho dourado, partículas ou texto embutido.
- Foto gerada de pessoas, equipe ou produto real.

## Ao terminar
Liste as heurísticas que a tela viola, com o trecho afetado e a correção.
