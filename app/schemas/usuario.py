from pydantic import BaseModel, EmailStr, constr

class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr
    rol: constr(regex="^(admin|medico|asistente)$")
    hospital_id: int

class UsuarioCreate(UsuarioBase): pass

class UsuarioUpdate(BaseModel):
    nombre: str | None = None
    rol: constr(regex="^(admin|medico|asistente)$") | None = None

class UsuarioOut(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    rol: str
    hospital_id: int
    class Config:
        from_attributes = True
