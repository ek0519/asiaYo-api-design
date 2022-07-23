from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


def create_app():
    app = FastAPI(title="Currency Exchange",
                  description="Exchange API",
                  docs_url="/docs",
                  redoc_url="/redoc",
                  openapi_url="/api/openapi.json")
    # app.mount("/static", StaticFiles(directory="static"), name="static")

    origins = [
        "http://localhost",
        "http://127.0.0.1",
        "http://127.0.0.1:3000",
        "https://127.0.0.1:3000",
        "http://localhost:3000",
        "https://localhost:3000",
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
