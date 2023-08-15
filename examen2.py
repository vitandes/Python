def snail(n,m):

    if(n ==0 or m==0):
         return ""
    
    startRows= 0
    finalRows = n -1
    startColumns = 0
    finalColumns = m -1
    matriz = [[0 for _ in range (m)] for _ in range(n)]
    abc = "abcdefghijklmnopqrstuvwxyz"
    cont = 0
    a = ""
    
    while(startRows <= finalRows and startColumns <= finalColumns):
        
        if(startRows == finalRows):
            for i in range(startColumns, finalColumns +1):
                matriz[startRows][i] = abc[cont]
                cont += 1
                if cont >= len(abc):
                    cont = 0
            startRows += 1
        elif(startColumns == finalColumns):
            for i in range(startRows, finalRows + 1):
                matriz[i][finalColumns] = abc[cont]
                cont += 1 
                if cont >= len(abc):
                    cont = 0

            finalColumns += -1           
        else:
            for i in range(startColumns, finalColumns +1):
                matriz[startRows][i] = abc[cont]
                cont += 1 
                if cont >= len(abc):
                    cont = 0 
            startRows += 1
            

            for i in range(startRows, finalRows + 1):
                matriz[i][finalColumns] = abc[cont]
                cont += 1 
                if cont >= len(abc):
                    cont = 0

            finalColumns += -1
            

            for i in range(finalColumns, startColumns - 1, -1):
                matriz[finalRows][i] = abc[cont]
                cont += 1 
                if cont >= len(abc):
                    cont = 0

            finalRows += -1
            

            for i in range(finalRows, startRows -1, -1):
                matriz[i][startColumns] = abc[cont]
                cont += 1 
                if cont >= len(abc):
                    cont = 0

            startColumns += 1
            
    for i in range(0, n):
             print(matriz[i])
    
    
    for i in range(0, n):
             a= a + "".join(matriz[i])       
            
    return a
    
print(snail(10,8))