### 绝对路径，相对路径，super

 - crate::front_of_house::hosting::add_to_waitlist(); // 绝对路径调用，从create作为根开始向下到下一级
 - front_of_house::hosting::add_to_waitlist();  //相对路径
 - 通过路径进行访问，使得在该快下能使用其他模块的函数
```rust
pub fn refresh() {
fn front() {
fn clean() {
super::clean_room(); // 调用父模块(第十二行)中的 clean_room 函数,上一级只能有一个函数才能用
}
}
crate::front_of_house::hosting::add_to_waitlist(); // 绝对路径调用
front_of_house::hosting::add_to_waitlist(); // 相对路径调用，前提是它们在同一级
}
fn clean_room() {} // 当前模块中的 clean_room 函数pub fn refresh() {

fn front() {

fn clean() {

super::clean_room(); // 调用父模块(第十二行)中的 clean_room 函数,上一级只能有一个函数才能用

}

}

crate::front_of_house::hosting::add_to_waitlist(); // 绝对路径调用

front_of_house::hosting::add_to_waitlist(); // 相对路径调用，前提是它们在同一级别

}
fn clean_room() {} // 当前模块中的 clean_room 函数
```

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
// 公共结构体
mod back_of_house {
    pub struct Breakfast { //默认结构体也是私有的(所有条目)，所以要进行声明
        pub toast:String, //即便是结构体里面的内容也是私有的，要进行公开
        seasonal_fruit: String,
    }

    impl Breakfast { //针对上面的结构体构建的方法
        pub fn summer(toast: &str) -> Breakfast {
            Breakfast {
                toast: String::from(toast),
                seasonal_fruit: String::from("peaches"),
            }
        }
    }

    pub enum Appetizer { //与结构体不同，枚举声明以后所有的都是公共的，不用再一个个加pub
        Soup,
        Salad,
    }
}
```

### struct和impl，元组
```rust
#[derive(Debug)]
struct Rectangle { //定义一个结构体类型
    width: u32,
    length: u32,
}

impl Rectangle { //根据结构体新建方法，跟着的是结构体名
    fn area(&self) -> u32 { //借用原则,这里是一个函数
        self.width * self.length
    }
    fn can_hold(&self, other:&Rectangle) -> bool { //此处判断结构体一能否容纳结构体二
        self.width > other.width && self.length > other.length
    }
    fn square(size: u32) -> Rectangle {// 一个结构体允许多个impl块，即这个区域可以踢出去另起炉灶
        Rectangle {
            width: size,
            length: size,
        }
    }
}
fn main() {
    let s: Rectangle = Rectangle::square(20);
            let rect1: Rectangle = Rectangle { //引用上面你的结构体生成对应结构
                width: 30,
                length: 50,
            };
            let rect2: Rectangle = Rectangle {
                width: 10,
                length: 40,
            };
            let rect3: Rectangle = Rectangle {
                width: 50,
                length: 70,
            };
            println!("{}", rect1.area());
            println!("{}", rect1.can_hold(&rect2)); //使用rect1作为结构体使用can_hold方法导入rect2结构进行比较
            println!("{}", rect1.can_hold(&rect3));
            println!("{:#?}", rect1);// :?将代码展示出来，使用#进行格式优化，美化输出
        }
        fn area(rect: &Rectangle) -> u32 {
            rect.width * rect.length //更直观的看出长和宽
        }#[derive(Debug)]
struct Rectangle { //定义一个结构体类型
    width: u32,
    length: u32,
}

impl Rectangle { //根据结构体新建方法，跟着的是结构体名
    fn area(&self) -> u32 { //借用原则,这里是一个函数
        self.width * self.length
    }
    fn can_hold(&self, other:&Rectangle) -> bool { //此处判断结构体一能否容纳结构体二
        self.width > other.width && self.length > other.length
    }
    fn square(size: u32) -> Rectangle {// 一个结构体允许多个impl块，即这个区域可以踢出去另起炉灶
        Rectangle {
            width: size,
            length: size,
        }
    }
}
fn main() {
    let s: Rectangle = Rectangle::square(20);
            let rect1: Rectangle = Rectangle { //引用上面你的结构体生成对应结构
                width: 30,
                length: 50,
            };
            let rect2: Rectangle = Rectangle {
                width: 10,
                length: 40,
            };
            let rect3: Rectangle = Rectangle {
                width: 50,
                length: 70,
            };
            println!("{}", rect1.area());
            println!("{}", rect1.can_hold(&rect2)); //使用rect1作为结构体使用can_hold方法导入rect2结构进行比较
            println!("{}", rect1.can_hold(&rect3));
            println!("{:#?}", rect1);// :?将代码展示出来，使用#进行格式优化，美化输出
        }
        fn area(rect: &Rectangle) -> u32 {
            rect.width * rect.length //更直观的看出长和宽
        }
```


### 枚举
```rust
// 枚举的讲解学习
// ip地址举例

// 定义方法一:
enum IpAddrKind {
    V4,
    V6,
}
struct IpAddr{
    kind: IpAddrKind,
    address: String,
}
// 定义方法二:
// enum IpAddKind{
//     V4(u8, u8, u8, u8),
//     V6(String),
// }这样做可以节省一个结构体，而且类型更清晰，每个变体可以拥有不同类型以及关联的数据量

fn main(){
    let home: IpAddr = IpAddr{
        kind: IpAddrKind::V4,
        address: String::from("127.0.0.1"),
    };

    let loopback: IpAddr = IpAddr {
        kind: IpAddrKind::V6,// enum类型使用::进行相关的访问，而结构体使用.进行访问，相比于c.cpp,rust只有(*指针).方法的访问办法
        address: String::from("::1"),
    };
    //let four: IpAddKind = IpAddKind::V4;
    //let six: IpAddKind = IpAddKind::V6;

    // route(four);
    // route(six);
    // route(IpAddKind::V6);
}
// fn route(ip_kind: IpAddKind){

// }
```

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

impl Message {//对于enum类型的枚举，我们也使用impl进行方法的定义
    fn call(&self){}
}

fn main(){
    let q = Message::Quit;
    let m = Message::Move { x: 12, y: 24 };
    let w = Message::Write(String::from("Hello"));
    let c = Message::ChangeColor(0, 255, 255);

    m.call();
}
```

### match的使用，对类型进行绑定
```rust
enum Coin{
    Penny,
    Nickel,
    Dime,
    Quarter,
}
enum UsState {
    Alaska,
    kkk,
    sss,
}
fn value_in_cents(coin: Coin) -> u8 {
    match coin { // 挨个对应使用::进行绑定
        Coin::Penny => {
            println!("sss");
            1
        },// 可以使用块状结构
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter(state) => {
            println!("State quarter from {:?}!", state);
            25
        }, // 进行模式化输出，可以使用参数
    }
}

fn main(){
    let c = Coin::Quarter(UsState::Alaska); //访问的模式
    println!("{}", value_in_cents(c));
} 
```

### rust对可能存在的数的处理
```rust
//rust中没有null的概念  防止使用非null值那样使用null时出现错误
//但是null存在时有意义的，， -- Option<T> => Some(T),None本家null
//可以使用Some(i8)对数据进行假设值，假设的值与i8不是同类型，不可直接进行计算，确定后可以将其转化为对应的值进行计算
//// 避免了null的乱用
// fn main(){
//     let some_number = Some(5);
//     let some_string = Some("s b");

//     let abcent: Option<i32> = None;
// }
fn plus_one(x: Option<i8>) -> Option<i8> {
    // rust的match必须穷举所有可能性，或者使用- => (),进行代替
    match x { // 对于不同的x类型进行分类讨论
        None => None,
        Some(i) => Some(i + 1),
    }
}

fn main() { 
    let five = Some(5);
    let six = plus_one(five); //可以用这种方式对some类型进行讨论
    let none = plus_one(None);
}
```

### if let 模块对于一个细节进行布尔判断处理

```rust
//只针对一种匹配可以使用iflet模块，但是放弃了穷举的可能

// if let Some(3) = v {
//     println!("three");
// } else {
//     println!("others")
// }  只对v等于三的情况进行处理
```

### use关键字

use +路径  将相应的函数引入到该模块下，遵循私有制原则
`use std::collection::HashMap;`之类的方法调用hashmap到当前目录。


### 使用外部包
1. 在toml文件中完成对包的引用，比如rand='0.5.5'
2. 之后在主函数中use rand::Rng;进行引用
3. 嵌套引用 ；use std::{cmp::Ordering, io}即相同路径{不同路径,}
4. use std::*将所有std标准库下的所有函数进行引用

### 模块化
1. 如果一个模块定义后面是分号，而不是代码块，rust会从模块的父路径下寻找同名文件作为模块的内容。
2. 这时我们需要新建一个rust文件对该模块进行定义，定义的内容就是引入的内容
3. 对于子模块（二级以下）时，需要新建目录，从目录下进行文件的引入。

### 集合
常用的集合有三种：向量（Vector）、哈希映射（HashMap）和链表（LinkedList），string
#### vector
1. 创建新变量：let 名字:Vec<i32> = Vec::new(); 创建了一个`名字`变量
2. 使用宏：let `名字` = vec![1,2,3]; 创建vector数组
3. 添加元素 v.push(1); 无需声明类型
4. vector离开作用域以后就会被清理掉，所含元素也一样
5. 读取vector里的元素`let three: &i32 = &v[2]`将对应数值转移到`three`中，第二种方法我们可以使用`get`方法，`get`方法返回的是`option<T>`类型，所以我们可以使用`match`对其进行引用。
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4OTg1MTQyNTQsLTE2MTg3Njg4NzgsLT
EzMjUzNzMzMDMsLTEyNDIzMzY3NDUsMTExMTE2MzM5MCw3NjEw
MzczMTQsLTczNjE3Mzc4Miw3NjI0MDU0MDAsNjU5ODQ4MjksLT
g4NTEwNjk5MSwtMTg1MjY0Mjk0NSwtMTQ4NTExMTcyMSwtMjA4
ODc0NjYxMl19
-->