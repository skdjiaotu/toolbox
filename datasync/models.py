# coding: utf-8
from sqlalchemy import Column, DECIMAL, DateTime, Index, String, text, CHAR, Text, SMALLINT, TIMESTAMP, Enum, Date
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


# sqlacodegen   mysql+pymysql://xfang:shanghaijiayou@10.50.5.66:55193/ecshop?charset=utf8 --tables lace_info  --outfile ./models_temp.py
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
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
                         comment='更新时间')
    weight = Column(DECIMAL(8, 4), nullable=False, comment='物品单重')
    app_categories = Column(String(200), nullable=False, server_default=text("''"), comment='适用样衣类别')


class Category(Base):
    __tablename__ = 'category'
    __table_args__ = {'comment': 'jjshouse 分类表'}

    cat_id = Column(SMALLINT, primary_key=True)
    cat_name = Column(String(90), nullable=False, server_default=text("''"))
    cat_goods_name = Column(String(90), nullable=False, server_default=text("''"),
                            comment='商品名称中显示的分类名称')
    depth = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    keywords = Column(String(255), nullable=False, server_default=text("''"))
    cat_desc = Column(String(255), nullable=False, server_default=text("''"))
    parent_id = Column(SMALLINT, nullable=False, index=True, server_default=text("'0'"))
    sort_order = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_show = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    party_id = Column(INTEGER(10), nullable=False, server_default=text("'1'"), comment='分离id')
    config = Column(Text, nullable=False, comment='配置信息，制作时间 6 - 8 等')
    erp_cat_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='erp 分类id')
    erp_top_cat_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='erp 父分类id')
    pk_cat_id = Column(TINYINT(4), nullable=False, server_default=text("'0'"), comment='see category_erp.pk_cat_id')
    is_accessory = Column(TINYINT(1), nullable=False, server_default=text("'0'"), comment='是否配件')
    last_update_time = Column(TIMESTAMP, nullable=False,
                              server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
                              comment='最后更新时间')
    hscode_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    cat_name_cn = Column(String(255), nullable=False, server_default=text("''"))


class EditorGood(Base):
    __tablename__ = 'editor_goods'
    __table_args__ = (
        Index('is_on_sale', 'is_on_sale', 'is_delete', 'is_display'),
    )

    goods_id = Column(INTEGER(10), primary_key=True)
    goods_party_id = Column(INTEGER(10), nullable=False, server_default=text("'0'"), comment='分隔不同用户')
    cat_id = Column(SMALLINT, nullable=False, index=True, server_default=text("'0'"))
    goods_sn = Column(String(60), nullable=False, index=True, server_default=text("''"))
    sku = Column(String(60), nullable=False, unique=True)
    goods_name = Column(String(255), nullable=False, server_default=text("''"))
    goods_url_name = Column(String(255), nullable=False, server_default=text("''"), comment='url 重写')
    brand_id = Column(SMALLINT, nullable=False, server_default=text("'0'"))
    goods_number = Column(SMALLINT, nullable=False, index=True, server_default=text("'0'"))
    goods_weight = Column(INTEGER(11), nullable=False, index=True, server_default=text("'0'"), comment='商品重量，克(g)')
    goods_weight_bak = Column(INTEGER(11), nullable=False, server_default=text("'0'"),
                              comment='goods_weight的备份20110420-201800')
    market_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    shop_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    no_deal_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    wrap_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"), comment='披肩价格')
    fitting_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    promote_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    promote_start = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    promote_end = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    warn_number = Column(INTEGER(11), nullable=False, server_default=text("'1'"))
    keywords = Column(String(255), nullable=False, server_default=text("''"))
    goods_brief = Column(String(1024), nullable=False)
    goods_desc = Column(Text, nullable=False)
    goods_thumb = Column(String(255), nullable=False, index=True, server_default=text("''"))
    goods_img = Column(String(255), nullable=False, server_default=text("''"))
    original_img = Column(String(255), nullable=False, server_default=text("''"))
    is_on_sale = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    add_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    is_delete = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_promote = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    last_update_time = Column(TIMESTAMP, nullable=False, index=True,
                              server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
                              comment='最后更新时间')
    goods_type = Column(SMALLINT, nullable=False, server_default=text("'0'"), comment='区分录入商品与定制生成商品')
    goods_details = Column(Text)
    is_on_sale_pending = Column(TINYINT(1), nullable=False)
    top_cat_id = Column(SMALLINT, nullable=False, index=True, server_default=text("'0'"))
    sale_status = Column(Enum('tosale', 'presale', 'shortage', 'normal', 'withdrawn', 'booking'), nullable=False,
                         server_default=text("'normal'"))
    is_display = Column(TINYINT(4), nullable=False, server_default=text("'1'"))
    is_complete = Column(TINYINT(1), nullable=False, server_default=text("'0'"), comment='编辑是否完成')
    comment_count = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='comment count')
    question_count = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='商品提问数量')
    is_new = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"), comment='是否新品')
    fb_like_count = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"), comment='facebook like')
    model_card = Column(String(100), nullable=False, server_default=text("''"), comment='模特卡')
    old_goods_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='原记录ID')
    on_sale_time = Column(TIMESTAMP, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    cp_goods_id = Column(INTEGER(11), nullable=False, index=True, server_default=text("'0'"), comment='复制商品用')


class PmsGoodsMapping(Base):
    __tablename__ = 'pms_goods_mapping'
    __table_args__ = {'comment': '共库存商品ID映射关系'}

    id = Column(INTEGER(11), primary_key=True)
    p_id = Column(INTEGER(11), nullable=False, index=True, server_default=text("'0'"), comment='商品管理系统id')
    external_goods_id = Column(INTEGER(11), nullable=False, unique=True, server_default=text("'0'"))
    master_goods_id = Column(INTEGER(11), nullable=False, index=True, server_default=text("'0'"), comment='同组商品主ID')
    pms_cat_id = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"), comment='盘古品类ID')
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, index=True, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    updated_by = Column(String(30), nullable=False, server_default=text("''"))


class GoodsSpecialShopPrice(Base):
    __tablename__ = 'goods_special_shop_price'
    __table_args__ = (
        Index('external_goods_id', 'external_goods_id', 'color', 'size'),
        Index('udx_uniq_sku', 'uniq_sku', 'external_goods_id', unique=True),
        {'comment': '低价ID数据表'}
    )

    id = Column(INTEGER(11), primary_key=True, comment='主键')
    external_goods_id = Column(INTEGER(11), nullable=False, comment='商品id')
    uniq_sku = Column(String(255), nullable=False, comment='sku')
    color = Column(String(255), nullable=False, comment='颜色')
    size = Column(String(60), nullable=False, comment='尺码')
    shop_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"), comment='售价')
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='最后一次更新时间')

class DressShawlRelation(Base):
    __tablename__ = 'dress_shawl_relations'

    abs_id = Column(INTEGER(11), primary_key=True)
    dress_id = Column(INTEGER(11), nullable=False, index=True)
    same_id = Column(INTEGER(11), index=True)
    shawl_id = Column(INTEGER(11), index=True)
    maintenance_record = Column(INTEGER(11), index=True)
