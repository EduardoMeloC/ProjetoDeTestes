# m's length must be N * M
def isStairMatrix(N, M, m):
    ans = 'S'

    lastc = -1
    for i in range(0, N):
        print("i < N: true")
        flag = 1
        c = 0
        for j in range(0, M):
            print("j < M: true")
            mm = m[(i*N)+j]
            if mm == 0 and flag:
                print("mm == 0 and flag: true")
                c += 1
            else:
                print("m == 0: " + str(m == 0) + ", flag: " + str(flag))
                flag = 0

        print("j < M: false")
        
        if c <= lastc and c < M:
            print("c <= lastc and c < M")
            ans = 'N'
            break
        else:
            print("c <= lastc: " + str(c <= lastc) + ", flag: " + str(c < M))

        lastc = c

    print("i < N: false")

    return ans