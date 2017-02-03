print range(2,10)
for n in range(2,10):
    print range(2,n)
    for x in range(2,n):
        print n,"%",x,"=",n%x
        pass #hola

        if n%x ==0:
            print n, 'es igual a', x, '*', n/x
            break
    else:
        print n, 'es un numero primo'
