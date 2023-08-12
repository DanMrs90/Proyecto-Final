# %%
import csv
# %%
import sqlite3
# %%
import sqlite3
import csv

def create_temp_table():
    conn = sqlite3.connect("temperaturasGto.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS temperaturas(
                   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                   dia INTEGER NOT NULL,
                   temp_maxima INTEGER NOT NULL,
                   temp_min INTEGER NOT NULL,
                   temp_promedio INTEGER NOT NULL
                   )
                   """)
    
    conn.commit()
    conn.close()


# %%
def read_csv_file(csv_file):
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def insert_into_temp_table(data):
    conn = sqlite3.connect("temperaturasGto.db")
    cursor = conn.cursor()

    for row in data:
        cursor.execute("""
            INSERT INTO temperaturas(dia,temp_maxima,temp_min,temp_promedio)
            VALUES (?,?,?,?)
        """, (int(row["Dias"]), int(row["Temperaturas Maxima"]), int(row["Temperaturas Minima"]),int(row["Temperatura media  dia"])))

    conn.commit()
    conn.close()

# %%
if __name__ == "__main__":
    csv_file = "temperaturas_AGOSTO.csv"
    data_to_insert = read_csv_file(csv_file)
    insert_into_temp_table(data_to_insert)

# %%
if __name__ == "__main__":
    create_temp_table()
# %%