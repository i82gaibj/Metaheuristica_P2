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
        #print("Longuitud: ", len(padres))
        for i in range(0, len(padres), 2):
            #print("iteracion: ", i)
            corte = random.randint(1, len(padres[0])-1)
            #print("corte: ", corte)
            hijo1 = padres[i].copy()
            if(i+1 > len(padres[0])):
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
    else:
        generacion = padres
    #print("Generacion: ", generacion)
    
    #Mutar padres con probabilidad mProb
    if random.randint(1,100) <= (mProb*100):
        for i in range(len(generacion)):
            mutacion = random.randint(0, len(generacion[0])-1)
            #print("Mutacion: ", generacion[i][mutacion] == 0)
            if generacion[i][mutacion] == 0:
                generacion[i][mutacion] == 1
            else:
                generacion[i][mutacion] == 0


    return generacion #Devolver la nueva poblacion (sin evaluar)

def main():

    iterations = 10

    pesos = [ 34, 45, 14, 76, 32 ] #Para 5 objetos
    precios = [ 340, 210, 87, 533, 112 ] #Para 5 objetos
    pesoMax = 100 #Peso máximo que se puede poner en la mochila. Para 5 objetos
    
    #pesos = [ 34, 45, 14, 76, 32, 61, 37, 54, 23, 90, 26, 8, 17, 41, 28, 57, 68, 19, 48, 3 ] #Para 20 objetos
    #precios = [ 340, 210, 87, 533, 112, 427, 260, 356, 145, 637, 234, 72, 102, 358, 295, 384, 443, 123, 237, 27 ] #Para 20 objetos
    #pesoMax = 400 #Peso máximo que se puede poner en la mochila. Para 20 objetos
    
    nSolucionesInicial = 25 #Tamaño de la poblacion Default 25
    maxGeneraciones = 5 #Numero de generaciones Default 5
    k = 3 #Tamaño torneo selector de padres Default 3
    cProb = 0.0 #Probabilidad de cruce Default 0.7
    mProb = 0.0 #Probabilidad de mutacion Default 0.1
    results = []
    l=len(pesos)
    
    for c in range(0, 11, 1):
        iterationResults = []
        for m in range(0, 11, 1):
            cProb = float(c/10);
            mProb = float(m/10);  
            sumaAverage = 0
            
            for repeticiones in range(iterations):
                ##Creamos n soluciones aleatorias que sean válidas
                
                poblacion = []
                
                nSoluciones = nSolucionesInicial
                
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
                
                it=1
                while it < maxGeneraciones:
                    
                    nSoluciones = aplicarOperadoresGeneticos(poblacion,k,cProb,mProb)
                    #Modelo generacional
                    poblacion = []
                    for solucion in nSoluciones:
                        poblacion.append([solucion,evaluarSolucion(solucion,precios,pesos,pesoMax)])
                    
                    if it==4:
                        
                        generationAvg = 0
                        for i in range (len(poblacion)):
                            generationAvg += poblacion[i][1]
                        generationAvg /= (len(poblacion))
                        #print(generationAvg)
                        sumaAverage += generationAvg
                    
                    #print(repeticiones)

                    it+=1
            sumaAverage /= iterations
            #print("Hola: ", sumaAverage)
            
            iterationResults.append(sumaAverage)
            print(iterationResults)
        results.append(iterationResults)
    print(" ")
    print("El vector results guarda: ")
    for i in range(len(results)):
            print("Posicion ", i, " = ", results[i])
            

    #Export data to csv file
    with open("prueba.csv", "w") as file:
        file.write(",".join([" ", "0.0", "0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"]) + "\n")
        for i in range(11):
            data = [i]
            data = data + results[i]
            file.write(",".join([str(e) for e in data]) + "\n")

if __name__ == "__main__":
    main()
