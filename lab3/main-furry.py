def argmin(a):
    return min(range(len(a)), key=lambda x : a[x])

def banco():
    arrival = []
    service = []
    cashier = []
    waiting = []

    count = 0

    C,N = [int(x) for x in input().split()]
    
    for i in range(N):
        T,D = [int(x) for x in input().split()]
        arrival.append(T)
        service.append(D)
    
    print(C)
    print(N)
    print(arrival)
    print(service)

    #perhaps sort arrival and service by arrival
    last_arrival = 0
    cashier = [0]*C
    waited = 0
    argwaited = 0

    for t in range(N):
        diff = arrival[t]-last_arrival #-waited
        print(f"{t} arrived {diff}s after {t-1}")
        last_arrival = arrival[t]
        if(diff>0):
            cashier = [max(x - diff,0) for x in cashier]
        print(f"cashiers = {cashier}")
        waited = min(cashier)
        argwaited = argmin(cashier)
        for c in range(C):
            succ = False
            if(cashier[c]<=0):
                print(f"{t} got served")
                cashier[c]=service[t]
                succ = True
                break
        if(not succ):
            print(f"{t} waited {waited} to get served by {argwaited}")
            #waiting.append([t,0])
            if(waited>20):
                count += 1
            cashier[argwaited]+=(service[t])
    print(count)


            


        

banco()
