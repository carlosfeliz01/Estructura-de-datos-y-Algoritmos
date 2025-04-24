# Este programa simula el lanzamiento de dos dados y determina si el jugador gana o pierde.
# Se considera que el jugador gana si la suma de los dos dados es 7 o 11.

import random
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

print("Primer dado:", dado1)
print("Segundo dado:", dado2)

suma = dado1 + dado2

if suma == 7:
    print("Ganaste! La suma es 7.") 
elif suma == 11:
    print("Ganaste! La suma es 11.")
else:
    print("Perdiste! La suma es:", suma)