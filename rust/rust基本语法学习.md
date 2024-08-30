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
fn another_funnction(x:i32, y:&str){//参数必须表明类型

println!("function!");

}
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjUwMDI1MTkzLC04ODUxMDY5OTEsLTE4NT
I2NDI5NDUsLTE0ODUxMTE3MjEsLTIwODg3NDY2MTJdfQ==
-->