from FreeProxy import ProxyTool
pt = ProxyTool.ProxyTool()
proxies = pt.getProxy(num_proxies=10, max_tries=5)
print(proxies)

#num_proxies為Proxy數量