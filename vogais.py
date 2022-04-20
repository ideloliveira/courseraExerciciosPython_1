def vogal(letra):
    
    vogal = False
    if (letra.upper()== 'A' or
        letra.upper() == 'E' or
        letra.upper() == 'I' or
        letra.upper() == 'O' or
        letra.upper() == 'U'):
        vogal = True
    else:
        vogal = False

    return vogal
