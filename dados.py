from databricks import sql
import pandas as pd
import datetime
from datetime import datetime
from datetime import timedelta
import locale
import string
from unidecode import unidecode


class BaseDados_tratamentos:
    
    def token():
        with open(r"C:\Users\ezequ\OneDrive\Documentos\não_excluir_token.txt",'r') as t:
            meu_token = t.read()
        print(meu_token)
        return meu_token
    
    def tratar_texto_pxr(x):
        lista = x.split('_')
        return lista[0]
    
    def tratar_texto_pxr_numerico(x):
        lista_numerica = x.split('.')
        return lista_numerica[1]
    
    def tratar_texto_num(x):
        lista = x.split('_')
        return lista[1]
    
    def tratar_texto_resto(x):
        lista = x.split('_')
        return lista[2]

    def __init__(self) :
        self.DATABRICKS_SERVER_HOSTNAME="adb-5979074469666640.0.azuredatabricks.net"
        self.DATABRICKS_HTTP_PATH="/sql/1.0/endpoints/9d983a38a6027f4e"
        self.DATABRICKS_TOKEN = BaseDados_tratamentos.token()
    
    def importar_dados_sql(self):
        
        with sql.connect(
        server_hostname = self.DATABRICKS_SERVER_HOSTNAME,
        http_path       = self.DATABRICKS_HTTP_PATH,
        access_token    = self.DATABRICKS_TOKEN) as connection:

            with connection.cursor() as cursor:
                # Consulta aqui, testa antes no databricks pra depois colocar aqui.
                query = """
                WITH BASE AS (
                SELECT DISTINCT
                    work_item_id AS CODIGO_OCEAN,
                    split_part(split_part(level_3_work_item_name, '_',2),'.',1) as SIGLA,
                    level_1_work_item_name AS NOME_CARD,
                    level_3_work_item_name AS COD_VERSAO_PXR,
                    level_3_month AS mes,
                    level_3_year as ano,
                    CASE mes
                        WHEN 'JAN' THEN '01'
                        WHEN 'FEV' THEN '02'
                        WHEN 'MAR' THEN '03'
                        WHEN 'ABR' THEN '04'
                        WHEN 'MAI' THEN '05'
                        WHEN 'JUN' THEN '06'
                        WHEN 'JUL' THEN '07'
                        WHEN 'AGO' THEN '08'
                        WHEN 'SET' THEN '09'
                        WHEN 'OUT' THEN '10'
                        WHEN 'NOV' THEN '11'
                        WHEN 'DEZ' THEN '12'
                        ELSE 0
                    END AS novo_mes,
                    to_date(concat('01','-',novo_mes,'-',level_3_year),'dd-MM-yyyy') as data
                FROM
                    `sandbox`.`gi_sgq`.`rpt_operacoes`
            

                    
            ),

            maior_data as(
            Select DISTINCT
                CODIGO_OCEAN,
                SIGLA,
                NOME_CARD,
                max(data) as MAXIMA_DATA

            From Base
            where
              data >= '2023-12-01'
            group by
            CODIGO_OCEAN,
            SIGLA,
            NOME_CARD
          

            ),
            Final as (

                Select 
                M.*,
                B.COD_VERSAO_PXR
                From maior_data as M
                INNER JOIN
                BASE as B
                    ON
                    B.SIGLA = M.SIGLA
                    AND B.CODIGO_OCEAN = M.CODIGO_OCEAN
                    AND B.data = M.MAXIMA_DATA 
            
            )

            SELECT 
                CODIGO_OCEAN,
                SIGLA,
                NOME_CARD,
                COD_VERSAO_PXR
            FROM Final a

                """ 

                # Puxa os dados do databricks
                cursor.execute(query)
                result = cursor.fetchall()

            # Os dados são retornados em linha, então convertemos em tabela. Coloque os nomes das colunas corretamente.
                self.tabela_df = pd.DataFrame(result, columns=["CODIGO_OCEAN", "SIGLA", "NOME_CARD","COD_VERSAO_PXR"])

        
        
    def importar_dados_excel(self,base):
        self.tabela_excel_df = pd.read_excel(str(base),'Itens de trabalho')
        colunas = ['CODIGO_OCEAN','E-mail do analista','Modalidade','Compartilhar Esteira']
        self.tabela_excel_df = self.tabela_excel_df[colunas]
        self.tabela_excel_df['Compartilhar Esteira']
        self.tabela_excel_df['Modalidade'] = self.tabela_excel_df['Modalidade'].str.upper().str.strip()    
        print(self.tabela_excel_df)
    
    def definir_data(self,nome_mes,ano):
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')
        data_atual = datetime.now()
        primeiro_dia_mes_atual =  datetime(data_atual.year, data_atual.month, 1)
        mes_anterior = primeiro_dia_mes_atual.replace(month=primeiro_dia_mes_atual.month - 1)
        nome_mes1 = mes_anterior.strftime('%b')
        ano1 = mes_anterior.strftime('%Y')
        nome_mes = str(nome_mes).upper()
        mes_ano = str(nome_mes) + '.' + ano           
        self.mes_ano = mes_ano.upper()  
        print(f'mes anterior é {self.mes_ano}')
        return self.mes_ano.upper()
        
    def tratar_dados(self):  
                       
        self.tabela_excel_df = self.tabela_excel_df.rename(columns={'CODIGO_OCEAN':'CODIGO_OCEAN'})
        self.tabela_df = self.tabela_df.merge(self.tabela_excel_df,on='CODIGO_OCEAN')
        
        self.tabela_df['NOVA_VERSAO_PXR'] = '-'
        self.tabela_df['NOVA_VERSAO_NUM'] = '-'
        self.tabela_df['NOVA_VERSAO_RESTO'] = '-'
        
        self.tabela_df['NOVA_VERSAO_PXR'] = self.tabela_df['COD_VERSAO_PXR'].apply(BaseDados_tratamentos.tratar_texto_pxr)
        self.tabela_df['NOVA_VERSAO_NUM'] = self.tabela_df['COD_VERSAO_PXR'].apply(BaseDados_tratamentos.tratar_texto_num)
        self.tabela_df['NOVA_VERSAO_RESTO'] = self.tabela_df['COD_VERSAO_PXR'].apply(BaseDados_tratamentos.tratar_texto_resto)
        self.tabela_df['NOVA_VERSAO_NUMERICO'] = self.tabela_df['NOVA_VERSAO_PXR'].apply(BaseDados_tratamentos.tratar_texto_pxr_numerico)
        self.tabela_df['NOVA_VERSAO_NUMERICO'] = self.tabela_df['NOVA_VERSAO_NUMERICO'].astype('int64')
        
        self.tabela_df['NOVA_VERSAO_RESTO'] = self.mes_ano
        
        for i , valor in enumerate(self.tabela_df['NOVA_VERSAO_NUMERICO']):
            self.tabela_df.loc[i,'NOVA_VERSAO_NUMERICO'] = self.tabela_df.loc[i,'NOVA_VERSAO_NUMERICO'] + 1
            
        for i , valor in enumerate(self.tabela_df['NOVA_VERSAO_NUMERICO']):
            if self.tabela_df.loc[i,'NOVA_VERSAO_NUMERICO'] <= 9 :
                self.tabela_df.loc[i,'NOVA_VERSAO_NUMERICO'] = str('PXR.00')+  str(self.tabela_df.loc[i,"NOVA_VERSAO_NUMERICO"])
            else:
                self.tabela_df.loc[i,'NOVA_VERSAO_NUMERICO'] = str('PXR.0') +  str(self.tabela_df.loc[i,"NOVA_VERSAO_NUMERICO"])
            
        self.tabela_df['NOVA_VERSAO_NUMERICO'] = self.tabela_df['NOVA_VERSAO_NUMERICO'] + '_' +self.tabela_df['NOVA_VERSAO_NUM'] + '_' + self.mes_ano
        
        self.tabela_df['COD_VERSAO_PXR'] =  self.tabela_df['NOVA_VERSAO_NUMERICO']
        
        colunas  = ['CODIGO_OCEAN','SIGLA','NOME_CARD','COD_VERSAO_PXR','E-mail do analista','Modalidade','Compartilhar Esteira']
        self.tabela_df = self.tabela_df[colunas]
        self.tabela_df = self.tabela_df.sort_values(by='CODIGO_OCEAN',ascending= True,ignore_index=True)
        self.tabela_df = self.tabela_df.fillna(value=0)
        self.tabela_df['Compartilhar Esteira'] = self.tabela_df['Compartilhar Esteira'].replace('Builders / ','',regex=True).replace(['/',',',''],';',regex=True)
        self.tabela_df['Compartilhar Esteira'] = self.tabela_df['Compartilhar Esteira'].str.replace(r';\s*(\d)', r';\1', regex=True)
        self.tabela_df['Compartilhar Esteira'] = self.tabela_df['Compartilhar Esteira'].str.replace(r'\.\s*;', '.;', regex=True)
        self.tabela_df['Compartilhar Esteira'] = self.tabela_df['Compartilhar Esteira'].str.strip()
        self.tabela_df.to_excel('Dados_criados.xlsx',index=False)
        print(self.tabela_df)
        
   
    
    
    
    def itens_trabalho(self):
        self.versao_pxr = self.tabela_df['COD_VERSAO_PXR']
        self.sigla = self.tabela_df['SIGLA']
        self.nome_card = self.tabela_df['NOME_CARD']
        self.email = self.tabela_df['E-mail do analista']
        self.modalidade = self.tabela_df['Modalidade']
        self.compartilhar_esteira = self.tabela_df['Compartilhar Esteira']
    
        return {
            
            'COD_VERSAO_PXR': self.versao_pxr,
            'SIGLA': self.sigla,
            'NOME_CARD': self.nome_card,
            'E-MAIL': self.email,
            'MODALIDADE':self.modalidade,
            'COMPARTILHAR_ESTEIRA': self.compartilhar_esteira
        }


if __name__ == "__main__":
    iniciar_dados = BaseDados_tratamentos()  
    iniciar_dados.importar_dados_sql()
    iniciar_dados.importar_dados_excel()
    iniciar_dados.definir_data()
    dados = iniciar_dados.tratar_dados()
    atributos_ocean = iniciar_dados.itens_trabalho()
