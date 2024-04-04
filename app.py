import sys
from asyncio import Task
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from src.api import api
from src.logger import logger

app = FastAPI(
    title="FastAPI Quickstart",
    description="FastAPI Quickstart",
    version="0.0.1",
    docs_url="/doc",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api, prefix="/api", tags=["API"])

Path("static").mkdir(parents=True, exist_ok=True)
app.mount("/", StaticFiles(directory="static"), name="static")


async def startup_event():
    logger.info("服务启动成功")


async def stop_event():
    pass


app.add_event_handler("startup", startup_event)
app.add_event_handler("shutdown", stop_event)


def main():
    uvicorn.run(
        app="app:app",
        host="0.0.0.0",
        port=52380,
        reload="--reload" in sys.argv,
    )


if __name__ == "__main__":
    main()
