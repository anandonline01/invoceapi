import datetime
from sqlalchemy import Column, Integer, String,TIMESTAMP
from app.database import Base

# Models
class organization(Base):
    __tablename__ = "organizations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

