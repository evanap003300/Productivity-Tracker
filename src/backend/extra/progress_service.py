from sqlmodel import Session
from .db_models import UserModel

def calculate_progress(user: UserModel) -> list[float]:
    # Define your goals here
    programming_goal = 1000
    goal_body_weight = 187
    goal_bench = 315
    goal_squat = 315
    goal_linkedin = 500
    goal_ig = 1000
    goal_gpa = 4.0
    goal_money = 100000

    # Simulated actual values (you should store these in the DB later!)
    programming_hours = 504
    bench = 240
    squat = 265
    body_weight = 192
    linkedin = user.linkedin_connections
    ig = user.ig_followers
    gpa = 4.0
    money = 13000

    programming_pct = (programming_hours / programming_goal) * 100
    lifting_pct = ((bench / goal_bench) + (squat / goal_squat) + (goal_body_weight / body_weight)) * 100 / 3
    networking_pct = ((linkedin / goal_linkedin) + (ig / goal_ig)) * 100 / 2
    school_pct = (gpa / goal_gpa) * 100
    money_pct = (money / goal_money) * 100

    return [programming_pct, lifting_pct, networking_pct, school_pct, money_pct]