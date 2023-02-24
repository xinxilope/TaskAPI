from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import DATETIME, Column, ForeignKey, Integer, String, Boolean, text

class Post(Base):
    __tablename__ = 'T_POSTS'

    POS_ID = Column(Integer, primary_key=True, nullable=False)
    POS_TITLE = Column(String, nullable=False)
    POS_DESCRIPTION = Column(String)
    POS_PUBLISHED = Column(Boolean, server_default='TRUE', nullable=False)
    POS_CREATED_AT = Column(DATETIME(timezone=True), nullable=False, server_default=text('GETDATE()'))
    POS_USU_ID = Column(Integer, ForeignKey('T_USUARIOS.USU_ID', ondelete="CASCADE"), nullable=False)

    Dono = relationship("Users")

class Users(Base):
    __tablename__ = 'T_USUARIOS'

    USU_ID = Column(Integer, primary_key=True, nullable=False)
    USU_EMAIL = Column(String(100), nullable = False, unique=True)
    USU_PASSWORD = Column(String, nullable=False)
    USU_CREATED_AT = Column(DATETIME(timezone=True), nullable=False, server_default=text('GETDATE()'))


class Likes(Base):
    __tablename__ = 'T_LIKES'

    LIK_POS_ID = Column(Integer, ForeignKey('T_POSTS.POS_ID'), primary_key=True, nullable=False)
    LIK_USU_ID = Column(Integer, ForeignKey('T_USUARIOS.USU_ID'), primary_key=True, nullable=False)