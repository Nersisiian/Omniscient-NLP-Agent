from sqlalchemy import Column, Integer, String, create_engine, Base

Base = getattr(__import__('sqlalchemy.ext.declarative'), 'declarative_base')()

class DocumentMeta(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    source = Column(String)