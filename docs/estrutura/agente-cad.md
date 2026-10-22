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
