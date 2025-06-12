from fastapi import APIRouter, Depends
from sqlmodel import Session

from .database import get_session
from .schema import UpdateFollowers, UpdateConnections
from .user_crud import get_user, update_followers, update_connections
from .progress_service import calculate_progress

router = APIRouter()

@router.get("/user/{user_id}")
def read_user(user_id: int, session: Session = Depends(get_session)):
    return get_user(session, user_id)

@router.post("/update-followers")
def post_followers(data: UpdateFollowers, session: Session = Depends(get_session)):
    return update_followers(session, user_id=1, new_val=data.ig_followers)

@router.post("/update-connections")
def post_connections(data: UpdateConnections, session: Session = Depends(get_session)):
    return update_connections(session, user_id=1, new_val=data.linkedin_connections)

@router.get("/progress/")
def get_progress(session: Session = Depends(get_session)):
    user = get_user(session, user_id=1)
    return calculate_progress(user)