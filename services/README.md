# MLOps Services

Deployed applications and dashboards.

## Apps

- **api/** - FastAPI service for model serving
- **bi-dashboard/** - Streamlit dashboard for business intelligence

## Local Development

```bash
cd services/deployments/api
uvicorn main:app --reload
```

## Deploy

```bash
obproject-deploy
```
