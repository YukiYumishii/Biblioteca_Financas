def juros_simples(capital_inicial, taxa_juros, tempo):
    return capital_inicial * (1 + taxa_juros * tempo)

def juros_compostos(capital_inicial, taxa_juros, tempo):
    return capital_inicial * ((1 + taxa_juros) ** tempo)
