from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# import os
# from dotenv import load_dotenv

# load_dotenv(dotenv_path=".env")

# db_user = os.getenv("POSTGRES_USER")
# db_password = os.getenv("POSTGRES_PASSWORD")
# db_name = os.getenv("POSTGRES_DB")
# db_host = os.getenv("DB_HOST")
# db_port = os.getenv("DB_PORT")

# DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
# engine = create_engine(DATABASE_URL)
engine = create_engine("postgresql://olist:postgresql@localhost:5432/olist")
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()