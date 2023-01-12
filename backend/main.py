from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.contact_router import contact_router
from database import async_engine
from base import Base


app = FastAPI()

app.include_router(contact_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    pass
