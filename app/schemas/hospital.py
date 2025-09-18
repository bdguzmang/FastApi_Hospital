from pydantic import BaseModel

class HospitalBase(BaseModel):
    nombre: str
    ciudad: str
    direccion: str

class HospitalCreate(HospitalBase): pass
class HospitalUpdate(HospitalBase): pass

class HospitalOut(HospitalBase):
    id: int
    class Config:
        from_attributes = True
