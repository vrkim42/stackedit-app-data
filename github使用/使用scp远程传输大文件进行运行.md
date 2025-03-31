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
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQxMjI4MDEyXX0=
-->