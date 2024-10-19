from datetime import date
from typing import List  
from pydantic import BaseModel

class MaeBase(BaseModel):
    cep: str
    nome: str
    logradouro: str
    numero: int
    bairro: str
    cidade: str
    fixo: str
    celular: str
    comercial: str
    data_nascimento: date
class Mae(MaeBase):
    id: int
    class Config:
        orm_mode = True
class PaginatedMae(BaseModel):
    limit: int
    offset: int
    data: List[Mae]

class MedicoBase(BaseModel):
    especialidade: str
    nome: str
    celular: str
class Medico(MedicoBase):
    crm: int
    class Config:
        orm_mode = True
class PaginatedMedico(BaseModel):
    limit: int
    offset: int
    data: List[Medico]

class BebeBase(BaseModel):
    id_mae: int
    crm_medico: int
    nome: str
    data_nascimento: date
    peso: float
    altura: int
class Bebe(BebeBase):
    id: int
    mae: Mae = {}
    medico: Medico = {}
    class Config:
        orm_mode = True
class PaginatedBebe(BaseModel):
    limit: int
    offset: int
    data: List[Bebe]