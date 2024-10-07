
#abrimos nuestro archivo

file=open("my_notes.txt","r")
print(file)
#verificamos si se puede abrir


#leemos linea por linea utilizamos readlines
linea_por_linea1= file.readlines(1)
linea_por_linea2=file.readlines(2)
linea_por_linea3=file.readlines(3)

#ejecutamos el codigo

print(linea_por_linea1)
print(linea_por_linea2)
print(linea_por_linea3)


file.close()  # cerramos el archivo
