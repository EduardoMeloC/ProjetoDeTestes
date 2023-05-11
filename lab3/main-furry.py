def main():
    arrival = []
    service = []
    C,N = [int(x) for x in input().split()]
    for i in range(N):
        T,D = [int(x) for x in input().split()]
        arrival.append(T)
        service.append(D)
    
    print(banco(C, arrival, service))

def argmin(a):
    return min(range(len(a)), key=lambda x : a[x])

def banco(C, arrival, service):
    #perhaps sort arrival and service by arrival
    last_arrival = 0
    cashier = [0]*C
    waited = 0
    argwaited = 0
    count = 0

    for t in range(len(arrival)):
        diff = arrival[t]-last_arrival
        #print(f"{t} arrived {diff}s after {t-1}")
        last_arrival = arrival[t]
        if(diff>0):
            cashier = [max(x - diff,0) for x in cashier]
        #print(f"cashiers = {cashier}")
        argwaited = argmin(cashier)
        waited = cashier[argwaited]
        if(waited<=0):
            #print(f"{t} got served")
            cashier[argwaited]=service[t]
        else:
            #print(f"{t} waited {waited} to get served by {argwaited}")
            if(waited>20):
                count += 1
            cashier[argwaited]+=(service[t])

    return count

main()