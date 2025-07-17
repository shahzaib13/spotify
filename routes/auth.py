from   fastapi import APIRouter, HTTPException, status
from model.login import LoginModel
from model.user import UserModel
from schema.user import UserTable
import bcrypt
import uuid
import jwt


router = APIRouter()

@router.get('/info')
def get():
    return 'User Is created'