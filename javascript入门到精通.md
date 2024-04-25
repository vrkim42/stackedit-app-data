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
#### js的
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTUwNTc4OTkxMSwxNTA2MjM2MjczLC0xOT
MzNjIxOTA0LC0xMjUxOTA5NTA4LC05MjM0ODcwNDcsLTU2NTU3
MjcwMCwxNTI3ODI4MDMsLTgwMzYxMDE0MF19
-->