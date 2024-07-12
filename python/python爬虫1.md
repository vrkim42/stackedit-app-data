- requests.request()构造一个请求，支撑以下基本方法
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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzMDc1ODM3NjQsLTU0MDA1MjQ5NCwxMz
g5MjQ1NTMxXX0=
-->