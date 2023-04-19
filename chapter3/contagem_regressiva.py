#loop infinito
def regressiva(i):
    print(i)
    regressiva(i-1)

def regressiva2(i):
    if i <= 1:
        return
    else:
        regressiva2(i-1)

regressiva2(5)
