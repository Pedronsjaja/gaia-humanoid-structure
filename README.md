# Gaia — estrutura, CAD e montagem do humanoide

Arquivos mecânicos e documentação de montagem da equipe **Gaia**, com referência no **ROBOTIS OP3** e objetivo de participação na **CBR Humanoid**.

## Comece pelo que você precisa

| Objetivo | Abrir |
| --- | --- |
| Aprender a encontrar e baixar arquivos | [Guia GitHub](docs/primeiros-passos-github.md) |
| Escolher CAD, STEP ou STL | [Catálogo mecânico](hardware/README.md) |
| Abrir o CAD compartilhado LX-224/LX-225 | [Montagem do servo](hardware/cad/servo-lx224-lx225/) |
| Imprimir os suportes disponíveis | [STL](hardware/suportes/gaia-3d/STL/) |
| Editar suportes em CAD | [STEP](hardware/suportes/gaia-3d/STEP/) · [Inventor](hardware/suportes/gaia-3d/IPT/) |
| Entender as entregas da frente mecânica | [Estrutura](docs/estrutura/README.md) |
| Escolher software para abrir as peças | [Softwares CAD](docs/softwares-cad.md) |
| Preparar massas, eixos e limites para simulação | [Do CAD ao modelo Gaia](docs/modelo-gaia.md) |
| Conferir limitações da CBR | [Regulamentos](docs/competicao/README.md) · [Matriz de requisitos](docs/competicao/matriz-requisitos.md) |
| Montar o painel auxiliar ESP32-S3 | [Joystick/OLED](docs/joystick.md) |

## Roteiro de montagem

1. Consulte os regulamentos e registre as dimensões ainda pendentes.
2. Baixe o conjunto CAD completo em **Code → Download ZIP**, extraia e mantenha juntas as peças referenciadas.
3. Confira unidades, furos e encaixe no servo real. O CAD LX-224/LX-225 é a equivalência informada pelo mantenedor.
4. Fabrique uma peça de teste antes de repetir a impressão.
5. Registre material, parâmetros, massa, folgas, eixo e limites.
6. Entregue esses dados à equipe de [simulação](https://github.com/Pedronsjaja/gaia-humanoid-simulation).

Os arquivos incluem **29 itens mecânicos originais**, com [inventário de integridade](hardware/manifest.json). Ainda não há montagem completa Gaia nem ensaio estrutural aprovado dos suportes.

O painel joystick/OLED está em `firmware/` como componente auxiliar da montagem; seu firmware atual é de diagnóstico e não controla servos.

## Organização

```text
hardware/cad/          CAD e referências do servo
hardware/suportes/     Peças nativas, STEP e STL
docs/estrutura/        Orientações da frente mecânica
docs/modelo-gaia.md    Dados físicos para URDF e simulação
docs/competicao/       Regras, fontes e requisitos
docs/joystick.md       Painel auxiliar de diagnóstico
firmware/              Diagnóstico do painel ESP32-S3
```

A categoria escolhida é **CBR Humanoid**; subcategoria e regulamento vigente precisam ser confirmados. Os documentos históricos estão identificados por edição.

Consulte a [procedência da migração](docs/migracao.md). As licenças e autorias dos materiais originais permanecem as informadas no catálogo.

## Repositórios da equipe Gaia

| Preciso de… | Repositório |
| --- | --- |
| Servo LX-225, BusLinker, drivers e testes de bancada | [LX-225 / BusLinker](https://github.com/Pedronsjaja/gaia-lx225-buslinker) |
| Gazebo, OP3, ROS 2 e autonomia | [Simulação](https://github.com/Pedronsjaja/gaia-humanoid-simulation) |
| CAD, suportes, montagem e requisitos físicos da CBR | [Estrutura](https://github.com/Pedronsjaja/gaia-humanoid-structure) |
| Instalar Ubuntu 24.04 e ROS 2 Jazzy | [Ambiente Linux / ROS 2](https://github.com/Pedronsjaja/gaia-ros2-ubuntu24) |

Cada repositório tem seus próprios arquivos, Issues e histórico. Abra dúvidas na área correspondente; inclua links quando uma mudança depender de outra área.
