from typing import KeysView
import selenium 
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import locale
from pathlib import Path

class rpa_ocen():
    def __init__(self):
        self.qtde_erro = 0
        self.dados()
        self.iniciar()
        self.credencias()
        self.login()
        self.espaco_ocean()
        self.selecionar_cad()

    def fechar_navegador(self):
        self.navegador_oficial.close()

    def erro(self):
        self.fechar_navegador()
        self.iniciar()
        self.credencias()
        self.login()
        self.espaco_ocean()

    def dados(self):
        caminho_arquivo = Path(__file__)
        caminho_arquivo = caminho_arquivo.parent
        self.nome_arquivo = caminho_arquivo/'BASE'
        self.tabela = pd.read_excel(f'{self.nome_arquivo}.xlsx','Itens de trabalho')
        locale.setlocale(locale.LC_ALL,'pt_BR.utf8')
        self.data_atual = datetime.date.today()
        self.mes_anterior = self.data_atual.replace(day=1) - datetime.timedelta(days=1)
        self.mes_anterior_str = self.mes_anterior.strftime('%b_%Y').upper()
        
        for  linha in self.tabela.index:
            self.tabela.loc[linha,'Cod_Versão_PXR'] += 1
            if self.tabela.loc[linha,'Cod_Versão_PXR'] <=9:
                self.tabela.loc[linha,'Cod_Versão_PXR'] = '00' + str(self.tabela.loc[linha,'Cod_Versão_PXR'])
            else:
                self.tabela.loc[linha,'Cod_Versão_PXR'] = '0' + str(self.tabela.loc[linha,'Cod_Versão_PXR'])
            self.tabela.loc[linha,'Cod_Versão_PXR'] = 'PXR.'+ str(self.tabela.loc[linha,'Cod_Versão_PXR']) + '_' + str(self.tabela.loc[linha,'Sigla']) + '.' + str(self.tabela.loc[linha,'Código Sonar']) + '_' + self.mes_anterior_str
            self.chave_esteira = self.tabela.loc[linha,'Compartilhar Esteira']
            self.lista = self.chave_esteira.split(',')
            self.tabela['Status'] = 'null'
        print(self.tabela['Cod_Versão_PXR'])


    def iniciar(self):
        self.navegador_oficial = webdriver.Chrome()
        self.navegador_oficial.maximize_window()
        self.link = 'https://login.microsoftonline.com/3e57d4dc-f016-4540-b3b8-d667b5cb9512/oauth2/v2.0/authorize?response_type=id_token&scope=user.read%20openid%20profile&client_id=642a14f3-7b12-458f-9e7c-8a0c1f7cf47e&redirect_uri=https%3A%2F%2Focean.trinus.co%2F&state=eyJpZCI6IjIzYmJjNzM1LTFlNTUtNGZlOS05ZWI2LWJhZDRmN2I1ZWNjYyIsInRzIjoxNzA0ODU0NDk4LCJtZXRob2QiOiJwb3B1cEludGVyYWN0aW9uIn0%3D&nonce=3257e416-541c-422e-ae61-89eadf1131205&client_info=1&x-client-SKU=MSAL.JS&x-client-Ver=1.4.18&client-request-id=aba0de3d-f9d9-4c5b-ad7a-91f7c2ed79ea&response_mode=fragment&sso_reload=true'
        self.navegador_oficial.get(f'{self.link}')
        
    def credencias(self):
        self.usuario = 'ezequiel.aguiar@trinusco.com.br'
        self.senha = '16112018Ep@'
        
    def login(self):
        try:
            self.clique_digitar_usuário = WebDriverWait(self.navegador_oficial,120).until(EC.visibility_of_element_located((By.CLASS_NAME , 'form-control.ltr_override.input.ext-input.text-box.ext-text-box')))
            self.clique_digitar_usuário = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.CLASS_NAME , 'form-control.ltr_override.input.ext-input.text-box.ext-text-box')))
            self.clique_digitar_usuário.click()
            self.clique_digitar_usuário.send_keys(f'{self.usuario}')
            self.clique_avancar = WebDriverWait(self.navegador_oficial,120).until(EC.visibility_of_element_located((By.CLASS_NAME,'win-button.button_primary.button.ext-button.primary.ext-primary')))
            self.clique_avancar = self.navegador_oficial.find_element(By.CLASS_NAME,'win-button.button_primary.button.ext-button.primary.ext-primary')
            self.clique_avancar.click()
            self.clicar_senha = WebDriverWait(self.navegador_oficial,120).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input')))
            self.clicar_senha = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input')))
            self.clicar_senha.click()
            self.clicar_senha.send_keys(f'{self.senha}')
            time.sleep(2)
            self.clicar_ok = WebDriverWait(self.navegador_oficial,120).until(EC.visibility_of_element_located((By.ID,'idSIButton9')))
            self.clicar_ok = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.ID,'idSIButton9')))
            self.clicar_ok.click()
            self.clicar_sim = WebDriverWait(self.navegador_oficial,120).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input')))
            self.clicar_sim = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input')))
            self.clicar_sim.click()
            self.clique_elemento_login = WebDriverWait(self.navegador_oficial,120).until(EC.visibility_of_element_located((By.XPATH,'//*[contains(text(),"Login Conta Microsoft")]')))
            self.clique_elemento_login = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.CSS_SELECTOR,'//*[contains(text(),"Login Conta Microsoft")]')))
            self.clique_elemento_login.click()
        except:
            self.fechar_navegador()
            self.iniciar()
            self.credencias()
            self.login()

    
    def espaco_ocean(self):      
        self.clicar_espaco_trabalho = WebDriverWait(self.navegador_oficial,120).until(EC.visibility_of_element_located((By.CLASS_NAME,'sc-cspYLC.fBFRyU')))
        self.clicar_espaco_trabalho = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.CLASS_NAME,'sc-cspYLC.fBFRyU')))
        self.clicar_espaco_trabalho.click()
        self.clicar_pxp = WebDriverWait(self.navegador_oficial,120).until(EC.visibility_of_element_located((By.CLASS_NAME,'sc-dExYaf.cCSpRx' )))
        self.clicar_pxp = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div[3]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div')))
        self.clicar_pxp.click()

    def selecionar_cad(self):
        print(self.qtde_erro)
        try:
            for  linha in self.tabela.index : 
                if self.qtde_erro >= 2 :
                    self.tabela['Status'] = 'Pulou'
                    print('Pulou')
                    self.qtde_erro = 0
                    continue
                self.vericar_banco_card = WebDriverWait(self.navegador_oficial,120).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'[data-rbd-droppable-context-id]')))
                self.vericar_banco_card = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[data-rbd-droppable-context-id]')))
                self.clicar_pesquisar = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[placeholder="Pesquisar"]')))
                self.clicar_pesquisar.click()
                self.clicar_pesquisar.send_keys(self.tabela.loc[linha,'Sigla'])
                self.clicar_pesquisar.send_keys(Keys.ENTER)
                self.chave_card = self.tabela.loc[linha,'Nome Item']
                self.elemento_chave_card = f'//span[@id="card-title" and text()="{self.chave_card}"]'
                self.clicar_card_spe = WebDriverWait(self.navegador_oficial,120).until(EC.visibility_of_element_located((By.XPATH,self.elemento_chave_card)))
                self.clicar_card_spe = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,self.elemento_chave_card)))
                self.clicar_card_spe.click()
                #Funções
                self.card_selecionado()
                self.cria_versao(linha)
                self.importar_modelo_templete(linha)
                self.selecionar_shark(linha)
                self.inserir_tags()
                self.compartilha()
                self.home()
        except:
                print('Deu ruim')
                self.qtde_erro += 1
                print(self.qtde_erro)
                if self.qtde_erro == 1 :
                    self.navegador_oficial.refresh()
                    self.aguardar_pagina = WebDriverWait(self.navegador_oficial,120).until_not(EC.presence_of_all_elements_located((By.CLASS_NAME,'react-loading-skeleton')))
                    self.card_selecionado()
                    self.cria_versao(linha)
                    self.importar_modelo_templete(linha)
                    self.selecionar_shark(linha)
                    self.inserir_tags()
                    self.compartilha()
                    self.selecionar_cad()
                else:
                    self.erro()
                    self.selecionar_cad()

    def card_selecionado(self):
            self.aguardar_pagina = WebDriverWait(self.navegador_oficial,120).until_not(EC.presence_of_all_elements_located((By.CLASS_NAME,'react-loading-skeleton')))
            self.Encontrar_EV = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'[title="EV ACOMPANHAMENTO - PxR"][class="task-name-text-content normal"]')))
            self.clicar_EV_Acompanhamento = WebDriverWait(self.navegador_oficial,120).until(EC.visibility_of_element_located((By.XPATH,'//span[@title="EV ACOMPANHAMENTO - PxR"]')))
            self.clicar_EV_Acompanhamento = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,'//span[@title="EV ACOMPANHAMENTO - PxR"]')))
            self.clicar_EV_Acompanhamento.click()
            
            
    def cria_versao(self,linha):
            try:
                self.aguardar_versão = WebDriverWait(self.navegador_oficial,120).until_not(EC.presence_of_all_elements_located((By.CLASS_NAME,'react-loading-skeleton')))
                print('Versão ja criada')
                self.chave_versao = self.tabela.loc[linha,'Cod_Versão_PXR']
                self.chave_versao_final = f'[title="{self.chave_versao}"]'
                print(f'{self.chave_versao_final}')
                self.clicar_versao_final = WebDriverWait(self.navegador_oficial,2).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.chave_versao_final)))
                self.clicar_versao_final.click()
            except:
                print('Criando nova versão')
                self.criar_item_trabalho = WebDriverWait(self.navegador_oficial,120).until(EC.visibility_of_element_located((By.XPATH,'//div[@role="button"]//span[contains(text(),"Item")]')))
                self.criar_item_trabalho = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,'//div[@role="button"]//span[contains(text(),"Item")]')))
                self.criar_item_trabalho.click()
                self.clicar_item_Gi = WebDriverWait(self.navegador_oficial,120).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'[data-test*="item-type-menu-list"]')))
                self.clicar_item_GI = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[data-test*="item-type-menu-list"]')))
                self.clicar_item_Gi.click()
                self.digitar_versao = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[type="text"]')))
                self.digitar_versao.click()
                self.digitar_versao.send_keys(self.tabela.loc[linha,'Cod_Versão_PXR'])
                self.confirmar_versao = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[type="button"][id="submit-text-input-button"]')))
                self.confirmar_versao.click()
                self.selecionar_versão_criada(linha)

    def selecionar_versão_criada(self,linha):
            self.aguardar_pagina = WebDriverWait(self.navegador_oficial,120).until_not(EC.presence_of_all_elements_located((By.CLASS_NAME,'react-loading-skeleton')))    
            try:
                self.chave_versao = self.tabela.loc[linha,'Cod_Versão_PXR']
                self.chave_versao_final = f'[title="{self.chave_versao}"]'
                self.clicar_versao = WebDriverWait(self.navegador_oficial,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,self.chave_versao_final)))
                self.clicar_versao_final = self.navegador_oficial.find_element(By.CSS_SELECTOR, self.chave_versao_final)
                self.clicar_versao_final.click()
            except:
                 pass
            
    def importar_modelo_templete(self,linha):
            self.aguardar_criacao_versao = WebDriverWait(self.navegador_oficial,120).until_not(EC.presence_of_all_elements_located((By.CLASS_NAME,'react-loading-skeleton')))
            self.importar_modelo = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,'//div[@id="idChildrenContainer"]//button[@type="submit"]//div[@class="icones"]')))
            self.importar_modelo.click() 
            print('Criando modelo')
            self.variavel_modalidade = self.tabela.loc[linha,'Modalidade']
            match self.variavel_modalidade:
                case 'Urbanismo':
                    caminho = '//div[contains(text(),"GI_PXR URBANISMO E MULTIPROPRIED...")]'
                    print('funcionou')
                case 'Incoporação':
                    caminho = '//div[contains(text() ,"GI_PXR INCORPORAÇÃO")]'
                case 'Maranhão':
                    caminho = '//div[contains(text(),"GI_PXR URB (MARANHÃO)")]'
            self.clicar_dentro_modelo = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,caminho)))
            self.clicar_dentro_modelo.click()
                # break
            self.aplicar_modelo = WebDriverWait(self.navegador_oficial,120).until(EC.visibility_of_element_located((By.XPATH,'//*[contains(text(),"Aplicar modelo")]'))) 
            self.aplicar_modelo.click()
            self.mensagem_aplicar_modelo = WebDriverWait(self.navegador_oficial,120).until(EC.visibility_of_element_located((By.XPATH,'//h5[contains(text(),"Aplicar Modelo")]')))
            self.click_aplica_modelo = self.mensagem_aplicar_modelo.find_element(By.XPATH,'//button[contains(text(),"APLICAR")]')
            self.click_aplica_modelo.click()
            self.mensagem_aplicar_modelo_sair = WebDriverWait(self.navegador_oficial,120).until_not(EC.presence_of_element_located((By.XPATH,'//div[contains(text(),"Estamos preparando o item de trabalho com o modelo escolhido. Aguarde alguns instantes")]')))
            self.mensagem_aplicar_modelo_sair = WebDriverWait(self.navegador_oficial,120).until_not(EC.presence_of_element_located((By.XPATH,'//div[contains(text(),"Estamos preparando o item de trabalho com o modelo escolhido. Aguarde alguns instantes")]')))
            print('Selecionar modelo deu certo')
    
    def selecionar_shark(self,linha):
            self.aguardar_pagina = WebDriverWait(self.navegador_oficial,120).until_not(EC.presence_of_all_elements_located((By.CLASS_NAME,'react-loading-skeleton')))                 
            shark_responsavel = WebDriverWait(self.navegador_oficial,120).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'[class="icones"][id="icone"][style = "width: 35px; height: 35px; display: block; cursor: pointer;"]')))
            shark_responsavel = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="icones"][id="icone"][style = "width: 35px; height: 35px; display: block; cursor: pointer;"]')))
            shark_responsavel.click()
            email_desejado = self.tabela.loc[linha,'E-mail do analista']
            print(email_desejado)
            lista_email_shark = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,f'//span[@class="responsible-option-email"][contains(text(),"{email_desejado}")]')))
            lista_email_shark.click()
            aguardar_inserir_shark = WebDriverWait(self.navegador_oficial,120).until_not(EC.presence_of_element_located((By.CLASS_NAME,'responsible-menu-heading')))
            print('Deu certo shark')
            

    def inserir_tags(self):
            self.aguardar_pagina = WebDriverWait(self.navegador_oficial,10).until_not(EC.presence_of_all_elements_located((By.CLASS_NAME,'react-loading-skeleton')))
            self.mes_anterior_str = self.mes_anterior_str.replace('_','.')
            try:    
                 print('Ja tem teg')
                 tag_ocean = WebDriverWait(self.navegador_oficial,3).until(EC.visibility_of_element_located((By.XPATH,f'//span[text()="{self.mes_anterior_str}"]')))
            except:    
                print('Inserir as tegs')
                self.tag_ocean = WebDriverWait(self.navegador_oficial,120).until(EC.visibility_of_element_located((By.XPATH,'//div[@id="aside-header"]//*[@data-test="show-tags"][@title="Atribuir ou excluir tags"]')))
                self.tag_ocean.click()
                self.aguardar_tag = WebDriverWait(self.navegador_oficial,120).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'[id="tagMenu"]')))
                self.aguardar_tag = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[id="tagMenu"]')))
                self.selecionar_tag = WebDriverWait(self.navegador_oficial,120).until(EC.visibility_of_element_located((By.XPATH,f'//span[contains(text(),"{self.mes_anterior_str}")]')))
                self.selecionar_tag = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,f'//span[contains(text(),"{self.mes_anterior_str}")]')))
                self.selecionar_tag.click()
                self.fechar_tela_tag = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,'//div[@id="tagMenu"]//div[2][@class="icones"]')))
                self.fechar_tela_tag.click()
                self.fechar_tela_tag = WebDriverWait(self.navegador_oficial,120).until_not(EC.presence_of_element_located((By.XPATH,'//div[@id="tagMenu"]//div[2][@class="icones"]')))
                print('deu certo tags')

    def compartilha(self):
            self.aguardar_pagina = WebDriverWait(self.navegador_oficial,120).until_not(EC.presence_of_all_elements_located((By.CLASS_NAME,'react-loading-skeleton')))
            print('Entrou no compartilhamento')
            for i , item in enumerate(self.lista) :
                item = item.upper()
                print(item)
                self.botao_compartilha = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,'//div[1]//div[2]//span/div[@class="icones"]')))
                self.botao_compartilha.click()                                                                                                       
                self.aguarda_tela_compartilhar = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,'//button[contains(text(),"COMPARTILHAR EXECUÇÃO")]')))
                self.compartilhar_execucao = self.aguarda_tela_compartilhar
                self.compartilhar_execucao.click()
                self.aguardar_tela_compartilhar_execucao = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,'//div[contains(text(),"Compartilhar execução de item")]')))
                self.aguardar_Builders_inserir = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,'//div[@id = "idChildrenContainer"]//*[(text() ="Builders")]')))
                self.clicar_selecao_esteira = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,'//div[@id="selectedItemWrapper"]//span[contains(text(),"Selecione")]')))
                self.clicar_selecao_esteira.click()
                self.selecionar_esteira = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,f'//*[@id="idChildrenContainer"]//*[text()="{item}"]')))
                self.selecionar_esteira.click()
                self.botao_compartilha = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,'//button//div[contains(text(),"Compartilhar")]')))                
                self.botao_compartilha.click()
                self.aguardar_janela_compartilhar = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,'//button[@data-testid="cancel-button"][text()="Cancelar"]')))
                print('Passou compartilhar')
                self.confirmar_compartilhamento = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,'//div/button[@id="confirm-button"][contains(text(),"Compartilhar")]')))
                self.confirmar_compartilhamento.click()
                self.aguardar_janela_compartilhar = WebDriverWait(self.navegador_oficial,120).until_not(EC.presence_of_element_located((By.XPATH,'//header//p[contains(text(),"Deseja compartilhar o item")]')))
                print('Terminou de compartilhar')
                self.aguardar_janela_compartilhar = WebDriverWait(self.navegador_oficial,120).until_not(EC.presence_of_element_located((By.XPATH,'//button[@data-testid="cancel-button"][text()="Cancelar"]')))
                self.aguardar_pagina = WebDriverWait(self.navegador_oficial,120).until_not(EC.presence_of_all_elements_located((By.CLASS_NAME,'react-loading-skeleton'))) 

    def home(self):
            print('Entrou na home')
            self.navegador_oficial.get('https://ocean.trinus.co/ocean/workspaces/9/boards/446/item-view/kanban')
            self.aguardar_pagina = WebDriverWait(self.navegador_oficial,120).until_not(EC.presence_of_all_elements_located((By.CLASS_NAME,'react-loading-skeleton')))
            self.vericar_banco_card = WebDriverWait(self.navegador_oficial,120).until(EC.visibility_of_element_located((By.XPATH,'//*[text()= "#BANCO DE CARDS"]')))
            self.vericar_banco_card = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,'//*[text()= "#BANCO DE CARDS"]')))
            self.clicar_pesquisar = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,'//*[@id="idChildrenContainer"]//*[@placeholder="Pesquisar"]')))             
            self.clicar_pesquisar.clear()
            self.clicar_pesquisar.clear()
            self.clicar_pesquisar.send_keys(Keys.ENTER)
            time.sleep(3)
            self.pesquisar = WebDriverWait(self.navegador_oficial,120).until(EC.presence_of_element_located((By.XPATH,'//div[@id="idChildrenContainer"]//div[2]')))
            self.pesquisar.click()
            
    