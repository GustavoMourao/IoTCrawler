from sqlalchemy import Column, Integer, ForeignKey, Date, String, Float
from sqlalchemy.orm import relationship
from Database.base import Base


class Meteorologia(Base):
    __tablename__ = 'Meteorologia'

    Id = Column(Integer, primary_key=True)
    CidadeId = Column(Integer, ForeignKey('Cidades.Id'))
    DataLeitura = Column(Date)
    Nebulosidade = Column(Float)
    Umidade = Column(Float)
    Pressao = Column(Float)
    Temperatura = Column(Float)
    Sensacao = Column(Float)
    DirecaoVento = Column(Float)
    VelocidadeVento = Column(Float)
    Cidades = relationship(
        'Cidades',
        backref='Meteorologia',
        lazy='subquery'
    )

    def __init__(
        self,
        CidadeId,
        DataLeitura,
        Nebulosidade,
        Umidade,
        Pressao,
        Temperatura,
        Sensacao,
        DirecaoVento,
        VelocidadeVento
    ):
        self.CidadeId = CidadeId
        self.Nebulosidade = Nebulosidade
        self.DataLeitura = DataLeitura
        self.Umidade = Umidade
        self.Pressao = Pressao
        self.Temperatura = Temperatura
        self.Sensacao = Sensacao
        self.DirecaoVento = DirecaoVento
        self.VelocidadeVento = VelocidadeVento
