from .Requisition import Requesition
from threading import Thread

class Threads(Requesition):
    #Herdando de Requisition
    def __init__(self) -> None:
        super().__init__()
        #inicializando o set parametro
        self.set_param()
        #lista de Thread
        self.thread_list = []

    def read_arq(self):
        try:
            with open(f"{self.path}", "r+") as arq:
                #lendo wordlist e dividindo em duas atraves do index 
                self.wordlist = arq.read()
                self.division_wordlist = len(self.wordlist) // 2
        except:
            raise FileExistsError("Arquivo inexistente")
       
    # Metodo para inicializar, criar as threds, fazer a leitura da wordlist divider ela em 2 para cada thred
    def thred_request(self) -> None:
        #tenta fazer a leitura do arquivo wordlist que esta no caminho self.path 
        try:
            #wordlist com a primeira metade
            wordlist_1 = self.wordlist[:self.division_wordlist]
            #wordlist com a segunda metade
            wordlist_2 = self.wordlist[self.division_wordlist:]

            #definindo o metodo para as threds   
            for wordlist_part in [wordlist_1, wordlist_2]:
                dir = "".join(wordlist_part)
                #passando o metodo e o parametro de request_get
                th = Thread(target=self.request_GET, args=(dir.split(),))
                self.thread_list.append(th)
                th.start()
                    
        except:
           print("Wordlist não reconhecida ou inexistente")