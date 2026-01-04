from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(title="Earthquake DSP Visualizer")
app.include_router(router)


@app.get("/")
async def root():
    return {"backend is running"}
