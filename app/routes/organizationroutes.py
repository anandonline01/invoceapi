
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.organizations import OrganizationCreate
from app.model.organization import organization




# Create an API router
router = APIRouter()


# Create Organization
@router.post("/organizations/")
def create_organization(org: OrganizationCreate, db: Session = Depends(get_db)):
    new_org = organization(name=org.name)
    db.add(new_org)
    db.commit()
    db.refresh(new_org)
    return new_org

# Get Organizations
@router.get("/organizations/")
def get_organizations(db: Session = Depends(get_db)):
    return db.query(organization).all()

# Get Organization by ID
@router.get("/organizations/{org_id}")
def get_organization(org_id: int, db: Session = Depends(get_db)):
    org = db.query(organization).filter(organization.id == org_id).first()
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return org

# Update Organization
@router.put("/organizations/{org_id}")
def update_organization(org_id: int, org: OrganizationCreate, db: Session = Depends(get_db)):
    db_org = db.query(organization).filter(organization.id == org_id).first()
    if not db_org:
        raise HTTPException(status_code=404, detail="Organization not found")
    db_org.name = org.name
    db.commit()
    db.refresh(db_org)
    return db_org