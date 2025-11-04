import flet as ft
from UI.view import View
from model.model import Model
from database.DB_connect import ConnessioneDB

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view
        self._DB_connect = ConnessioneDB()

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def popola_dropdown_musei(self):
        musei = self._model.get_musei()
        if musei:
            self._view.popola_dropdown_musei(musei)

    def popola_dropdown_epoche(self):
        epoche = self._model.get_epoche()
        if epoche:
            self._view.popola_dropdown_epoche(epoche)

    def popola_dropdown(self):
        if ConnessioneDB.get_connection() is None:
            self._view.show_alert("⚠️ Impossibile stabilire connessione con il database")
            return None
        self.popola_dropdown_musei()
        self.popola_dropdown_epoche()
        return

    # CALLBACKS DROPDOWN
    def handler_museo(self):
        museo = self._view.filtro_museo.value
        return museo

    def handler_epoca(self):
        epoca = self._view.filtro_epoche.value
        return epoca

    # AZIONE: MOSTRA ARTEFATTI
    def handler_mostra(self, e):
        if ConnessioneDB.get_connection() is None:
            self._view.show_alert("⚠️ Impossibile stabilire connessione con il database")
            return None
        museo = self.handler_museo()
        if museo != "None":
            museo = museo[0]
        epoca = self.handler_epoca()
        mostra = self._model.get_artefatti_filtrati(museo, epoca)
        self._view.lista_risultato.controls.clear()
        for elemento in mostra:
            self._view.lista_risultato.controls.append(ft.Text(f'{elemento}'))
        self._view.update()
        if len(mostra) == 0 or mostra == "None":
            self._view.show_alert("⚠️ La ricerca non ha prodotto alcun risultato")
