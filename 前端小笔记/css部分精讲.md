
## css选择器部分讲解
### css的链接方式
1. 行内元素，直接在body中的任意标签内执行，样式为style="各种属性"。
2. 在head部分使用选择器对body中的html进行相关css操作。
3. 在外部文件中新建链接，样式为<link rel="stylesheet" type="text/css" href="css/style.css"/>类似的
### 选择器讲解
####  > 1.对于最普通的class标签元素

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

#### >2.对于id属性的元素

我们选择用“#”的方式进行访问
```css
#number{
		代码
	}
```
```html
<div id="number">清华大学</div>
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM0NDg5MjQ2LC0xNDk5MzA4NzA3XX0=
-->