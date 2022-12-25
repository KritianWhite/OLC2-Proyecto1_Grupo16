element = 0
while (element < 10):
    print(element)
    element = element + 1

transferencias = 0
while (transferencias < 100):
    if(transferencias == 5):
        transferencias = transferencias + 1
        continue
    if(transferencias == 9):
        break
    transferencias = transferencias + 1
    print(transferencias)

