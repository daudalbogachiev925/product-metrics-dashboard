from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.api import events, metrics

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product Metrics Dashboard", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_methods=["*"], allow_headers=["*"])
app.include_router(events.router, prefix="/api/events", tags=["events"])
app.include_router(metrics.router, prefix="/api/metrics", tags=["metrics"])

@app.get("/health")
def health():
    return {"status": "ok"}
