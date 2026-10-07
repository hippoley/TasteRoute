from fastapi import FastAPI

app = FastAPI(
    title="TasteRoute",
    version="0.1.0",
    description="Taste-aware travel recommendations powered by Qloo.",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "TasteRoute"}
