def tipo_triangulo(a,b,c):
    if (a <= 0 or b <= 0 or c <= 0):
        return "invalido"
    
    
    if (a+b >= c and a+c >= b and b+c >= a):
        if (a==b and b == c):
            return "equilatero"
        if (a==b or a==c or b==c):
            return "isosceles"
        return "escaleno"
    return "invalido"