import httpx

from app.config import settings


class QlooClient:
    def __init__(self) -> None:
        if not settings.qloo_api_key:
            raise RuntimeError("QLOO_API_KEY is not configured")
        self.base_url = settings.qloo_base_url.rstrip("/")
        self.headers = {"x-api-key": settings.qloo_api_key}

    async def get(self, path: str, params: dict | None = None) -> dict:
        async with httpx.AsyncClient(timeout=20.0) as client:
            response = await client.get(
                f"{self.base_url}/{path.lstrip('/')}",
                headers=self.headers,
                params=params or {},
            )
            response.raise_for_status()
            return response.json()
