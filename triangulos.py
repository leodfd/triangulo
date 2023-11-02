def triangulo(tr1, tr2, tr3):
    if tr1 == tr2 == tr3:
        return "Triangulo equilatero"
    elif tr1 == tr2 or tr1 == tr3 or  tr3 == tr2:
        return "Triangulo isosceles"
    elif tr1 == 90 or tr2 == 90 or tr3 == 90:
        return "Triangulo retangulo"
    elif tr1 < 90 or tr2 < 90 or tr3 < 90:
        return "Triangulo acutangulo"
    elif tr1 > 90 or tr2 > 90 or tr3 > 90:
        return "Triangulo obtusangulo"
    else:
        return False
    
tr1 = (int(input("Digite o primeiro angulo: ")))
tr2 = (int(input("Digite o segundo angulo: ")))
tr3 = (int(input("Digite o terceiro angulo: ")))

tipo = triangulo(tr1, tr2, tr3)
print("O triangulo é:", tipo)

