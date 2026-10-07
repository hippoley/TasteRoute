from fastapi import FastAPI, HTTPException

from app.config import settings
from app.qloo import QlooClient

app = FastAPI(
    title="TasteRoute",
    version="0.1.0",
    description="Taste-aware travel recommendations powered by Qloo.",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "TasteRoute"}


@app.get("/qloo/status")
def qloo_status() -> dict[str, bool]:
    return {"configured": bool(settings.qloo_api_key)}


@app.get("/qloo/ping")
async def qloo_ping() -> dict:
    try:
        client = QlooClient()
        return await client.get("/v2/insights")
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Qloo request failed: {exc}") from exc
