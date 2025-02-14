import sys
sys.path.append("E:/Anand/New Project/PictureToExcel/API/invoceapi")
from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.routes import userroutes,organizationroutes
app = FastAPI()

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (you can restrict this for security)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
# Include routes
app.include_router(userroutes.router, prefix="/users", tags=["Users"])

app.include_router(organizationroutes.router, prefix="/organizations", tags=["Organizations"])
