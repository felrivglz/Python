a=['gato', 'ventana', 'defenestrado']
for x in a:
  print x, len(x)

for x in a[:]:
    if len(x)>3:
        a.insert(0,x)
print a
