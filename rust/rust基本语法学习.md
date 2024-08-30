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

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwNzI0NDgzNjQsLTE0ODUxMTE3MjEsLT
IwODg3NDY2MTJdfQ==
-->