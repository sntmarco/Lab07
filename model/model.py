from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        artefatti = self._artefatto_dao.leggiArtefatti()
        artefatti_filtrati = []

        for artefatto in artefatti:
            epoca_ok = False
            museo_ok = False
            print(artefatto.id_museo)
            print(museo)
            if epoca == "None" or str(artefatto.epoca) == str(epoca):
                epoca_ok = True
            if museo == "None" or str(artefatto.id_museo) == str(museo):
                museo_ok = True
            if museo_ok and epoca_ok:
                artefatti_filtrati.append(artefatto)

        artefatti_filtrati.sort()
        return artefatti_filtrati

    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        epoche = []
        artefatti = self._artefatto_dao.leggiArtefatti()
        for artefatto in artefatti:
            epoca = artefatto.epoca
            if epoca not in epoche:
                epoche.append(epoca)
        epoche.sort()
        return epoche

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        musei = self._museo_dao.leggiMusei()
        return musei