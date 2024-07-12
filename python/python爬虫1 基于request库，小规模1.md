- requests.request('method',url,**kwargs)构造一个请求，支撑以下基本方法(除了下面的method还有一个option可以使用，不常用)（**kwargs 各种字段添加功能如cookie，timeout等，主要的有params,data,json,headers,auth,files,timeout,cookies,proxies,allow_redirects,stream,verify,cert）(其中`data`是字典，文件对象等`data = body`   `body` 是你存储的内容 `json`是作为内容部分向服务器提交`json = kv` `kv`是你定义的字典 `params`是字典或字节序列，作为参数增加到URL中 `header`字典，定制http的头
- requests.get(url,params = None,**kwargs)获取HTML网页，对应http的get  __最常用__
- requests.head(url,**kwargs)获取HTML网页头信息的方法，对应于http的head
- requests.post(url,params = None,json = None,**kwargs)向HTML网页提交post请求的方法，对应于http的post
- requests.put(url,params = None,**kwargs)向HTML网页提交put请求的方法，对应于http的put
- requests.patch(url,params = None,**kwargs)向HTML网页提交局部修改请求，对应于http的patch
- requests.delete(url,**kwargs)向HTML页面提交删除请求，对应于http的delete
- r.status_code http请求的返回格式，200成功，404失败
- r.text http响应的字符串格式，即URL对应的页面内容
- r.encoding 从http header中猜测的响应内容编码方式
- r,apparent_encoding 从内容分析出的响应内容编码方式
- r.content http响应内容的二进制形势

<hr>
<h3>request的库异常
- requests.ConnectionError 网络连接错误异常，如DNS查询失败，拒绝连接
- requests.HTTPError http错误异常
- requests.URLRequired URL缺失异常
- requests.TooManyRedirects 超过最大重定向次数，产生重定向异常
- requests.ConnectTimeout 连接远程服务器超时异常（获得内容超时）
- requests.Timeout 请求URL超时，产生超时异常（远程服务器连接超时）
- r,raise_fore_status()如果不是200，产生requests.HTTPError
<hr>
# 网络连接有风险，一定要处理好异常情况


## 网络爬虫限制
1. 判断user-agent进行限制，检查他的user-agent域，只允许合适的
2. robot协议，通知爬虫规则，，要按照

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2MzEwNDE4NDcsMTg4ODI5OTQ4Nl19
-->