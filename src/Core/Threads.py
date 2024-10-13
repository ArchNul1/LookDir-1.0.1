from .Requisition import Requesition
import aiohttp
import asyncio

class Threads(Requesition):
    def __init__(self, max_threads=4) -> None:
        super().__init__()
        self.set_param()
        self.max_threads = max_threads
        self.wordlist = []  # Inicializando wordlist / Initializing wordlist

    def read_arq(self):
        try:
            with open(self.path, "r+") as arq:
                self.wordlist = arq.read().splitlines()  # Convertendo para lista / Converting to list
        except FileNotFoundError:
            raise FileNotFoundError("file Not exist")  # Arquivo inexistente / File does not exist

    async def thred_request(self):
        self.read_arq()  # Lendo o arquivo antes de executar as threads / Reading the file before executing the threads
        timeout = aiohttp.ClientTimeout(total=5)  # Exemplo de timeout de 5 segundos
        async with aiohttp.ClientSession(timeout=timeout) as session:  # Criando uma sessão uma vez / Creating a session once
            tasks = []
            for dir in self.wordlist:  # Loop pelas palavras / Loop through the words
                tasks.append(self.request_GET(session, dir))  # Adiciona tarefas à lista / Add tasks to the list
            await asyncio.gather(*tasks)  # Executa todas as tarefas / Execute all tasks
