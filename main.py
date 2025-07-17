from fastapi import FastAPI
from routes.auth import router
from schema.base import Base
from database.setup import engine

app = FastAPI()
Base.metadata.create_all(engine)
app.include_router(router=router, prefix='/auth')
