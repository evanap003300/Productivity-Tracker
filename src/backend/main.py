from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from models import UserCreate, UpdateFollowers, UpdateConnections, get_db, User, UserDBCreate, UserRead, UpdateProgramming, UpdateGPA, UpdateLifting, UpdateMoney, UserLogin
from typing import List
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

app = FastAPI()

user1 = UserCreate(
    username = 'evanap0330',
    goals = ['Programming', 'Lifting', 'Networking', 'School', 'Money']
)

origins = [
    "http://localhost:3000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

programming_hours_done = 504
programming_hours_goal = 1000

programming_goal_completion = (programming_hours_done / programming_hours_goal) * 100

actual_body_weight = 192
actual_bench_press_max = 240
actual_squat_reps = 265

goal_body_weight = 187
goal_bench_press_max = 315
goal_squat_reps = 315

lifing_goal_completion = (
    (actual_bench_press_max / goal_bench_press_max)
    + (actual_squat_reps / goal_squat_reps)
    + (goal_body_weight / actual_body_weight)
) * 100 / 3

actual_linkedin_connections = 162
actual_ig_followers = 450

goal_linkedin_connections = 500
goal_ig_followers = 1000

networking_goal_completion = ((actual_linkedin_connections / goal_linkedin_connections) + (actual_ig_followers / goal_ig_followers)) * 100 / 2

actual_gpa = 4.0
goal_gpa = 4.0

school_goal_completion = (actual_gpa / goal_gpa) * 100

actual_money = 13000
goal_money = 100000

money_goal_completion = (actual_money / goal_money) * 100

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    return user

@app.get("/progress/{user_id}")
def get_progress(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"error": "User not found"}

    programming_goal_completion = (user.programming_hours_done / 1000) * 100
    lifting_goal_completion = ((user.bench_press_max / 315) + (user.squat_reps / 315) + (187 / user.body_weight)) * 100 / 3
    networking_goal_completion = ((user.linkedin_connections / 500) + (user.ig_followers / 1000)) * 100 / 2
    school_goal_completion = (user.gpa / 4.0) * 100
    money_goal_completion = (user.money / 100000) * 100

    return {
        "progress": [
            programming_goal_completion,
            lifting_goal_completion,
            networking_goal_completion,
            school_goal_completion,
            money_goal_completion
        ]
    }

@app.post('/users/')
def create_user(user: UserDBCreate, db: Session = Depends(get_db)):
    user_hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=user_hashed_password, 
                   programming_hours_done=user.programming_hours_done, body_weight=user.body_weight,
                   bench_press_max=user.bench_press_max, squat_reps=user.squat_reps,
                   ig_followers=user.ig_followers, linkedin_connections=user.linkedin_connections,
                   gpa=user.gpa, money=user.money)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get('/users/', response_model=List[UserRead])
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users 

# Updates

@app.put("/users/update-connections/{user_id}")
def update_user(user_id: int, update_connections: UpdateConnections, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return 'User not found'
    
    user.linkedin_connections = update_connections.linkedin_connections

    db.commit()
    db.refresh(user)
    return user

@app.put("/users/update-programming/{user_id}")
def update_programming(user_id: int, data: UpdateProgramming, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.programming_hours_done = data.programming_hours
    db.commit()
    db.refresh(user)
    return user

@app.put("/users/update-lifting/{user_id}")
def update_lifting(user_id: int, data: UpdateLifting, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.body_weight = data.body_weight
    user.bench_press_max = data.bench_max
    user.squat_reps = data.squat_max
    db.commit()
    db.refresh(user)
    return user

@app.put("/users/update-followers/{user_id}")
def update_followers(user_id: int, data: UpdateFollowers, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.ig_followers = data.ig_followers
    db.commit()
    db.refresh(user)
    return user

@app.put("/users/update-gpa/{user_id}")
def update_gpa(user_id: int, data: UpdateGPA, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.gpa = data.gpa
    db.commit()
    db.refresh(user)
    return user

@app.put("/users/update-money/{user_id}")
def update_money(user_id: int, data: UpdateMoney, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.money = data.money
    db.commit()
    db.refresh(user)
    return user

@app.post('/login/')
def post_login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    
    if not db_user:
        return {"message": "User not found"}

    if verify_password(user.password, db_user.hashed_password):
        return {"message": "Login successful"}
    else:
        return {"message": "Incorrect password"}
