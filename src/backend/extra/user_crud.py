from sqlmodel import Session
from .db_models import UserModel

def get_user(session: Session, user_id: int):
    return session.get(UserModel, user_id)

def update_followers(session: Session, user_id: int, new_val: int):
    user = session.get(UserModel, user_id)
    if user:
        user.ig_followers = new_val
        session.add(user)
        session.commit()
        session.refresh(user)
    return user

def update_connections(session: Session, user_id: int, new_val: int):
    user = session.get(UserModel, user_id)
    if user:
        user.linkedin_connections = new_val
        session.add(user)
        session.commit()
        session.refresh(user)
    return user