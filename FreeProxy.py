# 自動抓取可用的Proxy
# 可指定每次抓取Proxy數量(num_proxies為Proxy數量)

from FreeProxy import ProxyTool
pt = ProxyTool.ProxyTool()
proxies = pt.getProxy(num_proxies=10, max_tries=5)
print(proxies)
