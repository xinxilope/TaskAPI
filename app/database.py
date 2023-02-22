from urllib.parse import quote_plus
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pyodbc, os, time
from .config import settings

server = settings.TASKAPI_HOST
database = settings.TASKAPI_DATABASE
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




# while True:
#     try:
#         server = os.environ['taskAPIdbHOST'] 
#         database = os.environ['taskAPIdbDATABASE']
#         cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
#         cursor = cnxn.cursor()
#         print("Database Connected!")
#         break
#     except Exception as error:
#         print("Connecting to database failed\nError: ", error)
#         time.sleep(5)