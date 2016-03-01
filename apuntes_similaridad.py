'''For each word in each context, similar_words() calculates the sum of the product of the frequencies:

man ('a', 'who') 9 39  # 'a man who' occurs 39 times in text;
                       # 'a woman who' occurs 9 times
                       # Similarity score for the context is the product:
                       #     score['man'] = 9 * 39
girl ('a', 'who') 9 6
writer ('a', 'who') 9 4
boy ('a', 'who') 9 3
child ('a', 'who') 9 2
dealer ('a', 'who') 9 2
...
man ('a', 'and') 6 11  # score += 6 * 11
...
man ('a', 'he') 4 6    # score += 4 * 6
...
[49 more occurrences of 'man']

### 
1.Buscar los contextos de la palabra
2. Hacer un diccionario de frecuencia de contextos --> { contexto1: 5, contexto2: 1, ...}
3. Igual que 2 pero para todas las palabras del texto:
scores = {'de'{contexto1: 6, contexto2: 19,...},'mujer':{ contexto1: 5, contexto2: 1, ...}


diccionario[contexto] * scores'''


def get_context (texto, palabra, izq, der):
  texto.insert (0, "*START*")
	texto.append ("*END*")

	contextos = []

	for i in range(len(texto)):

		if re.match(palabra, texto[i]):

			if i < izquierda: # hay menos contexto izquierdo que palabras
				context_i = texto[:i]

			else:
				context_i = texto[i-izquierda:i]


			if len(texto) < (i+derecha):
				context_d = texto[i+1:]

			else: 
				context_d = texto[i+1:(i+derecha+1)]

			context = tuple(context_i + context_d)

			contextos.append(context)
			
	return tuple(contextos)
	
contextos = {}

	
for palabra in set(texto):
  
  contextos[palabra] = concordancia(palabra)

scores = defaultdict(int)

for key in contextos:
  for contexto in contextos[key]:
    if contexto in contextos_palabra:
      scores[key] += 1

sort.scores()[:10]

print numero de contextos en los que aparece la palabra (len contextos)
print numero de contextos en los que aparece la otra palabra (similar) len(contextos_palabrasimilar)
print numero de contextos que comparten ambos score[palabra_similar]

  
  


