#1. pedir o numero de qual tabuada faremos 
numero = int(input('digite a tabuada que iremos fazer:')) 
  
#2. deve digitar da onde a tabuada devera comecar.
i = int(input('onde desejar comecar a tabuada:'))

#3. deve digitar da onde a tabuada devera encerrar.
termino = input('onde desejar encerrar a tabuada') 



while i <= 10:
    print(f' {i} x {numero} = {i* numero}')
    i +=1
