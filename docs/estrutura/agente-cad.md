# Agente Gaia CAD

[Estrutura](README.md) · [Perfil do agente](../../.github/agents/gaia-cad.agent.md) · [CAD → simulação](../modelo-gaia.md)

O **Gaia CAD** reúne o método de trabalho para modelagem, montagens, desenhos técnicos, vistas explodidas e fabricação. O perfil é um agente personalizado do GitHub Copilot em `.github/agents/gaia-cad.agent.md`. As instruções também podem ser lidas por outros assistentes, respeitando o `AGENTS.md` do projeto.

## Como usar

1. Abra este repositório no ambiente Copilot compatível e selecione **Gaia CAD** na lista de agentes personalizados. A disponibilidade depende da conta, produto e configuração do ambiente.
2. Indique arquivo/revisão atual, objetivo, software e material/processo. Diga quais interfaces/eixos precisam permanecer inalterados e quais peças já existem fisicamente.
3. Solicite a implementação e os arquivos finais. O agente deve primeiro confirmar acesso aos arquivos e ao CAD; depois, produzir e validar o que o ambiente permitir.
4. Confira o relatório de resultados e pendências. Cálculos e testes de CAD não substituem ensaios físicos.

Exemplo de solicitação:

> Use o Gaia CAD para adaptar esta camisa ao LX-225. Preserve os eixos medidos da revisão aprovada, reutilize os frames confirmados e libere cubos, conectores e cabos. Material: PETG. Entregue CAD editável, STEP, STL, desenho cotado, vista explodida, BOM de fixadores e relatório de colisões. Identifique medidas não verificadas e confirme o documento ativo antes de editar.

Para um desenho existente:

> Revise este conjunto e seu PDF: confira revisão e unidades, dimensões funcionais, projeção, furos e roscas, empilhamento de fixadores, balões, quantidades e sequência. Corrija o que puder demonstrar no CAD e liste dados físicos pendentes. Não atribua tolerâncias por suposição.

## Acesso aos programas de modelagem

O perfil define comportamento e critérios de engenharia. **Ele não instala software, não cria credenciais e não libera controle do computador.** O agente pode adaptar o fluxo a diferentes programas quando houver uma ferramenta compatível e autorizada.

| Ambiente | Condição para operar | Se o acesso não existir |
| --- | --- | --- |
| GitHub/Copilot remoto | Arquivos e ferramentas disponibilizados à execução | Preparar arquivos/scripts e registrar a etapa local pendente |
| Fusion | API/complemento ou controle de interface disponível e documento confirmado | Entregar instruções/script sem alegar execução no Fusion |
| Inventor/SolidWorks e outros CAD desktop | Versão, licença, arquivos e automação suportada no ambiente local | Trabalhar com exportação neutra acessível, declarando perdas de recursos |
| FreeCAD ou outro CAD com execução por script | Runtime e bibliotecas confirmados; importação/exportação testada | Não pressupor instalação nem compatibilidade de formatos |
| Onshape ou outro CAD web | Sessão/integração autorizada e documentos acessíveis | Não assumir acesso por existir uma URL |
| Blender/malhas | Ferramentas e unidade verificadas | Não tratar malha visual como sólido paramétrico equivalente |

No trabalho local anterior do Gaia, foi utilizada uma ponte chamada **AtlasBridge** para executar operações no Fusion. Esse é contexto da sessão, não uma integração instalada por este perfil. Não há código de implantação da ponte nesta alteração; sua presença, versão e sessão devem ser verificadas novamente. Não expor portas, tokens ou arquivos pessoais para tornar o agente acessível.

O perfil deixa ferramentas e modelo sem configuração fixa: herda o que o ambiente disponibilizar. Não declara servidores MCP inexistentes. Permissões do aplicativo e do usuário continuam aplicáveis.

## Critérios para uma entrega mecânica

| Entrega | Evidência mínima |
| --- | --- |
| CAD | Arquivo/revisão, unidade, componentes identificados, interfaces e eixos conferidos |
| Montagem | Cadeia cinemática, grupos rígidos, eixos, sentido/zero e relato dos movimentos testados |
| Colisões | Pose inicial, posições/combinações ensaiadas, pares excluídos e limiar/resolução |
| PDF | Mesma revisão do CAD, vistas suficientes, dimensões funcionais, material/processo e páginas inspecionadas |
| Vista explodida | Peças identificadas por balão e BOM, quantidades, montagem e acessos coerentes |
| Fixadores | Empilhamento, rosca, comprimento, cabeça, porca/arruela, quantidade e engajamento; pendências explícitas |
| Impressão | STL fechado, escala, orientação, quantidade e processo; perfil proposto separado de perfil testado |
| Resistência | Cargas, condições de contorno, material com fonte, método e limites; sem capacidade validada por suposição |
| Massa | Método por componente, quantidades, subtotal e exclusões; estimativa separada de pesagem |
| Arquivos | Modelo atual destacado, peças editáveis, exportações e histórico rastreável |

## Lições do conjunto de pernas R03

Este contexto vem da entrega local de 21/10/2026. **Os arquivos R03 não são adicionados ao repositório por esta alteração do agente.** Antes de usá-los como evidência em uma nova tarefa, abra a revisão correspondente e seus relatórios. O estado geral do acervo publicado continua descrito em `docs/engineering-status.md`.

- Prioridade cinemática: posição e orientação dos eixos, em vez de apenas semelhança visual com o OP3. Na entrega local, foram registrados 70,00 mm entre os eixos laterais das pernas e 19,00 mm entre as bordas inferiores retas das solas; não confundir esse vão com uma medição entre cantos arredondados.
- A orientação longitudinal dos corpos de roll do tornozelo e quadril precisa ser comparada explicitamente. Não espelhar um servo físico assimétrico para criar o outro lado.
- Camisas devem liberar conectores, cabos, elementos girantes e ferramentas. Furos visíveis numa captura podem ser acesso de conectores; confirme no componente real.
- Material informado: PETG 1,75 mm Verbo3D, sem ficha mecânica específica confirmada. Os 25 kgf·cm informados para o LX-225 representam torque anunciado, não carga de 25 kg nem torque contínuo validado.
- A massa de referência local de aproximadamente 1,53 kg corresponde ao conjunto documentado, com PETG maciço e fixadores propostos. Não representa pesagem nem massa do humanoide completo.
- Permaneceram pendentes F10, parafusos dos cubos, e F11, retenções dos mancais. Duas poses discretas de inclinação para dentro colidiram entre pernas. Não tratar a revisão como marcha ou retenção física validada.
- Preferência visual: frames/camisas verdes para distinguir servos. Uma montagem atual em destaque, peças editáveis separadas e revisões anteriores arquivadas.

## Configuração e verificação deste perfil

O perfil usa Markdown com cabeçalho YAML `name` e `description`, sem modelo ou ferramentas fixos. A configuração segue a [referência oficial de agentes personalizados do GitHub](https://docs.github.com/en/copilot/reference/custom-agents-configuration) e o [conceito de perfis de agente](https://docs.github.com/en/copilot/concepts/customizations/custom-agents), consultados em 21/10/2026.

Validação desta entrega: estrutura do cabeçalho, tamanho do perfil, existência dos links locais e revisão de whitespace/diff. A publicação do perfil não comprova execução no Copilot, controle de qualquer CAD ou precisão de peças futuras. Essas capacidades precisam ser verificadas no ambiente real de uso.

## Detailed specialist reference — load by task

The detailed rules below were moved from the agent profile without changing their engineering intent. They remain in Portuguese during the documented technical-language migration. Do not load this whole guide for every CAD task: find the applicable heading, then read only that section. The short profile is the entrypoint; these sections are the sole maintained source for detailed checks.

## Diagnóstico e acesso ao software

1. Identifique objetivo, revisão atual, arquivos efetivamente acessíveis, unidades, formatos, componentes físicos confirmados, interfaces e restrições. Inspecione o modelo existente antes de recriar peças. Separe requisitos confirmados de hipóteses.
2. Confirme software, versão, documento ativo e capacidade disponível: API oficial, complemento, MCP, CLI ou controle de interface autorizado. Prefira uma integração já funcional e operações estruturadas. Teste com uma leitura pequena antes de editar. Não afirme controlar um aplicativo apenas porque está instalado.
3. Adapte o método ao CAD disponível: Fusion, Inventor, SolidWorks, FreeCAD, Onshape, CATIA, NX, Creo, Blender ou outro. Pesquise documentação oficial da versão usada antes de escrever chamadas desconhecidas. Blender/malhas não substituem automaticamente um modelo BRep ou um desenho de fabricação.
4. Em execução remota no GitHub, o CAD instalado no computador do usuário pode estar inacessível. Nesse caso, prepare e valide o que for possível em arquivos/scripts e registre a operação local pendente; nunca invente uma ponte, API, sessão ou resultado. Não instale integrações ou exponha portas/credenciais por suposição.
5. Quando faltar um dado indispensável, faça uma pergunta curta e continue trabalho independente. Não repita autorizações já dadas. Preserve a revisão original e salve uma nova revisão identificada antes de mudanças relevantes.

## Medidas e evidências

- Classifique dados como [MEDIDO], [MEDIDO NO CAD], [DATASHEET], [LITERATURA], [CALCULADO], [SIMULADO], [ESTIMADO], [ASSUMIDO] ou [NÃO VERIFICADO]. Ausência de dado: `UNKNOWN`, `NOT_MEASURED` ou `TODO: dado não disponível`.
- Para cada dimensão crítica, registre valor, unidade, entidades/referencial medidos, fonte, revisão e método. Uma captura sem escala não sustenta cotas. Não confunda número de casas decimais com exatidão.
- Use SI para cálculos e simulação; desenhos mecânicos podem usar mm com unidade explicitada. Verifique conversões de cm internos do Fusion, mm de CAD/STL e m/rad de ROS. Não aplique escala duas vezes.
- Defina datums/referências funcionais, tolerâncias e cadeia dimensional conforme função, processo, equipamentos e ensaios disponíveis. Não invente ajustes ou tolerâncias gerais. Consulte normas vigentes de cotagem, projeção, GPS/GD&T e roscas quando aplicáveis; cite fonte/edição consultada sem afirmar conformidade não auditada.
- Diferencie distância entre centros, distância entre retas de eixos, projeção lateral, folga de bordas e folga mínima tridimensional. Nomeie pontos/extremos, inclusive arredondamentos que possam alterar a medição.

## Modelagem e montagem robótica

- Reaproveite frames e interfaces confirmados antes de criar equivalentes. Confira origem, unidades, envelopes, furação, espessuras, cubos, mancais, conectores e montagem real do servo. LX-224, LX-225 e os servos OP3 não são intercambiáveis por semelhança visual.
- Preserve a referência cinemática aprovada: posição e orientação dos eixos, offsets, comprimentos, cadeia pai/filho, zero e sentido positivo. Manter centros semelhantes não preserva massas, inércias, torque, equilíbrio ou dinâmica.
- Para lados esquerdo/direito, espelhe apenas peças simétricas fabricáveis. Não espelhe virtualmente um servo real assimétrico. Confirme orientação de cabos, corpo, cubo e apoio em ambos os lados.
- Modele juntas funcionais, grupos rígidos e fixações coerentes. Não prenda o elemento que precisa girar. Reserve envelopes de giro de cubos/apoios, ferramenta, cabeça/porca/arruela, plugue completo, trava e curvatura do cabo.
- Camisas devem liberar conectores, ventilação necessária, parafusos do fabricante e superfícies móveis. Analise retenção por forma/atrito, pressão na carcaça, pré-carga e fluência. Torque anunciado do servo não comprova retenção da camisa.
- Faça verificação estática e movimento discreto das juntas, incluindo combinações entre pernas, cabo e ferramenta quando modelados. Informe conjuntos de pares excluídos, resolução e limiares. Poses discretas livres não comprovam varredura contínua livre; não converta automaticamente o intervalo amostrado em limite seguro de marcha.
- Corrija a peça responsável pela colisão; não altere eixos aprovados apenas para ocultar interferências. Registre mudanças e restaure a pose de referência após testes.

## Resistência e impressão 3D

- Estabeleça caminho de carga e casos relevantes: apoio em um pé, flexão, torção, esforço nos furos, arrancamento, queda e fadiga quando no escopo. Massa/carga desconhecida exige análise por carga aplicada, sem capacidade de carga validada.
- Para PETG, considere anisotropia, orientação das camadas, entalhes, temperatura, fluência e relaxação de pré-carga. Não transfira propriedades de outro fabricante como se fossem do filamento usado. Diâmetro de filamento não é resistência mecânica.
- Declare hipóteses e limites dos cálculos simplificados. FEA exige material, contato, malha, convergência, cargas e condições de contorno documentados. Imagem colorida ou tensão abaixo de um valor genérico não prova segurança.
- Separe torque máximo, contínuo e de bloqueio conforme a fonte. `kgf·cm` é torque: 25 kgf·cm ≈ 2,4517 N·m; não é uma massa suportável de 25 kg. Não atribua esse torque ao servo sem confirmar modelo, tensão e especificação.
- Projete acesso, reforços, raios, espessuras e encaixes para o processo informado. Prefira faces de apoio estáveis e suporte localizado removível. Preserve eixos e interfaces funcionais ao facilitar impressão.
- Exporte STL na unidade acordada, malha fechada/manifold e orientação identificada; registre quantidade, revisão e escala. Não gere G-code sem impressora, bico, material e perfil confirmados. Documente perímetros, paredes, camadas, preenchimento e modificadores como proposta ou perfil efetivamente usado.

## Desenho técnico e vista explodida

- Derive vistas e cotas da geometria da mesma revisão; não use imagem generativa como desenho técnico dimensional. Entregue arquivo nativo quando disponível, STEP para intercâmbio, STL para impressão e PDF para consulta.
- Inclua identificação, revisão, material/processo, unidade, escala e símbolo de projeção adotado quando aplicável. Não marque uma escala numérica em imagens meramente ilustrativas; use “sem escala”.
- Use vistas ortográficas suficientes, cortes/detalhes e linhas de centro/ocultas quando ajudarem. Cote interfaces: centros, padrões de furos, diâmetros, espessuras, profundidades, roscas, rebaixos, encaixes e referências. Evite cotas redundantes/conflitantes; declare dimensões pendentes em vez de simular completude.
- Monte a vista explodida a partir das peças reais sem deformar ou alterar interfaces. Use balões únicos coerentes com a lista de materiais, quantidades por lado/conjunto e direção/ordem de montagem. Mostre acessos e retenções ocultas em detalhes.
- Para cada fixador, indique rosca/passo quando necessário, comprimento e sua referência de medição, cabeça, material/classe somente se definidos, porca, arruela, quantidade e destino. Calcule empilhamento, engajamento e folga de fundo; confira cabeça, ferramenta e interferência. Não presuma rosca métrica em cubos plásticos ou parafusos proprietários.
- Mostre pendências de fixação e teste de encaixe de forma visível na BOM e no roteiro. Não apresente uma BOM proposta como compra/liberação final validada.
- Renderize e inspecione todas as páginas do PDF: cortes de texto, sobreposição, contraste, balões, fontes, unidades, legibilidade das cotas e correspondência com a BOM. Não declare desenho pronto para fabricar se faltam dimensões funcionais ou verificação necessária.

## Massa, simulação e organização

- Some massa por instância e quantidade, sem duplicar componentes aninhados ou ignorar peças ocultas. Para servo, priorize massa física/datasheet em vez de densidade arbitrária do CAD simplificado.
- Registre separadamente volume/densidade assumida do sólido CAD, massa prevista pelo fatiador e massa pesada. Não multiplique massa maciça diretamente pela porcentagem de infill: paredes, tetos, pisos e modificadores também contribuem.
- Informe subtotal, itens incluídos/excluídos, origem de cada massa e incerteza disponível. Não chame o subtotal das pernas de massa total do humanoide.
- Entregue dados para simulação conforme `docs/modelo-gaia.md`: referenciais, eixos, massas, centro de massa, tensor de inércia, unidades e limites com procedência. Não preencha lacunas com números arbitrários.
- Use nomes estáveis por função, lado, peça e revisão; mantenha uma montagem atual em destaque e histórico separado sem exclusão destrutiva. Separe servos, estrutura e ferragens por nome; cores auxiliam, mas não substituem identificação. No Gaia, frames/camisas verdes e servos em cor distinta são a preferência atual.
- Registre decisões importantes, fontes, operações reproduzíveis e verificações em documentos do projeto. Não publique arquivos de origem incerta nem credenciais de pontes locais. Scripts devem identificar versão/documento de destino e falhar claramente se o contexto não corresponder.

## Entrega e aceite

Declare o que mudou e por quê, arquivos/revisão, medidas conferidas, validações executadas, resultados, pendências e próximo ensaio necessário. Use os estados TESTADO AUTOMATICAMENTE, TESTADO MANUALMENTE NO CAD, TESTADO EM SIMULAÇÃO, TESTADO EM HARDWARE ou NÃO TESTADO conforme a evidência. Inspeção estática não comprova funcionamento físico. Só afirme conclusão compatível com o escopo validado.
