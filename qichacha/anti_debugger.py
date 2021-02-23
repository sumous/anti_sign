# -*- coding:utf-8 -*-
"""Description: """
# Created_at: Thu Feb 18 01:06:21 2021 (+0800)
# 企查查apph5绕过web反调试
# 地址：apph5.qichacha.com，
# 企查查的商标查询等绕过javascript无限debugger反调试，采用mitmproxy脚本，直接运行python anti_debugger.py，然后设置系统代理


import json
import time
import os
import threading
import asyncio
import re
import urllib

from mitmproxy.options import Options
from mitmproxy.proxy.config import ProxyConfig
from mitmproxy.proxy.server import ProxyServer
from mitmproxy.tools.dump import DumpMaster
import mitmproxy.http
from mitmproxy import ctx


import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)




class AntiDebugger:

    def request(self, flow: mitmproxy.http.HTTPFlow):
        pass

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.host == 'qcc-static.qichacha.com' or flow.request.host == 'apph5.qichacha.com':
            print(flow.request.path)
            flow.response.set_content(flow.response.content.replace(b'debugger', b''))
            print('debugger' in flow.response.content)


# see source mitmproxy/master.py for details
def loop_in_thread(loop, m):
    asyncio.set_event_loop(loop)  # This is the key.
    m.run_loop(loop.run_forever)


if __name__ == "__main__":
    options = Options(listen_host='0.0.0.0', listen_port=8080, http2=False)
    m = DumpMaster(options, with_termlog=False, with_dumper=False)
    config = ProxyConfig(options)
    m.server = ProxyServer(config)
    m.addons.add(AntiDebugger())

    loop = asyncio.get_event_loop()
    t = threading.Thread(target=loop_in_thread, args=(loop,m) )
    t.start()
    print('启动代理完成，监听端口8080，设置完代理后，访问mitm.it安装代理证书')

    t.join()

    m.shutdown()

