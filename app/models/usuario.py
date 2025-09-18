from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.db.base import Base

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120), nullable=False)
    email = Column(String(160), nullable=False, unique=True, index=True)
    rol = Column(String(20), nullable=False)
    hospital_id = Column(Integer, ForeignKey("hospital.id"), nullable=False)
    creado_en = Column(DateTime(timezone=True), server_default=func.now())
    hospital = relationship("Hospital", back_populates="usuarios")
