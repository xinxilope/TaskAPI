from .database import Base
from sqlalchemy import DATETIME, Column, Integer, String, Boolean, text

class Post(Base):
    __tablename__ = 'T_POSTS'

    POS_ID = Column(Integer, primary_key=True, nullable=False)
    POS_TITLE = Column(String, nullable=False)
    POS_DESCRIPTION = Column(String)
    POS_PUBLISHED = Column(Boolean, server_default='TRUE', nullable=False)
    POS_CREATED_AT = Column(DATETIME(timezone=True), nullable=False, server_default=text('GETDATE()'))

