import mysql.connector
ef execute_stored_procedure(conn, procedure_name, params):
cursor = conn.cursor()
    placeholders = ', '.join(['%s'] * len(params))
    try:
cursor.callproc(procedure_name, params)
        results = cursor.fetchall()
        return results
    except 
