import requests
import csv
import time

# 新建csv，存储数据
csvf = open('美团评论-美兹客汉堡炸鸡（师大西门店）.csv', 'a+', encoding='utf-8', newline='')
fieldnames = ['userName', 'avgPrice', 'comment', 'commentTime', 'replyCnt', 'zanCnt', 'readCnt', 'star', 'hilignt',
              'userLevel', 'userId', 'uType', 'quality', 'alreadyZzz', 'reviewId', 'menu', 'did', 'dealEndtime',
              'anonymous']
writer = csv.DictWriter(csvf, fieldnames=fieldnames)
writer.writeheader()
# 伪装头，用于反爬

# 设置请求头
header = {
    "Accept-Encoding": "Gzip",  # 使用gzip压缩传输数据让访问更快
    "Connection": "keep-alive",
    "Cookie": "uuid=de1065629e9f44628716.1613396853.1.0.0; client-id=f52eda1c-6ab0-4e8f-907e-5cb24ec77b75; mtcdn=K; lt=jP63TigLMR7la4eRkGogQcmKejsAAAAARg0AAIW5hGK67Kv5Ksh00LNCiCJBW3SQa2vTijqnWL_ocrZP_SkCHsllQlG6GSgSKWp9Pw; u=2246617980; n=mVY677051970; token2=jP63TigLMR7la4eRkGogQcmKejsAAAAARg0AAIW5hGK67Kv5Ksh00LNCiCJBW3SQa2vTijqnWL_ocrZP_SkCHsllQlG6GSgSKWp9Pw; _lxsdk_cuid=178cfa36842c8-037c4ff6329f28-336a7c09-fa000-178cfa36842c8; _lxsdk=178cfa36842c8-037c4ff6329f28-336a7c09-fa000-178cfa36842c8; unc=mVY677051970; __mta=220445223.1618391296666.1618391296666.1618391296666.1; lat=36.098371; lng=103.731354; _hc.v=de63833d-8651-301b-58e0-62c0bc8976f2.1618391313; _lxsdk_s=178cfa36844-2b0-3f-88e%7C%7C9; firstTime=1618391485512",
    "Host": "www.meituan.com",

    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}

# 网址模板
base_url = 'https://www.meituan.com/meishi/api/poi/getMerchantComment?'
for page in range(0, 580):
    parameters = {
        'platform': 1,
        'partner': 126,
        'originUrl': 'https://www.meituan.com/meishi/1454935/',
        'riskLevel': 1,
        'optimusCode': 10,
        'id': 1454935,
        'userId': 2246617980,
        'offset': 30,
        'pageSize': 10,
        'sortType': 1

    }
    # 设置请求头
    parameters['offset'] = page * 10
    # get方法请求网页数据
    resp = requests.get(base_url, headers=header, params=parameters)

    # 解析定位第page页的数据
    for info in resp.json()['data']['comments']:
        #         print(info)
        userName = info['userName']
        #         'avgPrice', 'commenTime','commentTime','replyCnt','zanCnt','readCnt','star']
        avgPrice = info['avgPrice']
        comment = info['comment']
        commentTime = info['commentTime']
        replyCnt = info['replyCnt']
        zanCnt = info['zanCnt']
        readCnt = info['readCnt']
        star = info['star']
        hilignt = info['hilignt']
        userLevel = info['userLevel']
        userId = info['userId']
        uType = info['uType']
        quality = info['quality']
        alreadyZzz = info['alreadyZzz']
        reviewId = info['reviewId']
        menu = info['menu']
        did = info['did']
        dealEndtime = info['dealEndtime']
        anonymous = info['anonymous']

        data = {'userName': userName,
                'avgPrice': avgPrice,
                'comment': comment,
                'commentTime': commentTime,
                'replyCnt': replyCnt,
                'zanCnt': zanCnt,
                'readCnt': readCnt,
                'star': star,
                'hilignt': hilignt,
                'userLevel': userLevel,
                'userId': userId,
                'uType': uType,
                'quality': quality,
                'alreadyZzz': alreadyZzz,
                'reviewId': reviewId,
                'menu': menu,
                'did': did,
                'dealEndtime': dealEndtime,
                'anonymous': anonymous

                }
        # 存入csv

        writer.writerow(data)

    # 降低爬虫对meituan
    time.sleep(1)
    print(f'正在爬取第{page}页')
# 关闭csvf
csvf.close()