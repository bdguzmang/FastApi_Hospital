from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.hospital import Hospital
from app.schemas.hospital import HospitalCreate, HospitalUpdate, HospitalOut

router = APIRouter(prefix="/hospitals", tags=["Hospitals"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[HospitalOut])
def list_hospitals(db: Session = Depends(get_db)):
    return db.query(Hospital).all()

@router.post("/", response_model=HospitalOut)
def create_hospital(payload: HospitalCreate, db: Session = Depends(get_db)):
    hospital = Hospital(**payload.dict())
    db.add(hospital)
    db.commit()
    db.refresh(hospital)
    return hospital

@router.get("/{hospital_id}", response_model=HospitalOut)
def get_hospital(hospital_id: int, db: Session = Depends(get_db)):
    hospital = db.query(Hospital).filter(Hospital.id == hospital_id).first()
    if not hospital:
        raise HTTPException(status_code=404, detail="Hospital not found")
    return hospital

@router.put("/{hospital_id}", response_model=HospitalOut)
def update_hospital(hospital_id: int, payload: HospitalUpdate, db: Session = Depends(get_db)):
    hospital = db.query(Hospital).filter(Hospital.id == hospital_id).first()
    if not hospital:
        raise HTTPException(status_code=404, detail="Hospital not found")
    for field, value in payload.dict().items():
        setattr(hospital, field, value)
    db.commit()
    db.refresh(hospital)
    return hospital

@router.delete("/{hospital_id}")
def delete_hospital(hospital_id: int, db: Session = Depends(get_db)):
    hospital = db.query(Hospital).filter(Hospital.id == hospital_id).first()
    if not hospital:
        raise HTTPException(status_code=404, detail="Hospital not found")
    db.delete(hospital)
    db.commit()
    return {"deleted": hospital_id}
