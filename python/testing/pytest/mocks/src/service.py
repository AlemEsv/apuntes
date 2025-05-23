# SERVICIO: base de datos que almacena usuarios por sus ID

# dictionary
database = {
    1: "Alice",
    2: "Antony",
    3: "Maria"
}

# creacion de un DUMMY
# solo se observa la firma del método
def get_user_from_db(user_id):
    return database.get(user_id)