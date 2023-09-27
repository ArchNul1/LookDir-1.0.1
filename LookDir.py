import sys
import requests
import pyfiglet
from termcolor import colored
import whois
from tqdm import tqdm
import os.path

### MENU SIMPLES 
class Menu:
    def menu_User(self):

        print(colored('#' * 50, 'red'))
        title = pyfiglet.figlet_format("LookDir", font="doom")
        print(colored(title, 'red'))
        print(colored("\t By: Arch_0x3f5", 'red'))
        print(colored("\t Discord: Arch_0x3f5", 'blue'))
        print(colored("\t GitHub: __arch_0x3f5", 'green'))
        print(colored("\n\n[1] - Explorar Diretórios\n[2] - Reconhecimento\n[3] - Sair", "green"))
        print(colored('#' * 50, 'red'))

    #Verifica se o Caminho da wordlist esta correto 
    def wordlist_local(self, path):
        if os.path.exists(path):
            return path
        
        else:
            print(colored(f'\n\n>>>>>>>>>>O ARQUIVO{path} NAO EXISTE<<<<<<<<<<<<<<<\n\n.', 'red'))
            return None


    #Verifica se existe o diretorio, verificando se o codigo response e 200
    def verificar_dir(self):
        try:
            #url do alvo 
            self.url_alvo = input(colored("\nDIGITE A URL: ", 'green'))
            print(colored('#' * 50, 'red'))

            self.wordlist = input(colored("\n\nDIGITE O CAMINHO DA WORDLIST: ", 'green'))
            self.wordlist = self.wordlist_local(self.wordlist)
            print(colored('#' * 50, 'blue'))
            print('\n\n')

            #leitura da wordlist e cada dir em tempo real que esta sendo verificado 
            with open(self.wordlist, 'r') as arquivos:
                leitura_wordlist = arquivos.readlines()

                for dir in tqdm(leitura_wordlist, desc="Verificando diretórios"):
                    dir = dir.strip()

                    sys.stdout.write("\r" + colored('Verificando:', 'red') + colored(f'{self.url_alvo}/{dir}', 'green'))
                    sys.stdout.flush()

                    response = requests.get(f'{self.url_alvo}/{dir}')

                    if response.status_code == 200:
                        print(colored(f'\n\n{self.url_alvo}/{dir}', 'green') + colored(' ENCONTRADO', 'blue') + '\n')
                        print(colored('#' * 50, 'blue'))

        except Exception as e:
            print(colored("Erro:", 'red'), e)

    #Busca de informaçoes ultilizando Whois
    def buscar_info(self):
        self.url = input(colored("\nURL ALVO: ", "green"))
        busca = whois.whois(self.url)
        print(colored(busca, 'green'))


        # Opção de voltar ou sair do programa após a verificação
        while True:
            try:
                voltar = input(colored("\n\nDeseja voltar ao menu? (sim/não): ", "green"))
                if voltar.lower() == "sim":
                    return
                elif voltar.lower() == "não":
                    sys.exit()  # Encerra o programa
                else:
                    print(colored("Digite sim ou não.", "red"))
            except Exception as e:
                print(colored("Erro:", 'red'), e)


    # inicializador menu e opões 
    def run(self):
        while True:
            self.menu_User()
            try:
                self.opt = int(input(colored("\nDIGITE A OPÇÃO: ", "green")))
                print(colored('#' * 50, 'red'))
                if self.opt == 1:
                    self.verificar_dir()

                elif self.opt == 2:
                    self.buscar_info()

                elif self.opt == 3:
                    print(colored("LOOKDIR", "green"))
                    sys.exit()
                else:
                    print(colored("Digite uma opção válida ", 'red'))
            except ValueError:
                print(colored("Digite uma opção válida ", 'red'))



if __name__ == "__main__":
    run = Menu()
    run.run()
