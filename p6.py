def lis(arr):
  n = len(arr)
  lis = [1]*n
  for i in range(1,n):
    for j in range(0,i):
      if arr[i] > arr[j]:
        lis[i] = max(lis[i],lis[j]+1)
  return max(lis)

if __name__ == '__main__':
  n = int(input())
  x = [int(x) for x in input().split()]