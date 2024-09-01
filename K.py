def kuy(mydick, mydor):
    pricemin = 0
    for day, required_items in mydor.items():
        min_cost_for_day = float('inf')
        for price, items in mydick.items():
            for item_list in items:
                if all(req_item in item_list for req_item in required_items):
                    min_cost_for_day = min(min_cost_for_day, price)
        pricemin += min_cost_for_day
    return pricemin


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

print(kuy(mydick, mydor))

