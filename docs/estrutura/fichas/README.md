# Fichas para transformar CAD em entrega de engenharia

[Trilha](../trilha-atlas-gaia.md) · [Do CAD à simulação](../../modelo-gaia.md)

Abra os CSVs em Excel, LibreOffice ou editor de texto, usando UTF-8 e vírgula como separador. Eles contêm somente cabeçalhos: nenhum valor foi inventado. Use ponto decimal em campos numéricos e deixe vazio o que ainda não foi medido. Registre `pendente`, `em_revisao` ou `validado` no estado; o último exige evidência e responsável.

| Ficha | Uma linha representa | Quando preencher |
| --- | --- | --- |
| [Lista de materiais](lista-materiais.csv) | Um item e sua revisão | Antes de comprar, fabricar ou montar |
| [Corpos rígidos](corpos-rigidos.csv) | Um corpo do futuro modelo | Ao extrair propriedades do CAD/pesagem |
| [Juntas](juntas.csv) | Uma articulação | Ao definir a cadeia cinemática e calibrar |
| [Registro de ensaio](ensaio.md) | Uma execução documentada | A cada abertura CAD, impressão ou teste |

Massa em kg; centro de massa e posição em m; ângulos em rad; inércia em kg·m²; velocidade em rad/s; esforço em N·m para juntas rotativas. Em corpos rígidos, informe o referencial e expresse o tensor no centro de massa, com eixos identificados. Em juntas, posição/orientação referem-se ao corpo pai e o eixo ao referencial da junta. Estes campos documentam dados; não são configuração executável de controle.

Use o caminho relativo do CAD e a revisão/commit. Quantidades, material, IDs, zero e limites precisam ser definidos pela equipe. Não confunda torque de travamento com esforço contínuo admissível. Guarde capturas e resultados em um caminho de evidência e referencie-os na ficha.
