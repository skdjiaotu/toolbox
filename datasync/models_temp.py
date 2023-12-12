# coding: utf-8
from sqlalchemy import Column, DECIMAL, DateTime, Index, String, text
from sqlalchemy.dialects.mysql import INTEGER, MEDIUMINT, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

#  sqlacodegen   mysql+pymysql://xfang:shanghaijiayou@10.50.5.66:55193/ecshop?charset=utf8 --tables category  --outfile ./models_temp.py
class ScheduleStatisticOrderGood(Base):
    __tablename__ = 'schedule_statistic_order_goods'
    __table_args__ = (
        Index('goods_order_goods_id_UNIQ', 'order_goods_id', 'purchase_sn', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    order_id = Column(INTEGER(11), nullable=False)
    order_goods_id = Column(INTEGER(11), nullable=False)
    purchase_sn = Column(String(200), nullable=False, comment='工单号或者是采购单号')
    taobao_order_sn = Column(String(60), nullable=False)
    shipping_time = Column(DateTime, nullable=False, index=True)
    goods_size = Column(String(30), nullable=False, server_default=text("''"))
    goods_color = Column(String(30), nullable=False, server_default=text("''"))
    uniq_sku = Column(String(120), nullable=False, server_default=text("''"))
    external_goods_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    external_cat_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    goods_number = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    goods_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"), comment='商品单价')
    region_name = Column(String(20), nullable=False, server_default=text("''"), comment='下单地区')
    source_id = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='商品款式')
    order_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"), comment='订单下单时间')
    provider_id = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='售卖商品对应的供应商')
    is_dispatch = Column(TINYINT(6), nullable=False, server_default=text("'0'"), comment='是不是工单')
    facility_id = Column(String(30), nullable=False, server_default=text("''"), comment='仓库id')
    party_id = Column(String(30), nullable=False, server_default=text("''"), comment='组织')
    from_domain = Column(String(40), nullable=False, server_default=text("''"), comment='来源网站')
    currency = Column(String(100), nullable=False, comment='货币')
    region_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='国家id')
    is_new_goods = Column(TINYINT(4), nullable=False, server_default=text("'0'"), comment='1 是新id ， 0不是新id')
