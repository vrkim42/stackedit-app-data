
## css选择器部分讲解
### css的链接方式
1. 行内元素，直接在body中的任意标签内执行，样式为style="各种属性"。
2. 在head部分使用选择器对body中的html进行相关css操作。
3. 在外部文件中新建链接，样式为<link rel="stylesheet" type="text/css" href="css/style.css"/>类似的
### 选择器讲解
####  > 1.对于最普通的class标签元素(类选择器)

我们选择用"."的形式进行访问
如下所示：
```css
.one{
		css代码
		}
```
对这个部分进行操作：
```html
<div class="one">元素选择器</div>
```
后续均采用css➕html的方式展示。

#### >2.对于id属性的元素(id选择器)

我们选择用“#”的方式进行访问
```css
#number{
		代码
	}
```
```html
<div id="number">清华大学新雅书院</div>
```

#### >3.元素选择器
我们可以直接选取对应的内容如p或者h标题。
```css
p {
    color: blue;
    font-size: 16px;
}
```
```HTML 
<p>这段文本将显示为蓝色，字体大小为16px。</p>
```

#### >4.后代选择器
它用于选择位于另一个元素内的特定元素，**无论这些元素之间有多少层次**。后代选择器由两个或更多选择器组成，中间用空格分隔。它选择所有符合最左端选择器的元素，然后选择这些元素的后代中符合后续选择器的元素。
```css
ul li {
    color: blue;
    font-size: 16px;
}
```
```html
<ul>
    <li>这段文本将显示为蓝色，字体大小为16px。</li>
    <li>这段文本也将显示为蓝色，字体大小为16px。</li>
</ul>
```

#### >5.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTkyMTEwNTAyNiwtMTQ3MjU0ODEyNiwxNj
U5OTMwNzQ4LC0xNDk5MzA4NzA3XX0=
-->