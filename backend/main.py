from fastapi import FastAPI
from .routers import auth, steps, user, payment
from .database import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(steps.router)
app.include_router(user.router)
app.include_router(payment.router)