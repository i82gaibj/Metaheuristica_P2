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
    padres = []
    mejor = [0,0]

    for i in range(0, len(poblacion)-1):
        for j in range(0, k):
            randomN = random.randint(0,len(poblacion)-1)
            padre = poblacion[randomN]   
            if(padre[1] > mejor[1]):
                mejor = padre;
            print("hola")
        padres.append(mejor);
        #print("Padre mejor", mejor)
        
    #Cruzar padres con probabilidad cProb
    if random.randint(1,100) <= cProb:
        # vas a cruzar padres[i] con padres[i+1] y luego i+2
        # para cruzar partes los dos padre[0] por un bit aleatorio y intercambias sus partes 

    #Mutar padres con probabilidad mProb
    #if random.randint(1,100) <= mProb:


    return poblacion #Devolver la nueva poblacion (sin evaluar)

def main():
    pesos = [ 34, 45, 14, 76, 32, 61, 37, 54, 23, 90 ]
    precios = [ 340, 210, 87, 533, 112, 427, 260, 356, 145, 637 ]
    pesoMax = 100 #Peso máximo que se puede poner en la mochila
    nSoluciones = 25 #Tamaño de la poblacion
    maxGeneraciones = 10 #Numero de generaciones
    k = 3 #Tamaño torneo selector de padres
    cProb = 0.7 #Probabilidad de cruce
    mProb = 0.1 #Probabilidad de mutacion

    l=len(pesos)
    ##Creamos n soluciones aleatorias que sean válidas
    poblacion = []
    for i in range(nSoluciones):
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

if __name__ == "__main__":
    main()
