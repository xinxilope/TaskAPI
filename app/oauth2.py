from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "jaij0ea350an53uuu349305j30n53094j305n403n4053n45"
ALGORITHM = "HS256"
ACESS_TOKEN_EXPIRE_MINUTES = 30


def create_acess_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt