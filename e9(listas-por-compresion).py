TEXTO=" BANANA hola"
print TEXTO.strip()

vec=[2,4,6]
hola =[3*x for x in vec]
print hola

print [3*x for x in hola if x > 7]
print [(x, x**3)for x in vec if x < 5]
print [str(round(355/113.0, i)) for i in range(1,10)]
