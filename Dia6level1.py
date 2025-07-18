#Dia 6, crea un tuple
#==//Paso 1 
#Crea un tuple vacio 
tuple_vacia= ()
#crea una con nombres de hermanos y hermanas (imaginarios esta bien)
tuple_vacia= ("Juanita" , "Frida ")
tuple_vacia1= ("Juan" , "Pepe")
tuplellena= (tuple_vacia+tuple_vacia1)
cantidad= len(tuplellena)
print ("Tengo:", cantidad, "De hermanos")
papas= ("Laura" , "Honorio")
miembros_de_la_familia= papas+tuplellena
print (miembros_de_la_familia)