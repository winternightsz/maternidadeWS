from fastapi import FastAPI, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from exceptions import MaeException, MedicoException, BebeException
from database import get_db, engine
import crud, models, schemas

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# mãe
@app.get("/api/maes/{mae_id}", response_model=schemas.Mae)
def get_mae_by_id(mae_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_mae_by_id(db, mae_id)
    except MaeException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/api/maes", response_model=schemas.PaginatedMae)
def get_all_maes(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_maes = crud.get_all_maes(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_maes}
    return response

@app.post("/api/maes", response_model=schemas.Mae)
def create_mae(mae: schemas.MaeBase, db: Session = Depends(get_db)):
    try:
        return crud.create_mae(db, mae)
    except MaeException as cie:
        raise HTTPException(**cie.__dict__)

@app.put("/api/maes/{mae_id}", response_model=schemas.Mae)
def update_mae(mae_id: int, mae: schemas.MaeBase, db: Session = Depends(get_db)):
    try:
        return crud.update_mae(db, mae_id, mae)
    except MaeException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/api/maes/{mae_id}")
def delete_mae_by_id(mae_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_mae_by_id(db, mae_id)
    except MaeException as cie:
        raise HTTPException(**cie.__dict__)

# médico
@app.get("/api/medicos/{medico_id}", response_model=schemas.Medico)
def get_medico_by_crm(medico_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_medico_by_crm(db, medico_id)
    except MedicoException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/api/medicos", response_model=schemas.PaginatedMedico)
def get_all_medicos(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_medicos = crud.get_all_medicos(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_medicos}
    return response

@app.post("/api/medicos", response_model=schemas.Medico)
def create_medico(medico: schemas.MedicoBase, db: Session = Depends(get_db)):
    try:
        return crud.create_medico(db, medico)
    except MedicoException as cie:
        raise HTTPException(**cie.__dict__)

@app.put("/api/medicos/{medico_id}", response_model=schemas.Medico)
def update_medico(medico_id: int, medico: schemas.MedicoBase, db: Session = Depends(get_db)):
    try:
        return crud.update_medico(db, medico_id, medico)
    except MedicoException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/api/medicos/{medico_id}")
def delete_medico_by_crm(medico_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_medico_by_crm(db, medico_id)
    except MedicoException as cie:
        raise HTTPException(**cie.__dict__)
    
# bebê
@app.get("/api/bebes/{bebe_id}", response_model=schemas.Bebe)
def get_bebe_by_id(bebe_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_bebe_by_id(db, bebe_id)
    except BebeException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/api/bebes", response_model=schemas.PaginatedBebe)
def get_all_bebes(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_bebes = crud.get_all_bebes(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_bebes}
    return response

@app.post("/api/bebes", response_model=schemas.Bebe)
def create_bebe(bebe: schemas.BebeBase, db: Session = Depends(get_db)):
    try:
        return crud.create_bebe(db, bebe)
    except BebeException as cie:
        raise HTTPException(**cie.__dict__)

@app.put("/api/bebes/{bebe_id}", response_model=schemas.Bebe)
def update_bebe(bebe_id: int, bebe: schemas.BebeBase, db: Session = Depends(get_db)):
    try:
        return crud.update_bebe(db, bebe_id, bebe)
    except BebeException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/api/bebes/{bebe_id}")
def delete_bebe_by_id(bebe_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_bebe_by_id(db, bebe_id)
    except BebeException as cie:
        raise HTTPException(**cie.__dict__)