from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.user import User
from app.schemas.user import UserCreate, UserLogin
from app.services.auth import hash_password, verify_password

# Create an API router
router = APIRouter()

# Register API
@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Hash the password before storing
    hashed_password = hash_password(user.password)

    # Create new user
    new_user = User(username=user.username, password_hash=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully", "username": user.username}

# Login API
@router.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    # Fetch user from database
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Verify the password
    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Incorrect password")

    return {"message": "Login successful", "username": user.username}
