import os

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


APP_NAME = os.getenv("APP_NAME", "Simple API")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
SUB_PATH = os.getenv("SUB_PATH", "")

app = FastAPI(
    docs_url=f"{SUB_PATH}/swagger-ui",
    openapi_url=f"{SUB_PATH}/openapi.json",
    redoc_url=None,
    title="Simple Api",
    description="This is Simple API.",
    version=APP_VERSION,
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(f"{SUB_PATH}/")
async def root():
    return {"message": f"Hello {APP_NAME}!"}


@app.get(f"{SUB_PATH}/version")
async def version():
    return {"name": f"{APP_NAME}", "version": APP_VERSION}


if __name__ == "__main__":
    import uvicorn

    worker = os.getenv("WORKER", 4)
    app_port = os.getenv("APP_PORT", 8000)
    print(
        f"AZURE INTEGRATION APPLICATION ARE RUNNING WITH {worker} WORKERS AT PORT {app_port}."
    )
    uvicorn.run("main:app", host="0.0.0.0", port=app_port, workers=worker, reload=False)
