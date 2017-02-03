#this is a lista de frutas
canasta= ['Manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana']
#whit the  function set(), we can convert a list to a set
frutas =set(canasta)
print  "esto es un conjuto ", frutas #in the set don't repit the elements
print "esto es una lista de la cual se hizo el conjunto", canasta

#you can check if any element find in the set, this sentence return true or fal
print "si el elemento se encuentra mada:", 'naranja' in frutas

print 'tambien lo podemos observar en conjutos de caracteres osea palabras'

a=set('abracalabra')
b=set('alcanzam')
print 'conjunto a=',a
print 'conjunto b=',b

print 'a - b =', a - b  #letras de  a menos las de b
print 'a | b =', a | b  #letras en a o en b
print 'a & b =', a & b # letras en a y en b
print 'a ^ b =', a ^ b  #letras en a o en b pero no en ambas

 
