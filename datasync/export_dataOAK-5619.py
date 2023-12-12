#!/usr/bin/env python3
# coding=utf-8
import asyncio
from decimal import Decimal

from sqlalchemy import func, or_

import models
import databaseSession
import pandas as pd

CATEGORY = {
    '1': '蕾丝',
    '2': '花边',
    '3': '朵花',
    '4': '辅料',
}

PARTY = {
    "65598": "海外业务样衣FD",
    "65535": "总公司",
    "65599": "Tendaisy",
    "65600": "AiryDress-New",
    "65581": "海外业务耗材",
    "65601": "海外业务样衣VV",
    "65602": "Lambkingo",
    "65603": "smalo",
    "65582": "Azazie",
    "65583": "LoveProm",
    "65584": "海外业务样衣",
    "65542": "海外业务",
    "65585": "ND",
    "65545": "jjshouse",
    "65586": "MoonProm",
    "65587": "海外业务样衣VB",
    "65588": "floryday",
    "65589": "海外业务样衣AZ",
    "65554": "Amormoda",
    "65560": "faucetland",
    "65564": "JenJenHouse",
    "65567": "JennyJoseph",
    "65590": "DressAdore",
    "65591": "AZCA",
    "65570": "Amormoda2",
    "65592": "AiryDress",
    "65593": "InvitationsKnot",
    "65578": "DressDepot",
    "65579": "DressFirst",
    "65580": "VBridal",
    "65594": "VeryVoga",
    "65595": "SisDress",
    "65596": "PPML",
    "65597": "lalamira"
}


def getShipmentData(goodsIdSet, startTime, endTime):
    resultList = []
    sourceSession = databaseSession.createSession("sourceDatabase")
    for i in range(0, len(goodsIdSet), 2000):
        b = goodsIdSet[i:i + 2000]

        result = sourceSession.query(
            models.ScheduleStatisticOrderGood.external_goods_id,
            models.ScheduleStatisticOrderGood.external_cat_id,
            models.EditorGood.is_on_sale,
            func.CONCAT(models.Category.cat_id, '_', models.Category.cat_name).label('cat_name'),
            func.SUM(models.ScheduleStatisticOrderGood.goods_number).label("shipment_number")
        ).join(
            models.Category, models.ScheduleStatisticOrderGood.external_cat_id == models.Category.cat_id
        ).join(
            models.EditorGood, models.ScheduleStatisticOrderGood.external_goods_id == models.EditorGood.goods_id
        ).where(
            models.ScheduleStatisticOrderGood.shipping_time >= startTime
        ).where(
            models.ScheduleStatisticOrderGood.shipping_time < endTime
        ).where(
            models.ScheduleStatisticOrderGood.external_goods_id.in_(b)
        ).group_by(models.ScheduleStatisticOrderGood.external_goods_id).all()

        resultList.extend(result)

    return resultList


def getRefundData(goodsIdSet, startTime, endTime):
    resultList = []
    sourceSession = databaseSession.createSession("sourceDatabase")
    for i in range(0, len(goodsIdSet), 2000):
        b = goodsIdSet[i:i + 2000]
        result = sourceSession.query(
            models.ScheduleStatisticOrderRefund.external_goods_id,
            models.ScheduleStatisticOrderRefund.external_cat_id,
            models.EditorGood.is_on_sale,
            func.CONCAT(models.Category.cat_id, '_', models.Category.cat_name).label('cat_name'),
            func.SUM(models.ScheduleStatisticOrderRefund.refund_goods_number).label("refund_number")
        ).join(
            models.Category, models.ScheduleStatisticOrderRefund.external_cat_id == models.Category.cat_id
        ).join(
            models.EditorGood, models.ScheduleStatisticOrderRefund.external_goods_id == models.EditorGood.goods_id
        ).where(
            models.ScheduleStatisticOrderRefund.shipping_time >= startTime
        ).where(
            models.ScheduleStatisticOrderRefund.shipping_time < endTime
        ).where(
            models.ScheduleStatisticOrderRefund.external_goods_id.in_(b)
        ).group_by(models.ScheduleStatisticOrderRefund.external_goods_id).all()

        resultList.extend(result)

    return resultList


def getSampleCloth():
    # 2	轻排花
    # 3	重排花
    sourceSession = databaseSession.createSession("sourceDatabase")
    sql = """
           select gs.cloth_style_id as style_id
                , cs.style
                ,gs.goods_id 
                ,pgm.p_id 
            from ecshop.goods_style gs                
            left join ecshop.cloth_style cs ON cs.id = gs.cloth_style_id
            inner join ecshop.editor_goods eg   ON gs.goods_id = eg.goods_id
            left join ecshop.pms_goods_mapping as pgm   ON pgm.external_goods_id  = eg.goods_id
            where 1
              and gs.cloth_style_id in(2,3)
    """
    data = sourceSession.execute(sql)
    resultList = {}
    pidResult = {}
    pidMap = {}
    for row in data:
        key = str(row.goods_id)
        if key not in resultList:
            resultList[key] = []
        resultList[key].append(row)
        pidMap[key] = str(row.p_id)

    for key, value in resultList.items():
        pidKey = pidMap[key]
        if pidKey not in pidResult:
            pidResult[pidKey] = []
        pidResult[pidKey].append(value)

    return resultList, pidResult


def getLaceSample():
    sourceSession = databaseSession.createSession("sourceDatabase")
    goodsIdLaceIdDict = dict()
    lastId = 0
    dataList = []
    while True:
        result = sourceSession.query(
            models.LaceInfo
        ).where(
            models.LaceInfo.id > lastId
        ).order_by(models.LaceInfo.id.asc()).limit(2000).all()

        if len(result) <= 0:
            break
        lastId = max([row.id for row in result])
        dataList.extend(result)

    loop = asyncio.get_event_loop()
    tasks = [formateData(dataList[0:100], 0),
             formateData(dataList[100:200], 1),
             formateData(dataList[200:300], 2),
             formateData(dataList[300:400], 3),
             formateData(dataList[400:500], 4),
             formateData(dataList[500:600], 5),
             formateData(dataList[600:700], 6),
             formateData(dataList[700:800], 7),
             formateData(dataList[800:900], 8),
             formateData(dataList[1000:1100], 9),
             formateData(dataList[1100:1200], 10),
             formateData(dataList[1200:], 11),
             ]

    done, _ = loop.run_until_complete(asyncio.wait(tasks))

    for fut in done:
        for k, v in fut.result().items():
            if k not in goodsIdLaceIdDict:
                goodsIdLaceIdDict[k] = v

    return goodsIdLaceIdDict


async def formateData(result, i):
    goodsIdLaceIdDict = {}
    for row in result:
        if len(row.dress_id) > 0:
            dressIdList, isLaceAllSale = await getGoodsIdAndLaceStatus(row)
            for dressId in dressIdList:
                if dressId not in goodsIdLaceIdDict:
                    goodsIdLaceIdDict[dressId] = []

                goodsIdLaceIdDict[dressId].append({
                    "lace_id": row.id,
                    "lace_number": row.number,
                    "location": row.location,
                    "kind": row.kind,
                    "create_time": row.create_time,
                    "is_delete": row.is_delete,
                    "is_lace_all_sale": isLaceAllSale,
                    "app_categories": row.app_categories,
                    "category": CATEGORY[str(row.category)],
                })

    return goodsIdLaceIdDict


async def getGoodsIdAndLaceStatus(row):
    dressIdList = row.dress_id.replace('；', ';').strip(';').split(";")
    pIdGidMap = getPidGidDataByGid(dressIdList)
    pidGid = set()
    for pidGidRow in pIdGidMap:
        pidGid.add(str(pidGidRow.external_goods_id))

    sameIsList = getShawlData(dressIdList)
    isLaceAllSale = False
    for sameRow in sameIsList:
        dressIdList.append(sameRow)

    dressIdList = list(set(dressIdList).union(pidGid))

    gidDress = getPidGidDataByGidV2(dressIdList)
    for dressRow in gidDress:
        goodsId = str(dressRow.external_goods_id)
        if goodsId not in dressIdList:
            dressIdList.append(goodsId)
        if not isLaceAllSale:
            isLaceAllSale = dressRow.is_on_sale == 1

    return dressIdList, isLaceAllSale


def getOnGidData(gid):
    sourceSession = databaseSession.createSession("sourceDatabase")
    result = sourceSession.query(
        models.LaceInfo
    ).where(
        models.LaceInfo.id.in_(gid)
    ).order_by(models.LaceInfo.id.asc()).limit(2000).all()

    goodsIdLaceIdDict = {}
    loop = asyncio.get_event_loop()
    tasks = [formateData(result, 1), ]
    done, _ = loop.run_until_complete(asyncio.wait(tasks))
    for fut in done:
        for k, v in fut.result().items():
            if k not in goodsIdLaceIdDict:
                goodsIdLaceIdDict[k] = v

    return goodsIdLaceIdDict


def getGoodsAttributes(goodsIdSet):
    sourceSession = databaseSession.createSession("sourceDatabase")
    fabricMap = {}
    fabricPidMap = {}
    for i in range(0, len(goodsIdSet), 1500):
        b = map(lambda x: str(x), goodsIdSet[i:i + 1500])
        goodsIdArray = ','.join(b).replace('text', '0')
        sql = """
                SELECT 
                    ga.goods_id 
                    , al.attr_name
                    , pgm.p_id
                    , if(ea.attr_type = 'text',egal.attr_value,al.attr_values) as attr_value  
                FROM eris.editor_goods_attr AS ga
                         inner join ecshop.pms_goods_mapping AS pgm on pgm.external_goods_id = ga.goods_id                                                                 
                         inner join eris.editor_attribute AS ea on ga.attr_id = ea.attr_id
                                                                     and ea.is_delete = 0
                                                                     and ea.is_show = 1
                         inner join eris.editor_attribute_languages AS al ON al.attr_id = ea.attr_id 
                                                                    and al.languages_id = 1
                         left join  eris.editor_goods_attr_languages as egal on egal.goods_attr_id = ga.goods_attr_id 
                                                                    and egal.languages_id = 1 
                WHERE ga.goods_id in ({0})
                  and ga.is_show = 1
                  and ga.is_delete = 0
                  and al.attr_name = 'Fabric'
                """.format(goodsIdArray)

        fabricList = sourceSession.execute(sql)
        fabricSet = {}
        pidMap = {}
        for row in fabricList:
            key = str(row.goods_id)
            if key not in fabricSet:
                fabricSet[key] = set()
            fabricSet[key].add(row.attr_value)
            pidMap[key] = str(row.p_id)

        for k, v in fabricSet.items():
            fabricMap[k] = ','.join(v)
            if pidMap[k] not in fabricPidMap:
                fabricPidMap[pidMap[k]] = []
            fabricPidMap[pidMap[k]].append(fabricMap[k])

    return fabricMap, fabricPidMap


def getPid(goodsIdSet):
    sourceSession = databaseSession.createSession("sourceDatabase")
    gidMap = {}
    for i in range(0, len(goodsIdSet), 2000):
        b = map(lambda x: str(x), goodsIdSet[i:i + 2000])
        result = sourceSession.query(
            models.PmsGoodsMapping.external_goods_id,
            models.PmsGoodsMapping.p_id,
        ).where(
            models.PmsGoodsMapping.external_goods_id.in_(b)
        ).group_by(models.PmsGoodsMapping.external_goods_id).all()

        for row in result:
            key = str(row.external_goods_id)
            gidMap[key] = row.p_id

    return gidMap


def getEditorGoods(goodsIdSet):
    sourceSession = databaseSession.createSession("sourceDatabase")
    goodsMap = {}
    for i in range(0, len(goodsIdSet), 2000):
        b = map(lambda x: str(x), goodsIdSet[i:i + 2000])
        result = sourceSession.query(
            models.EditorGood.goods_id,
            models.EditorGood.is_on_sale,
            models.EditorGood.goods_party_id,
            models.PmsGoodsMapping.p_id,
            func.CONCAT(models.Category.cat_id, '_', models.Category.cat_name).label('cat_name'),
        ).outerjoin(
            models.EditorGood, models.PmsGoodsMapping.external_goods_id == models.EditorGood.goods_id
        ).outerjoin(
            models.Category, models.EditorGood.cat_id == models.Category.cat_id
        ).where(
            models.EditorGood.goods_id.in_(b)
        ).all()

        for row in result:
            key = str(row.goods_id)
            goodsMap[key] = row

    return goodsMap


def getPidGidDataByGid(goodsIdList):
    pIdMap = getPid(goodsIdList)

    pIdSet = list(pIdMap.values())
    sourceSession = databaseSession.createSession("sourceDatabase")
    result = sourceSession.query(
        models.PmsGoodsMapping.external_goods_id,
        models.PmsGoodsMapping.p_id,
        models.EditorGood.is_on_sale,
    ).join(
        models.EditorGood, models.PmsGoodsMapping.external_goods_id == models.EditorGood.goods_id
    ).where(
        models.PmsGoodsMapping.p_id.in_(pIdSet)
    ).group_by(models.PmsGoodsMapping.external_goods_id).all()

    return result


def getPidGidDataByGidV2(gidSet):
    sourceSession = databaseSession.createSession("sourceDatabase")
    result = sourceSession.query(
        models.PmsGoodsMapping.external_goods_id,
        models.PmsGoodsMapping.p_id,
        models.EditorGood.is_on_sale,
    ).join(
        models.EditorGood, models.PmsGoodsMapping.external_goods_id == models.EditorGood.goods_id
    ).where(
        models.EditorGood.goods_id.in_(gidSet)
    ).all()

    return result


def getAllShawlData():
    sourceSession = databaseSession.createSession("sourceDatabase")
    result = sourceSession.query(
        models.DressShawlRelation.dress_id,
        models.DressShawlRelation.same_id,
    ).all()

    allSameIdMap = {}
    allDressIdMap = {}
    for row in result:
        allSameIdMap[str(row.dress_id)] = str(row.same_id)
        allDressIdMap[str(row.same_id)] = str(row.dress_id)

    return allSameIdMap, allDressIdMap


def getShawlData(goodsIdList):
    goodsIdList = list(set(goodsIdList))
    sourceSession = databaseSession.createSession("sourceDatabase")
    result = sourceSession.query(
        models.DressShawlRelation.dress_id,
        models.DressShawlRelation.same_id,
    ).join(
        models.EditorGood, models.DressShawlRelation.same_id == models.EditorGood.goods_id
    ).where(
        or_(models.DressShawlRelation.dress_id.in_(goodsIdList), models.DressShawlRelation.same_id.in_(goodsIdList))
    ).all()

    allDressId = set()
    for row in result:
        allDressId.add(str(row.same_id))
        allDressId.add(str(row.dress_id))

    allDressId = allDressId.union(set(goodsIdList))

    if set(goodsIdList) == allDressId:
        return allDressId

    goodsIdList = list(set(goodsIdList).union(allDressId))
    return getShawlData(goodsIdList)


def getIsAllSale(goodsIdList):
    result = getPidGidDataByGid(goodsIdList)
    isAllSale = False
    for row in result:
        if row.is_on_sale == 1:
            isAllSale = True
            break

    return isAllSale


def getGoodsByGid(goodsIdList):
    resultList = []
    sourceSession = databaseSession.createSession("sourceDatabase")
    for i in range(0, len(goodsIdList), 2000):
        b = map(lambda x: str(x), goodsIdList[i:i + 2000])
        result = sourceSession.query(
            models.PmsGoodsMapping.external_goods_id,
            models.PmsGoodsMapping.p_id,
            models.EditorGood.is_on_sale,
        ).join(
            models.EditorGood, models.PmsGoodsMapping.external_goods_id == models.EditorGood.goods_id
        ).where(
            models.EditorGood.goods_id.in_(b)
        ).group_by(models.PmsGoodsMapping.external_goods_id).all()

        for row in result:
            key = str(row.external_goods_id)
            if key not in resultList:
                resultList.append(key)

    return resultList


def dataExport():
    goodsIdSet = set()
    # # 查询的样衣id
    sampleClothDataMap, pidResult = getSampleCloth()
    for k, v in sampleClothDataMap.items():
        goodsIdSet.add(k)

    laceSample = getLaceSample()
    for k, v in laceSample.items():
        k = k.strip()
        if len(k) > 0:
            goodsIdSet.add(k)

    goodsIdList = list(goodsIdSet)

    # 获取所有id 面料
    fabricMap, fabricPidMap = getGoodsAttributes(goodsIdList)
    # 获取相同的gid
    allGoodsIdList = getGoodsByGid(goodsIdList)
    # 获取所有的goods
    goodsMap = getEditorGoods(allGoodsIdList)

    # 初始化数据
    D30DataList = {}
    for key, row in goodsMap.items():
        fabric = fabricMap.get(key)
        pidKey = str(row.p_id)
        if not fabric:
            dataList = fabricPidMap.get(pidKey)
            if dataList and len(dataList) > 0:
                fabric = dataList[0]

        style = ''
        if key in sampleClothDataMap:
            style = ",".join([row['style'] for row in sampleClothDataMap.get(key)])

        if style == '' and pidKey in pidResult and len(pidResult.get(pidKey)) > 0:
            style = ",".join([row['style'] for row in pidResult.get(pidKey)[0]])

        D30DataList[key] = {
            "external_goods_id": key,
            "cat_name": row.cat_name,
            "is_on_sale": "不在架" if row.is_on_sale == 0 else "在架",
            "pid": row.p_id,
            "lace_data": laceSample.get(key),
            "is_lace_all_sale": '',
            "is_delete": '',
            "create_time": '',
            "goods_party": PARTY.get(str(row.goods_party_id)),
            "fabric": fabric,
            "style": style,
            "shipment_number_month_10": 0,
            "refund_number_month_10": 0,
            "D30_month_10": 0.0,
            "shipment_number_month_09": 0,
            "refund_number_month_09": 0,
            "D30_month_09": 0.0,
            "shipment_number_month_08": 0,
            "refund_number_month_08": 0,
            "D30_month_08": 0.0,
            "shipment_number_month_07": 0,
            "refund_number_month_07": 0,
            "D30_month_07": 0.0,
            "shipment_number_month_06": 0,
            "refund_number_month_06": 0,
            "D30_month_06": 0.0,
            "shipment_number_month_05": 0,
            "refund_number_month_05": 0,
            "D30_month_05": 0.0,
        }

    # 使用样衣id 查询退货数据
    monthList = ['11', '10', '09', '08', '07', '06', '05']
    for index in range(len(monthList) - 1):
        # 查询发货数据
        startTime = '2023-{0}-01 00:00:00'.format(monthList[index + 1])
        endTime = '2023-{0}-01 00:00:00'.format(monthList[index])
        shipmentData = getShipmentData(goodsIdList, startTime=startTime, endTime=endTime)
        monthD30 = {}
        for row in shipmentData:
            key = str(row.external_goods_id)
            if key not in monthD30:
                monthD30[key] = {
                    "shipment_number": 0,
                    "cat_name": row.cat_name,
                    "is_on_sale": row.is_on_sale,
                    "refund_number": 0,
                    "D30": 0,
                }

            monthD30[key]["shipment_number"] = row.shipment_number
        # 查询退货数据
        refundData = getRefundData(goodsIdList, startTime=startTime, endTime=endTime)
        for row in refundData:
            key = str(row.external_goods_id)
            if key not in monthD30:
                monthD30[key] = {
                    "shipment_number": 0,
                    "refund_number": 0,
                    "cat_name": row.cat_name,
                    "is_on_sale": row.is_on_sale,
                    "D30": 0,
                }

            monthD30[key]["refund_number"] += row.refund_number

        for k, v in monthD30.items():
            if k in D30DataList:
                D30DataList[k]["shipment_number_month_{0}".format(monthList[(index + 1)])] = v['shipment_number']
                D30DataList[k]["refund_number_month_{0}".format(monthList[(index + 1)])] = v['refund_number']
                if v['shipment_number'] > 0:
                    D30DataList[k]["D30_month_{0}".format(monthList[(index + 1)])] = Decimal(
                        v['refund_number'] * 100 / v['shipment_number']).quantize(Decimal('1.00'))

    fileData = []
    for k, row in D30DataList.items():
        if row['lace_data']:
            for laceRow in row['lace_data']:
                fileData.append({
                    '样衣ID': k,
                    '品类': row.get('cat_name'),
                    '样衣ID是否在架': row.get('is_on_sale'),
                    '对应PID': row.get('pid'),
                    '蕾丝ID': laceRow.get('lace_id'),
                    '蕾丝编号下相关ID是否均在架': "在架" if laceRow.get('is_lace_all_sale') else "不在架",
                    '蕾丝编码': laceRow.get('lace_number'),
                    '所属地': laceRow.get('location'),
                    '分类': laceRow.get('category'),
                    '适用类别': laceRow.get('app_categories'),
                    '蕾丝启用状态': "在架" if laceRow.get('is_delete') == 1 else "不在架",
                    '蕾丝编号创建时间': laceRow.get('create_time'),
                    'GID组织': row.get('goods_party'),
                    '面料': row.get('fabric'),
                    '制作款式': row.get('style'),
                    '10月发货量': row.get('shipment_number_month_10'),
                    '10月退款率(%)': row.get('D30_month_10'),
                    '9月发货量': row.get('shipment_number_month_09'),
                    '9月退款率(%)': row.get('D30_month_09'),
                    '8月发货量': row.get('shipment_number_month_08'),
                    '8月退款率(%)': row.get('D30_month_08'),
                    '7月发货量': row.get('shipment_number_month_07'),
                    '7月退款率(%)': row.get('D30_month_07'),
                    '6月发货量': row.get('shipment_number_month_06'),
                    '6月退款率(%)': row.get('D30_month_06'),
                    '5月发货量': row.get('shipment_number_month_05'),
                    '5月退款率(%)': row.get('D30_month_05'),
                })
        else:
            fileData.append({
                '样衣ID': k,
                '品类': row.get('cat_name'),
                '样衣ID是否在架': row.get('is_on_sale'),
                '对应PID': row.get('pid'),
                '蕾丝ID': '',
                '蕾丝编号下相关ID是否均在架': row.get('is_lace_all_sale'),
                '蕾丝编码': '',
                '所属地': '',
                '分类': '',
                '适用类别': '',
                '蕾丝启用状态': '',
                '蕾丝编号创建时间': '',
                'GID组织': row.get('goods_party'),
                '面料': row.get('fabric'),
                '制作款式': row.get('style'),
                '10月发货量': row.get('shipment_number_month_10'),
                '10月退款率(%)': row.get('D30_month_10'),
                '9月发货量': row.get('shipment_number_month_09'),
                '9月退款率(%)': row.get('D30_month_09'),
                '8月发货量': row.get('shipment_number_month_08'),
                '8月退款率(%)': row.get('D30_month_08'),
                '7月发货量': row.get('shipment_number_month_07'),
                '7月退款率(%)': row.get('D30_month_07'),
                '6月发货量': row.get('shipment_number_month_06'),
                '6月退款率(%)': row.get('D30_month_06'),
                '5月发货量': row.get('shipment_number_month_05'),
                '5月退款率(%)': row.get('D30_month_05'),
            })

    fileData.sort(key=lambda k: (
            k.get('5月发货量', 0) + k.get('6月发货量', 0) + k.get('7月发货量', 0) + k.get('8月发货量', 0)
            + k.get('9月发货量', 0) + k.get('10月发货量', 0)), reverse=True)
    writer = pd.ExcelWriter('../data/采购-婚纱礼服用蕾丝发货及D30数据v2.xlsx')
    data = pd.DataFrame(fileData)
    data.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()
    writer.close()


def dataExportV2():
    goodsIdSet = set()
    # # 查询的样衣id
    sampleClothDataMap = {}
    # sampleClothDataMap, pidResult = getSampleCloth()
    # for k, v in sampleClothDataMap.items():
    #     goodsIdSet.add(k)

    laceSample = getOnGidData([3088])
    print(laceSample)

    exit()
    laceSample = getLaceSample()
    for k, v in laceSample.items():
        k = k.strip()
        if len(k) > 0:
            goodsIdSet.add(k)

    goodsIdList = list(goodsIdSet)

    # 获取所有id 面料
    fabricMap, fabricPidMap = getGoodsAttributes(goodsIdList)
    # 获取相同的gid
    allGoodsIdList = getGoodsByGid(goodsIdList)
    # 获取所有的goods
    goodsMap = getEditorGoods(allGoodsIdList)


if __name__ == "__main__":
    # dataExportV2()
    dataExport()
