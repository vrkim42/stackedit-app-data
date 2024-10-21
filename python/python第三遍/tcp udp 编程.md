## 综述
python语言在网络通信方面的优点特别突出，远远领先其他语言。

ip地址标识网络中一个通信实体的地址，通信实体可以是计算机，路由器等。计算机要通信也必须配置ip地址，路由器是连接两个或多个网络的网络设备。

ipv4是一个32位整数，ipv6是一个128位整数（字符串表示）


### osi模型
应用层，表示层，会话层，传输层，网络层，数据链路层，物理层

### tcp/ip协议
协议族，按照层次划分，共四层：应用层（对应osi的应用层，表示层，会话层），传输层（tcp/udp），互联网络层（ip），网络接口层（物理数据链路）

### socket编程
Socket 编程就分为 **TCP 编程**和 **UDP 编程**两类。
在网络通讯中，**TCP 方式就类似于拨打电话**，使用该种方式进行网络通讯时，需要建立专门的虚拟连接，然后进行可靠的数据传输，如果数据发送失败，则客户端会自动重发该数据。而 **UDP 方式就类似于发送短信**，使用这种方式进行网络通讯时，不需要建立专门的虚拟连接，传输也不是很可靠，如果发送失败则客户端无法获得。

- TCP 是面向连接的，传输数据安全，稳定，效率相对较低。 
- UDP 是面向无连接的，传输数据不安全，效率较高。

### socket
socket.socket([family[, type[, proto]]])
其中参数 family: 套接字家族可以使 AF_UNIX 或者 AF_INET；type: 套接字类型可以根据是面向连接的还是非连接分为 SOCK_STREAM 或 SOCK_DGRAM；protocol: 一般不填默认为 0。
tcpSocket=socket.socket(AF_INET,SOCK_STREAM)
socket 主要分为面向连接的 socket 和无连接的 socket。面向连接的 socket 使用的主要协议是传输控制协议，也就是常说的 TCP，TCP 的 socket 名称是 SOCK_STREAM。创建套接字 TCP/IP 套接字，可以调用 socket.socket()。
udpSocket=socket.socket (AF_INET,SOCK_DGRAM)

![输入图片说明](/imgs/2024-10-14/zDKYXtGTdg8axwkj.png)

### 使用udp传递数据
[使用udp传递数据 - Pastebin.com](https://pastebin.com/UhaXnpBp)
[多线程udp传输信息 - Pastebin.com](https://pastebin.com/s6Ba10bZ)

### 使用tftp传递文件
使用struct模块进行传输
![输入图片说明](/imgs/2024-10-14/7V5VOEu9j32VKOcQ.png)
![输入图片说明](/imgs/2024-10-14/llwIx2jbgMoMxDgD.png)
![输入图片说明](/imgs/2024-10-14/2nOR61lVDvXqclGA.png)
[使用socket和struct实现tftp文件传输 - Pastebin.com](https://pastebin.com/nWAhvshP)
这个是tftp客户端的代码实现，但是想要实现服务端就需要下载相应的服务端软件进行操作

### tcp协议进行通信
tcpSocket=socket.socket(AF_INET,SOCK_STREAM)原型定义
![输入图片说明](/imgs/2024-10-14/QGZwTjdPwbyQK7CC.png)
[使用socket创建tcp服务端 - Pastebin.com](https://pastebin.com/Aa46XSca)
[使用socket实现tcp客户端 - Pastebin.com](https://pastebin.com/d3Ak6YHB)


<!--stackedit_data:
eyJoaXN0b3J5IjpbNTczMTU5NzkxLDEwOTU1OTIwNDksMTA4OT
I4NjY3NywtMTc1MDI3NTQ4MSwxMzA5ODU2NzU4LDEwNDk3NDY5
OTQsLTE5MTg2MDE3NzYsNzMwNzQ3Nzk0LDMxNTc3NTAxLDYwNj
U4MzM5OCwtMTE2MjkyNjM1OCw5NjU5ODcwODAsLTE3ODM5MjE4
MDQsLTc5MzI3MzI5NV19
-->