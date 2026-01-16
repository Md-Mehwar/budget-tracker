from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import stats

app = FastAPI()


# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,

    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/api/health")
def health():
    return {"status": "ok"}


app.include_router(stats.router, prefix="/stats")

app.include_router(stats.router, prefix="/api/stats")

