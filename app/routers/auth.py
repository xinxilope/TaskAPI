from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models, database, utils


router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):

    user = db.query(models.Users).filter(models.Users.USU_EMAIL == user_credentials.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials')

    if not utils.verify(user_credentials.password, user.USU_PASSWORD):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials')

    return {"token": "example"}