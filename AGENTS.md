# Instrucoes do projeto

Acervo CAD/mesh e documentacao em docs/modelo-gaia.md, docs/estrutura e docs/competicao. Firmware joystick_diagnostic diagnostica botoes/OLED; nao e controlador de servos. Nao alterar binarios CAD ou atribuir licenca/autoria sem origem confirmada.

Ler README e docs antes de alterar. Preservar arquitetura, dados brutos e
autoria/licencas dos materiais externos. Nao inventar hardware, medidas ou
resultados. Marcar UNKNOWN/NOT_MEASURED e separar SIMULATED de REAL.
Fazer mudancas pequenas, com regressao para defeitos corrigidos.

Validacao: conferir manifestos, unidades e links; montagem, massa, inercia e firmware exigem validacoes proprias.

Definition of Done: verificacoes pertinentes, documentacao das alteracoes,
comandos reproduziveis e limites de validacao. Inspecao estatica nao comprova
funcionamento fisico. Ver docs/engineering-status.md para prioridades e estudo.

Para tarefas de CAD, montagem, desenho tecnico e fabricacao, consultar o perfil
`.github/agents/gaia-cad.agent.md` e `docs/estrutura/agente-cad.md`.
Esses arquivos definem o metodo; nao comprovam acesso a aplicativos nem
substituem validacao dimensional, de simulacao ou de hardware.
