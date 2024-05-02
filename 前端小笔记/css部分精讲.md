
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
同时，也可以和其他选择器结合使用。
```css
.container .highlight {
    background-color: yellow;
}
```
```html
<div class="container">
    <p class="highlight">这段文本将有黄色背景。</p>
    <section>
        <p class="highlight">这段文本也将有黄色背景。</p>
    </section>
</div>
```

#### >5.子代选择器
子代选择器是一种用于选择某个元素的直接子元素的选择器。它由两个选择器构成，中间用大于号（>）连接。第一个选择器是父元素，第二个选择器是要匹配的子元素。

子代选择器与后代选择器（由空格分隔）的不同之处在于，后代选择器会选择所有符合条件的后代元素，无论它们在DOM树中的层级有多深。而子代选择器**只选择直接子元素，即紧随其后的子元素，不包括孙元素或其他更低层级后代**。
```css
<style>
		div > p{
		color : red;
		font-family: "宋体";
		
	}
</style>
```
```html
<div>
    	新雅书院
        <p>这段文字将变成红色，宋体</p>
        <p>这段文字将变成红色，宋体</p>
</div>
```
#### >6.UI伪类选择器
很抽象的一个选择器（纯吐槽），他是专门为用户界面元素设计的，它们可以根据用户的交互状态来选择元素。这些伪类选择器通常与表单元素、链接等相关，但也可以用于其他UI元素。
包括以下的几种类型：
1. `:hover`
   - 当用户将鼠标悬停在元素上时，这个选择器会匹配元素。
2. `:active`
   - 当元素被激活（例如，在鼠标点击时按下的状态）时，这个选择器会匹配元素。
3. `:focus`
   - 当元素获得焦点（通常是表单元素通过键盘导航获得焦点）时，这个选择器会匹配元素。
4. `:focus-within`
   - 当元素本身或它的后代元素获得焦点时，这个选择器会匹配元素。
5. `:enabled`
   - 匹配所有启用的表单元素。
6. `:disabled`
   - 匹配所有禁用的表单元素。
7. `:checked`
   - 匹配所有选中的复选框或单选按钮。
8. `:default`
   - 匹配一组表单元素中的默认元素（例如，提交按钮或者表单中的默认选中的单选按钮或复选框）。
9. `:valid` 和 `:invalid`
   - `:valid` 匹配输入值通过验证的表单元素，而 `:invalid` 匹配输入值不满足验证条件的表单元素。
10. `:required` 和 `:optional`
    - `:required` 匹配必填的表单元素，而 `:optional` 匹配非必填的表单元素。
11. `:read-only` 和 `:read-write`
    - `:read-only` 匹配只读的表单元素，而 `:read-write` 匹配非只读的表单元素。
这些伪类选择器可以帮助开发者根据用户的交互行为来改变UI元素的样式，从而提供更好的用户体验。例如，可以使用`:focus`伪类为获得焦点的输入框添加边框，或者使用`:hover`伪类为链接添加悬停效果。

```css
/* 当鼠标悬停在文本框上时，文本框背景变为红色 */
input[type="text"]:hover,
input[type="password"]:hover {
    background-color: red;
}
```
```html
<form>  
    姓名：<input type="text" placeholder="请输入姓名">  
    <br/>  
    <br/>  
    密码：<input type="password" placeholder="请输入密码">  
</form>  
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwNjE0MDQ4MTEsMTY0NzA0NzY1NiwtMT
Q3MjU0ODEyNiwxNjU5OTMwNzQ4LC0xNDk5MzA4NzA3XX0=
-->