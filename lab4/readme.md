# Particionamentos

- P1 (C = 1, 1 < C < 10, C = 10)
- P2 (N = 1, 1 < N < 1000, N = 1000)
- P3 (N < C, N = C, N > C)
- P4 (Ocorrem repetições de tempo de chegadas = (sim, não))
- P5 (todos duram 10 minutos = (sim, não))

---

## Each choice

Foram gerados 29 mutantes, dentre os quais 11 sobreviveram.

- P11, P12, P13
- P21, P22, P23
- P32, P31, P33
- P42, P41
- P51, P52

**Casos de Teste**:

1. C=1,N=1,T=[0],D=[10]
2. C=9,N=4,T=[2,2,2,6],D=[5,6,2,10]
3. C=10,N=1000,T=1000*[0],D=1000*[10]

# Pairwise

Foram gerados 29 mutantes, dentre os quais 11 sobreviveram.
Abaixo estão apresentados os casos de teste, e em seguida, a combinação pairwise dos particionamentos e seu respectivo caso de teste correspondente.

**Casos de Teste**:

1. C=1,N=1,T=[0],D=[10]
2. C=1,N=4,T=[2,2,2,6],D=[5,6,2,10]
3. C=1,N=1000,T=1000*[0],D=1000*[10]
4. C=4,N=1,T=[0],D=[10]
5. C=4,N=4,T=[2,2,2,6],D=[5,6,2,10]
6. C=4,N=1000,T=1000*[0],D=1000*[10]
7. C=10,N=1,T=[0],D=[10]
8. C=10,N=4,T=[2,2,2,6],D=[5,6,2,10]
9. C=10,N=1000,T=1000*[0],D=1000*[10]
10. C=10,N=10,T=10*[0],D=10*[10]
11. C=4, N=4, T=[1,2,3,4], D=4\*[10]
12. C=4, N=4,T=[1,2,3,4], D=[5,6,2,10]
13. C=10,N=1,T=[0],D=[1]
14. C=10,N=1000,T=1000*[0],D=1000*[5]
15. C=4, N=5, T=[1,2,3,4,5],D=[5,6,2,10,1]

**Combinações entre P1 e P2**:

- P11, P21 X 1
- P11, P22 X 2
- P11, P23 X 3
- P12, P21 X 4
- P12, P22 X 5
- P12, P23 X 6
- P13, P21 X 7
- P13, P22 X 8
- P13, P23 X 9

**Combinações entre P1 e P3**:

- P11, P31 Insatisfativel
- P11, P32 X 1
- P11, P33 X 2
- P12, P31 X 4
- P12, P32 X 5
- P12, P33 X 6
- P13, P31 X 7
- P13, P32 X 10
- P13, P33 X 9

**Combinações entre P1 e P4**:

- P11, P41 X 2
- P11, P42 X 1
- P12, P41 X 5
- P12, P42 X 4
- P13, P41 X 8
- P13, P42 X 7

**Combinações entre P1 e P5**:

- P11, P51 X 1
- P11, P52 X 2
- P12, P51 X 4
- P12, P52 X 5
- P13, P51 X 7
- P13, P52 X 8

**Combinações entre P2 e P3**:

- P21, P31 X 4
- P21, P32 X 1
- P21, P33 Insatisfativel
- P22, P31 X 8
- P22, P32 X 5
- P22, P33 X 6
- P23, P31 Insatisfativel
- P23, P32 Insatisfativel
- P23, P33 X 3

**Combinações entre P2 e P4**:

- P21, P41 Insatisfativel
- P21, P42 X 1
- P22, P41 X 2
- P22, P42 X 11
- P23, P41 X 6
- P23, P42 X Insatisfativel

**Combinações entre P2 e P5**:

- P21, P51 X 1
- P21, P52 X 13
- P22, P51 X 11
- P22, P52 X 12
- P23, P51 X 3
- P23, P52 X 14

**Combinações entre P3 e P4**:

- P31, P41 X 8
- P31, P42 X 7
- P32, P41 X 10
- P32, P42 X 11
- P33, P41 X 14
- P33, P42 X 15

**Combinações entre P3 e P5**:

- P31, P51 X 4
- P31, P52 X 8
- P32, P51 X 1
- P32, P52 X 5
- P33, P51 X 9
- P33, P52 X 15

**Combinações entre P4 e P5**:

- P41, P51 X 3
- P41, P52 X 5
- P42, P51 X 11
- P42, P52 X 12

---

# Base choice

Foram gerados 29 mutantes, dentre os quais 18 sobreviveram.

- Base: P12, P22, P33, P42, P52 - C=2, N=3, T=[1,2,3], D=[1,5,10]

Testes:

1. P11, P22, P33, P42, P52 - C=1, N=3, T=[1,2,3], D=[1,5,10]
2. P13, P22, P33, P42, P52 - C=10, N=11, T=[1,2,3,4,5,6,7,8,9,10,11], D=11\*[5]
3. P12, P21, P33, P42, P52 - Insatisfativel
4. P12, P23, P33, P42, P52 - Insatisfativel
5. P12, P22, P31, P42, P52 - C=3, N=2, T=[1,2], D=[1,2]
6. P12, P22, P32, P42, P52 - C=3, N=3, T=[1,2,3], D=[1,2,3]
7. P12, P22, P33, P41, P52 - C=2, N=3, T=[3,3,3], D=[1,5,10]
8. P12, P22, P33, P41, P51 - C=2, N=3, T=[1,2,3], D=[10,10,10]
