For each word in each context, similar_words() calculates the sum of the product of the frequencies:

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


diccionario[contexto] * scores



