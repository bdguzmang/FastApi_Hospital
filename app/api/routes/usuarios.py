from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate, UsuarioOut

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[UsuarioOut])
def list_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

@router.post("/", response_model=UsuarioOut)
def create_usuario(payload: UsuarioCreate, db: Session = Depends(get_db)):
    usuario = Usuario(**payload.dict())
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

@router.get("/{usuario_id}", response_model=UsuarioOut)
def get_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return usuario

@router.put("/{usuario_id}", response_model=UsuarioOut)
def update_usuario(usuario_id: int, payload: UsuarioUpdate, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario not found")
    for field, value in payload.dict(exclude_unset=True).items():
        setattr(usuario, field, value)
    db.commit()
    db.refresh(usuario)
    return usuario

@router.delete("/{usuario_id}")
def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario not found")
    db.delete(usuario)
    db.commit()
    return {"deleted": usuario_id}
