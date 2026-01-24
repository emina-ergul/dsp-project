from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.endpoints import router

app = FastAPI(title="Earthquake DSP Visualizer")
app.include_router(router)


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


@app.get("/status")
async def status():
    return {"status": "running"}
