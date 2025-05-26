def retorno_percentual(investimento_inicial, investimento_final):
    if investimento_inicial <= 0:
        return 'O investimento inicial deve ser maior que zero.'
    else:
        return ((investimento_final - investimento_inicial) / investimento_inicial) * 100

def retorno_mensal(investimento_inicial, investimento_final, meses):
    if meses <= 0 or investimento_inicial <= 0:
        return 'O número de meses deve ser maior que zero e o investimento inicial deve ser maior que zero.'
    else:
        return (investimento_final / investimento_inicial) / meses

def retorno_anual(investimento_inicial, investimento_final, anos):
    if anos <= 0 or investimento_inicial <= 0:
        return 'O número de anos deve ser maior que zero e o investimento inicial deve ser maior que zero.'
    else:
        return (investimento_final / investimento_inicial) / anos

def retorno_diario(investimento_inicial, investimento_final, dias):
    if dias <= 0 or investimento_inicial <= 0:
       return 'O número de dias deve ser maior que zero e o investimento inicial deve ser maior que zero.'
    else:
        return (investimento_final / investimento_inicial) / dias
