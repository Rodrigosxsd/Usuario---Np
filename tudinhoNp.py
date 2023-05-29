from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import pandas as pd


navegador = webdriver.Firefox()
navegador.get('https://app.napista.com.br/login/')
navegador.current_window_handle

#logar no sistema.
def login():
    sleep(2)
    login_acess = navegador.find_element('css selector', 'input[id="email"]').send_keys('xxxxxxx')
    senha_acess = navegador.find_element('css selector', 'input[id="senha"]').send_keys('xxxxxxxxx')
    button_acess = navegador.find_element('css selector', 'button[id="login-button"]').click()
    
    sleep(2)
    dropdown = navegador.find_element('css selector','legend[class="bv-no-focus-ring col-form-label pt-0"]').click()
    selecionar_grupo = navegador.find_element('css selector', f'li[id="vs1__option-12"]').click()
    sleep(2)
    entrar = navegador.find_element('css selector', 'button[class="btn btn-primary"]').click()

#acessar menu lateral.
def menuSide():
    sleep(10)
    menu = navegador.find_element('css selector', 'div[class="main-menu menu-fixed menu-accordion menu-shadow menu-light"]').click()
    config = navegador.find_element('css selector', 'a[href="/administrativo/configuracoes"] span[class="menu-title text-truncate"]').click()

#cadastrar usuario.
def user():    
    sleep(5)
    management_user = navegador.find_element('css selector', 'div[class="card-configuracoes"] a[href="/administrativo/configuracoes/usuarios/"]').click()
    planilha = pd.read_excel(r'D:\cadastratodinho\grs.xlsx', dtype= str)

    for i, Cpf in enumerate(planilha["Cpf"]): 
        print(planilha) 
        name = planilha.loc[i, "Nome"]
        phone = planilha.loc[i, "Telefone"]
        email = planilha.loc[i, "Login"]
        try:
            sleep(15)
            add = navegador.find_element('css selector', 'div[data-v-13428635] [class="btn btn-primary"]').click()
            cpf_person = navegador.find_element('css selector', 'input[placeholder="000.000.000-00"]').send_keys(Cpf)
            name_complet = navegador.find_element('css selector', 'input[placeholder="Seu nome completo..."]').send_keys(name)
            phone_person = navegador.find_element('css selector', 'input[placeholder="(99) 99999-9999"]').send_keys(str(phone))
            email_person = navegador.find_element('css selector', 'input[placeholder="Seu melhor email..."]').send_keys(email)
            sleep(2)
            perfil = navegador.find_element('css selector', 'div[selectlabel="Perfil"]').click()
            sleep(2)
            type_perfil = navegador.find_element('css selector', 'input[placeholder="Selecione um perfil"]').send_keys('Gerente')
            sleep(2)
            perfil = navegador.find_element('css selector', 'li[role="option"]').click()
            active = navegador.find_element('css selector', 'div[class="custom-control custom-switch"]').click()
            save = navegador.find_element('css selector', 'button[id="buttonSubmit"]').click()
        except NoSuchElementException:
            cancel = navegador.find_element('button[class="btn tw-ml-4 btn-outline-primary"]').click()
            return  
        #Salva log dos usuarios cadastrados.
        try: 
            with open ('log.txt', 'a') as arquivo:
                arquivo.write(Cpf + '\n')
                
        except FileNotFoundError:
            print('Erro')
        finally: 
            arquivo.close()    
                  
if __name__ == '__main__':
    login()   
    menuSide()
    user()