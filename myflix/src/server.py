from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import SessionLocal, criar_db, engine, get_db, criar_db
from src.schema import schemas
from src.infra.sqlalchemy.respositorios.serie import RepositorioSerie
from typing import List

criar_db() # Criar banco de dados
app = FastAPI()

@app.post ('/series', response_model=schemas.Serie)
def registrar_serie (serie: schemas.Serie, db:Session=Depends(get_db)):
    return RepositorioSerie(db).criar(serie)

@app.get('/series', response_model=List[schemas.Serie])
def listar_series(db: Session = Depends(get_db)):
    return RepositorioSerie(db).listar()