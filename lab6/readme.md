i < N
j < M
m == 0 && flag
c <= lastc && c < M

CRITERIO PREDICADO
p1: i < N
p2: j < M
p3: m == 0 && flag
p4: c <= lastc && c < M

Requisitos: p1, !p1, p2, !p2, p3, !p3, p4, !p4

O caso de teste 2, 2, [0,1,1,0] satisfaz


CRITERIO CLAUSULA
p1: i < N
p2: j < M
p3: m == 0
p4: flag
p5: c <= lastc 
p6: c < M

Requisitos: p1, !p1, p2, !p2, p3, !p3, p4, !p4, p5, !p5, !p6, p6

O caso de teste 2, 2, [0,0,1,0] satisfaz


CRITERIO COC
p1: i < N
p2: j < M
p3: m == 0
p4: flag
p5: c <= lastc 
p6: c < M

Requisitos: p1 v, !p1 v, p2 v, !p2 v, p3p4 v, !p3p4 v12, p3!p4 v2, !p3!p4 v12, p5p6 v12, !p5p6 v12, p5!p6 v3, !p5!p6 v23

Os casos de teste (2, 2, [0,1,1,0]), (2, 2, [1,1,1,0]), (2, 2, [0,0,0,0]) satisfaz 
// Acredito que se fizer com matriz 3x3 precise de menos casos de teste 


CRITERIO RACC
p1: i < N
p2: j < M
p3: m == 0
p4: flag
p5: c <= lastc 
p6: c < M

p3p4 = true -> pa		
!p3p4 = false -> p!a
p3!p4 = false 
!p3!p4 = false

p5p6 = true -> pb
p5p6 = false -> p!b
p5!p6 = false 
!p5!p6 = false

Requisitos: p1, !p1, p2, !p2, pa, pb

O caso de teste 2, 2, [0,1,1,0] satisfaz



CRITERIO GACC
p1: i < N
p2: j < M
p3: m == 0
p4: flag
p5: c <= lastc 
p6: c < M

p3p4 = true -> pa		
!p3p4 = false -> p!a
p3!p4 = false 
!p3!p4 = false

p5p6 = true -> pb
!p5p6 = false -> p!b
p5!p6 = false 
!p5!p6 = false

Requisitos: p1, !p1, p2, !p2, pa, p!a

O caso de teste 2, 2, [0,1,1,0] satisfaz


