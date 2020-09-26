import os
from welcome import welcome
import json
from colorama import Fore, Back, Style


def fullcontact():

    def alterar_linha(path, cont): #,index_linha,nova_linha
        with open(path, 'r') as arquivo:
            linhas = arquivo.readlines() #cada linha é um elemento da lista linhas
        # editando a segunda linha
        linhas[5] = cont + '\n'

            # escrevendo de novo
        with open(path, 'w') as arquivo:
            arquivo.writelines(linhas)

    def questions():
        print("Escolha uma opção:\n")
        print("1 - Tenho um nome e um email")
        print("2 - Tenho um nome e um telefone")
        print("3 - Tenho um email e um telefone")
        print("4 - Tenho um email")
        print("5 - Tenho um telefone")

        opcao = input("\n~ ")
        return opcao

    opcao = questions()
    str(opcao)

##OPÇÃO 1 NOME E EMAIL

    if opcao == '1':
        full = input("Nome Completo: ")
        print("Separe os Emails por vírgulas")
        emails = input("Emails: ")
        tamanho = len(full.split(" "))
        tamanhomail = len(emails.split(", "))

        if tamanhomail > 1 and tamanho == 2:
            email1 = emails.split(", ")[0]
            email2 = emails.split(", ")[1]
            given = full.split(" ")[0]
            family = full.split(" ")[1]
            cont = "  -d" + "'"+"{"+ '"'+ "name" + '"' + ":"+"{"+ '"'+"full" + '"' + ":" + '"' + full + '"' + ',' + '"' + "given"+ '"' + ':' + '"' + given + '"' + ',' + '"family"' + ':' + '"' + family + '"' + "}," + '"'+ "emails" + '"' + ":"+"[" '"' + email1 + '"' + "," + '"' + email2 + '"'  + "]" + "}'"

        elif tamanho != 2:
            print("Teve um erro no nome, por favor use nome e sobrenome. Ex: João Souza. Infelizmente ainda não aceitamos outros padrões.")
        
        elif len(emails.split(", ")) == 1:
            given = full.split(" ")[0]
            family = full.split(" ")[1]
            email1 = emails
            cont = "  -d" + "'"+"{"+ '"'+ "name" + '"' + ":"+"{"+ '"'+"full" + '"' + ":" + '"' + full + '"' + ',' + '"' + "given"+ '"' + ':' + '"' + given + '"' + ',' + '"family"' + ':' + '"' + family + '"' + "}," + '"'+ "emails" + '"' + ":"+"[" '"' + email1 + '"' + "]" + "}'"


        alterar_linha("modules/fullcontact.sh", cont)
        os.system("sh modules/fullcontact.sh && clear")
        welcome()


##OPÇÃO 2 TELEFONE E NOME

    if opcao == '2':
        full = input("Nome Completo: ")
        phone = input("Phones: ")
        tamanhonome = len(full.split(" "))
        tamanhophone = len(phone.split(", "))

        if tamanhophone > 1 and tamanhonome == 2:
            given = full.split(" ")[0]
            family = full.split(" ")[1]
            phone1 = phone.split(", ")[0]
            phone2 = phone.split(", ")[1]
            cont = "  -d" + "'"+"{"+ '"'+ "name" + '"' + ":"+"{"+ '"'+"full" + '"' + ":" + '"' + full + '"' + ',' + '"' + "given"+ '"' + ':' + '"' + given + '"' + ',' + '"family"' + ':' + '"' + family + '"' + "}," + '"'+ "phones" + '"' + ":"+"[" '"' + phone1 + '"' + "," + '"' + phone2 + '"'  + "]" + "}'"

        elif tamanhonome != 2:
            print("Teve um erro no nome, por favor use nome e sobrenome. Ex: João Souza. Infelizmente ainda não aceitamos outros padrões.")
        
        elif len(phone.split(", ")) == 1:
            given = full.split(" ")[0]
            family = full.split(" ")[1]

            phone1 = phone
            cont = "  -d" + "'"+"{"+ '"'+ "name" + '"' + ":"+"{"+ '"'+"full" + '"' + ":" + '"' + full + '"' + ',' + '"' + "given"+ '"' + ':' + '"' + given + '"' + ',' + '"family"' + ':' + '"' + family + '"' + "}," '"'+ "phones" + '"' + ":"+"[" '"' + phone1 + '"' + "]" + "}'"

        alterar_linha("modules/fullcontact.sh", cont)
        os.system("sh modules/fullcontact.sh && clear")
        welcome()

        
##OPÇÃO 3 TELEFONE E EMAIL

    if opcao == '3':
        emails = input("Emails: ")
        phone = input("Phones: ")
        tamanhomail = len(emails.split(", "))
        tamanhophone = len(phone.split(", "))

        if tamanhophone == 2 and tamanhomail == 2:
            email1 = emails.split(", ")[0]
            email2 = emails.split(", ")[1]
            phone1 = phone.split(", ")[0]
            phone2 = phone.split(", ")[1]
            cont = "  -d" + "'"+"{"+ '"'+ "emails" + '"' + ":"+"[" '"' + email1 + '"' + "," + '"' + email2 + '"'  + "]," + '"'+ "phones" + '"' + ":"+"[" '"' + phone1 + '"' + "," + '"' + phone2 + '"'  + "]" "}'"
        
        elif len(phone.split(", ")) == 1 and len(emails.split(", ")) == 1:

            email1 = emails
            phone1 = phone
            cont = "  -d" + "'"+"{"+ '"'+ "phones" + '"' + ":"+"[" '"' + phone1 + '"' + "]," + '"'+ "emails" + '"' + ":"+"[" '"' + email1 + '"' + "]" + "}'"

        alterar_linha("modules/fullcontact.sh", cont)
        os.system("sh modules/fullcontact.sh && clear")
        welcome()



##OPÇÃO 4 EMAIL
            
    if opcao == '4':
        emails = input("Emails: ")
        if len(emails.split(", ")) > 1:
            email1 = emails.split(", ")[0]
            email2 = emails.split(", ")[1]
            cont = "  -d" + "'"+"{"+ '"'+ "emails" + '"' + ":"+"[" '"' + email1 + '"' + "," + '"' + email2 + '"'  + "]" + "}'"
            
            
        elif len(emails.split(", ")) == 1:
            email1 = emails
            cont = "  -d" + "'"+"{"+ '"'+ "emails" + '"' + ":"+"[" '"' + email1 + '"' + "]" + "}'"
            
            
        else:
            print("Houve um erro")
            
        alterar_linha("modules/fullcontact.sh", cont)
        os.system("sh modules/fullcontact.sh && clear")
        welcome()


##OPÇÃO 5 PHONE

    if opcao == '5':
        phone = input("Phones: ")
        if len(phone.split(", ")) > 1:
            phone1 = phone.split(", ")[0]
            phone2 = phone.split(", ")[1]
            cont = "  -d" + "'"+"{"+ '"'+ "phones" + '"' + ":"+"[" '"' + phone1 + '"' + "," + '"' + phone2 + '"'  + "]" + "}'"
            
            
        elif len(phone.split(", ")) == 1:
            phone1 = phone
            cont = "  -d" + "'"+"{"+ '"'+ "phones" + '"' + ":"+"[" '"' + phone1 + '"' + "]" + "}'" 
            
            
        else:
            print("Houve um erro")
            
        alterar_linha("modules/fullcontact.sh", cont)
        os.system("sh modules/fullcontact.sh && clear")
        welcome()
        

    with open("infos.json", 'r') as f:
        datastore = json.load(f)
        datass = json.dumps(datastore)

        def datasst(arg):
            return json.dumps(datastore[arg])

        if "Profile not found" in datass:
            print("Profile not found.")
            exit(1)

        else:
            #Full Name
            paz = datasst("fullName")
            if paz != "" and paz != "null":
                print ( "-" + Fore.WHITE + "Full Name:", datasst("fullName"))   
            else:
                pass

            #Age Range
            paz = datasst("gender")
            if paz != "" and paz != "null":
                print ( "-" + Fore.WHITE + "Age Range:", datasst("ageRange"))
            else:
                pass   
            
            #Gender
            paz = datasst("gender")
            if paz != "" and paz != "null":
                print ( "-" + Fore.WHITE + "Gender:", datasst("gender")) 
            else:
                pass

            #Location
            paz = datasst("location")
            if paz != "" and paz != "null":
                print ( "-" + Fore.WHITE + "Location:", datasst("location"))
            else:
                pass
            
            #Title
            paz = datasst("title")
            if paz != "" and paz != "null":
                print ( "-" + Fore.WHITE + "Title:", datasst("title")) 
            else:
                pass

            #Organization
            paz = datasst("organization")
            if paz != "" and paz != "null":
                print ( "-" + Fore.WHITE + "Organization:", datasst("organization"))   
            else:
                pass

            #Twitter
            paz = datasst("twitter")
            if paz != "" and paz != "null":
                print ( "-" + Fore.WHITE + "Twitter:", datasst("twitter"))    
            else:
                pass
            
            #Linkedin
            paz = datasst("linkedin")
            if paz != "" and paz != "null":
                print ( "-" + Fore.WHITE + "Linkedin:", datasst("linkedin"))   
            else:
                pass

            #Facebook
            paz = datasst("facebook")
            if paz != "" and paz != "null":
                print ( "-" + Fore.WHITE + "Facebook:", datasst("facebook"))   
            else:
                pass

            paz = datasst("bio")
            if paz != "" and paz != "null":
                print ( "-" + Fore.WHITE + "Bio:", datasst("bio"))   
            else:
                pass
            
            #avatar
            paz = datasst("avatar")
            if paz != "" and paz != "null":
                print ( "-" + Fore.WHITE + "Avatar Icon:", datasst("avatar"))    
            else:
                pass

            #Web Site
            paz = datasst("website")
            if paz != "" and paz != "null":
                print ( "-" + Fore.WHITE + "Web Site:", datasst("website"))    
            else:
                pass



