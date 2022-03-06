import random

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

    mejor = [0,0]
    cProb = cProb * 100

    for i in range(len(poblacion)):
        padres = []

        for j in range(k):
            randomN = poblacion[random.randint(0,len(poblacion)-1)]
            padre = poblacion[randomN]
            if(padre[1] > mejor[1]):
                mejor = padre;
            print("hola")
        padres.append(mejor);
        #print("Padre mejor", mejor)

        mejor_valor = padres[0][1]
        mejor_site = padres[0][0]

        for j in range(k):
            if mejor_valor < padres[i][1]:
                mejor_valor = padres[i][1]
                mejor_site = padres[i][0]

        mejor.append(mejor_site)


    #cruzar padres con probabilidad cprob:

    size = []
    generacion_i = []


    for z in range (0 , len(mejor), 2):
        padre_1 = mejor[z].copy()
        if z+1 == len(mejor):
            generacion_i.append(padre_1)
            break

        padre_2 = mejor[z + 1].copy()
        if random.randint(1, 100) <=cProb:
            cruce = random.randint(0, size-1)

            for x in range(cruce, size-1):
                aux_padre = padre_1[x]
                padre_1[x] = padre_2[x]
                padre_2[x] = aux_padre

        generacion_i.append(padre_1)
        generacion_i.append(padre_2)


        # vas a cruzar padres[i] con padres[i+1] y luego i+2
        # para cruzar partes los dos padre[0] por un bit aleatorio y intercambias sus partes 

    #Mutar padres con probabilidad mProb
    #if random.randint(1,100) <= mProb:

    for y in range (len(generacion_i)):

        if random.randint(1,100) <= (mProb*100):
            mutacion = random.randint(0, size-1)
            generacion_i[y][mutacion] = 0 if generacion_i[y][mutacion] == 1 else 1


    return generacion_i #Devolver la nueva poblacion (sin evaluar)

def main():

    iterations = 1000

    pesos = [ 34, 45, 14, 76, 32 ] #Para 5 objetos
    precios = [ 340, 210, 87, 533, 112 ] #Para 5 objetos
    pesoMax = 100 #Peso máximo que se puede poner en la mochila. Para 5 objetos
    
    #pesos = [ 34, 45, 14, 76, 32, 61, 37, 54, 23, 90, 26, 8, 17, 41, 28, 57, 68, 19, 48, 3 ] #Para 20 objetos
    #precios = [ 340, 210, 87, 533, 112, 427, 260, 356, 145, 637, 234, 72, 102, 358, 295, 384, 443, 123, 237, 27 ] #Para 20 objetos
    #pesoMax = 400 #Peso máximo que se puede poner en la mochila. Para 20 objetos
    
    nSoluciones = 25 #Tamaño de la poblacion
    maxGeneraciones = 10 #Numero de generaciones
    k = 3 #Tamaño torneo selector de padres
    cProb = 0.7 #Probabilidad de cruce
    mProb = 0.1 #Probabilidad de mutacion
    results = []



    l=len(pesos)

    time_average = 0

    ##Creamos n soluciones aleatorias que sean válidas
    poblacion = []



    for i in range(iterations):

        aux_nsoluciones = nSoluciones

        print("\n------------------" + str(rep) + "------------------")


        for j in range(aux_nsoluciones):
            s = []

            for i in range (l):
                s.append(random.randint(0, 1))

            poblacion.append([s, evaluarSolucion(s, precios, pesos, pesoMax)])

        generation_average, generation_best = 0,0

        for i in range(len(poblacion)):
            generation_average += poblacion[i][1]
            if (poblacion[i][1] > generation_best):
                generation_best = poblacion[i][1]

        generation_average /= (len(poblacion))

        #que coño es esto XD






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
            poblacion.append([solucion[0],evaluarSolucion(solucion[0],precios,pesos,pesoMax)])
        it+=1




    #Export data to csv file
    with open("results.csv", "w") as file:
        file.write(",".join(["Generation", "Fitness Avg", "Fitness Best", "Execution Time"]) + "\n")
        for i in range(len(results)):
            data = [i]
            data = data + results[i]
            if (i == 0):
                data += [time_average]
            file.write(",".join([str(e) for e in data]) + "\n")

if __name__ == "__main__":
    main()
