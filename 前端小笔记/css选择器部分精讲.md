
## css选择器部分讲解
### css的链接方式
1. 行内元素，直接在body中的任意标签内执行，样式为style="各种属性"。
2. 在head部分使用选择器对body中的html进行相关css操作。
3. 在外部文件中新建链接，样式为<link rel="stylesheet" type="text/css" href="css/style.css"/>类似的
### 选择器讲解
####  > 1.对于最普通的class标签元素(类选择器)

- 我们选择用"."的形式进行访问
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
- 后续均采用css➕html的方式展示。

#### >2.对于id属性的元素(id选择器)

- 我们选择用“#”的方式进行访问
```css
#number{
		代码
	}
```
```html
<div id="number">清华大学新雅书院</div>
```

#### >3.元素选择器
- 我们可以直接选取对应的内容如p或者h标题。
```css
p {
    color: blue;
    font-size: 16px;
}
```
```HTML 
<p>这段文本将显示为蓝色，字体大小为16px。</p>
```
- 当然我们也可以用*对本文所有元素进行操作。
```css
/!-- 我们也可以使用这种方式对全部元素进行操作--/
* {
	css代码;
}
```
#### >4.后代选择器
- 它用于选择位于另一个元素内的特定元素，**无论这些元素之间有多少层次**。后代选择器由两个或更多选择器组成，中间用空格分隔。它选择所有符合最左端选择器的元素，然后选择这些元素的后代中符合后续选择器的元素。
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
  - 子代选择器是一种用于选择某个元素的直接子元素的选择器。它由两个选择器构成，中间用大于号（>）连接。第一个选择器是父元素，第二个选择器是要匹配的子元素。

- 子代选择器与后代选择器（由空格分隔）的不同之处在于，后代选择器会选择所有符合条件的后代元素，无论它们在DOM树中的层级有多深。而子代选择器**只选择直接子元素，即紧随其后的子元素，不包括孙元素或其他更低层级后代**。
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
5. `E:root`
- :root选择器用于匹配文档根元素，在HTML中，根元素始终是html元素。也就是说用“:root选择器”定义的样式，对所有页面元素都生效。对于不需要该样式的元
素，可以单独设置样式进行覆盖。:root选择器用于匹配文档根元素，在HTML中，根元素始终是html元素。也就是说“:root选择器”定义的样式，对所有页面元素都生效。对于不需要该样式的元素，可以单独设置样式进行覆盖。
6. `E:not`
- CSS中的`:not()`伪类选择器用于匹配不符合一组选择器条件的元素。这个选择器非常有用，因为它允许开发者根据排除条件来选择元素，而不是直接指定它们。
`:not()`伪类可以与任何其他简单选择器配合使用，包括类选择器、类型选择器、属性选择器等，但不能与伪元素配合使用，也不能嵌套`:not()`伪类。
下面是一个基本的例子：
```css
/* 为所有不是段落（p）的元素设置样式 */
:not(p) {
  color: blue;
}
/* 为所有不是类名为 .example 的元素设置样式 */
:not(.example) {
  color: red;
}
/* 为所有类型不是 div 且没有 id 的元素设置样式 */
:not(div):not([id]) {
  font-size: 14px;
}
```
在`:not()`伪类中，可以使用多个选择器，用逗号隔开，例如：
```css
/* 排除多个类 */
:not(.class1, .class2, .class3) {
  margin: 0;
}
```
`:not()`伪类在CSS3中引入，并且得到了现代浏览器的广泛支持。在使用时，需要注意选择器的性能问题，尤其是在选择器中包含大量复杂的选择条件时，**可能会导致页面加载速度变慢**。

7. `E:only-child`
- `:only-child` 是一个CSS伪类选择器，它选择的是没有任何兄弟元素的元素，即它是其父元素的唯一子元素。换句话说，使用 `:only-child` 选择器的元素必须是它的父元素的唯一直接子元素。
例如，如果你有一个列表，并且只想对列表中唯一的列表项进行样式化，你可以使用 `:only-child` 伪类：
```css
li:only-child {
  color: red;
}
```
在上面的例子中，只有当 `<li>` 元素是它父元素（比如 `<ul>` 或 `<ol>`）的唯一子元素时，它才会被设置为红色。
需要注意的是，`:only-child` 是针对唯一子元素的选择器，而不是针对唯一类型的子元素。如果一个元素是它父元素的唯一子元素，即使它有多个不同类型的子元素，`:only-child` 仍然会应用样式。
此外，`:only-child` 可以与其他伪类结合使用，例如，如果你想选择一个既是唯一子元素又是鼠标悬停状态的元素，你可以这样写：
```css
li:only-child:hover {
  background-color: yellow;
}
```
在这个例子中，只有当 `<li>` 元素是它父元素的唯一子元素，并且鼠标悬停在该元素上时，它才会获得黄色的背景。

8. `E:nth-last-child`
- `:nth-last-child` 是一个CSS伪类选择器，它选择一个元素，该元素在其父元素的子元素列表中按照特定的顺序倒序排列。它允许你按照一个公式来选择一个或多个子元素，这个公式可以是关键字 `even` 或 `odd`，也可以是一个简单的算术表达式，如 `n`、`2n+1`、`3n-1` 等。
例如，如果你想选择一个列表中的倒数第二个子元素，你可以使用 `:nth-last-child(2)`：
```css
li:nth-last-child(2) {
  color: red;
}
```
在这个例子中，列表中每个 `<li>` 元素都会检查它是否是其父元素的倒数第二个子元素，如果是，则它的文本颜色会被设置为红色。
`:nth-last-child` 伪类也可以使用 `an+b` 形式的公式，其中 `a` 和 `b` 是整数，`n` 代表一个计数器（从0开始）。例如，如果你想选择每个列表的倒数第五个元素，你可以使用 `:nth-last-child(5n)` 或 `:nth-last-child(5)`（因为 `5n` 在 `n=1` 时就是5）。
这里有一些使用 `:nth-last-child` 的例子：
```css
/* 选择每个父元素下的倒数第二个子元素 */
:nth-last-child(2) {
  color: red;
}
/* 选择每个父元素下的倒数第五个子元素 */
:nth-last-child(5) {
  color: blue;
}
/* 选择每个父元素下的倒数奇数个子元素 */
:nth-last-child(odd) {
  font-weight: bold;
}
/* 选择每个父元素下的倒数偶数个子元素 */
:nth-last-child(even) {
  font-style: italic;
}
/* 选择每个父元素下的倒数第1个子元素，然后每隔 3 个子元素选择一次 */
:nth-last-child(3n+1) {
  text-decoration: underline;
}
```
`:nth-last-child` 选择器在CSS3中引入，并且得到了现代浏览器的广泛支持。它对于对列表或网格布局中的元素进行复杂的样式设计非常有用。

9. `E:nth-of-type(n)`
- `:nth-of-type(n)` 是一个CSS伪类选择器，它选择特定类型的元素，这些元素在其父元素的所有相同类型的子元素中按照一定的顺序排列。与 `:nth-child(n)` 不同，`:nth-of-type(n)` 仅考虑特定类型的元素，而 `:nth-child(n)` 则考虑所有子元素。
`:nth-of-type(n)` 选择器中的 `n` 可以是预定义的关键字 `even` 或 `odd`，也可以是一个简单的算术表达式，如 `n`、`2n+1`、`3n-1` 等。
例如，如果你想选择一个列表中的每个偶数位置 `<li>` 元素，你可以使用 `:nth-of-type(even)`：
```css
li:nth-of-type(even) {
  color: red;
}
```
在这个例子中，每个 `<li>` 元素都会检查它是否是其父元素中 `<li>` 类型元素的偶数位置，如果是，则它的文本颜色会被设置为红色。
`:nth-of-type` 伪类也可以使用 `an+b` 形式的公式，其中 `a` 和 `b` 是整数，`n` 代表一个计数器（从0开始）。例如，如果你想选择每个列表的第三个 `<li>` 元素，你可以使用 `:nth-of-type(3n)` 或 `:nth-of-type(3)`（因为 `3n` 在 `n=1` 时就是3）。
这里有一些使用 `:nth-of-type` 的例子：
```css
/* 选择每个父元素下的偶数位置的 <li> 元素 */
li:nth-of-type(even) {
  color: red;
}
/* 选择每个父元素下的第三个 <li> 元素 */
li:nth-of-type(3) {
  color: blue;
}
/* 选择每个父元素下的奇数位置的 <li> 元素 */
li:nth-of-type(odd) {
  font-weight: bold;
}
/* 选择每个父元素下的第5个 <li> 元素，然后每隔四个 <li> 元素选择一次 */
li:nth-of-type(5n+1) {
  text-decoration: underline;
}
```
`:nth-of-type` 选择器在CSS3中引入，并且得到了现代浏览器的广泛支持。它对于对复杂文档结构中的特定类型元素进行样式设计非常有用。
  
10. `E:empty`
-  
这些伪元素和伪类选择器提供了强大的选择和样式化能力，使得CSS能够以更加精细和灵活的方式控制页面布局和设计。
#### 8.兄弟选择器
在CSS中，兄弟选择器用于选择一个元素后的兄弟元素。CSS提供了两种兄弟选择器：
1. **相邻兄弟选择器** (`+`)
   - 相邻兄弟选择器选择紧随其指定元素后的第一个兄弟元素。例如，如果你想要选择紧随一个`<div>`元素后的第一个`<p>`元素，你可以使用以下选择器：
     ```css
     div + p {
       /* 样式规则 */
     }
     ```
     在这个例子中，只有紧随`<div>`元素后的第一个`<p>`元素会应用指定的样式。如果`<div>`和`<p>`之间有其他元素，或者`<p>`不是紧随`<div>`之后的第一个元素，那么这个`<p>`不会被选中。
2. **通用兄弟选择器** (`~`)
   - 通用兄弟选择器选择指定元素后的所有兄弟元素，而不考虑它们之间的位置。例如，如果你想要选择一个`<div>`元素后的所有`<p>`兄弟元素，你可以使用以下选择器：
     ```css
     div ~ p {
       /* 样式规则 */
     }
     ```
     在这个例子中，`<div>`元素后的所有`<p>`元素都会应用指定的样式，无论它们之间有多少个其他元素。
兄弟选择器对于样式化特定位置的元素非常有用，尤其是在你需要基于文档结构而不是类或ID来应用样式时。它们可以帮助你减少对类的依赖，并创建更加简洁和可维护的CSS代码。

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
#### 辩论相邻兄弟选择器和子代选择器
当然，让我们通过具体的代码示例来展示相邻兄弟选择器（Adjacent Sibling Selector）和子代选择器（Child Selector）的区别。
##### 子代选择器（Child Selector）
子代选择器（`>`）用于选择某个元素的直接子元素。这里是一个简单的HTML和CSS示例：
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Child Selector Example</title>
<style>
  div > p {
    color: red;
  }
</style>
</head>
<body>
<div>
  <p>这是直接子元素，文本将变成红色。</p>
  <section>
    <p>这不是直接子元素，文本不会变红。</p>
  </section>
</div>
</body>
</html>
```
在这个示例中，只有`<div>`元素的直接子元素`<p>`的文本颜色会变成红色。`<section>`元素内的`<p>`不会受到影响，因为它不是`<div>`的直接子元素。
##### 相邻兄弟选择器（Adjacent Sibling Selector）
相邻兄弟选择器（`+`）用于选择紧随另一个元素后的第一个兄弟元素。这里是一个简单的HTML和CSS示例：
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Adjacent Sibling Selector Example</title>
<style>
  h1 + p {
    color: blue;
  }
</style>
</head>
<body>
<h1>这是一个标题</h1>
<p>这是紧随标题后的段落，文本将变成蓝色。</p>
<p>这不是紧随标题后的段落，文本不会变蓝。</p>
</body>
</html>
```
在这个示例中，只有紧随`<h1>`元素后的第一个`<p>`元素的文本颜色会变成蓝色。第二个`<p>`元素不受影响，因为它不是紧随`<h1>`元素后的第一个兄弟元素。
通过这两个示例，我们可以清楚地看到子代选择器和相邻兄弟选择器的区别和它们各自的作用范围。

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyMjM3MjY3OTMsMTU4ODU2NTY2MiwxMT
k5Mjg4MzU4LDYxNTk4MjE3NywxMTMwMzI0NDA2XX0=
-->