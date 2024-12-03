## 白山每日流量报告推送
Time: 2024-12-03

API文档参考：https://portal.baishancloud.com/track/document/api/1/1043

### 参数说明

| 参数名 | 类型 | 说明 | 示例 |
| --- | --- | --- | --- |
| token | str | 白山API密钥 | 64dv42u5nb09a1uee6c7pdw9ytymip7i |
| domains | str | 待查域名，多域名用,分隔 | www.9kr.cc,www.2bps.cn |
| limit | int | 流量记录展示条数 | 3 |
| end_time | string | 结束时间 | 是 |
| webhook | string | 企业微信群Bot WebHook链接 | https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=82f3a1b7-c324-9cda-9752-726b9c3c2d1a |

### 使用方法

- 用Linux自带的定时任务，设置每日运行一次

- 用宝塔自带的定时任务，设置每日运行一次
