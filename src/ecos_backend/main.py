import contextlib
import os

import uvicorn

import fastapi


@contextlib.asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    yield


def create_app() -> fastapi.FastAPI:
    title: str = "Ecos REST API"
    description: str = "REST API for Ecos project"
    version: str = os.getenv("ECOS_API_VERSION", "0.1.0")
    docs_url: str = "/swagger-ui"
    redoc_url: str = "/redoc"

    app: fastapi.FastAPI = fastapi.FastAPI(
        title=title,
        description=description,
        version=version,
        docs_url=docs_url,
        redoc_url=redoc_url,
        lifespan=lifespan,
    )
    return app


if __name__ == "__main__":
    uvicorn.run("main:create_app", factory=True, reload=True, port=8000)
