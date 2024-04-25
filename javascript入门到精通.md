## Javascript入门

#### 使用js显示本地时间
```javascript
<button type="button" onclick="document.getElementById('demo').innerHTML = Date()">
<p id="demo"></p>
```
#### 使用js改变HTML内容
```javascript
<p id="demo"> JavaScript可以改变目标段落的内容。 </p>
<button type="button" onclick='document.getElementById("demo").innerHTML = "Hello JavaScript!"'>
点击我！</button>
```
#### 使用js改变文本显示
```javascript
<p id="demo">JavaScript 能够隐藏 HTML 元素。</p>
<button type="button" onclick="document.getElementById('demo').style.display='none'">
点击我！</button>
```
#### 使用js对目标进行输出
![输入图片说明](/imgs/2024-04-25/aFW397yHAhSoUrt3.png)
输出方式：
```js
-window.alert(1+1)
-document.write(1+1)
-document.getElementById(id).innerHTML(1+1)
-console.log(1+1)
```
#### js注释方式与C语言一致
#### js的特殊运算
```js
- var x = 5;
- var z  = Math.pow(x,2); // var z = x ** 2;
```
#### js的数据类型
```js
- var a = 7;//数字
- var lastName = "Gates";// 字符串
- var cars = ["Porsche" "Volvo" "BMW"]// 数组
- var x = {firstName:"Bill", lastName:"Gates"}; // 对象
```
####  js的动态类型
	一个变量可以多次重复声明改变数据类型
#### js的typeof
	与C语言不同，typeof运算符在js里返回声明的数据类型，尚未声明值的变量类型为Undefined，
	将undefined或者null赋值给变量可以清空对象。
#### 通过function声明函数调用
```js
function toCelsius(fahrenhrit){
	return (5/9) * (fahrenheit - 32);
	}
```
#### js对象的创建和显示
```js
var person = {
    firstName: "Bill",
    lastName : "Gates",
    id       : 12345,
    fullName : function() {
       return this.firstName + " " + this.lastName;
    }
};

// 显示对象中的数据：
document.getElementById("demo").innerHTML = person.fullName();
```
#### js的HTML特殊事件
![输入图片说明](/imgs/2024-04-25/iVIi36GgH7A0g6JI.png)
	用在 button onclick=""> /button>上。
#### js的单双引号
var x = "中国是瓷器的故乡，因此 china 与\"China（中国）\"同名。"
一般情况下，双引号不能同时出现多次，但是通过转义字符可以实现多个双引号的并用。
#### js的转译字符
![输入图片说明](/imgs/2024-04-25/sElG7tfMOE8CMyeA.png)
如图所示即为常用转义字符
#### js的数据类型相等判断的特例

```js
var x = "Bill";             
var y = new String("Bill");

// (x === y) 为 false，因为 x 和 y 的类型不同（字符串与对象）
```
这里使用new 关键字将字符串声明为对象，所以二者不相等。所以说new 关键字使代码复杂化。也可能产生一些意想不到的结果，甚至更糟。对象无法比较：
```js
var x = new String("Bill");             
var y = new String("Bill");

// (x == y) 为 false，因为 x 和 y 是不同的对象
```
#### js字符串的查找
![输入图片说明](/imgs/2024-04-25/ouwT8EwcPuR3LWv7.png)
使用lastIndexOf()可以检索最后一次出现的位置，未找到二者均返回-1；二者也均接受第二个参数元素：var pos = str.lastIndexOf("China", 50);
请记住，lastIndexOf（）方法向后搜索，因此位置 50 表示在第 50 位开始搜索，并搜索到开头。
```js
<p id="demo"></p>

<script>
var str = "The full name of China is the People's Republic of China.";
var pos = str.search("China");
document.getElementById("demo").innerHTML = pos;
</script>
`
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA4NTI2MDkxNSwtNTI1ODM1NTAsLTI5Mz
cxNTQxMywxNTA2MjM2MjczLC0xOTMzNjIxOTA0LC0xMjUxOTA5
NTA4LC05MjM0ODcwNDcsLTU2NTU3MjcwMCwxNTI3ODI4MDMsLT
gwMzYxMDE0MF19
-->