# Esta función toma un diccionario con la distribución de frecuencia y plotea la ley de Zipf


def zip_law (dist_frec, scale = 'log'):
	
	frecuencia = [i for i in dist_frec.values()]
	
	frecuencia.sort(reverse = True)
	
	rank_freq = [(rank, frec for rank,frec in enumerate(frecuencia)]
	
	rank, frec = zip(*frecuencia_rank)
	
	pyplot.clf()
	
	if scale:
		pyplot.xscale(scale)
    		pyplot.yscale(scale)
    		
    	pyplot.title('Zipf plot')
	pyplot.xlabel('rank')
    	pyplot.ylabel('frequency')
    	pyplot.plot(rs, fs, 'r-')
    	return pyplot.show()
		
	

        




