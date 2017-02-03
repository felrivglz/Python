
def fib(n):
    a, b =0, 1
    while b < n:
        print b,
        a, b =b, a+b

def pedir_confirmacion(prompt, reintentos=4, queja='Si o no, por favor!'):
     while True:
        ok = raw_input(prompt)
        if ok in ('s', 'S', 'si', 'Si', 'SI'):
             return True
        if ok in ('n', 'no', 'No', 'NO'):
            return False
        reintentos = reintentos - 1
        if reintentos < 0:
            raise IOError('usuario duro')
        print queja

fib(2000)
pedir_confirmacion("hoal que ahces")
