
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
#### 7.结构性伪类选择器（归属伪类选择器，但是单列出来强调一下）
包括E:after、E:before、E:nth-child()、E:first-child、E:last-child等，它们用于选择和样式化文档中的特定元素，基于它们的位置、状态或其他条件。下面是每个选择器的解释：
1. `E:after` 和 `E:before`
   - 这两个伪元素用于在指定的元素`E`的内容前或后插入内容。它们通常与`content`属性一起使用，来添加装饰性内容或生成内容。例如，可以使用`:before`伪元素来添加前置图标，而使用`:after`伪元素来清除浮动。
   ```css
   .icon:after {
     content: '†';
   }
   ```
2. `E:nth-child()`
   - 这个伪类选择器用于匹配一组兄弟元素中的第n个`E`元素。`n`可以是数字、关键词（如`even`或`odd`）或公式（如`2n+1`）。例如，`li:nth-child(3)`会选择一组列表中的第三个`<li>`元素。
   ```css
   li:nth-child(2n) {
     background-color: yellow;
   }
   ```
3. `E:first-child`
   - 这个伪类选择器用于匹配一组兄弟元素中的第一个`E`元素。如果`E`是其父元素的第一个子元素，它就会被选中。
   ```css
   p:first-child {
     font-size: 120%;
   }
   ```
4. `E:last-child`
   - 这个伪类选择器用于匹配一组兄弟元素中的最后一个`E`元素。如果`E`是其父元素的最后一个子元素，它就会被选中。
   ```css
   p:last-child {
     margin-bottom: 0;
   }
   ```
这些伪元素和伪类选择器提供了强大的选择和样式化能力，使得CSS能够以更加精细和灵活的方式控制页面布局和设计。
#### 8.
#### >last1.辩证div p、div>p、div,p
1. `div p`
   - 这是一个后代选择器（Descendant combinator），用于选择所有属于`div`元素后代的`p`元素，无论它们在DOM树中的层级有多深。这意味着，如果`p`元素是`div`元素的子元素、孙元素或其他更低层级的后代元素，它都会被这个选择器选中。
2. `div>p`
   - 这是一个子代选择器（Child combinator），用于选择父元素为`div`的直接子元素`p`。这意味着只有当`p`元素紧随`div`元素之后，并且是它的直接子元素时，才会应用样式。不会选择`div`的孙子元素或其他更低层级中的`p`元素。
3. `div,p`
   - 这是一个分组选择器（Grouping selector），用于将多个选择器组合在一起，以便为它们应用相同的样式。在这种情况下，`div,p`选择器会选择所有的`div`元素和所有的`p`元素，并将相同的样式规则应用于它们。这个选择器实际上是`div`和`p`两个选择器的并集。
下面是一个例子，展示了如何使用这些选择器：
```css
/* 这将选择所有是 div 后代的 p 元素 */
div p {
  color: red;
}
/* 这将选择所有是 div 的直接子元素的 p 元素 */
div > p {
  font-weight: bold;
}
/* 这将选择所有的 div 元素和所有的 p 元素 */
div, p {
  margin: 10px;
}
```
在实际的HTML中使用时，这些选择器将如下所示：
```html
<div>
  <p>This is a child p of a div.</p>
  <div>
    <p>This is a grandchild p, still a descendant of the initial div.</p>
  </div>
</div>
<p>This is a standalone p element.</p>
```
在这个例子中，所有作为`div`后代（包括直接子元素和更低层级的后代）的`p`元素都会有红色的文本，因为它们被`div p`选择器选中。紧随`div`之后的`p`元素会有粗体文本，因为它们是`div`的直接子元素，被`div > p`选择器选中。所有的`div`和`p`元素都会有10像素的外边距，因为它们被分组选择器`div, p`选中。

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5MjUzNDk2ODYsMjI0NzcxMTc4LDE2ND
cwNDc2NTYsLTE0NzI1NDgxMjYsMTY1OTkzMDc0OCwtMTQ5OTMw
ODcwN119
-->