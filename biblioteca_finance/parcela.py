def parcela_price(valor, taxa_juros, n_parcelas):
    if taxa_juros == 0:
        return valor / n_parcelas
    else:
        taxa = taxa_juros / 100
        return round(valor * (taxa * (1 + taxa) ** n_parcelas) / ((1 + taxa) ** n_parcelas - 1), 2)