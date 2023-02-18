from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# import psycopg2
# from psycopg2.extras import RealDictCursor

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost/fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# try:
#     conn = psycopg2.connect(
#         host="localhost",
#         database="fastapi",
#         user="postgres",
#         password="root",
#         cursor_factory=RealDictCursor,
#     )
#     cursor = conn.cursor()
#     print("Connection to PostgreSQL DB successful")

# except Exception as error:
#     print("Error while connecting to PostgreSQL")
#     print(error)
