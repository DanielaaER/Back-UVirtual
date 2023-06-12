from datetime import datetime 
from sqlalchemy import Table, Column, Integer,String, Text, DateTime
from config.db import meta_data, engine 



archivos = Table("archivos", meta_data,
    Column('id', Integer, primary_key=True),
    Column("matricula", String(10)),
    Column('credencial', Text),
    Column('video', Text),
)

meta_data.bind = engine
meta_data.create_all(meta_data.bind)
