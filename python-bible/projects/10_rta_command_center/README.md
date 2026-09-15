# RTA Command Center — Final Capstone

## Pipeline

Ingestion → mapping → data quality → calculation engine → risk engine → analytics → API → dashboard → tests → deployment.

## Required engineering gates

- 30-minute interval model
- Offered as demand metric
- AHT target: 20:00 / 1,200 seconds
- SLA targets: CountyCare 90%, Premera 85%, MPC 85%, SOMOS 80%
- Answer-time target: 30 seconds
- Occupancy target: 80%
- Shrinkage: 25%
- UM skills remain separate from existing LOBs
- Retention skills excluded from RTA calculations and risk rollups
- Pharmacy excluded
- PostgreSQL persistence
- FastAPI service boundary
- pytest unit/integration coverage
- structured logging
- authentication and authorization
- Docker + CI/CD

The capstone must demonstrate that the learner can design, implement, test, debug, optimize, package and deploy a production-style Python system.
