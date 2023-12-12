#!/usr/bin/env python3
# coding=utf-8
from sqlalchemy import func

import models
import databaseSession
import pandas as pd

def dataExport():
    sourceSession = databaseSession.createSession("sourceDatabase")
    result = sourceSession.query(
        models.ScheduleStatisticOrderGood
    ).filter(
        models.ScheduleStatisticOrderGood.shipping_time >= "2023-10-01 00:00:00"
    ).filter(
        models.ScheduleStatisticOrderGood.shipping_time <= "2023-10-03 05:00:00"
    ).all()
    fileData = []
    for row in result:
        print(row)
        fileData.append({
            '采购单号': row.purchase_sn,
            "淘宝订单": row.taobao_order_sn,
            "发货时间": row.shipping_time,
            "size": row.goods_size,
            "color": row.goods_color,
            "SKU": row.uniq_sku,
            "goods_id": row.external_goods_id,
            "品类": row.external_cat_id,
            "发货数": row.goods_number,
            "价格": row.goods_price,
            "国家": row.region_name,
            "来源id": row.source_id,
            "下单时间": row.order_time,
            "供应商": row.provider_id,
            "是不是工单": row.is_dispatch,
            "工厂": row.facility_id,
            "组织": row.party_id,
            "来源网站": row.from_domain,
            "货币": row.currency,
            "国建": row.region_id,
            "是不是新品": row.is_new_goods,
            })
    sourceSession.commit()
    sourceSession.close()

    writer = pd.ExcelWriter('../data/导出发货数据.xlsx')
    data = pd.DataFrame(fileData)
    data.to_excel(writer,  sheet_name='Sheet1')
    writer.save()
    writer.close()

if __name__ == "__main__":
    dataExport()
