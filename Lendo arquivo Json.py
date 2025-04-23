#Simulando erro obs: se tiver encoding utf-8 padrao o pandas ler sem prescisar passar parametro encoding
import pandas as pd

#pd.set_option('display.max_columns', None)# ver todas as colunas  
caminho_do_arquivo = r"C:\Users\Matheus Neves\Documents\arquivojasonANAC"
df = pd.read_json(caminho_do_arquivo) 
df.head()

#%%
import pandas as pd
caminho_do_arquivo = r"C:\Users\edmil\OneDrive\Documentos\Cursos\Python - SGBDS - Arquivos\Origem de dados\V_OCORRENCIA_AMPLA.json"
df = pd.read_json(caminho_do_arquivo, encoding='utf-8-sig')
df.head()
# %%
