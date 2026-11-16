# Português do Brasil: regras para o agente

Use este arquivo ao escrever qualquer texto em português: interface, e-mail, documentação, mensagens de erro.
Escreva em português do Brasil. Ao terminar, aplique o checklist da última seção e corrija antes de entregar.

## Princípios
- Escreva em português, sem traduzir do inglês. Frases curtas, com sujeito e verbo.
- Use só palavras dicionarizadas. Se tiver dúvida sobre uma palavra, não a use e liste a dúvida ao final, para uma pessoa conferir no VOLP (academia.org.br/nossa-lingua/busca-no-vocabulario).
- Não invente termo, sigla ou nome de funcionalidade que não tenha sido dado.
- Cuidado com substantivos derivados por analogia. De "emplacar", o substantivo registrado é "emplacamento", e não "emplacação". Ao derivar um substantivo de um verbo, confira se ele existe.
- Quando nenhuma regra abaixo resolver o caso, escolha a construção mais simples que esteja correta e sinalize a dúvida.

## Variante e tratamento
- Use pt-BR: usuário, tela, salvar, celular, arquivo. Não use termos de Portugal, como utilizador, ecrã, guardar e telemóvel, nem a construção "estar a" + infinitivo.
- Trate o leitor por "você" e "seu" em todo o texto. Não misture com "tu", "teu" nem "o senhor".
- Nos botões, use um só modo verbal em todo o produto. O padrão é o infinitivo: Salvar, Cancelar, Enviar.
- Sem marca de gênero entre parênteses ou com barra. Use fórmulas neutras (Olá), o nome da pessoa ou um substantivo coletivo.

## Ortografia e codificação
- Todos os arquivos em UTF-8, com o charset declarado. Acentue todas as palavras, inclusive nas strings de código.
- Siga o Acordo Ortográfico em vigor.
- Maiúscula só no início de frase e em nomes próprios. Título não capitaliza cada palavra. Dias da semana e meses ficam em minúscula.

## Pontuação
- Sem vírgula única entre sujeito e verbo, nem entre verbo e complemento.
- Intercalações (aposto, vocativo, oração explicativa) ficam entre duas vírgulas.
- Oração adjetiva restritiva não leva vírgula: "Os pacientes que chegaram cedo foram atendidos". A explicativa leva: "Os pacientes, que chegaram cedo, foram atendidos". Use a que o sentido pedir.
- Sem vírgula antes do "e" que fecha uma enumeração: "consultas, exames e retornos".
- Oração subordinada ou adjunto adverbial longo antes da principal pede vírgula: "Quando o código chegar, digite-o aqui."
- Use travessão com parcimônia. Prefira vírgula, ponto ou parênteses.

## Concordância, regência e crase
- Haver no sentido de existir e fazer indicando tempo decorrido ficam no singular: "Havia dez vagas", "Faz dois anos".
- Com o "se" apassivador, o verbo concorda com o sujeito: "Aceitam-se cartões", "Alugam-se salas".
- Depois de "um dos que", use o verbo no plural, como pede a norma-padrão: "um dos erros que mais ocorrem".
- "A partir de" não leva crase. Use crase só quando houver a preposição "a" e o artigo "a" juntos.
- Pares que se confundem:
  - por que (pergunta), porque (explicação), por quê (fim de frase), porquê (substantivo);
  - onde (lugar em que se está), aonde (lugar para onde se vai);
  - mal (oposto de bem), mau (oposto de bom);
  - há (tempo decorrido), a (tempo futuro ou distância).
- Plural: use a regra de plural da biblioteca de i18n. Escreva uma frase própria para o zero: "Você não tem notificações".

## Estilo
- Não use "estar" + gerúndio para o futuro ("vou estar enviando"). Use o verbo simples: "vou enviar".
- Prefira voz ativa e verbos a nominalizações: "Confirme o agendamento", e não "A realização da confirmação deve ser efetuada".
- Sem pleonasmo: "há dois anos", e não "há dois anos atrás".
- Não use clichês: "no cenário atual", "é importante ressaltar", "vale destacar", "revolucione", "mergulhe", "desbloqueie o potencial".
- Conectivos como "além disso" e "portanto" só quando ligarem ideias de fato, no máximo um por parágrafo.

## Formatos
- Moeda: R$ 1.299,90 (ponto nos milhares, vírgula nos centavos).
- Data: 25/11/2026, com dia, mês e ano. Por extenso: 25 de novembro de 2026.
- Hora: 14h30, no relógio de 24 horas.
- Número: vírgula decimal (3,5) e ponto nos milhares (12.000).
- Use as funções de formatação do idioma (por exemplo, Intl) em vez de montar datas e valores à mão.

## Checklist ao terminar
1. Todas as palavras existem no dicionário? As dúvidas foram listadas para conferência no VOLP?
2. Alguma vírgula separa sujeito de verbo ou verbo de complemento?
3. Os verbos concordam com os sujeitos (haver, fazer, "se" apassivador, "um dos que")?
4. Acentos, crase e maiúsculas conferidos? Arquivos em UTF-8?
5. Valores, datas e horas estão no formato brasileiro?
6. Há um só tratamento (você) e um só modo verbal nos botões?
7. Há clichê, gerundismo, pleonasmo ou frase burocrática?
8. Lida em voz alta, alguma frase exige fôlego extra?

Ao final, liste qualquer dúvida de norma que você não resolveu.
