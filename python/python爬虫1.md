- requests.request('method',url,**kwargs)构造一个请求，支撑以下基本方法(除了下面的method还有一个option可以使用，不常用)（**kwargs 各种字段tian'jia）
- requests.get()获取HTML网页，对应http的get
- requests.head()获取HTML网页头信息的方法，对应于http的head
- requests.post()向HTML网页提交post请求的方法，对应于http的post
- requests.put()向HTML网页提交put请求的方法，对应于http的put
- requests.patch()向HTML网页提交局部修改请求，对应于http的patch
- requests.delete()向HTML页面提交删除请求，对应于http的delete
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


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MDMwMjYxMTQsLTk2MDg0NTk4OCwyMT
MyMzYyNTI2LC0xMzA3NTgzNzY0LC01NDAwNTI0OTQsMTM4OTI0
NTUzMV19
-->