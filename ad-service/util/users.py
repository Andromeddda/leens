import os
import httpx
from fastapi import HTTPException

USER_SERVICE_URL = os.environ.get("USER_SERVICE_URL", "http://user-service:8082")

# Check if user exist for safe channel and order requests
async def verify_user_exists(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{USER_SERVICE_URL}/users/{user_id}")
        if response.status_code == 404:
            raise HTTPException(status_code=400, detail=f"User {user_id} not found")
        elif response.status_code != 200:
            raise HTTPException(status_code=502, detail="User service is unavailable")
