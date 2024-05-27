## 1
```js
<script>
    var mymath = {
        score: 750,
        add: function(num1, num2){
            console.log(num1 + num2);
        }
    };

    console.log(mymath.score); // 输出750
    mymath.add(1, 3); // 调用add方法，输出4
</script>
```
我的
```js
var mymath = {
				score: 750;
				function add(num1, num2){
					console.log(num1 + num2)
				}
			}
			console.log(mymath.score)
			console.log(mymath.function(1,3))
```
1.  对象属性和方法的定义应使用逗号分隔，而不是分号。
2.  对象方法不能在定义时直接使用`function`关键字，而应作为对象的属性
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU2OTE0NjkxNF19
-->