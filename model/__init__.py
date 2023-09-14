from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

""" engine = create_engine("mysql+pymysql://root@localhost:3306/gym") """


engine = create_engine("mysql+pymysql://gym:gym123@mysql:3306/gym") 

session = sessionmaker(bind=engine)

session = session()

Base = declarative_base()