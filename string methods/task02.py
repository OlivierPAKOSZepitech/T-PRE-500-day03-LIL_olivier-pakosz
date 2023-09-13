string = " hello world "
position = string . find ( " a " )
print ( position )

# L'ordinateur part de la fin pour trouver les indices. Il ne l'a pas trouvé en revenant jusqu'à l'indice 0. 
# -1 signifie donc que le string ne possède pas de "a"