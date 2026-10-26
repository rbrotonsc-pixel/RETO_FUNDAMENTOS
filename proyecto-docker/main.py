import os
import psycopg

url = os.getenv("DATABASE_URL")

try:
    with psycopg.connect(url) as connection:
        print("Conectado")
        with connection.cursor() as cur:
            #Crear Tabla
            cur.execute("CREATE TABLE IF NOT EXISTS characters (" \
            "               id              INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY, " \
            "               name            TEXT NOT NULL, " \
            "               status          TEXT, " \
            "               species         TEXT, " \
            "               type            TEXT, " \
            "               gender          TEXT, " \
            "               origin_name     TEXT, " \
            "               location_name   TEXT, " \
            "               image           TEXT, " \
            "               url             TEXT, " \
            "               created         TIMESTAMPTZ);")

            insert_query= """
                INSERT INTO characters (
                    name, status, species, type, gender, 
                    origin_name, location_name, image, url, created
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s); """
            
            characters_data = [
                (
                    "Rick Sanchez",
                    "Alive",
                    "Human",
                    "",
                    "Male",
                    "Earth (C-137)",
                    "Citadel of Ricks",
                    "https://rickandmortyapi.com/api/character/avatar/1.jpeg",
                    "https://rickandmortyapi.com/api/character/1",
                    "2017-11-04T18:48:46.250Z"
                ),
                (
                    "Morty Smith",
                    "Alive",
                    "Human",
                    "",
                    "Male",
                    "unknown",
                    "Citadel of Ricks",
                    "https://rickandmortyapi.com/api/character/avatar/2.jpeg",
                    "https://rickandmortyapi.com/api/character/2",
                    "2017-11-04T18:50:21.651Z"
                ),
                (
                    "Summer Smith",
                    "Alive",
                    "Human",
                    "",
                    "Female",
                    "Earth (Replacement Dimension)",
                    "Earth (Replacement Dimension)",
                    "https://rickandmortyapi.com/api/character/avatar/3.jpeg",
                    "https://rickandmortyapi.com/api/character/3",
                    "2017-11-04T19:09:56.428Z"
                ),
                (
                    "Birdperson",
                    "Dead",
                    "Alien",
                    "Bird-Person",
                    "Male",
                    "Bird World",
                    "Planet Squanch",
                    "https://rickandmortyapi.com/api/character/avatar/47.jpeg",
                    "https://rickandmortyapi.com/api/character/47",
                    "2017-11-05T10:48:44.584Z"
                ),
                (
                    "Mr. Meeseeks",
                    "unknown",
                    "Humanoid",
                    "Meeseeks",
                    "Male",
                    "Mr. Meeseeks Box",
                    "Earth (Replacement Dimension)",
                    "https://rickandmortyapi.com/api/character/avatar/242.jpeg",
                    "https://rickandmortyapi.com/api/character/242",
                    "2017-12-30T17:32:47.452Z"
                )
            ]
            
            cur.executemany(insert_query, characters_data)
            connection.commit()
            cur.execute("SELECT id, name, species FROM characters LIMIT 10")
            filas = cur.fetchall()
            for fila in filas:
                print(fila[0], fila[1])
        
except:
    print("Error de conexión")



# with connection.cursor() as cur:
#     cur.execute(insert_query)

# #Comprobar Tabla
# cur.execute("SELECT id, name, species FROM characters LIMIT 10")
# filas = cur.fetchall()
# for fila in filas:
#     print(fila[0], fila[1])



