一般步骤
rust为ahead of time文件

小型项目使用rustc
 1. makdir 文件夹
 2. cd h* 转移到相应文件夹
 3. code .用vscode打开
 4. rustc main.rs 编译
 5. .\相关文件名


rust 缩进为4个空格，不是tab
ls可以查看当前目录下的所有文件
顶层目录可以放置readme.md,许可信息，配置文件和其他与源码无关的文件

较大型用cargo

 1. cargo new 文件名
 2. cd 新创建的文件
 3. code .用vscode打开
 4. 

将一般文件转化为cargo

 1. 将源代码移动到src文件夹下
 2. 创建cargo.toml填写相应配置


构建cargo项目（cargo build）

 1. 创建可执行文件target\debug\hello_cargo.exe
 2. 运行可执行文件 .\target\debug\hello_cargo.exe
 3. 第一次运行会在项目目录生成cargo.lock文件追踪项目依赖的精确版本，无需手动修改文件
 

(cargo check)相对于chago build运行快得多，检查代码确保能通过编译，但是不产生任何可执行文件
~~删除线文本~~
构建和运行cargo项目

cargo run，编译代码 + 执行结果
编译成功代码未改变直接会运行

为发布创建
cargo build --release编译时会进行优化，运行更快但是编译时间更长，会在target/release创建可执行文件（与开发时的配置不同）

#### 消除重复代码
* 识别重复代码
* 提取重复代码到函数中，并在函数中指定函数的输入和返回值
* 将重复代码使用函数调用进行替换

<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAyODMzNzM2MiwtNDM3MDQ1MjgyXX0=
-->