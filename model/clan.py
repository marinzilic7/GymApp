from __init__ import Base

from sqlalchemy import *


class Clan (Base):
    __tablename__ = "clanovi"
    ID_clana = Column(Integer, primary_key = True)
    ime = Column(String(50))
    prezime =Column(String(50))
    kontakt=Column(String(20))