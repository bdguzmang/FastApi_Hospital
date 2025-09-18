from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from app.db.base import Base

class Hospital(Base):
    __tablename__ = "hospital"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120), nullable=False)
    ciudad = Column(String(120), nullable=False)
    direccion = Column(String(200), nullable=False)
    creado_en = Column(DateTime(timezone=True), server_default=func.now())
    usuarios = relationship("Usuario", back_populates="hospital")
