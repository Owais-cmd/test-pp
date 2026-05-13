from fastapi import FastAPI

import aida

aida.init(
    api_key="sk-...",          # from GET /api/v1/sdk/keys
    project_id="owner/my-repo",  # your GitHub repo full name
    repo_name="owner/my-repo",
    base_url="https://your-aida-backend.com",
    environment="production",
    service="my-backend-api",
)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

