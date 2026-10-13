import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._grafo = None


    def creaGrafo(self,input_str):
        self._grafo = nx.Graph()
        self._compagnie = {}

        compagnie = DAO.getCompagnie(input_str)

        # dizionario di supporto per collegare id e nome compagnia
        for c in compagnie:
            id_compagnia = c["ID"]
            nome_compagnia = c["AIRLINE"]

            self._compagnie[id_compagnia] = c
            self._grafo.add_node(id_compagnia)



        # 2. Carichiamo TUTTE le rotte e le raggruppiamo per compagnia in un set

        tutte_le_rotte = DAO.getAllRotte()
        compagnie_rotte = {}
        for r in tutte_le_rotte:
            airline_id = r["AIRLINE_ID"]

            # Consideriamo solo le compagnie che sono effettivamente nodi del grafo

            if airline_id in self._grafo.nodes():
                if airline_id not in compagnie_rotte:
                    compagnie_rotte[airline_id] = set()
                compagnie_rotte[airline_id].add((r["ORIGIN_AIRPORT_ID"], r["DESTINATION_AIRPORT_ID"]))

        print(f"COMPAGNIE CON ROTTE MEMORIZZATE: {len(compagnie_rotte)}")  # DEBUG

        # 4. Creazione degli archi in Python confrontando i set

        nodi = list(self._grafo.nodes()) # serve a estrarre tutti i nodi presenti nel grafo e a trasformarli in una lista Python standard.

        for i in range(len(nodi)):
            for j in range(i + 1, len(nodi)):
                c1 = nodi[i]  # Questo è il nome della compagnia 1
                c2 = nodi[j]  # Questo è il nome della compagnia 2

                rotte1 = compagnie_rotte.get(c1, set())
                rotte2 = compagnie_rotte.get(c2, set())

                # Intersezione tra i set di rotte
                comuni = rotte1.intersection(rotte2)
                peso = len(comuni)

                # Se hanno almeno una rotta in comune, creiamo l'arco pesato
                if peso > 0:
                    self._grafo.add_edge(c1, c2, weight=peso)

            print(f"ARCHI CREATI: {self._grafo.number_of_edges()}")  # DEBUG

            return self._grafo.number_of_nodes(), self._grafo.number_of_edges()


