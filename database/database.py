from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

user = 'root'
password = 'RcBaR_-315'
host = '127.0.0.1'
port = '3306'
database_name = 'BDH'

url = f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database_name}'
engine = create_engine(url)

Session = sessionmaker(bind=engine)
session = Session()
