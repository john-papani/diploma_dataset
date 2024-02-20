import sqlite3
import json
import csv


def export_table_as_json_and_csv(database_path, table_name, json_file_path, csv_file_path):

    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    try:
        # Fetch all rows from the specified table
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        # Get the column names from the table
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [column[1] for column in cursor.fetchall()]

        # Convert the data to a list of dictionaries
        data = [dict(zip(columns, row)) for row in rows]

        # Export data as JSON
        with open(json_file_path, 'w', encoding="utf8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

        print(f"Exported {table_name} data to {json_file_path}")

        # Export data as CSV
        with open(csv_file_path, 'w', newline='',encoding="utf8") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=columns)
            csv_writer.writeheader()
            csv_writer.writerows(data)

        print(f"Exported {table_name} data to {csv_file_path}")

    except sqlite3.Error as e:
        print(f"Error reading data from {table_name}: {e}")

    finally:
        # Close the database connection
        conn.close()


db_path = "../raw_text_data/my_harvester_last.db"
db_table = "debates"
csv_file_path = "./praktikaVoulis.csv"
json_file_path = "./praktikaVoulis.json"
export_table_as_json_and_csv(db_path, db_table, json_file_path, csv_file_path)
