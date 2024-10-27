# Author:
#  Henrique Trivelato de Angelo

def negativeCheck(number):
    if(number[0] == '-'):
        return True
    return False


def segundaStringVazia(string):
    if(string == ""):
        return True
    return False


# -------------------------
def numberCheck(number):
    eh_negativo = negativeCheck(number)

    if(eh_negativo == True):
        number = number[1:]   # Retirando o sinal '-'
        # print(number)

    eh_numeric = number.isnumeric()

    if(eh_numeric == False):

        # Se for letra, retorna False (eh_numeric = False)
        if(number.isalpha() == True):
            return eh_numeric
        
        # Se não for numerico, quebra em 2 substrings a partir do char '.'
        substrings = number.split(".", 1)   # quebra a String no maximo 1 vez (1 quebra = substrings)
                                            #                                 (2 quebras = 3 substrings)

        sub1_eh_numeric = substrings[0].isnumeric()
        sub2_eh_numeric = substrings[1].isnumeric()

        # Se a 2a string for vazia, logo eh um numero decimal
        if(sub2_eh_numeric == False):
            sub2_eh_numeric = segundaStringVazia(substrings[1])

        # True -> É numero decimal
        # False -> Não é número
        return (sub1_eh_numeric and sub2_eh_numeric)
    # Fim if()

    # É numero (mas nao eh numero decimal)
    return eh_numeric


# -------------------------
def checkOperacao(operacao):

    if(operacao == "+"):
        return True
    
    if(operacao == "-"):
        return True
    
    if(operacao == "*"):
        return True
    
    if(operacao == "/"):
        return True
    
    if(operacao == "^"):
        return True
    
    return False


# -------------------------
def calculadora(elemento_1, elemento_2, sinal):
    val_1 = str(elemento_1)
    val_2 = str(elemento_2)
    operacao = str(sinal)

    if(numberCheck(val_1) == False):
        return None
    
    if(numberCheck(val_2) == False):
        return None
    
    if(checkOperacao(operacao) == False):
        return None
    
    # Operação e números válidos
    var1 = float(val_1)
    var2 = float(val_2)

    if(operacao == "+"):
        return var1 + var2
    
    if(operacao == "-"):
        return var1 - var2
    
    if(operacao == "*"):
        return var1 * var2
    
    if(operacao == "/"):

        if(var2 == 0):
            return None
        return var1 / var2
    
    if(operacao == "^"):
        return pow(var1,var2)
    

# -------- MAIN 
# elemento_1 = input()
# elemento_2 = input()
# operation = input()

# resultado = calculadora(elemento_1, elemento_2, operation)
# print(resultado)