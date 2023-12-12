# coding: utf-8
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class DressShawlRelation(Base):
    __tablename__ = 'dress_shawl_relations'

    abs_id = Column(INTEGER(11), primary_key=True)
    dress_id = Column(INTEGER(11), nullable=False, index=True)
    same_id = Column(INTEGER(11), index=True)
    shawl_id = Column(INTEGER(11), index=True)
    maintenance_record = Column(INTEGER(11), index=True)
