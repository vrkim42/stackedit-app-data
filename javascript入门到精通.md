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
#### 

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyNTE5MDk1MDgsLTkyMzQ4NzA0NywtNT
Y1NTcyNzAwLDE1Mjc4MjgwMywtODAzNjEwMTQwXX0=
-->