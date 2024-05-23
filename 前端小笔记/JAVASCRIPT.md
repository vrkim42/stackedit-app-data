![输入图片说明](/imgs/2024-05-17/UKxNwArwbGBQLY3p.jpeg)
for in 语句此时输出下面的 tim。
使用 for in 语句遍历现状。

### JavaScript事件

 - onclick 点击事件
 - onmouseover 鼠标经过
 - onmouseout 鼠标移出
 - onchange 文本内容发生改变
 - onselect 文本框选中
 - onfocus 光标聚集
 - onblur 移开光标
### 输出方式
 - alert()警告框
 - console.log()控制台
 - prompt()输入框
### dom
document.getElementById('   ').innerHTML
document.getElementByClassName('   ').innerText
document.getElementByTagName('   ')[0];
console.log(element_tag);
element_tag.style.color = 'red';
### 声明对象
```js
var user = {
			name : '111',
			sex : 'male',
			age : 20,
			eat : function(){
				alert('111');
			}
		};
		console.log(user.name);
		user.eat();

//json对象指键队
var jsonstr = '{"name" :"vscode" , "age" : 18, "addr" : ['北京', '上海', '深圳']}';
		alert(jsonstr.name);
		var jsobject = JSON.parse(jsonstr);// json转化为js对象
		alert(jsobject);
		var userJSONStr = JSON.stringify(jsobject); // js对象转化为json字符串
		alert(userJSONStr);
```

### BOM
```js
//定时器 -- 周期性执行某一个函数
		var i = 0;
		setInterval(){
			i++;
			console.log("定时器被执行了"+i+"次 ");
		},2000};

//定时器 - 延迟时间执行一次
		setTimeout(function){
			alert("JS");
		}, 3000};

//地址跳转
alert(location.href);
location.href = "http://www.baidu.com";


```

### DOM(首字母大写)
document 整个文档对象
element 元素对象
attribute 属性对象
text 文本对象
comment 注释对象


```html
<input type=“button“> id="btn1" value="时间绑定一" onclick="on()">

<input type=“button“> id="btn2" value="时间绑定二" onclick="on()">


script
function on(){
 alert('   ');
}
document.getElementById('btn2').onclick = function(){
}
```
`onload` `onblur` `onfocus` `onsubmit` `onkeydown`


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzMzE2NjQ0MTgsLTE3MTQyODk4NTksMj
E0NzE3NjY1NSwtODU3MzkyODAzLC0zMTc3MzYzNTgsLTEwOTIz
NTg0MDIsNzY4MDkwNTI0LDIyNzUxNTk2OCwtMTUyMjc0NTkwOC
wtMjA4ODc0NjYxMiwtMTA4MTAzNzI5XX0=
-->