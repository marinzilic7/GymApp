from __init__ import Base

from sqlalchemy import *


class Trener (Base):
    __tablename__ = "treneri"
    ID_trenera = Column(Integer, primary_key = True)
    ime = Column(String(50))
    prezime =Column(String(50))
    kontakt=Column(String(20))