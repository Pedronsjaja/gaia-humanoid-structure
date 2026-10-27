# GAIA Humanoid Structure

Mechanical CAD assets and integration documentation for the GAIA humanoid team.

**Status: documented mechanical assets / work in progress.** Native CAD, STEP/STL supports and an integrity manifest are available. A complete GAIA kinematic assembly, identified dynamics and approved structural tests are not available.

**R&D role:** mechanical inputs for **Planned** CAD → URDF/USD → simulation → Digital Twin work. Masses, inertia, joint axes, zero positions, units and mechanical limits must be identified first. OP3 is a reference model; it does not supply GAIA measurements or become GAIA by replacing visual meshes.

English is the primary language for new R&D documentation and these entrypoints. Most detailed guides below remain in Portuguese during the transition; their paths are preserved. English coverage is not yet complete.

[Mechanical catalog](hardware/README.md) · [Model-data contract](docs/modelo-gaia.md) · [Validation gaps](docs/engineering-status.md)

Original files and team attribution are preserved. Third-party CAD authorship/licensing remains unresolved; this repository does not grant a new license to those assets.

<a id="inicio-rapido"></a>
## Start here

Explore the [mechanical catalog](hardware/README.md), select a file, confirm its dimensions and units, fabricate a test part when appropriate, and record the result before repeating fabrication or building a joint.

<a id="guia-do-projeto"></a>
## Documentation and source of truth

| Need | Reference |
| --- | --- |
| Find and download files | [GitHub basics](docs/primeiros-passos-github.md) |
| Choose CAD, STEP or STL | [Mechanical catalog](hardware/README.md) |
| Open the shared LX-224/LX-225 servo CAD | [Servo assembly](hardware/cad/servo-lx224-lx225/) |
| Find printable supports | [STL](hardware/suportes/gaia-3d/STL/) |
| Edit supports | [STEP](hardware/suportes/gaia-3d/STEP/) · [Inventor](hardware/suportes/gaia-3d/IPT/) |
| Understand mechanical deliverables | [Structure guide](docs/estrutura/README.md) |
| Follow the CAD and technical-drawing workflow | [GAIA CAD](docs/estrutura/agente-cad.md) |
| Select software for the files | [CAD software](docs/softwares-cad.md) |
| Prepare mass, axes and limits for simulation | [GAIA model-data contract](docs/modelo-gaia.md) |
| Review physical competition requirements | [Regulations](docs/competicao/README.md) · [Requirements matrix](docs/competicao/matriz-requisitos.md) |
| Prepare the auxiliary ESP32-S3 panel | [Joystick/OLED](docs/joystick.md) |
| Review missing measurements and acceptance criteria | [Engineering status](docs/engineering-status.md) |

`docs/modelo-gaia.md` defines the mechanical data required for a future robot description. Per-link mass, center of mass, inertia and frames, and per-joint axes, limits, zero, direction and servo IDs must come from identified evidence. Final joint count, dimensions and sensors are not established by the current asset catalog. The LX-225 serial driver belongs to the actuation repository; a ROS hardware interface remains future integration work.

## Assets and assembly workflow

The repository contains **29 original mechanical/reference files**, tracked in the [integrity inventory](hardware/manifest.json): servo SolidWorks files and images, four support models in IPT/STEP/STL, one additional support in IPT, and eight other LX-225 support IPT files. There is no STEP/STL of the servo body in the supplied material. File hashes establish integrity, not dimensional accuracy or mechanical suitability.

1. Review applicable competition rules and record missing dimensions.
2. Download the full CAD set with **Code → Download ZIP**, extract it and retain referenced parts together.
3. Check units, holes and fit against the actual servo. LX-224/LX-225 CAD equivalence is maintainer-reported; it requires dimensional confirmation and does not establish electrical equivalence.
4. Make one test part before repeating fabrication. No validated print profile or documented structural test is supplied.
5. Record material, process parameters, mass, clearance, joint axis and mechanical limits. Use UNKNOWN / NOT_MEASURED for missing data.
6. Deliver identified data to the [simulation team](https://github.com/Pedronsjaja/gaia-humanoid-simulation) using the model-data contract.

There is no complete GAIA assembly or approved support structural test. Opening the native servo assembly in SolidWorks was not validated during catalog organization. CAD assets alone do not establish masses, inertia, fit, strength or a validated Digital Twin.

The joystick/OLED component in `firmware/` is an auxiliary diagnostic panel. Its current firmware does not control servos.

```text
hardware/cad/          Servo CAD and reference images
hardware/suportes/     Native support parts, STEP and STL
hardware/manifest.json Original-file integrity and provenance inventory
docs/estrutura/        Mechanical workflow and deliverables
docs/modelo-gaia.md    Required physical data for modeling
docs/competicao/       Rules, sources and requirements
docs/joystick.md       Auxiliary diagnostic panel
firmware/              ESP32-S3 panel diagnostic firmware
```

The intended competition category is **CBR Humanoid**; the subcategory and applicable current rules still require confirmation. Historical regulations are labeled by edition and must not be treated as current automatically.

See [migration provenance](docs/migracao.md). Original materials retain the attribution and licensing information reported in the catalog. No root LICENSE is currently supplied; third-party CAD licensing must be resolved before redistribution or reuse that requires permission.

## Validation and learning

Use the [engineering status](docs/engineering-status.md) to close one identified joint before attempting the whole humanoid. Check manifest hashes, units, references and links. Physical fit, mass, inertia, firmware operation and structural behavior require their own evidence; static inspection does not prove them.

Study rigid transforms, SI units, joint frames and inertia through the [model-data contract](docs/modelo-gaia.md). The next useful milestone is one documented joint with an identified CAD revision, dimensions, mass, axis, direction and limits, followed by a traceable simulation/bench comparison.

## GAIA repositories

| Responsibility | Repository |
| --- | --- |
| LX-225, BusLinker, drivers and bench experiments | [Actuation](https://github.com/Pedronsjaja/gaia-lx225-buslinker) |
| Gazebo, OP3 reference, ROS 2 and autonomy experiments | [Simulation](https://github.com/Pedronsjaja/gaia-humanoid-simulation) |
| CAD, supports, assembly and physical competition requirements | [Structure](https://github.com/Pedronsjaja/gaia-humanoid-structure) |
| Ubuntu 24.04 and ROS 2 Jazzy environment | [Linux / ROS 2](https://github.com/Pedronsjaja/gaia-ros2-ubuntu24) |

Each repository owns its files, issues and history. Cross-link questions and changes that depend on another area.

<!-- Legacy section fragments retained for inbound links. -->
<a id="-comece-aqui"></a>
<a id="caminho-do-projeto"></a>
<a id="-documentação"></a>
<a id="comece-pelo-que-você-precisa"></a>
<a id="roteiro-de-montagem"></a>
<a id="organização"></a>
<a id="repositórios-da-equipe-gaia"></a>
<a id="engenharia-e-validacao"></a>
