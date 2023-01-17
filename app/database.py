from urllib.parse import quote_plus
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


server = os.environ['taskAPIdbHOST'] 
database = os.environ['taskAPIdbDATABASE']
parametros = (
    'DRIVER={SQL Server Native Client 11.0};'
    'SERVER='+server+';'
    'DATABASE='+database+';'
    'Trusted_Connection=yes'
    )
url_db = quote_plus(parametros)
engine = create_engine('mssql+pyodbc:///?odbc_connect=%s' % url_db)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()