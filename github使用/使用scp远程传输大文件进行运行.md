#### . 使用 SCP 上传文件或文件夹

假设你的本地文件路径为 `E:/111`，目标是将它上传到远程主机的指定目录，例如 `/home/your_username/project`，可以使用以下命令：

<BASH>

```
scp -r E:/111 your_username@remote_host:/home/your_username/project
```

-   `-r`：表示递归上传整个文件夹。
-   `your_username`：你的远程主机用户名。
-   `remote_host`：远程主机地址（IP 或域名）。
-   `/home/your_username/project`：远程主机上的目标目录。


### 方法 3：压缩文件后通过 SSH 上传

如果文件较大，可以先在本地将文件压缩，然后通过 SCP 上传到远程主机，再解压。

#### 1. 在本地压缩文件

使用 zip 或 tar 工具压缩文件夹，例如：

<BASH>

```
zip -r 111.zip E:/111
```

或者使用 tar 压缩：

<BASH>

```
tar -czvf 111.tar.gz -C E:/111 .
```

#### 2. 上传压缩文件

通过 SCP 将压缩文件上传到远程主机：

<BASH>

```
scp 111.zip your_username@remote_host:/home/your_username/project
```

#### 3. 解压文件

登录远程主机后，进入目标目录并解压文件：

-   如果是 zip 文件：
    
    <BASH>
    
    ```
    unzip 111.zip
    ```
    
-   如果是 tar.gz 文件：
    
    <BASH>
    
    ```
    tar -xzvf 111.tar.gz
    ```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY0Mzc4MzM5N119
-->