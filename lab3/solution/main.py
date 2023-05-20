import Banco

def main():
    arrival = []
    service = []
    C,N = [int(x) for x in input().split()]
    for i in range(N):
        T,D = [int(x) for x in input().split()]
        arrival.append(T)
        service.append(D)
    
    print(Banco.banco(C, arrival, service))


if __name__ == "__main__":
    main()