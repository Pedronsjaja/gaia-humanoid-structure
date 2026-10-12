# Roteiro para uma junta identificada

Diagnostico: o acervo nao constitui por si so um modelo dinamico integrado.
O primeiro incremento deve fechar uma junta antes de integrar o humanoide.
Use docs/modelo-gaia.md como contrato de modelagem; este registro transforma
as lacunas em criterios de aceite, sem inventar parametros.

| Campo | Estado / unidade | Evidencia necessaria |
| --- | --- | --- |
| Junta, peca e revisao CAD | UNKNOWN | arquivo e hash do conjunto |
| Material e processo | UNKNOWN | ficha de fabricacao |
| Massa / centro de massa | NOT_MEASURED / kg, m | balanca, montagem e origem do referencial |
| Tensor de inercia | UNKNOWN / kg m² | metodo CAD ou experimento identificado |
| Eixo e sentido positivo | UNKNOWN | desenho e referenciais |
| Limites mecanicos | UNKNOWN / rad | inspecao da montagem sem carga perigosa |
| Folga / repetibilidade | NOT_MEASURED / rad | dados brutos e referencia externa |
| Servo, alimentacao, transmissao | UNKNOWN | modelo, datasheet e montagem |

ALTO: confirmar origem/licencas e unidades das pecas antes de redistribuir ou
exportar URDF. ALTO: levantar limites e massa da junta escolhida. MEDIO:
exportar URDF com inercia consistente e comparar com ensaio. BAIXO: integrar
cadeia completa depois de aceitar cada junta. Regras de competicao 2025
sao historicas; edicao aplicavel continua pendente de verificacao.

Protocolo de ensaio: definir hipotese (erro angular dependente da carga),
instrumento/referencia, montagem, parada, limites e criterio de aceite ANTES
de executar. Registrar angulo comandado, feedback, referencia externa, carga,
tempo, tensao e temperatura; repetir em ambos os sentidos. Numero de ciclos,
carga e tolerancia: TODO, dependem da montagem. Preservar CSV bruto e separar
media/desvio derivados. Sem referencia externa, nao concluir exatidao.

Para entender esta implementacao: estude transformacoes rigidas, tensor de
inercia, folga e propagacao de incerteza. Desafio: desenhe os referenciais de
uma junta e demonstre as unidades dos termos de energia cinetica.

Referencias: [REP-103](https://www.ros.org/reps/rep-0103.html) para convencoes;
[GUM/JCGM 100](https://www.bipm.org/en/doi/10.59161/jcgm100-2008e) para incertezas.
Essas referencias definem metodos, nao fornecem medidas do GAIA.
