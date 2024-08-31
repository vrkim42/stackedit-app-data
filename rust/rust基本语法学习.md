### 路径

 - crate::front_of_house::hosting::add_to_waitlist(); // 绝对路径调用
 - front_of_house::hosting::add_to_waitlist();  //相对路径

### 数据类型

 - i8 i16 i32 i64 有符号整数
 - u8 u32 u16 u64 无符号整数
 - f32 f64单精度 双精度浮点数
 - 机制 隐藏(重复赋值，类型可变) 常量const 变量let mut

### tuple
```rust
let tup: (i32, f64, u8) = (500, 6.4, 1); //tup类型可以多次重复声明变量类型和对应值

let (x, y, z) = tup; //获取tuple的元素值

println!("{}, {}, {}", tup.0, tup.1, tup.2); //输出方式一

println!("{}, {}, {}", x, y, z); //2
```

### 数组
```rust
//数据存放在stack(栈)上而不是heap(堆)上,分配在块上的内存

let names: [&str; 4] = ["sss" , "rrr ", "ss", "s"];// let var_name: [i32; 3]

//let a = [3:5] = let a = [3,3,3,3,3] 及本声明过程：let 名字: [类型; 长度] = [值1,值2,值3,值4]

let _first_name: &str = names[0];// 访问数组过程

let index: [usize; 4] = [12, 13, 14, 15];

let name: &str = names[index[1]]; //访问数组过程,超限编译时报错

println!("{}", name);
```

### 函数命名

```rust
其中一种函数命名
fn another_funnction(x:i32, y:&str){//参数必须表明类型

println!("function!");

}

另外一种函数命名
fn five(x:i32) -> i32 {

x + 5

}
```

### if的学习

```
fn if_learning(){

let x: i32 = 3;

if x < 4{ // 后面的条件必须是布尔类型

println!("condition is true ");

} else { //也有elseif之类的与cpp相同，多于一个elseif不如match

println!("condition is false");

}

  

let condition: bool = true;

let number: i32 = if condition { 5 } else { 6 }; //三目运行符，每个返回的类型必须一样

}
```


### 循环的使用

```rust
fn loop_learning(){

let mut i: i32 = 5;

//first loop condition

loop {

println!("condition!"); // 一直执行直到ctrl + c停止

i -= 1;

if i == 0{

break; //或者使用break自动停止

}

}

//second loop condition 与cpp类似

while i <5{

println!("while!");

i+=1;

}

//third loop condition 与cpp类似

let a: [i32; 5] = [10, 20, 30, 40, 50];

for element in a.iter(){

println!("The value is : {}", element);

}

}
```

### stack 和 heap 的使用 -> 堆和栈
* satck 按照值的接受顺序存储，按照相反的顺序将它们移除（后进先出， LIFO），添加数据叫做压入栈，移除数据叫做弹出栈

* 所有存储在stack上的数据必须拥有已知的固定的大小，编译时未知数据或者大小变化数据存储在heap上

* heap的内存组织性差一些，当把数据放入heap，会请求一定数量的空间，操作系统在heap找到一块足够大的空间，标记为在用，返回一个指针，也就是地址

* 把值压到heap叫做分配，stack不是，指针是已知固定大小的，可以将指针存放在stack上，想要实际数据就要指针定位

* 数据压在stack比heap快得多，因为stack不需要寻找存储数据的空间，那个位置永远在stack的顶端，因此，访问也是stack快得多

* 在heap上分配空间需要找到一个足够大的空间来存放数据，然后要做好记录方便下次分配

* 对于现代的处理器来说，由于缓存的缘故，指令在内存跳转次数越少，速度越快，heap分配空间也要时间

* **管理heap数据是所有权存在的原因**，解决1.跟踪哪些代码使用heap数据，最小化heap的重复数据量，清理heap未使用的数据避免空间不足

* 1.每个值都有一个变量，这个变量是该值的所有者

* 2.每个值只有一个所有者

* 3.当所有者超出作用域(scope)时，该值会被删除。scope就是变量的适用范围

* 对于3:fn main(){

* //s不可用

* let s = 5;//s可用

* //可以对s操作

* }//s不可再用
### 创建string类型的值：使用from函数

* let s = String::from("hello");

* ::表示from是string类型下的函数

* s.push_str(", world");

* 这个可以在s之后新增内容，string类型可以修改，字符串字面值不能->内存处理方式不同

* string类型声明以后在heap上创建内存空间存放变量，在stack上创建指向对应内存指针，对应长度，对应容量

* 当第二个变量重复声明第一个变量的值时，只复制stack上的值，不复制heap，变量离开作用域rust自动调用drop函数，将变量使用的heap释放

* 当两个变量同时离开就会释放两次heap上的内存，出现bug，为了防止这个问题，第二个变量声明后第一个变量失效，除非深度克隆

* 所有需要分配内存和资源的是浅层copy，例如&str,(i32,String),反例i32,(i32,i32),bool,char

### pub, mod
// 定义module来控制作用域和私有性

// 在一个create中将代码进行分组，增加可读性，易于复用，控制项目私有性，public,private

// rust所有的条目一般都是私有的，除非标记，父级模块无法访问子模块的私有条目，子模块随便看祖辈的

```rsut
mod front_of_house{

pub mod hosting {

pub fn add_to_waitlist(){}

fn seat_at_table(){}

}

mod serving {

fn take_order() {}

fn serve_order() {}

pub fn take_payment() {}

}

}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3ODM5MDc3MDYsLTczNjE3Mzc4Miw3Nj
I0MDU0MDAsNjU5ODQ4MjksLTg4NTEwNjk5MSwtMTg1MjY0Mjk0
NSwtMTQ4NTExMTcyMSwtMjA4ODc0NjYxMl19
-->