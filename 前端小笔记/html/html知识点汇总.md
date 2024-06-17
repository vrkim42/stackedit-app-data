## 表格
```
<table border="9" align="center">
分窗数目
tr,td,th
tr表示表格中的一行
th表示表头单元格，字体会加粗。
td表示普通数据单元格

<input type="radio" name="sex" value="男" checked/>男
单标签，表示单选

<select name="籍贯">
多选一框，下面用的是option表示相应的值，使用value表示所代表的值

<th width="500px" height="40px" colspan="5"><form action="/demo/demo_form.asp">
相关的大小，占的行数，相关的操作。

<input  type="submit" value="submit"/>
提交框

<input type="checkbox" name="habbit" value="音乐"/>音乐
复选框，有相关的name属性框和属性值

<button id="on" value="" onclick="on()">全选</button>
按钮框，生成按钮，onclick衔接js代码，
function on(){
	var habbits = document.getElementsByName("habbit");
	for(let i = 0; i < habbits.length; i++){
		const element = habbits[i];
		element.checked = true;
	}
}/*全选*/

<input type="date"> 日期选择框，选择日期


```


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTkyNDMwMzA3MiwxNDMzNzA2MzE3XX0=
-->