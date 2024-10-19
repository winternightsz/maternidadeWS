from sqlalchemy import SmallInteger, Date, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from database import Base

class Mae(Base):
    __tablename__ = 'maes'
    
    id = Column(Integer, primary_key=True, index=True)
    cep = Column(String(9))
    nome = Column(String(100))
    logradouro = Column(String(200))
    numero = Column(Integer)
    bairro = Column(String(50))
    cidade = Column(String(50))
    fixo = Column(String(14))
    celular = Column(String(15))
    comercial = Column(String(15))
    data_nascimento = Column(Date)
    bebes = relationship("Bebe", back_populates="mae")

class Medico(Base):
    __tablename__ = 'medicos'
    
    crm = Column(Integer, primary_key=True, index=True)
    especialidade = Column(String(100))
    nome = Column(String(100))
    celular = Column(String(15))
    bebes = relationship("Bebe", back_populates="medico")

class Bebe(Base):
    __tablename__ = 'bebes'
    
    id = Column(Integer, primary_key=True, index=True)
    id_mae = Column(Integer, ForeignKey("maes.id"), nullable=False)
    crm_medico = Column(Integer, ForeignKey("medicos.crm"), nullable=False)
    nome = Column(String(100))
    data_nascimento = Column(Date)
    peso = Column(Float)
    altura = Column(SmallInteger)
    mae = relationship("Mae", back_populates="bebes")
    medico = relationship("Medico", back_populates="bebes")
