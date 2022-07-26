from sqlalchemy import create_engine, Table, Column, MetaData, Integer, String
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine("sqlite:///first", echo=True)

meta = MetaData()

worder = Table(
    'worker',meta,Column('id', Integer, primary_key=True), Column('name', String),

)

ins = worder.insert().values(name='ajit')
conn = engine.connect()
conn.execute(ins)
