#pip install sqlalchemy pymysql - instalando banco de dados sqlalchemy
from sqlalchemy import create_engine
import pandas as pd 

host = 'localhost'
user = 'root'
password = ''
database = 'bd_aula06'

engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}/{database}'
)

# Criar as planilhas com Data Frame (df)
try:
    df_clientes = pd.read_sql('tb_clientes', engine)
    df_itens = pd.read_sql('tb_itens', engine)
    df_pedidos = pd.read_sql('tb_pedidos', engine)
    df_produtos = pd.read_sql('tb_produtos', engine)

    
except Exception as e:
     print(f'Falha na conexão {e}')

# Unindo as planilhas em uma só 
     
try:
    df_merge1 = pd.merge(df_clientes, df_pedidos, on='codigo_cliente')
    df_merge2 = pd.merge(df_merge1, df_itens, on='codigo_pedido')
    df_final = pd.merge(df_merge2, df_produtos, on='codigo_produto')
# Criando filtro para a Cidade de Sâo Paulo
    filtro = (
        (df_final['cidade'] == 'Sao Paulo') 
    )
    #Pega apenas a Cidade de São Paulo
    df_sp = df_final[filtro]
    print(
        df_sp[[
            'nome', 'sobrenome',
            'cidade', 'codigo_pedido',
            'data_pedido', 'produto', 'valor'
        ]]
    )

except Exception as e:
    print(f'Erro tratamento dos dados {e}')