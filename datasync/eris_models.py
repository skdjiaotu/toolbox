# coding: utf-8
from sqlalchemy import Column, DECIMAL, DateTime, Index, String, text,CHAR,Text
from sqlalchemy.dialects.mysql import INTEGER, MEDIUMINT, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

# sqlacodegen  --generator  tables schedule_statistic_order_refund  mysql+pymysql://xfang:shanghaijiayou@10.50.5.66:55193/ecshop?charset=utf8   --outfile  ./models_temp.py
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

#  sqlacodegen   mysql+pymysql://xfang:shanghaijiayou@10.50.5.66:55193/ecshop?charset=utf8 --tables schedule_statistic_order_refund  --outfile ./models_temp.py
class ScheduleStatisticOrderRefund(Base):
    __tablename__ = 'schedule_statistic_order_refund'
    __table_args__ = (
        Index('goods_purchase_id_IDX', 'order_goods_id', 'purchase_sn'),
    )

    id = Column(INTEGER(11), primary_key=True)
    refund_detail_id = Column(String(20), unique=True, server_default=text("''"), comment='退款详情id')
    order_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='订单id')
    refund_id = Column(String(20), server_default=text("''"), comment='退款id')
    external_cat_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='品类')
    external_goods_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='品类')
    goods_size = Column(String(30), nullable=False, server_default=text("''"))
    goods_color = Column(String(30), nullable=False, server_default=text("''"))
    order_sn = Column(String(64), nullable=False, server_default=text("'订单号'"))
    uniq_sku = Column(String(120), nullable=False, server_default=text("''"))
    taobao_order_sn = Column(String(255), nullable=False, server_default=text("''"))
    refund_create_stamp = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    refund_execute_date = Column(DateTime, nullable=False, index=True, server_default=text("'0000-00-00 00:00:00'"))
    level1_reason = Column(String(50), nullable=False, server_default=text("''"), comment='一级退款原因')
    level2_reason = Column(String(200), nullable=False, server_default=text("''"), comment='二级退款原因')
    level3_reason = Column(String(300), nullable=False, server_default=text("''"), comment='三级退款原因')
    refund_dep_type = Column(String(10), comment='退款部门类型,处于哪一个部门审核')
    refund_amount = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    refund_order_status = Column(String(10), nullable=False, server_default=text("'0.0'"))
    region_name = Column(String(20), nullable=False, server_default=text("''"))
    order_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    shipping_time = Column(DateTime, nullable=False, index=True, server_default=text("'0000-00-00 00:00:00'"))
    order_goods_id = Column(INTEGER(11), nullable=False)
    is_dispatch = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    refund_goods_number = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    has_image = Column(CHAR(2), nullable=False, server_default=text("''"))
    refund_type = Column(String(10), comment='退款类型')
    provider_id = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='售卖商品对应的供应商')
    purchase_sn = Column(String(200), nullable=False, server_default=text("''"), comment='工单号或者是采购单号')
    facility_id = Column(String(30), nullable=False, server_default=text("''"), comment='仓库id')
    party_id = Column(String(30), nullable=False, server_default=text("''"), comment='组织')
    from_domain = Column(String(40), nullable=False, server_default=text("''"), comment='来源网站')
    source_id = Column(INTEGER(10), server_default=text("'0'"))
    currency = Column(String(50), nullable=False, comment='货币')
    goods_price = Column(DECIMAL(10, 2), nullable=False, comment='商品单价')
    region_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='国家id')
    is_new_goods = Column(TINYINT(4), nullable=False, server_default=text("'0'"), comment='1 是新id ， 0不是新id')


#sqlacodegen   mysql+pymysql://xfang:shanghaijiayou@10.50.5.66:55193/ecshop?charset=utf8 --tables lace_info  --outfile ./models_temp.py
class LaceInfo(Base):
    __tablename__ = 'lace_info'

    id = Column(INTEGER(10), primary_key=True)
    category = Column(String(30), nullable=False, server_default=text("''"), comment='蕾丝分类')
    number = Column(String(30), nullable=False, index=True, server_default=text("''"), comment='蕾丝编码')
    location = Column(CHAR(5), nullable=False, server_default=text("''"), comment='所属地')
    party = Column(CHAR(10), nullable=False, server_default=text("'jjs'"), comment='组织编号')
    dress_id = Column(Text, comment='适用样衣ID')
    provider_code = Column(String(30), nullable=False, server_default=text("''"), comment='供应商代码')
    provider_name = Column(String(30), nullable=False, server_default=text("''"), comment='供应商名称')
    provider_number = Column(String(255), nullable=False, server_default=text("''"), comment='供应商编号')
    provider_address = Column(String(30), nullable=False, server_default=text("''"), comment='供应商地址')
    is_spot = Column(CHAR(2), nullable=False, server_default=text("''"), comment='是否现货')
    price = Column(String(30), nullable=False, server_default=text("''"), comment='现货价格')
    unit = Column(String(30), nullable=False, server_default=text("''"), comment='规格')
    size = Column(String(30), comment='尺寸规格')
    kind = Column(String(80), nullable=False, server_default=text("''"), comment='蕾丝种类')
    spot_color = Column(String(30), nullable=False, server_default=text("''"), comment='现货颜色')
    width = Column(String(30), nullable=False, server_default=text("''"), comment='门幅')
    type = Column(String(30), nullable=False, server_default=text("''"), comment='蕾丝类型')
    elastic = Column(String(30), nullable=False, server_default=text("''"), comment='弹性')
    ingredient = Column(String(30), nullable=False, server_default=text("''"), comment='成分')
    dyeing_process = Column(String(30), nullable=False, server_default=text("''"), comment='染色工艺')
    custom_moq = Column(String(30), nullable=False, server_default=text("''"), comment='定制起订量')
    custom_price = Column(String(30), nullable=False, server_default=text("''"), comment='定制价格')
    custom_cycle = Column(String(30), nullable=False, server_default=text("''"), comment='定制交期')
    standard_img = Column(String(100), nullable=False, server_default=text("''"), comment='标准图片')
    actual_img = Column(String(100), nullable=False, server_default=text("''"), comment='蕾丝店图片')
    is_collected = Column(CHAR(2), nullable=False, server_default=text("'0'"), comment='收藏')
    note = Column(String(1000), nullable=False, server_default=text("''"), comment='备注')
    remark = Column(String(256), nullable=False, server_default=text("''"), comment='设计师备注')
    is_delete = Column(CHAR(1), nullable=False, server_default=text("'0'"))
    action_user = Column(String(30), nullable=False, index=True, server_default=text("''"), comment='创建人')
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='更新时间')
    weight = Column(DECIMAL(8, 4), nullable=False, comment='物品单重')
    app_categories = Column(String(200), nullable=False, server_default=text("''"), comment='适用样衣类别')