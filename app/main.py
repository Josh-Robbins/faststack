from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
from app.api.v1.endpoints import items, users
from app.core.config import settings

app = FastAPI(title="FastStack")

origins = [
    "http://localhost:3000",
    "https://your-production-domain.com",
]

app.add_middleware(
    CORSMiddleware,
    GZipMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    minimum_size=1000
)

app.include_router(items.router, prefix="/api/v1/items", tags=["items"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastStack"}
