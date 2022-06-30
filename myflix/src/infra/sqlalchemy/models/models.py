from sqlalchemy import Column, String, Integer
from src.infra.sqlalchemy.config.database import Base


class Serie(Base):

    __tablename__ = 'serie'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    genero = Column(String)
    ano = Column(Integer)
    qtd_temporadas = Column(Integer)