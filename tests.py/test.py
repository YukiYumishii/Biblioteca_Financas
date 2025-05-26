import sys
import os

# Caminho absoluto para a pasta pai de `biblioteca_finance`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from biblioteca_finance import juros, parcela, investimento, moeda

def menu():
    while True:
        print('\n\n', '='*50,'BIBLIOTECA FINANCEIRA', '='*50)
        print('\n 1 - Juros')
        print(' 2 - Parcelas')
        print(' 3 - Investimentos')
        print(' 4 - Converter Moedas')
        print(' 5 - Sair')

        opcao = input('\n Escolha uma opção:')
        
        match opcao:
            case '1':
             os.system('cls')
             print('\n\n', '='*50, 'JUROS', '='*50)
             print('\n 1 - Juros Simples')
             print(' 2 - Juros Compostos')
             print(' 3 - Voltar')

             opcao_juros = input('\n Escolha uma opção:')
             match opcao_juros:
                case '1':
                    capital_inicial = float(input('\nDigite o capital inicial: '))
                    taxa_juros = float(input('Digite a taxa de juros (em decimal): '))
                    tempo = float(input('Digite o tempo (em anos): '))
                    montante = juros.juros_simples(capital_inicial, taxa_juros, tempo)
                    print(f'\nMontante: {montante}')
                
                case '2':
                    capital_inicial = float(input('\nDigite o capital inicial:'))
                    taxa_juros = float(input('Digite a taxa de juros (em decimal): '))
                    tempo = float(input('Digite o tempo (em anos): '))
                    montante = juros.juros_compostos(capital_inicial, taxa_juros, tempo)
                    print(f'\nMontante: {montante}')
                
                case '3':
                    print('\nVoltando ao menu principal...')
                    continue
                case _:
                     print('\nOpção inválida. Tente novamente.')
                     continue
            
            case '2':
                os.system('cls')
                print('\n\n', '='*50, 'PARCELAS', '='*50)
                print('\n 1 - Calcular Preço da Parcela')
                print(' 2 - Voltar')
                opcao_parcela = input('\n Escolha uma opção:')
                match opcao_parcela:
                    case '1':
                        valor = float(input('\nDigite o valor total: '))
                        taxa_juros = float(input('Digite a taxa de juros (em decimal): '))
                        n_parcelas = int(input('Digite o número de parcelas: '))
                        valor_parcelas = parcela.parcela_price(valor, taxa_juros, n_parcelas)
                        print(f'\nPreço da Parcela: {valor_parcelas}')
                    
                    case '2':
                        print('\nVoltando ao menu principal...')
                        continue
                    case _:
                         print('\nOpção inválida. Tente novamente.')
                         continue
            
            case '3':
                os.system('cls')
                print('\n\n', '='*50, 'INVESTIMENTOS', '='*50)
                print('\n 1 - Retorno Percentual')
                print(' 2 - Retorno Mensal')
                print(' 3 - Retorno Anual')
                print(' 4 - Retorno Diário')
                print(' 5 - Voltar')
                opcao_investimento = input('\n Escolha uma opção:')

                match opcao_investimento:
                    case '1':
                        investimento_inicial = float(input('\nDigite o investimento inicial: '))
                        investimento_final = float(input('Digite o investimento final: '))
                        retorno = investimento.retorno_percentual(investimento_inicial, investimento_final)
                        print(f'\nRetorno Percentual: {retorno}%')
                    
                    case '2':
                        investimento_inicial = float(input('\nDigite o investimento inicial: '))
                        investimento_final = float(input('Digite o investimento final: '))
                        meses = int(input('Digite o número de meses: '))
                        retorno = investimento.retorno_mensal(investimento_inicial, investimento_final, meses)
                        print(f'\nRetorno Mensal: {retorno}')

                    case '3':
                        investimento_inicial = float(input('\nDigite o investimento inicial: '))
                        investimento_final = float(input('Digite o investimento final: '))
                        anos = int(input('Digite o número de anos: '))
                        retorno = investimento.retorno_anual(investimento_inicial, investimento_final, anos)
                        print(f'\nRetorno Anual: {retorno}')
                    
                    case '4':
                        investimento_inicial = float(input('\nDigite o investimento inicial: '))
                        investimento_final = float(input('Digite o investimento final: '))
                        dias = int(input('Digite o número de dias: '))
                        retorno = investimento.retorno_diario(investimento_inicial, investimento_final, dias)
                        print(f'\nRetorno Diário: {retorno}')

                    case '5':
                        print('\nVoltando ao menu principal...')
                        continue
                    case _:
                         print('\nOpção inválida. Tente novamente.')
                         continue
                
            case '4':
                os.system('cls')
                print('\n\n', '='*50, 'CONVERSOR DE MOEDAS', '='*50)
                print('\nCaso não saiba a sigla da sua moeda, você pode consultá-la em https://economia.awesomeapi.com.br/xml/available/uniq')
                moeda_origem = input('\nDigite a sigla da primeira moeda [Ex:USD]: ').upper()
                moeda_destino = input('\nDigite a sigla da segunda moeda [Ex:BRL]: ').upper()
                valor = float(input('\nDigite o valor que deseja converter: '))
                try:
                    resultado = moeda.converter_moeda(valor, moeda_origem, moeda_destino)
                    print(f'\n{valor} {moeda_origem} equivalem a {resultado} {moeda_destino}')
                except ValueError as e:
                    print(f'\nErro: {e}')
            
            case '5':
                print('\nEncerrando programa...\n')
                break
            
if __name__ == '__main__':
    menu()