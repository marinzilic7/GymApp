from model import *
from model.relacije import *
from model.cache import region, api


ID = 2
KEY = f'id_food{ID}'
pero = region.get(KEY)
print(pero)
if pero is api.NO_VALUE:
    pero = session.query(Clanarina).filter(Clanarina.ID_food==ID).one()
    region.set(KEY, pero)
