# 启信宝header加密生成
在启信宝中，有以下header，其中有一串key和value是采用hmac-sha512算法加密生成的。
目前加密的js版本是https://cache.qixin.com/pcweb/common.b911629e.js

```
Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br
Accept-Language: en,zh-CN;q=0.9,zh;q=0.8
c63911333e3672d2bba3: b6703ef31081f68e28339abaeada8b7bd367d65c17b1e031d21e93429ba0649037f0ef9abf4334b569ca6bc014a7637f131ef88e18dfc2c8a9be9f225c8ccb3a
Cache-Control: no-cache
Connection: keep-alive
Content-Length: 88
Content-Type: application/json;charset=UTF-8
Origin: https://www.qixin.com
Pragma: no-cache
Referer: https://www.qixin.com/
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36
X-Requested-With: XMLHttpRequest
```
