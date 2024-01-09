import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))

arr.sort()
cnt = Counter(arr)
result = 0

for i,a in enumerate(arr):
    left, right = i+1,n-1
    while left<right:
        sum = arr[left]+arr[right]+arr[i]

        if sum == 0:
            if arr[left] == arr[right]:
                result += right-left
            else:
                result += cnt[arr[right]]
            left +=1
        elif sum>0:
            right -= 1
        elif sum<0:
            left +=1
print(result)