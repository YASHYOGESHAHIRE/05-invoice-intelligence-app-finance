id="o31xqr"
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from starlette.middleware.sessions import SessionMiddleware

from database import Base, engine

from auth import router as auth_router

import os
from dotenv import load_dotenv


# =========================
# Load ENV
# =========================

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")


# =========================
# Create Tables
# =========================

Base.metadata.create_all(bind=engine)


# =========================
# FastAPI App
# =========================

app = FastAPI()


# =========================
# Session Middleware
# =========================

app.add_middleware(
    SessionMiddleware,
    secret_key=SECRET_KEY
)


# =========================
# CORS
# =========================

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)



# =========================
# Routers
# =========================

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)


# =========================
# Routes
# =========================

@app.get("/")
def home():

    return {
        "message": "FastAPI Auth System Running"
    }


@app.get("/success")
def success(token: str):

    return {
        "message": "Google Login Successful",
        "token": token
    }

