from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import traceback
comment = '''
import aida
from aida.integrations.fastapi import FastapiAidaMiddleware

# Initialize AIDA exactly as you did before
aida.init(
    api_key="e527iTm6tFYvr8rszfuFLe5yJLdLFeq35Oe0f0m_Wh8",
    project_id="owner/my-repo",
    repo_name="owner/my-repo",
    base_url="https://nondictatorially-spouseless-cornelius.ngrok-free.dev",
    environment="production",
    service="my-backend-api",
)
'''
app = FastAPI()

#app.add_middleware(FastapiAidaMiddleware)

@app.get("/")
def read_root():
    print("Received request at root endpoint...")
    raise ValueError("CRITICAL: Database connection lost during transaction!")
