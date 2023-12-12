#!/usr/bin/env python3
# coding=utf-8
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

from sqlalchemy import (
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

dbEngineMap = {}
dbDatabaseConfig = {
    'sourceDatabase': "mysql+pymysql://xfang:shanghaijiayou@10.50.5.66:55193/ecshop?charset=utf8",
    'sourceErisDatabase': "mysql+pymysql://xfang:shanghaijiayou@10.50.5.66:55193/eris?charset=utf8",
    'desDataBase': "mysql+pymysql://root:123456@10.50.5.66:3306/ecshop?charset=utf8",
}


def initDatabaseSource():
    for key in dbDatabaseConfig:
        dbEngineMap[key] = createEngine(dbDatabaseConfig[key])


def getEngine(bind="default"):
    s = dbEngineMap.get(bind, None)
    return s


def closeEngineBase(bind="default"):
    s = dbEngineMap.get(bind, None)
    if s:
        s.dispose()
    else:
        for key in dbDatabaseConfig:
            s = dbEngineMap.get(key, None)
            if s:
                s.close()


def createSession(key="sourceDatabase"):
    engine = createEngine(dbDatabaseConfig[key])
    return Session(engine)


def createEngine(databaseSourceString):
    # 创建引擎
    return create_engine(
        databaseSourceString,
        # "mysql+pymysql://tom@127.0.0.1:3306/db1?charset=utf8mb4", # 无密码时
        # 超过链接池大小外最多创建的链接
        max_overflow=0,
        # 链接池大小
        pool_size=5,
        # 链接池中没有可用链接则最多等待的秒数，超过该秒数后报错
        pool_timeout=10,
        # 多久之后对链接池中的链接进行一次回收
        pool_recycle=1,
        # 查看原生语句（未格式化）
        echo=True
    )


class DatabaseSession:
    def __init__(self):
        pass
