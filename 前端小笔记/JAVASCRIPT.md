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




<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMxNzczNjM1OCwtMTA5MjM1ODQwMiw3Nj
gwOTA1MjQsMjI3NTE1OTY4LC0xNTIyNzQ1OTA4LC0yMDg4NzQ2
NjEyLC0xMDgxMDM3MjldfQ==
-->