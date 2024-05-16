import argparse


class LookDir:
    #Metodo construtor, parametros url, local wordlist, methodo do request
    def __init__(self) -> None:
        #parametros
        self.url:str = None
        self.path:str = None
        self.methodo:str = None
        
    #setando os parametros do metodo construtor usando argumentos de linha de comando
    def set_param(self) -> None:
        parser = argparse.ArgumentParser(description='Explorado de Diretorios')
        #-u (Url)
        parser.add_argument('-u', '--url',help='Url alvo')
        #-w (Wordlist)
        parser.add_argument('-w', '--wordlist',help='Wordlist de Diretorios')
        #-m (metodo)
        parser.add_argument('-m', '--method',help='Requisiçao (GET,POST)')
        args = parser.parse_args()

        #parametros recebendo os valores dos argumentos 
        self.url = args.url
        self.path = args.wordlist
        self.methodo = args.method
        

    #def __str__(self) -> str:
        #return f"{self.url}\n{self.path}\n{self.methodo}"