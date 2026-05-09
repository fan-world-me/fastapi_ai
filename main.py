from fastapi import FastAPI
from routers.router import router
import os
import uvicorn
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY environment variable is required")

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"


app.include_router(router)



if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
