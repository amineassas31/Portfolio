import operator

with open("donnee_Notation_polonaise", "r") as fichier:
    operation = fichier.readline()
operation = operation.split(" ")
operateur_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}


def calcul(operation_polonaise):
    for i in range(0, len(operation_polonaise)):
        if operation_polonaise[i] in operateur_dict.keys():
            if operation_polonaise[i + 1] is not None and operation_polonaise[i + 2] is not None:
                if operation_polonaise[i + 1].lstrip("-").isnumeric() and operation_polonaise[i + 2].lstrip(
                        "-").isnumeric():
                    s = operateur_dict[operation_polonaise[i]](int(operation_polonaise[i + 1]),
                                                               int(operation_polonaise[i + 2]))
                    operation_polonaise[i] = str(s)
                    operation_polonaise[i + 1] = None
                    operation_polonaise[i + 2] = None
    while None in operation:
        operation.remove(None)


while "+" in operation or "-" in operation or "*" in operation or "/" in operation:
    calcul(operation)
print(operation[0])
