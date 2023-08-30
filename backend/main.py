from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from db.session import engine
from db.base_class import Base
from apis.base import api_router
from apps.base import app_router


# create tables in the db;
# def create_tables():
#     Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)
    app.include_router(app_router)


def configure_staticfiles(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def start_application():
    app = FastAPI(
        title=settings.PROJECT_TITLE,
        version=settings.PROJECT_VERSION
    )
    # create_tables()   propagate the changes to tables only through alembic, not when starting the server
    include_router(app)
    configure_staticfiles(app)
    return app


app = start_application()


@app.get("/")
def hello():
    return {"msg": "Hello FastAPI 🚀"}
