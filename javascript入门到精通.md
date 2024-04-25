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
var str = "The full name of China is the People's Republic of \
China.";
var pos = str.search("China");
document.getElementById("demo").innerHTML = pos;
</script>
```
search返回第一次找到的位置。
这两种方法是不相等的。区别在于：

- search() 方法无法设置第二个开始位置参数。
- indexOf() 方法无法设置更强大的搜索值（正则表达式）。
#### js字符串的读取
```js
1.slice(初始位置，终止位置)
如果省略第二个参数，将裁剪字符串的剩余部分。
- 从头读取：var res = str.slice(7)
- 从尾读取：var res = str.slice(-13)
2.substring(初始位置，终止位置)
用法与slice相同，但是不能接受负的索引。
3.substr(初始位置，字符串长度)
如果省略第二个参数，则substr将裁剪字符串的剩余部分。
- 如果首个参数为负，则将从末尾计算位置，读取到结尾。
```
#### js字符串内容的替换
```js
replace("目标字符串"，"要替换成的字符串")
特点：对大小写敏感，默认只替换首个字符串，不会改变调用的字符串，返回新的字符串。
- 但是可以使用正则表达式使其对大小写不敏感：
var n = str.replace(/MICROSOFT/i,"w3cschools");
- 也可以使用正则表达式使其对所有元素进行替换：
var n = str.replace(/MICROSOFT/g,"w3cschools");
```
#### 转换大小写
```js
通过toUpperCase()将字符串转换为大写：
var text1 = "Hello World!"
var text2 = text1.toUpperCase();//text2即为被转化为大写的text1
```
```js
通过toLowerCase()把字符串转换为小写：
var text1 = "Hello World!"
var text2 = text1.toLowerCase();//text2是被转换为小写的text1
```
#### 字符串的连接空白符删除
```js
var text = "Hello" + " " + "World!";
var text = "Hello".concat(" ","World!")
二者等价。
```
#### 输出已经删除两端空白符的字符串
```js
var str = "                Hello World!              ";
alert(str.trim());
```
#### 返回指定下标字符串
```js
var str = "Hello WORLD";
str.charAt（0）;//返回H
str.charCodeAt(0); //返回H的unicode编码
str[0]; //返回H
```
#### 把字符串替换为数组
```js
function myFunction() {
  var str = "a,b,c,d,e,f";
  var arr = str.split(",");
  document.getElementById("demo").innerHTML = arr[0];
}//返回a;


<p id="demo"></p>

<script>
var str = "Hello";
var arr = str.split("");
var text = "";
var i;
for (i = 0; i < arr.length; i++) {
  text += arr[i] + "<br>"
}
document.getElementById("demo").innerHTML = text;
</script>
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyNDA2OTgzNTgsLTEwNTgzMjUyODksLT
UyNTgzNTUwLC0yOTM3MTU0MTMsMTUwNjIzNjI3MywtMTkzMzYy
MTkwNCwtMTI1MTkwOTUwOCwtOTIzNDg3MDQ3LC01NjU1NzI3MD
AsMTUyNzgyODAzLC04MDM2MTAxNDBdfQ==
-->