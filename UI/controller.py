import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handle_creaGrafo(self, e):

        self._view.txt_result.controls.clear()

        # Punto 1a e 1d: Validazione dell'input inserito nella casella di testo txtNumAeroporti
        input_str = self._view.txtNumAeroporti.value

        if not input_str or input_str.strip() == "":
            self._view.txt_result.controls.append(
                ft.Text("Inserisci un valore per il numero minimo di aeroporti.", color="red")
            )
            self._view.update_page()
            return

        try:
            n_aeroporti = int(input_str)
        except ValueError:
            self._view.txt_result.controls.append(
                ft.Text("Il valore inserito deve essere un numero intero.", color="red")
            )
            self._view.update_page()
            return

        if n_aeroporti <= 0:
            self._view.txt_result.controls.append(
                ft.Text("Il numero di aeroporti deve essere maggiore di 0.", color="red")
            )
            self._view.update_page()
            return

        # Se la validazione va a buon fine, qui procederemo con la creazione del grafo (Punto 1b/1c/1d)
        self._view.txt_result.controls.append(
            ft.Text(f"Valore valido inserito: {n_aeroporti}", color="green")
        )
        self._view.update_page()

        input_str = int(input_str)

        try:
            num_nodi, num_archi= self._model.creaGrafo(input_str)
            self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato:", color="red"))
            self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {num_nodi}"))
            self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {num_archi}"))

            self._view.update_page()

        except Exception as ex:
            self._view.txt_result.controls.append(ft.Text(f"Errore durante la creazione del grafo: {ex}", color="red"))
            self._view.update_page()


    def handle_compagnieConcorrenti(self, e):
        pass
