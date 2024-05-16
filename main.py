from src.Views.Painel import Painel
from src.Core.Threads import Threads

#Instanciando
if __name__ == "__main__":  
    painel = Painel()  
    painel.paine_views()
    thred = Threads()
    thred.read_arq()
    thred.thred_request()
    