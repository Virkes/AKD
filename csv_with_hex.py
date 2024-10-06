import csv
import os
from datetime import datetime
from pandas import to_datetime

def load_csv_path():
    path = input("Unesite putanju do CSV datoteke: ")
    if os.path.exists(path):
        return path
    else:
        print("Datoteka ne postoji na zadanoj putanji. Pokušajte ponovo.")
        return load_csv_path()


path = load_csv_path()

data = []

with open(path, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        first_name = row['Ime'].upper()
        last_name = row['Prezime'].upper()

        birthdate = to_datetime(row['Datum rodjenja']).strftime('%d-%m-%Y')
        
        # try:
        #     datetime.strptime(birthdate, "%d-%m-%Y")
        # except ValueError:
        #     print(f"Format datuma za {first_name} {last_name}: {birthdate} nije validan. Očekivan format: DD-MM-YYYY.")
        #     continue
        
        first_name_hex = first_name.encode('utf-8').hex()
        last_name_hex = last_name.encode('utf-8').hex()
        birthdate_hex = birthdate.encode('utf-8').hex()
        
        print(f"Ime: {first_name}, Prezime: {last_name}, Datum rodjenja: {birthdate}")
        print(f"Ime (hex): {first_name_hex}, Prezime (hex): {last_name_hex}, Datum rodjenja (hex): {birthdate_hex}")
        print("-" * 50)
        
        data.append({
            'Ime': first_name, 'Prezime': last_name, 'Datum rodjenja': birthdate,
            'Ime (hex)': first_name_hex, 'Prezime (hex)': last_name_hex, 'Datum rodjenja (hex)': birthdate_hex
        })

parent = os.path.dirname(path)
new_file_path = os.path.join(parent, "formatted_data.csv")
with open(new_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Ime', 'Prezime', 'Datum rodjenja', 'Ime (hex)', 'Prezime (hex)', 'Datum rodjenja (hex)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(data)

print(f"The formatted data has been saved to: {new_file_path}")