from itertools import combinations
def kuy(mydick, mydor, K):
    
     
    
    return kuysus



N, M, K = map(int, input().split())
mydick = {}  
while N > 0 :
    med, price = map(int, input().split())
    stite = list(map(int, input().split()))
    if price in mydick:
        mydick[price].append(stite)
    else:
        mydick[price] = [stite]
    N -=1
    

mydor = {}
today = 1
while M > 0 :
    day = int(input())
    eiei = list(map(int,input().split()))
    mydor[today] = eiei
    M -= 1
    today +=1




kuysus = kuy(mydick, mydor, K)
for xxx in kuysus:
    print(xxx)