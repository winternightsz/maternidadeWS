from sqlalchemy.orm import Session
from exceptions import MaeNotFoundError, MedicoNotFoundError, BebeNotFoundError
import models, schemas

# mãe
def get_mae_by_id(db: Session, mae_id: int):
    db_mae = db.query(models.Mae).get(mae_id)
    if db_mae is None:
        raise MaeNotFoundError
    return db_mae

def get_all_maes(db: Session, offset: int, limit: int):
    return db.query(models.Mae).offset(offset).limit(limit).all()

def create_mae(db: Session, mae: schemas.MaeBase):
    db_mae = models.Mae(**mae.dict())
    db.add(db_mae)
    db.commit()
    db.refresh(db_mae)
    return db_mae

def update_mae(db: Session, mae_id: int, mae: schemas.MaeBase):
    db_mae = get_mae_by_id(db, mae_id)
    db_mae.cep = mae.cep
    db_mae.nome = mae.nome
    db_mae.logradouro = mae.logradouro
    db_mae.numero = mae.numero
    db_mae.bairro = mae.bairro
    db_mae.cidade = mae.cidade
    db_mae.fixo = mae.fixo
    db_mae.celular = mae.celular
    db_mae.comercial = mae.comercial
    db_mae.data_nascimento = mae.data_nascimento
    db.commit()
    db.refresh(db_mae)
    return db_mae

def delete_mae_by_id(db: Session, mae_id: int):
    db_mae = get_mae_by_id(db, mae_id)
    db.delete(db_mae)
    db.commit()
    return

# médico
def get_medico_by_crm(db: Session, medico_crm: int):
    db_medico = db.query(models.Medico).get(medico_crm)
    if db_medico is None:
        raise MedicoNotFoundError
    return db_medico

def get_all_medicos(db: Session, offset: int, limit: int):
    return db.query(models.Medico).offset(offset).limit(limit).all()

def create_medico(db: Session, medico: schemas.MedicoBase):
    db_medico = models.Medico(**medico.dict())
    db.add(db_medico)
    db.commit()
    db.refresh(db_medico)
    return db_medico

def update_medico(db: Session, medico_crm: int, medico: schemas.MedicoBase):
    db_medico = get_medico_by_crm(db, medico_crm)
    db_medico.nome = medico.nome
    db_medico.especialidade = medico.especialidade
    db_medico.celular = medico.celular
    db.commit()
    db.refresh(db_medico)
    return db_medico

def delete_medico_by_crm(db: Session, medico_crm: int):
    db_medico = get_medico_by_crm(db, medico_crm)
    db.delete(db_medico)
    db.commit()
    return

# bebê
def get_bebe_by_id(db: Session, bebe_id: int):
    db_bebe = db.query(models.Bebe).get(bebe_id)
    if db_bebe is None:
        raise BebeNotFoundError
    return db_bebe

def get_all_bebes(db: Session, offset: int, limit: int):
    return db.query(models.Bebe).offset(offset).limit(limit).all()

def create_bebe(db: Session, bebe: schemas.BebeBase):
    db_bebe = models.Bebe(**bebe.dict())
    db.add(db_bebe)
    db.commit()
    db.refresh(db_bebe)
    return db_bebe

def update_bebe(db: Session, bebe_id: int, bebe: schemas.BebeBase):
    db_bebe = get_bebe_by_id(db, bebe_id)
    db_bebe.crm_medico = bebe.crm_medico
    db_bebe.id_mae = bebe.id_mae
    db_bebe.nome = bebe.nome
    db_bebe.data_nascimento = bebe.data_nascimento
    db_bebe.peso = bebe.peso
    db_bebe.altura = bebe.altura
    db.commit()
    db.refresh(db_bebe)
    return db_bebe

def delete_bebe_by_id(db: Session, bebe_id: int):
    db_bebe = get_bebe_by_id(db, bebe_id)
    db.delete(db_bebe)
    db.commit()
    return