from pydantic import BaseModel

class UpdateFollowers(BaseModel):
    ig_followers: int

class UpdateConnections(BaseModel):
    linkedin_connections: int