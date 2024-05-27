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

## 2
```
<script>
			    let mymath = {
					score: 750,
					add: function(num1,num2){
						console.log(num1+num2);
					},
					arr:{1,3,4,5,7,2,4,2,8,90}//错了
				}
				let max = mymath.arr[1];
				for(let i = 0; i < mymath.arr.length(); i++){
					
					if(max < arr[i])//错了
					max = arr[i];
				}
				console.log(max)
				console.log(mymath.score)
				console.log(mymath.add(1,3))
			</script>
```
我的
```
<script>
    let mymath = {
        score: 750,
        add: function(num1, num2){
            console.log(num1 + num2);
        },
        arr: [1, 3, 4, 5, 7, 2, 4, 2, 8, 90] // 使用方括号定义数组
    };

    let max = mymath.arr[0]; // 初始化为第一个元素
    for(let i = 1; i < mymath.arr.length; i++){ // 从第二个元素开始比较
        if(max < mymath.arr[i]){
            max = mymath.arr[i];
        }
    }

    console.log(max); // 打印最大值
    console.log(mymath.score); // 打印分数
    mymath.add(1, 3); // 调用add方法并打印结果
</script>
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzODM5MjUyODksMTU2OTE0NjkxNF19
-->