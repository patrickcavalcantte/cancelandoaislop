# Antipadrões de interface gerada por IA

Regras para o agente. Cada item tem a severidade (escala de Nielsen, de 0 a 4, julgamento para um produto comum), o sinal que indica o problema e a regra de correção.
Ao terminar uma tela ou uma imagem, percorra a lista, corrija o que se aplicar e relate o que foi corrigido.

## Severidade 4: catástrofe

### 1. Elemento clicável sem semântica
- Sinal: ação feita com elemento que não é button nem a, sem foco por teclado.
- Regra: use button para ações e a para navegação. Garanta foco visível e operação só com Tab e Enter.

### 2. Ação destrutiva sem desfazer
- Sinal: excluir ou sobrescrever remove na hora, sem confirmação.
- Regra: toda ação destrutiva pede confirmação ou oferece desfazer por alguns segundos.

## Severidade 3: grave

### 3. Só o caminho feliz
- Sinal: a tela só existe com dados carregados e sem falhas.
- Regra: entregue os estados padrão, vazio, carregando, erro, sucesso, desabilitado e foco em todo componente.

### 4. Mensagem de erro genérica
- Sinal: texto como "algo deu errado", sem causa e sem caminho de correção.
- Regra: a mensagem diz o que aconteceu, por quê e o que fazer agora, na linguagem de quem usa.

### 5. Formulário sem rótulo de verdade
- Sinal: o placeholder faz o papel do label, a validação só ocorre ao enviar.
- Regra: label sempre visível, formato esperado escrito, validação junto ao campo.

### 6. Contraste fraco e texto miúdo
- Sinal: cinza claro sobre fundo claro, corpo de texto abaixo de 16 px.
- Regra: contraste mínimo de 4,5:1 para texto e corpo de 16 px ou mais. Meça com ferramenta, não a olho.

### 7. Conteúdo inventado
- Sinal: slogans genéricos, métricas sem fonte, depoimentos de pessoas que não existem.
- Regra: use o conteúdo e o vocabulário reais do produto. Nenhuma métrica sem fonte. Marque todo exemplo como exemplo.

### 8. Responsivo de fachada
- Sinal: a tela funciona em largura de desktop e quebra em celular.
- Regra: verifique em 390 px e 1280 px com captura de tela. Rolagem horizontal só dentro de tabelas e blocos de código.

### 9. Texto dentro de imagem gerada
- Sinal: placa, rótulo ou cartaz com letras trocadas ou palavras inventadas.
- Regra: nunca gere texto dentro da imagem. Gere a cena limpa e aplique o texto depois, em HTML ou na ferramenta de design.

### 10. Anatomia e objetos impossíveis
- Sinal: mãos com dedos a mais, talheres fundidos, relógios e dentes sem sentido.
- Regra: confira com zoom de 200% mãos, olhos, dentes e objetos antes de aceitar. Quando a pessoa ou o produto importam, use foto real.

### 11. Imagem que promete o que o produto não é
- Sinal: equipe, produto ou lugar que não existem como mostrados.
- Regra: use foto real para produto, equipe e lugar. Reserve a imagem gerada para ambientação e rotule quando a origem importar. Confira os termos de uso da ferramenta antes de publicar.

## Severidade 2: pequeno

### 12. O mesmo card para tudo
- Sinal: grade de caixas iguais com ícone, título e uma frase para qualquer tipo de conteúdo.
- Regra: o conteúdo decide a forma. Tabela para comparar, lista para escanear, parágrafo para explicar. Um papel por card.

### 13. Tipografia padrão e hierarquia plana
- Sinal: uma só fonte neutra em tudo, tamanhos próximos entre título e corpo.
- Regra: use o par de fontes e a escala definidos em DESIGN.md. Mantenha um foco principal por tela, com pelo menos três níveis claros.

### 14. Valores mágicos
- Sinal: cores quase iguais, espaçamentos e raios diferentes a cada componente.
- Regra: todo valor visual vem de variável definida em um único lugar. Cor, fonte ou espaço escritos direto no componente são defeito.

### 15. Dashboard decorativo
- Sinal: tiles de número grande, gráficos e cores chamativas, mas sem origem, período, referência de comparação, critério de contagem ou acesso ao detalhe. Parece profissional numa apresentação e não ajuda ninguém a decidir.
- Regra: resumo antes do detalhe. Cada número responde a cinco perguntas: de onde veio (origem), quando foi coletado (período), se é bom ou ruim (contexto, com meta ou período anterior), o que exatamente conta (critério) e onde está o detalhe que o explica (rastreabilidade). Cor semântica serve só para estado (bom, atenção, crítico).

### 16. Detalhe demais em imagem
- Sinal: tudo nítido e texturizado, sem ponto de foco.
- Regra: peça assunto único, fundo calmo e espaço vazio ao redor. Um foco por imagem.

### 17. Imagens que não combinam entre si
- Sinal: o rosto, a luz ou o estilo mudam de uma imagem para outra.
- Regra: defina em DESIGN.md o estilo de imagem (paleta, direção da luz, proporção) e reutilize uma imagem de referência a cada geração.

## Severidade 1: cosmético

### 18. Gradiente roxo e vidro fosco por padrão
- Sinal: gradiente de roxo para azul, desfoque e brilho sem relação com a marca.
- Regra: use só as cores de DESIGN.md. Sem gradiente decorativo nem efeito de vidro por padrão.

### 19. Emoji no lugar de ícone
- Sinal: emoji como ícone ou marcador de lista.
- Regra: use uma única biblioteca de ícones. Sem emoji em interface.

### 20. Tudo centralizado, abertura de tela cheia
- Sinal: parágrafos longos centralizados, topo com altura de tela que empurra o conteúdo para baixo.
- Regra: alinhe à esquerda para leitura, com linha perto de 65 caracteres. O topo tem o tamanho do conteúdo, e o conteúdo útil aparece na primeira tela.

### 21. Excesso de dourado, brilho e partículas em imagem
- Sinal: luz dourada em tudo, desfoque decorativo, faíscas e brilho saindo dos objetos.
- Regra: descreva a luz de verdade (janela lateral, luz do dia, fundo neutro) e proíba brilho, faíscas e partículas no pedido.

## Arquitetura da informação

### 22. Rótulos de marketing na navegação (severidade 3)
- Sinal: itens de menu como Soluções, Plataforma, Insights e Recursos, que não dizem o que há atrás.
- Regra: nomeie cada item pela tarefa ou pelo conteúdo, com o vocabulário de quem usa. Pergunte de cada rótulo: o que encontro aqui?

### 23. Ordem de template em vez de ordem da pergunta (severidade 3)
- Sinal: página que segue hero, recursos, depoimentos, logos, planos, perguntas e chamada final em qualquer produto.
- Regra: liste as três perguntas mais comuns de quem chega e ordene a página por elas. A resposta mais procurada vem primeiro.

### 24. Sem orientação de localização (severidade 3)
- Sinal: menu sem item ativo, sem trilha de navegação, títulos genéricos como "Detalhes".
- Regra: marque o item ativo, use trilha de navegação a partir do terceiro nível e dê a cada página um título que diga o assunto.

### 25. Títulos fora de hierarquia (severidade 3)
- Sinal: mais de um h1, saltos de nível, nível escolhido pelo tamanho visual.
- Regra: um h1 por página e níveis em sequência, sem pular. O tamanho se resolve em CSS.

### 26. Tudo no mesmo nível (severidade 2)
- Sinal: dez ou mais itens de navegação com o mesmo peso.
- Regra: agrupe por tarefa, com rótulo de grupo, e leve o que raramente se usa para um nível abaixo.

### 27. Mesma coisa, vários nomes (severidade 2)
- Sinal: a mesma ação ou o mesmo conceito com nomes diferentes em telas diferentes.
- Regra: use um glossário, com um nome por conceito, e proíba sinônimos na interface.

### 28. Links que não dizem para onde levam (severidade 2)
- Sinal: vários links como "Saiba mais", "Clique aqui" ou "Ver mais" na mesma tela.
- Regra: o texto do link diz o destino ou a ação e se entende fora de contexto.

### 29. Campos na ordem do banco de dados (severidade 2)
- Sinal: formulário com campos na ordem das colunas da tabela, com campos técnicos expostos.
- Regra: agrupe por assunto, na ordem em que a pessoa responderia, e deixe campos técnicos fora da tela.

## Português

### 30. Acentos perdidos e codificação quebrada (severidade 3)
- Sinal: textos de interface sem acento ("nao", "voce") ou com caracteres trocados ("NÃ£o").
- Regra: arquivos em UTF-8 com o charset declarado. Revise a acentuação de todas as strings de interface antes de entregar.

### 31. Palavras inventadas (severidade 3)
- Sinal: palavras que soam plausíveis e não estão nos dicionários, como "emplacação" (o substantivo registrado é "emplacamento"), "atendimentar" e "otimizacional". Substantivos derivados por analogia com outro verbo são o caso mais comum.
- Regra: use só palavras dicionarizadas. Liste as palavras em que tiver dúvida e confira no VOLP ou em um dicionário. Neologismo só como decisão explícita de marca.

### 32. Formatos à moda americana (severidade 3)
- Sinal: "R$ 1,299.90", data com o mês na frente ("11/25/2026"), hora com AM e PM.
- Regra: use R$ 1.299,90, 25/11/2026 e 14h30. Formate datas e valores com as funções do idioma (por exemplo, Intl), sem montar o texto à mão.

### 33. Vírgula entre sujeito e predicado (severidade 2)
- Sinal: vírgula única entre sujeito e verbo ("Nossa plataforma, permite...") ou entre verbo e complemento ("Você precisa, confirmar...").
- Regra: sem vírgula única entre sujeito e verbo, nem entre verbo e complemento. Intercalação leva duas vírgulas. Passe um corretor gramatical antes de entregar.

### 34. Vírgula que muda o sentido (severidade 2)
- Sinal: oração com "que" com ou sem vírgulas sem que o sentido tenha sido escolhido.
- Regra: oração adjetiva restritiva não leva vírgula e a explicativa leva. Use a que o sentido pedir e, se não souber qual é, pergunte.

### 35. Vírgula de série à moda inglesa (severidade 2)
- Sinal: vírgula antes do "e" que fecha uma enumeração ("consultas, exames, e retornos").
- Regra: sem vírgula antes do "e" que fecha uma enumeração.

### 36. Crase, regência e concordância (severidade 2)
- Sinal: "à partir de", "haviam dez vagas", "fazem dois anos".
- Regra: "a partir de" não leva crase. Haver e fazer no sentido de existir ou de tempo decorrido ficam no singular. Passe um corretor gramatical antes de entregar.

### 37. Concordância com "se" e com "um dos que" (severidade 2)
- Sinal: "Aceita-se cartões", "um dos erros que mais ocorre".
- Regra: com o "se" apassivador, o verbo concorda com o sujeito ("Aceitam-se cartões"). Depois de "um dos que", o verbo vai para o plural na norma-padrão.

### 38. Pares que se confundem (severidade 2)
- Sinal: "Porque o código não chegou?", "Aonde fica a clínica?", "preenchido mau".
- Regra: por que, porque, por quê e porquê; onde e aonde; mal e mau; há e a. Confira cada ocorrência contra o contexto.

### 39. Maiúsculas à moda inglesa (severidade 2)
- Sinal: títulos com todas as palavras capitalizadas, dias da semana e meses em maiúscula.
- Regra: maiúscula só no início de frase e em nomes próprios. Dias da semana e meses em minúscula.

### 40. Português de Portugal em produto brasileiro (severidade 2)
- Sinal: termos como utilizador, ecrã, guardar, telemóvel e a construção "estar a" + infinitivo.
- Regra: use pt-BR e o glossário do produto (usuário, tela, salvar, celular). Use gerúndio, como em "carregando".

### 41. Tradução literal e falsos cognatos (severidade 2)
- Sinal: "realizar" no sentido de perceber, "eventualmente" no sentido de por fim, "pretender" no sentido de fingir.
- Regra: escreva em português, sem traduzir do inglês. Revise falsos cognatos e use os nomes de botão da convenção do domínio.

### 42. Plural montado por template (severidade 2)
- Sinal: frases como "1 consultas" ou "0 notificações novas".
- Regra: use regras de plural (Intl.PluralRules ou biblioteca de i18n), teste com 0, 1 e 2 e escreva uma frase própria para o zero.

### 43. Tratamento e verbos inconsistentes (severidade 2)
- Sinal: "você", "tu" e "o senhor" na mesma tela, ou infinitivo e imperativo misturados nos botões.
- Regra: um tratamento (você) e um modo verbal para botões, definidos em DESIGN.md e usados em todo o produto.

### 44. Marca de gênero com parênteses (severidade 2)
- Sinal: "Bem-vindo(a)", "Prezado(a) cliente", "todos(as)".
- Regra: use fórmulas sem marca de gênero (Olá), o nome da pessoa ou um substantivo coletivo.

### 45. Gerundismo (severidade 2)
- Sinal: "vou estar enviando", "vamos estar verificando".
- Regra: use o verbo simples: "vou enviar", "vamos verificar".

### 46. Texto burocrático (severidade 2)
- Sinal: voz passiva e nominalização em excesso: "A realização da confirmação deve ser efetuada pelo usuário".
- Regra: prefira voz ativa e verbos. Escreva "Confirme seu agendamento".

### 47. Clichês de texto gerado (severidade 2)
- Sinal: "no cenário atual", "é importante ressaltar", "revolucione", "mergulhe", "desbloqueie o potencial", travessão em excesso.
- Regra: não use essas expressões. Escreva frases curtas, com sujeito e verbo, sobre o que o produto faz de fato.

### 48. Pleonasmos (severidade 1)
- Sinal: "há dois anos atrás", "subir para cima", "elo de ligação".
- Regra: escreva sem repetir o que a palavra anterior já diz.

### 49. Frases picotadas e enumeração com ponto (severidade 2)
- Sinal: ponto final no lugar da vírgula: "Nosso app é rápido. É seguro. É simples." e "Você recebe alertas. Relatórios. Lembretes." Cada pedaço vira uma frase, e os conectivos (porque, mas, então) somem.
- Regra: una orações curtas e relacionadas com vírgula, "e" ou conectivo. Separe itens de enumeração com vírgula, com "e" antes do último. Use fragmento isolado só como destaque raro, no máximo um por tela. Para listar de verdade, use lista com marcadores.

## Ao terminar
Liste cada item acima que a tela ou a imagem viola, com o trecho afetado e a correção aplicada.
