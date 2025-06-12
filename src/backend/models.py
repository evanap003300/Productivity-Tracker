# models.py
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

DATABASE_URL = 'sqlite:///./lifemaxxing.db'

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# SQLAlchemy Model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String, index=True)

    programming_hours_done = Column(Integer)
    body_weight = Column(Integer)
    bench_press_max = Column(Integer)
    squat_reps = Column(Integer)
    ig_followers = Column(Integer)
    linkedin_connections = Column(Integer)
    gpa = Column(Float)
    money = Column(Integer)

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic Schemas
class UserDBCreate(BaseModel):
    username: str
    password: str

    programming_hours_done: int
    body_weight: int
    bench_press_max: int
    squat_reps: int
    ig_followers: int
    linkedin_connections: int
    gpa: float
    money: int

class UserLogin(BaseModel):
    username: str
    password: str

class UserRead(BaseModel):
    id: int
    username: str
    
    programming_hours_done: int
    body_weight: int
    bench_press_max: int
    squat_reps: int
    ig_followers: int
    linkedin_connections: int
    gpa: float
    money: int

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str
    goals: list

class UpdateProgramming(BaseModel):
    programming_hours: int

class UpdateLifting(BaseModel):
    body_weight: int
    bench_max: int
    squat_max: int

class UpdateFollowers(BaseModel):
    ig_followers: int

class UpdateConnections(BaseModel):
    linkedin_connections: int

class UpdateGPA(BaseModel):
    gpa: float

class UpdateMoney(BaseModel):
    money: int
