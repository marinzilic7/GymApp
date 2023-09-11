
from sqlalchemy.orm import relationship
from clan import Clan
from teretana import Teretana
from trener import Trener
from trening import Trening
from clanarina import Clanarina
from __init__ import Base
from __init__  import engine


Clan.clanarina = relationship('Clanarina', back_populates='clanarina')
Teretana.clanarina = relationship('Clanarina', back_populates='teretana')
Trener.clanarina = relationship('Clanarina', back_populates='trener')



Base.metadata.bind = engine
Base.metadata.create_all(bind=engine)