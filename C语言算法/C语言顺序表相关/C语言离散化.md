只关注数的相对大小，将数改成一些理想化的数如将1,22,142,522,1314,10^9转化为1,2,3,4,5这样的数，实现将复杂的数简单化的目的，否则诸如10 ^ 9这种比较大的数在开数组时就会出现eml或者直接无法运行的情况。
```c++
//C语言离散化
#include<bits/stdc++.h>

int a[20010];
using namespace std;

int main(){
	int n ;
	cin >> n;
	for(int i = 1; i <= n; i++){
		scanf("%d", &a[i]);
	}
	//排序，左闭右开 
	sort(a+1, a+n+1);
	//去重 返回一个迭代器， 指向数组去重后不重复的序列中最后一个元素的下标
	int len = unique(a + 1, a + n + 1) - (a + 1);
	
	for(int i = 1; i <= n; i++){
		cout << a[i] << '\t';
		//在有序数组中查找大于等于a[i]的第一个数的下标。 
		a[i] = lower_bound(a + 1, a + n + 1, a[i]) - a;
		cout << a[i] << '\n';
	} 
}
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbMzUyODg2NTAyLC0xOTg2MDU4NzY2XX0=
-->