import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

class email():
    def __init__(self,email_remetente,senha_remetente,email_destinatario) -> None:
        self.remetente = email_remetente
        self.senha = senha_remetente
        self.destinatario = email_destinatario
        self.configurar_email()
        self.criar_mensagem()
        self.corpo_email
        self.anexar_arquivo()
        self.conexao_servidor()
        
        
    def configurar_email(self):
        self.remetente_email = self.remetente
        self.remetente_senha = self.senha
        self.destinatarios = [
            self.destinatario
        ]  # Lista de endereços de e-mail dos destinatários
        self.assunto = "RPA_OCEAN"
    
    def criar_mensagem(self):
        # Criar a mensagem de e-mail
        self.mensagem = MIMEMultipart()
        self.mensagem['From'] = self.remetente_email
        self.mensagem['To'] = ", ".join(self.destinatarios) #Jun
        self.mensagem['Subject'] = self.assunto
    
    def corpo_email(self):
        # Corpo do e-mail
        corpo = """
        Prezado(a),

        Espero que este e-mail o(a) encontre bem. \nTenho o prazer de informar que concluímos a automação do Ocean estou anexando o relatório detalhado com este e-mail.
 
        Agradecemos sua parceria e confiança em nosso trabalho.
        
        """
        self.mensagem.attach(MIMEText(corpo, 'plain'))
    
    def anexar_arquivo(self):  
        # Anexar a planilha
        excel = Path('Dados_criados.xlsx')
        attachment = open(excel, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {excel}")
        self.mensagem.attach(part)
        # Fechar o arquivo
        attachment.close()
        
    def conexao_servidor(self):
        # Conexão com o servidor
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(self.remetente_email, self.remetente_senha)
        text = self.mensagem.as_string()
        server.sendmail(self.remetente_email, self.destinatarios, text)
        server.quit()
        
# iniciar = email('bpocontroladoria.RPA@trinusco.com.br','Ctl102030$','ezequiel.aguiar@trinusco.com.br')
# iniciar.configurar_email()
# iniciar.criar_mensagem()
# iniciar.corpo_email()
# iniciar.corpo_email()
# iniciar.anexar_arquivo()
# iniciar.conexao_servidor()

