from database.DB_connect import DBConnect
from model.airport import Airport

class DAO:

    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * from airports a order by a.AIRPORT asc"""

        cursor.execute(query)

        for row in cursor:
            result.append(Airport(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getCompagnie(input_str):

        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query ="""select a.* 
        from flights f, airlines a
        where f.AIRLINE_ID = a.id 
        group by a.id 
        having count(distinct f.ORIGIN_AIRPORT_ID ) >= %s"""

        cursor.execute(query, (input_str,))

        for row in cursor:
            results.append(row)

        cursor.close()
        conn.close()
        return results

    # Presi i nodi vado nel model per costruire il metodo def creaGrafo

    # Per recuperare gli archi, dato che ho mesi per studiare questa materia provo a non farlo
    # con una query ma su python direttamente
    # prendo quindi tutte le rotte possibili

    @staticmethod
    def getAllRotte():

        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT f.AIRLINE_ID, f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID
                   FROM flights f"""

        cursor.execute(query)

        for row in cursor:
            results.append(row)

        cursor.close()
        conn.close()
        return results

    # Ora vado nel model
