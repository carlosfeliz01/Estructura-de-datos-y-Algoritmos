def suma(a,b):
    resutado =a+b
    return resutado
def resta(a,b):
    resultado = a-b
    return resultado
def multiplicar(a,b):
    resultado = a*b
    return resultado    
def dividir(a,b):
    resultado = a/b
    return resultado
def potencia(a,b):
    resultado = a**b
    return resultado
def raiz(a,b):
    resultado = a**(1/b)
    return resultado
def factorial(a):
    resultado = 1
    for i in range(1,a+1):
        resultado *= i
    return resultado
def modulo(a,b):
    resultado = a%b
    return resultado
def promedio(a,b):
    resultado = (a+b)/2
    return resultado
def mayor_o_meno(a,b):
    if a>b:
        return a
    else:
        return b


print("Suma: ",suma(5,6))
print("Resta: ",resta(5,6))
print("Multiplicar: ",multiplicar(5,6))
print("Dividir: ",dividir(5,6))
print("Potencia: ",potencia(5,6))
print("Raiz: ",raiz(5,6))
print("Factorial: ",factorial(5))
print("Modulo: ",modulo(5,6))
print("Promedio: ",promedio(5,6))
print("Mayor o menor: ",mayor_o_meno(5,6))