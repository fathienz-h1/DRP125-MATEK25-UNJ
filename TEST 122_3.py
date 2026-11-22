n = int(input('Banyak data= '))
b = int(input('Banyak baris= '))
for i in range (1,n+1):
    print(i, end='\t')
    if i%b==0:
        print()
    
