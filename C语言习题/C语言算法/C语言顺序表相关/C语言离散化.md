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
在C++中，`unique`函数是STL（Standard Template Library，标准模板库）算法的一部分，用于去除序列中的连续重复元素。它属于`<algorithm>`头文件。`unique`函数本身并不真正删除元素，而是通过重新排列序列中的元素，使得每个唯一的元素只出现一次，并返回一个指向新的最后一个元素之后的位置的迭代器。

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTcyODI4NTEwMl19
-->