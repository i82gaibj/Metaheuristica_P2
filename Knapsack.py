import random
import time

def evaluarSolucion(solucion, precios, pesos, pesoMax):
    precio = 0
    peso = 0
    for i in range(len(solucion)):
        precio += precios[i]*solucion[i]
        peso += pesos[i]*solucion[i]

    if peso > pesoMax:
        
        return 0
   
    else:
        return precio

def mutacion1bit(generacion):
    for i in range(len(generacion)):
            mutacion = random.randint(0, len(generacion[0])-1)
            #print("Mutacion: ", generacion[i][mutacion] == 0)
            if generacion[i][mutacion] == 0:
                generacion[i][mutacion] = 1
            else:
                generacion[i][mutacion] = 0
    return generacion

def mutacionRotacion(generacion):
    for i in range(len(generacion)):
            bit = random.randint(0, len(generacion[0])-1)
            bitDestino = random.randint(0, len(generacion[0])-1)
            generacion[i][bitDestino] = generacion[i][bit]

def cruce1corte(padres):
    generacion = []
    
    for i in range(0, len(padres), 2):
        #print("iteracion: ", i)
        corte = random.randint(1, len(padres[0])-1)
        #print("corte: ", corte)
        hijo1 = padres[i].copy()
        if(i+1 > len(padres)):
            hijo2 = padres[0].copy()
        else:
            hijo2 = padres[i+1].copy()
        #print("1-hijo: ", hijo1)
        for j in range(corte, len(padres[0])):
            #print(j)
            #print(j, " 2-hijo: ", hijo1[j])
            auxNodo = hijo1[j] 
            hijo1[j] = hijo2[j]
            hijo2[j] = auxNodo 
            
        generacion.append(hijo1)
        if(i+1 < len(padres)):
            generacion.append(hijo2)
    return generacion

def aplicarOperadoresGeneticos(poblacion, k, cProb, mProb):


    #Seleccionar padres mediante torneo tamaño k
    padres = []
    generacion = []
    
    for i in range(len(poblacion)):
        mejor = [0,0]
        for j in range(0, k):
            randomN = random.randint(0, len(poblacion)-1)
            padre = poblacion[randomN]

            if(padre[1] >= mejor[1]):
                mejor = padre;
                
        padres.append(mejor[0]);
        #print("iteracion: ", i , "Padre mejor", mejor[0])
    
    #Cruzar padres con probabilidad cProb
    if random.randint(1,100) <= (cProb*100):
        generacion = cruce1corte(padres)  
    else:
        generacion = padres
    
    #Mutar padres con probabilidad mProb
    if random.randint(1,100) <= (mProb*100):
        generacion = mutacion1bit(generacion)
            

    return generacion #Devolver la nueva poblacion (sin evaluar)

def main():

    iterations = 100

    #pesos = [ 34, 45, 14, 76, 32 ] #Para 5 objetos
    #precios = [ 340, 210, 87, 533, 112 ] #Para 5 objetos
    #pesoMax = 100 #Peso máximo que se puede poner en la mochila. Para 5 objetos
    
    #pesos = [ 34, 45, 14, 76, 32, 61, 37, 54, 23, 90, 26, 8 ] #Para 12 objetos
    #precios = [ 340, 210, 87, 533, 112, 427, 260, 356, 145, 637, 234, 72 ] #Para 12 objetos
    #pesoMax = 300 #Peso máximo que se puede poner en la mochila. Para 12 objetos
    
    #pesos = [ 34, 45, 14, 76, 32, 61, 37, 54, 23, 90, 26, 8, 17, 41, 28, 57, 68, 19 ] #Para 18 objetos
    #precios = [ 340, 210, 87, 533, 112, 427, 260, 356, 145, 637, 234, 72, 102, 358, 295, 384, 443, 123 ] #Para 18 objetos
    #pesoMax = 400 #Peso máximo que se puede poner en la mochila. Para 18 objetos
    
    pesos = [ 34, 45, 14, 76, 32, 61, 37, 54, 23, 90, 26, 8, 17, 41, 28, 57, 68, 19, 48, 3, 11, 87, 83, 21 ] #Para 24 objetos
    precios = [ 340, 210, 87, 533, 112, 427, 260, 356, 145, 637, 234, 72, 102, 358, 295, 384, 443, 123, 237, 27, 65, 602, 578, 137 ] #Para 24 objetos
    pesoMax = 500 #Peso máximo que se puede poner en la mochila. Para 24 objetos
    
    nSolucionesInicial = 100 #Tamaño de la poblacion Default 25
    maxGeneraciones = 5000 #Numero de generaciones Default 5000
    k = 9 #Tamaño torneo selector de padres Default 3
    cProb = 0.9 #Probabilidad de cruce Default 0.7 -> 0.9(Mejor)
    mProb = 0.1 #Probabilidad de mutacion Default 0.2
    results = []
    
    l=len(pesos)

    time_average = 0
    for i in range(maxGeneraciones):
        results.append([0,0])
    
    for repeticiones in range(iterations):
        ##Creamos n soluciones aleatorias que sean válidas
        poblacion = []
        iterationResults = []
        nSoluciones = nSolucionesInicial
        start = time.time()
        
        #----------------- Soluciones Iniciales No Validas ----------------
        
        #for i in range(nSoluciones):
        #    objetos = list(range(l))
        #    solucion = []
        #    peso = 0
        #    while peso < pesoMax:
        #        objeto = objetos[random.randint(0, len(objetos) - 1)]
        #        peso += pesos[objeto]
        #        solucion.append(objeto)
        #        objetos.remove(objeto)
        # 
        #    s = []
        #    for i in range(l):
        #        s.append(0)
        #    for i in solucion:
        #        s[i] = 1
        #    poblacion.append([s, evaluarSolucion(s, precios, pesos, pesoMax)])
        
        #-------------- Soluciones Iniciales Validas -------------------
        for j in range(nSoluciones):
            objetos = list(range(l))
            solucion = []
            peso = 0
            while peso < pesoMax:
                objeto = objetos[random.randint(0, len(objetos) - 1)]
                peso += pesos[objeto]
                if peso <= pesoMax:
                    solucion.append(objeto)
                    objetos.remove(objeto)
        
            s = []
            for i in range(l):
                s.append(0)
            for i in solucion:
                s[i] = 1
            poblacion.append([s,evaluarSolucion(s,precios,pesos,pesoMax)])
        
        generationAvg = 0
        generationBest = 0
            
        for i in range (len(poblacion)):
            generationAvg += poblacion[i][1]
            if (poblacion[i][1] > generationBest):
                generationBest = poblacion[i][1]
                #elite = poblacion[i]
        generationAvg /= (len(poblacion))
            
        iterationResults.append([generationAvg, generationBest])
            
        #print("Fitness medio de la generacion: ", 0, " = ", generationAvg)
        #print("Fitness mejor de la generacion: ", 0, " = ", generationBest)
        
        it=1
        while it < maxGeneraciones:
            
            nSoluciones = aplicarOperadoresGeneticos(poblacion,k,cProb,mProb)
            #Modelo generacional
            poblacion = []
            for solucion in nSoluciones:
                poblacion.append([solucion,evaluarSolucion(solucion,precios,pesos,pesoMax)])
            
            #---------------------- Elitismo ---------------------
            #Buscamos el peor individuo
            #peorValor = poblacion[0][1]
            #indice_peor_individuo = 0
            #for i in range(len(poblacion)-1):
            #    if peorValor > poblacion[i][1]:
            #        peorValor = poblacion[i][1]
            #        indice_peor_individuo = i
    
            #Sustituyo el peor individuo por el individuo elite
            #poblacion[indice_peor_individuo] = elite
            #-----------------------------------------------------
            
            generationAvg = 0
            generationBest = 0
            
            for i in range (len(poblacion)):
                generationAvg += poblacion[i][1]
                if (poblacion[i][1] > generationBest):
                    generationBest = poblacion[i][1]
                #if poblacion[i][1] > elite[1]:  #Elitismo
                    #elite = poblacion[i]        #Elitismo
            generationAvg /= (len(poblacion))
            
            iterationResults.append([generationAvg, generationBest])
            
            print(repeticiones)
            #print("generacion: ", it, " = ", generationAvg)
            #print("Fitness mejor de la generacion: ", it, " = ", generationBest)
            it+=1
        
        end = time.time()
        
        for i in range(len(iterationResults)):
            results[i][0] += iterationResults[i][0]
            if (iterationResults[i][1] > results[i][1]):
                results[i][1] = iterationResults[i][1]
 
        time_average += (end - start)
        
    time_average /= iterations

    print("Tiempo medio:", time_average*1000000)
    
    print(" ")
    print("El vector results guarda: ")
    for i in range(len(results)):
            results[i][0] /= iterations
            print("Posicion ", i, " = ", results[i])
            
    

    #Export data to csv file
    with open("Dataset24_SinElitismo.csv", "w") as file:
        file.write(",".join(["Generation", "Fitness Avg", "Fitness Best", "Execution Time"]) + "\n")
        for i in range(len(results)):
            data = [i+1]
            data = data + results[i]
            data += [time_average*1000000]
            file.write(",".join([str(e) for e in data]) + "\n")

if __name__ == "__main__":
    main()
