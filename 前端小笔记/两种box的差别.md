### content-box
content-box(内容盒模型）：
●这是CSS的默认盒模型。
·在这个模型中，元素设置的宽度和高度只包括内容区域（content area)，不包括边框
（border)和内边距(padding）
·举个例子，假设你有一个宽度设为100px的盒子,如果你给它添加10px的内边距和5px的边
框，那么这个盒子的总宽度实际上是130px(100px内容宽度+10px左内边距+10px右内
边距+5px左边框+5px右边框)
![输入图片说明](/imgs/2024-05-24/Mk1t7EQrVIili4l9.jpeg)


### boder-box
Border-box（边框盒模型）
●当你对一个元素设置box-sizing: border-box;时，这个元素就采用了边框盒模型。
在这个模型中，元素设置的宽度和高度包括内容区域、内边距和边框。
·同样的例子，如果你有一个宽度设为100px的盒子,即使你添加了内边距和边框,这个盒
子的总宽度依然是100px。这是因为内边距和边框的宽度会被包含在你设定的宽度内。![输入图片说明](/imgs/2024-05-24/98et2YtPmY7UyDgN.jpeg)

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg2Nzk3NDU3MV19
-->