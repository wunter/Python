# Esta función toma un diccionario con la distribución de frecuencia y plotea la ley de Zipf



def zipf_law (texto, scale = False, s = 0.5):

	'''
	Calcular la ley de Zipf.
	
	fi = t * (ki **-s) -->	frecuencia del elemento i es el resultado de t por el rango k del elemento i elevado a -s
	
	fi -> frecuencia del elemento i
	t  -> factor de normalización
	s  -> es un parámetro que controla la influencia del rank sobre la frecuencia 
	ki -> rango del elemento i
	
	Para calcular t
	
	t = (Sumatoria de N elementos kn**-s)**-1
	
	t = 1/sum([float(kn)**-s for kn in range(1,N+1)])
	
	N -> total de elementos
	
	

	scale = cambiar a False para desactivar / 'log' escala logaritmica


	'''
	# Distribución de frecuencia
	dist_frec = {}
	for w in texto:
		if w not in dist_frec:
			dist_frec[w] = 1
		else:
			dist_frec[w]+= 1
	
	
	# Distribución de Zipf del texto dado
	frecuencia = [i for i in dist_frec.values()]
	
	frecuencia.sort(reverse = True)
	
	datos_zipf = [(rank, frec for rank,frec in enumerate(frecuencia)]
	
	
	# Distribución de Zipf ideal
	
	t = 1/sum([float(kn)**-s for kn in range(1,len(texto)])
	
	zipf_ideal = [(k , t * (k**-s)) for k in range(1,len(texto)]

	
	# Plotear los datos obtenidos en una gráfica
	
	rank, frec = zip(*datos_zipf)
	r_ideal, f_ideal = zip(*zipf_ideal)
	
	
	pyplot.plot(rank, frec, 'r-', label = "Distribución del texto")

	pyplot.plot(r_ideal, f_ideal, "b-", label = "Distribución Ideal")
	
	if scale:
		pyplot.xscale(scale)
    pyplot.yscale(scale)
    		
  pyplot.title('Zipf plot')
  pyplot.xlabel('Rank')
  pyplot.ylabel('Frequency')
  pylab.legend(loc='upper left')
    	
  return pyplot.show()
		
	

        




