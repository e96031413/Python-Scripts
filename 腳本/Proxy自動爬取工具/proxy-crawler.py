from FreeProxy import ProxyTool
pt = ProxyTool.ProxyTool()
proxies = pt.getProxy(num_proxies=2, max_tries=5)
print(proxies)