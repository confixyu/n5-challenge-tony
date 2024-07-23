import os
import uvicorn
from fastapi import FastAPI, Request, Depends, Form
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse
from typing import Annotated

from src.config.settings import settings
from src.presentation.rest_api.router import api_router
from src.presentation.web_render.admin.render import web_router
from src.config.database import Base, engine


app = FastAPI(title=settings.MS_NAME, openapi_url=f"/openapi.json")
Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"health_check": "N5 Challenge :D"}


app.include_router(api_router)
app.include_router(web_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
