import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

        #Dropdown
        self.filtro_museo = None
        self.filtro_epoche = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        self.filtro_museo = ft.Dropdown(label="Museo",
                                        width = 400,
                                        hint_text = "Seleziona museo",
                                        options = None,
                                        on_change = self.controller.handler_museo)

        self.filtro_epoche = ft.Dropdown(label="Epoche",
                                        width=200,
                                        hint_text="Seleziona epoca",
                                        options=None,
                                        on_change=self.controller.handler_epoca)

        # Sezione 3: Artefatti
        self.btn_mostra = ft.ElevatedButton(text = "Mostra artefatti",
                                            width = 200,
                                            tooltip = "Mostra artefatti",
                                            on_click = self.controller.handler_mostra)

        self.lista_risultato = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            ft.Row(spacing=200,
                         controls = [self.filtro_museo, self.filtro_epoche],
                         alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            # Sezione 3: Artefatti
            self.btn_mostra,
            ft.Divider(),
            self.lista_risultato,
            ft.Divider(),
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()

    def popola_dropdown_musei(self, musei):
        self.filtro_museo.options = [ft.DropdownOption("None", "Nessuna selezione")]+[ft.DropdownOption(m) for m in musei]
        self.page.update()
        return

    def popola_dropdown_epoche(self, epoche):
        self.filtro_epoche.options = [ft.DropdownOption("None", "Nessuna selezione")]+[ft.DropdownOption(e) for e in epoche]
        self.page.update()
        return