from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv
import os

load_dotenv()  # reads your .env file

DATABASE_URL = os.getenv("DATABASE_URL") #access the database URL

# The engine is the actual connection to PostgreSQL
engine = create_async_engine(DATABASE_URL) #the engine knows the database is, how to connect to it and how to send queries to the SQL

# A session is like a conversation with the database
# The session handles creating, reading, updating and deleting records
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Base is the parent class all your table models will inherit from
class Base(DeclarativeBase):
    pass

# This is a "dependency" — FastAPI calls it automatically to give each
# endpoint a fresh database session, then closes it when the request is done
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session