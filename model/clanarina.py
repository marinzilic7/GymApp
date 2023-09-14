from __init__ import Base

from sqlalchemy import *


class Clanarina (Base):
    __tablename__ = "clanarina"
    ID_Clanarina = Column(Integer, primary_key = True)
    ID_clana = Column(Integer, ForeignKey('clanovi.ID_clana', ondelete="CASCADE"))
    ID_trenera = Column(Integer, ForeignKey('treneri.ID_trenera', ondelete="CASCADE"))
    ID_trening = Column(Integer, ForeignKey('trening.ID_trening', ondelete="CASCADE"))
    trajanje = Column(String(50));

   
   
   