# Multi-Project Outerbounds Repository

This repository demonstrates how to organize multiple Outerbounds projects in a single repository using the `obproject_multi.toml` configuration file.

## Repository Structure

```
.
├── obproject_multi.toml      # Multi-project manifest
├── ml-infra/                 # ML Infrastructure project
│   ├── obproject.toml
│   └── flows/
│       └── test/
│           └── flow.py
└── services/                 # MLOps Services project
    ├── obproject.toml
    └── deployments/
        ├── api/
        │   ├── main.py
        │   └── config.yml
        └── bi-dashboard/
            ├── app.py
            └── config.yml
```

## Projects

### 1. ML Infrastructure (`ml-infra`)
Contains Metaflow workflows for machine learning pipelines and data processing.

### 2. MLOps Services (`services`)
Contains deployed applications:
- **API**: FastAPI service for model serving
- **BI Dashboard**: Streamlit dashboard for business intelligence

## Deployment

### Deploy all projects:
```bash
obproject-deploy
```

### Deploy a specific project:
```bash
obproject-deploy --project ml_infra
obproject-deploy --project mlops_services
```

### CI/CD
The repository includes CI/CD configurations for:
- GitHub Actions (`.github/workflows/deploy.yml`)
- Azure DevOps (`azure-pipelines.yml`)

## Environment Variables

For CI/CD deployments, set:
- `CONTINUE_ON_ERROR=1` to continue deploying other projects if one fails
- `SPEC_ONLY=1` to only generate project specifications without deploying