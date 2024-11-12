from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/fastapi-test"

# engine is interface to database. 
# It's responsible for establishing the connection and managing communication with the database.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal is a class.
# It is a session class that provides a new database session for each request.
# Created using the sessionmaker function from SQLAlchemy's orm module.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# for orm to make models connect to db table
Base = declarative_base()

# helps to provide database session to use each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()