from __init__ import Base

from sqlalchemy import *


class Teretana (Base):
    __tablename__ = "teretana"
    ID_teretane = Column(Integer, primary_key = True)
    ime = Column(String(50))
    adresa =Column(String(50))
    kontakt=Column(Integer)