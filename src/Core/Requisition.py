import requests
from src.Model.LookDir import LookDir
from termcolor import colored
import sys


#Classe Requisiçoes
class Requesition(LookDir):
    def __init__(self) -> None:
        super().__init__()
        
    #Metodo que fara requisiçoes Get Usando lista Wordlist
    def request_GET(self, wordlist:list) -> None:
        #verificando se o parametro methodo de Lookdir e uma string 
        #verificando se method é GET
        if isinstance(self.methodo, str)and self.methodo.lower() == "get":
            try:
                #faz requisição para cada diretorio nas wordlists passadas a Thread
                for dir in wordlist:
                    #requisição get usando os diretorios das wordlists
                    req = requests.get(f"{self.url}/{dir}")
                    #mostrando cada url + diretorio que estão sendo requisitados
                    #flush para fazer a atualização na mesma linha 
                    print(f"URL:{self.url}/{dir}", end='\r',flush=True)
                   
                    """mostrando somente as requisiçoes que nos importa ou seja, acessivel ou redirecionavel
                    status entre 200 e 299"""
                    if req.status_code in [200,299]:
                        print(colored(f"URL: {self.url}/{dir.ljust(30)}\t STATUS:{req.status_code}", "green"))
                    #status entre 300 e 399
                    elif req.status_code in [300,399]:
                        print(colored(f"URL: {self.url}/{dir}\t STATUS:{req.status_code}", "grey"))       
            except:
                print("ERRO NAS REQUISIÇOES")
            
    