#!/usr/bin/env python3
# coding=utf-8
from sqlalchemy import func

import models
import databaseSession


def dataImport():
    sourceSession = databaseSession.createSession("sourceDatabase")
    startId = sourceSession.query(
        func.min(models.ScheduleStatisticOrderGood.id)
    ).filter(
        models.ScheduleStatisticOrderGood.shipping_time >= "2023-10-02 00:00:00"
    ).filter(
        models.ScheduleStatisticOrderGood.shipping_time <= "2023-10-02 05:00:00"
    ).scalar()

    endId = sourceSession.query(
        func.max(models.ScheduleStatisticOrderGood.id)
    ).filter(
        models.ScheduleStatisticOrderGood.shipping_time >= "2023-10-02 00:00:00"
    ).filter(
        models.ScheduleStatisticOrderGood.shipping_time <= "2023-10-02 05:00:00"
    ).scalar()
    sourceSession = databaseSession.createSession("sourceDatabase")
    resultList = []
    while startId < endId:
        result = sourceSession.query(
            models.ScheduleStatisticOrderGood
        ).filter(
            models.ScheduleStatisticOrderGood.id >= startId
        ).filter(
            models.ScheduleStatisticOrderGood.id < startId + 1000
        ).all()
        startId = startId + 1000
        resultList.extend(result)
    sourceSession.commit()

    desSession = databaseSession.createSession("desDataBase")
    resultList = resultList[0:10]
    for row in resultList:
        existData = desSession.query(models.ScheduleStatisticOrderGood).filter(
            models.ScheduleStatisticOrderGood.id == row.id
        ).first()

        if not existData:
            data = models.ScheduleStatisticOrderGood(
                id=row.id,
                order_id=row.order_id,
                order_goods_id=row.order_goods_id,
                purchase_sn=row.purchase_sn,
                taobao_order_sn=row.taobao_order_sn,
                shipping_time=row.shipping_time,
                goods_size=row.goods_size,
                goods_color=row.goods_color,
                uniq_sku=row.uniq_sku,
                external_goods_id=row.external_goods_id,
                external_cat_id=row.external_cat_id,
                goods_number=row.goods_number,
                goods_price=row.goods_price,
                region_name=row.region_name,
                source_id=row.source_id,
                order_time=row.order_time,
                provider_id=row.provider_id,
                is_dispatch=row.is_dispatch,
                facility_id=row.facility_id,
                party_id=row.party_id,
                from_domain=row.from_domain,
                currency=row.currency,
                region_id=row.region_id,
                is_new_goods=row.is_new_goods
            )
            desSession.add(data)

    desSession.commit()
    desSession.close()
    sourceSession.close()



if __name__ == "__main__":
    dataImport()
