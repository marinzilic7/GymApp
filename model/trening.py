from __init__ import Base

from sqlalchemy import *


class Trening (Base):
    __tablename__ = "trening"
    ID_trening = Column(Integer, primary_key = True)
    ime = Column(String(50))
    vrsta =Column(String(50))
    
   
   