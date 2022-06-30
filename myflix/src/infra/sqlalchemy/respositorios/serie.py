from src.infra.sqlalchemy.models import models
from src.schema import schemas
from .main import RepositorioBase

class RepositorioSerie(RepositorioBase):
    def criar (self, serie: schemas.Serie):
        db_serie = models.Serie(nome = serie.nome,
                                genero = serie.genero,
                                ano = serie.ano,
                                qtd_temporadas = serie.qtd_temporadas)
        self.db.add(db_serie)
        self.db.commit()
        self.db.refresh(db_serie)
        return db_serie   

    def listar(self):
        series = self.db.query(models.Serie).all()
        return series                    