negativos = 0
positivos = 0
zeros = 0

for i in range(12):
    n = float(input(f"Digite qualquer número, {i+1}ª número: "))
    
    if n > 0:
        positivos += 1
    
    elif n < 0:
        negativos += 1
        
    else:
        zeros += 1
   
print(f"Quantidade de positivos: {positivos}.")
print(f"Quantidade de negativos: {negativos}.")
print(f"Quantidade de zeros: {zeros}.")
