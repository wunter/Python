
""" 
"Fizz buzz" 

Escribe una funcion que reciba un numero entero y deverá devolver:
- "Fizz Buzz" si el número es divisible por 3 y por 5;
- "Fizz" si el número es divisible por 3;
- "Buzz" si el número es divisible por 5; 

Entrada: Un número como un entero.

Salida: La respuesta como una cadena de caracteres.
"""

def fizz_buzz (number):
  
  answer = number
  
  if number % 3 == 0 and number % 5 == 0:
      answer = "Fizz Buzz"
      
  elif number % 3 == 0:
      answer = "Fizz"
      
  elif number % 5 == 0:
      answer = "Buzz"
        
  return answer
