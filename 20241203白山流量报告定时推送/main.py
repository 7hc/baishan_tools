import requests, datetime

# 配置密钥
token = ""
# 配置待查域名，多域名逗号分割
domains = ""
# 配置展示的条数
limit = 3
# 企业微信机器人WebHook
webhook = ""

# 流量单位转换
def convert_traffic_units(traffic):
    if traffic > 1024*1024*1024:
        return f"{traffic/(1024*1024*1024):.2f} GB"
    elif traffic > 1024*1024:
        return f"{traffic/(1024*1024):.2f} MB"
    elif traffic > 1024:
        return f"{traffic/1024:.2f} KB"
    else:
        return f"{traffic} Byte"

url = "https://cdn.api.baishan.com/v2/stat/bandwidth/eachDomain"

params = {
    "token":token,
    "domains":domains,
    "start_time":(datetime.datetime.now() - datetime.timedelta(days=5)).strftime("%Y-%m-%d %H:%M"),
    "end_time":(datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M"),
    "data_type":"traffic",
    "grad":"day",
    "query_area":"all"
}

text = "---每日流量报告---\n\n"
try:
    r = requests.get(url=url,params=params)
    rj = r.json()

    if rj["code"] == 0:
        print("[BS-API] 调用成功")
        for i in rj["data"].keys():
            li = 0
            text = text + "域名：{}\n".format(rj["data"][i]["domain"])
            for d in rj["data"][i]["data"]:
                if li >= limit:
                    break
                text = text + ("{} --> {}\n".format(datetime.datetime.fromtimestamp(d[0]).strftime('%Y-%m-%d'),convert_traffic_units(d[1])))
                li = li + 1
            text = text + "\n"
    else:
        print("[BS-API] 查询失败->{}".format(r.text))
except Exception as e:
    print("[BS-API] 调用出错->{}".format(e))
    text = text + "[BS-API] 调用出错->{}".format(e)

# 发送企业微信Bot消息

dat = {
    "msgtype":"text",
    "text":{
        "content":text
    }
}

r2 = requests.post(url=webhook,json=dat)
if r2.status_code == 200:
    if r2.json()["errcode"] == 0:
        print("[WX-SEND] 发送成功")
    else:
        print("[WX-SEND] 发送失败->{}".format(r2.text))
else:
    print("[WX-SEND] 发送失败->{}->{}".format(r2.status_code,r2.text))


