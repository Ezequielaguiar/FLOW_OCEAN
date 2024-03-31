from pages.common.BasePage import BasePage
from pages.common.BasePageElement import BasePageElement
from pages.Login import Login
from components.tags.Tags import Tags

login = Login()
componenteTags = Tags()

login.open_browser()
login.go_to('/login')
login.loginWith('nomedousuario', 'senhadousuario')
componenteTags.adicionar_tag('nometag')
