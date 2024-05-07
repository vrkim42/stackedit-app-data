谈心算法没有固定套路，是由局部最优解推出全局最优解。 
![输入图片说明](/imgs/2024-05-07/bGy1sMGyYLd7sZOD.png)
答案：
```c
#include<bits/stdc++.h>
using namespace std;


int main() {
	int a[510] = {0};//总人数不超过500人开510个数组 
	int r, n, s = 0;//水龙头个数，总人数，打水时间
	scanf("%d%d", &n, &r);
	for(int i = 1 ; i <= n; i++){//循环打印人的打水时间
		scanf("%d", &a[i]);
	} 
	sort(a+1, a+n+1);//找到最少时间的先进行打水，这样就满足了局部最优。
	for(int i = 1 ; i <= n; i++){
		if(i >= r + 1){
			a[i] = a[i] + a[i - r];//从第r+1个人开始就是轮换的部分了
		}
		s = s + a[i];
	}
	cout << s;
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzc2MDg5MDEwLC03MDgyOTgwNjEsNTA5MT
ExMTU0XX0=
-->