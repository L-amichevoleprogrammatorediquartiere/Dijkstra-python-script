collegamenti_peso= None
nodo_peso_success= []

def calcolaPercorso(a):
    global collegamenti_peso
    global nodo_peso_success
    nodi = []
    for i in collegamenti_peso:
        if(i[0] not in nodi):
            nodi.append(i[0])

        if(i[1] not in nodi):
            nodi.append(i[1])
            
    #nodo - costo - nexthop
    for i in nodi:
        nodo_peso_success.append([i,-1,-1])
        
    #primo passo porre costo per i nodi adiacenti
    #e porre i successori uguali al nodo che abbiamo scelto
    assegnaCostoSucc(a,0,a)
    nodi_vicini=adiacenzaNodi(a)
    for i in nodi_vicini:
        assegnaCostoSucc(i,calcolaPeso(a,i),a)

    nodi_visti=[a]
    for i in range(len(nodi)-1):
        #non bisogna assegnare il primo tra i vicini ma quello con 
        #il costo minimo tra quelli vicini non visti
        #qui troviamo un costo su cui basarci
        for nodi in nodi_vicini:
            if(nodi not in nodi_visti):
                if(calcolaCostoFinal(nodi)!=-1):
                    costo_min= calcolaCostoFinal(nodi)
        #qui troviamo il costo minimo
        for nodi in nodi_vicini:
            if(nodi not in nodi_visti):
                if(calcolaCostoFinal(nodi)!=-1 and calcolaCostoFinal(nodi)<costo_min):
                    costo_min= calcolaCostoFinal(nodi)
        #qui scdgliamo il nodo
        for nodi in nodi_vicini:
            if(nodi not in nodi_visti):
                if(calcolaCostoFinal(nodi)== costo_min):
                    nodo_scelto=nodi
                    break            

        nodi_vicini=adiacenzaNodi(nodo_scelto)
        for nodi in nodi_vicini:
            assegnaCostoSucc(nodi,calcolaPeso(nodi,nodo_scelto)+
                             calcolaCostoFinal(nodo_scelto),nodo_scelto)
        nodi_visti.append(nodo_scelto)
        
def assegnaCostoSucc(n,c,s):
    global nodo_peso_success
    for i in nodo_peso_success:
        if (i[0] == n):
            if(i[1]>c or i[1] == -1):
                i[1]=c
                i[2]=s
            break

def calcolaCostoFinal(a):
    global nodo_peso_success
    for i in nodo_peso_success:
        if(i[0]==a):
            return i[1]

def calcolaPeso(a,b):
    global collegamenti_peso
    for i in collegamenti_peso:
        if((i[0] == a and i[1] == b) or (i[0] == b and i[1] == a)):
            return i[2]

def adiacenzaNodi(a):
    nodi_vicini= []
    global collegamenti_peso
    for i in collegamenti_peso:
        if(i[0]== a):
            nodi_vicini.append(i[1])
        elif(i[1]==a):
            nodi_vicini.append(i[0])
    return nodi_vicini

def stampaRisultati():
    global nodo_peso_success
    print("nodo\tcosto\tsuccessivo")
    for nodo in nodo_peso_success:
        print(nodo[0],"\t",nodo[1],"\t",nodo[2])

def calculate(array_collegamenti, nodo):
    global collegamenti_peso
    global nodo_peso_success
    nodo_peso_success=[]
    collegamenti_peso=array_collegamenti
    calcolaPercorso(nodo)
    stampaRisultati()