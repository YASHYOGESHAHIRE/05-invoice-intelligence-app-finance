id="frg5po"
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse

from sqlalchemy.orm import Session

from database import get_db
from models import User

from passlib.context import CryptContext

from jose import jwt

from authlib.integrations.starlette_client import OAuth

from pydantic import BaseModel

from dotenv import load_dotenv

from datetime import datetime, timedelta

import os


# =========================
# Load Environment Variables
# =========================

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_HOURS = 24


# =========================
# Router
# =========================

router = APIRouter()


# =========================
# Password Hashing
# =========================


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",

    bcrypt__rounds=12
)


# =========================
# OAuth Setup
# =========================

oauth = OAuth()

oauth.register(
    name="google",

    client_id=GOOGLE_CLIENT_ID,

    client_secret=GOOGLE_CLIENT_SECRET,

    server_metadata_url=(
        "https://accounts.google.com/.well-known/openid-configuration"
    ),

    client_kwargs={
        "scope": "openid email profile"
    }
)


# =========================
# Pydantic Schemas
# =========================

class SignupSchema(BaseModel):
    email: str
    password: str
    name: str


class LoginSchema(BaseModel):
    email: str
    password: str


# =========================
# Password Functions
# =========================

def hash_password(password: str):

    password = password[:72]

    return pwd_context.hash(password)



def verify_password(
    plain_password,
    hashed_password
):

    plain_password = plain_password[:72]

    return pwd_context.verify(
        plain_password,
        hashed_password
    )



# =========================
# JWT Token
# =========================

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        hours=ACCESS_TOKEN_EXPIRE_HOURS
    )

    to_encode.update(
        {
            "exp": expire
        }
    )

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


# =========================
# Email Signup
# =========================

@router.post("/signup")
def signup(
    user: SignupSchema,
    db: Session = Depends(get_db)
):

    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    hashed_password = hash_password(
        user.password
    )

    new_user = User(
        email=user.email,
        hashed_password=hashed_password,
        name=user.name
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    token = create_access_token(
        {
            "sub": new_user.email
        }
    )

    return {
        "message": "Signup successful",
        "access_token": token,
        "user": {
            "email": new_user.email,
            "name": new_user.name
        }
    }


# =========================
# Email Login
# =========================

@router.post("/login")
def login(
    user: LoginSchema,
    db: Session = Depends(get_db)
):

    db_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if not db_user:

        raise HTTPException(
            status_code=400,
            detail="Invalid credentials"
        )

    if not db_user.hashed_password:

        raise HTTPException(
            status_code=400,
            detail="Use Google login"
        )

    if not verify_password(
        user.password,
        db_user.hashed_password
    ):

        raise HTTPException(
            status_code=400,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "sub": db_user.email
        }
    )

    return {
        "message": "Login successful",
        "access_token": token,
        "user": {
            "email": db_user.email,
            "name": db_user.name
        }
    }


# =========================
# Google Login
# =========================

@router.get("/google/login")
async def google_login(
    request: Request
):

    redirect_uri = request.url_for(
        "google_callback"
    )

    return await oauth.google.authorize_redirect(
        request,
        redirect_uri
    )


# =========================
# Google Callback
# =========================

@router.get("/google/callback")
async def google_callback(
    request: Request,
    db: Session = Depends(get_db)
):

    token = await oauth.google.authorize_access_token(
        request
    )

    user_info = token.get("userinfo")

    if not user_info:

        raise HTTPException(
            status_code=400,
            detail="Google authentication failed"
        )

    email = user_info["email"]

    google_id = user_info["sub"]

    name = user_info.get("name")


    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:

        user = User(
            email=email,
            google_id=google_id,
            name=name
        )

        db.add(user)

        db.commit()

        db.refresh(user)

    jwt_token = create_access_token(
        {
            "sub": user.email
        }
    )

    return RedirectResponse(
        url=f"http://localhost:8000/success?token={jwt_token}"
    )

