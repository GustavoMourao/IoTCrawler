from sqlalchemy import Column, Integer, String, Float
from Database.base import Base


class Cidades(Base):
    __tablename__ = 'Cidades'

    Id = Column(Integer, primary_key=True)
    Nome = Column(String)
    Latitude = Column(Float)
    Longitude = Column(Float)

    def __init__(self, Nome, Latitude, Longitude):
        self.Nome = Nome
        self.Latitude = Latitude
        self.Longitude = Longitude
