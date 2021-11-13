import os
from os import device_encoding
from numpy import DataSource, e
import pandas as pd


#comandos df.head(4), df.tail(4), df.shape, df.describe, df.columns, df.dtypes, df.loc
path = r"C:\Projeto Análise de dados"
diretorio = os.listdir(path)
for file in diretorio:
    if file == "Novo.csv":
        os.remove(file)


df = pd.read_csv(f"{path}/CAD_IES.csv", encoding= 'ISO-8859-1', sep=";", error_bad_lines=False, skiprows=10)

lista = []  

#n = str()

    


def Escolha(msg):
    while True:
        try:
            n = str(input(msg))
        
        except (ValueError, TypeError, IndexError):
            print('\nFaça uma escolha correta!\n'.upper())
            continue

        if n == '1':
           n = 'Centro Oeste'
           break
        elif n == '2':
           n = 'Nordeste'
           break
        elif n == '3':
           n = 'Norte'
           break
        elif n == '4':
           n = 'Sudeste'
           break
        elif n == '5':
           n = 'Sul'
           break
        else:
            print('\nFaça uma escolha correta!\n'.upper())


    print(f'\nVocê escolheu: {str(n)}\n')

    return n



def Regiao(cidade):
    while True:
        try:
            cid = str(input(cidade)).upper().strip()
        except (ValueError, TypeError, IndexError):
            print('\nFaça uma escolha correta!\n'.upper())
            continue
        if cid in '':
            print('\nFaça uma escolha correta!\n'.upper())
        else:
            break

    mnp = []
    city= {}
    downtown = []
    mnp.clear()
    city.clear()
    mnp.append(df.loc[df['MUNICIPIOIES'] == str(cid)])
    
    for k, v in enumerate(mnp):
        try:
            for dados in v['NO_IES']:
                k +=1 
                city[f'INSTITUIÇÃO {str(k)}'] = str(dados).upper()
            k = 0
            for f in v['DS_ENDERECO']:
                k +=1    
                city[f'END {str(k)}'] = str(f).upper()
            k = 0 
            for g in v['NU_TELEFONE']:
                k +=1    
                city[f'CONTATO {str(k)}'] = str(g).upper()
            k = 0 
            for h in v['TX_EMAIL']:
                k +=1    
                city[f'EMAIL {str(k)}'] = str(h).upper()
            k = 0 
            downtown.append(city.copy())    
        except:
            print('\nESTA CIDADE/MUNICÍPIO NÃO PERTENCE A ESTA REGIÃO!')
            break 
    print() 
    print(f'{"instituição:":>15}{"endereço:":>40}{"contato:":>20}{"e-mail:":>20}\n'.title())
    try: 
        for i, e in enumerate(city):
            i += 1
            print(city[f'INSTITUIÇÃO {str(i)}'][:28], end='')
            print(" --", city[f'END {str(i)}'], end='')
            print(" --", city[f'CONTATO {str(i)}'], end='')
            print(" --", city[f'EMAIL {str(i)}'], end='')
            print('\n')
    except KeyError:
        pass   

    NovoDF = pd.DataFrame(downtown)               
    NovoDF.to_csv(f'{path}/Novo.csv', index=False)


    return cidade



print('Bem vindo a Análise de Dados das Instituições de Ensino Superior - Censo 2011\n')

regiao = Escolha("\n1 - Centro Oeste\n" 
                        "2 - Nordeste\n"
                        "3 - Norte\n"
                        "4 - Sudeste\n" 
                        "5 - Sul\n"
                        "\nQual região você quer pesquisar?: ")
  

municipio = Regiao('Qual é seu município regional?: ')
                    
