from src.Views.Painel import Painel
from src.Core.Threads import Threads
import asyncio

if __name__ == "__main__":  
    painel = Painel()  
    painel.paine_views()
    thred = Threads()
    
    # Define os parâmetros/set params
    thred.set_param()  
    
    # Verifica a URL e o caminho do wordlist/ verification url and file path
    if not thred.url or not thred.path:
        print("Erro: URL ou caminho do wordlist não foram fornecidos.")
        exit(1)

    # Executa a requisição /run requests
    try:
        asyncio.run(thred.thred_request())
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
