# GAIA mechanical engineering instructions

## Scope and source of truth

This repository holds CAD/mesh assets and mechanical documentation. Read README, `hardware/README.md`, `docs/modelo-gaia.md`, relevant `docs/estrutura/` and `docs/competicao/` files before changes. `docs/engineering-status.md` defines current gaps, priorities and study goals. `hardware/manifest.json` records integrity/provenance; it does not validate geometry or physical performance.

OP3 is a reference, not an identified GAIA model. The current assets are not a complete kinematic assembly or validated dynamics model. Use `docs/modelo-gaia.md` as the data contract for future URDF/simulation integration. The LX-225 serial driver is owned by the actuation repository; a ROS hardware interface is future integration work. `firmware/joystick_diagnostic` diagnoses buttons/OLED and does not control servos.

## Changes, evidence and attribution

Preserve architecture, raw files, attribution and third-party licenses. Do not alter CAD binaries or assign authorship/licensing without confirmed provenance. Specific licensing of supplied CAD remains unresolved; no root LICENSE is supplied. Never invent hardware, measurements or results. Mark missing data UNKNOWN / NOT_MEASURED and distinguish REAL, SIMULATED, CALCULATED and ESTIMATED data.

Prefer small changes and regression checks for corrected defects. English is primary for new R&D documentation and maintained entrypoints. Existing Portuguese technical guides and paths remain during migration; describe partial coverage honestly and preserve useful links.

For CAD, assembly, technical drawing and fabrication tasks, consult `.github/agents/gaia-cad.agent.md` and `docs/estrutura/agente-cad.md`. These define workflow; they do not prove access to CAD software or replace dimensional, simulation or hardware validation.

## Validation and Definition of Done

Check manifests, units and links as appropriate. Assembly, mass, inertia and firmware need their own validation. Static inspection and matching hashes do not prove physical operation, strength, fit or model accuracy.

Definition of Done: proportionate checks, documented changes/evidence, reproducible commands and explicit validation limits. Distinguish automatic tests, simulation, manual CAD inspection and hardware tests. Do not claim a complete GAIA model, accepted physical structure or validated Digital Twin without supporting evidence.
