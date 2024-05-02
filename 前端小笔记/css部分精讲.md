
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

<!--stackedit_data:
eyJoaXN0b3J5IjpbMzk3NzMxMjQ1LDE2NDcwNDc2NTYsLTE0Nz
I1NDgxMjYsMTY1OTkzMDc0OCwtMTQ5OTMwODcwN119
-->