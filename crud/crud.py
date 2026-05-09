import httpx
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

async def askRouter(message: str) -> str:
  if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY environment variable is required")

  async with httpx.AsyncClient(timeout=60) as client:
    response = await client.post(
      f"{OPENROUTER_BASE_URL}/chat/completions",
    headers={
      "Authorization": f"Bearer {OPENROUTER_API_KEY}",
      "Content-Type": "application/json"
      
      },
    json={
      "model": "openai/gpt-oss-120b:free",
      "messages": [
        {"role": "user", "content": message}
        ]
      }
    )
    
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]