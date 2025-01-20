from openpyxl import Workbook
from faker import Faker

try:
    # Creazione del generatore di dati
    fake = Faker()

    try:
        # Creazione di un nuovo workbook
        wb = Workbook()
        ws = wb.active
        ws.title = "Utenti"

        # Aggiunta delle intestazioni
        ws.append(["Nome", "Cognome", "Email", "Numero di Telefono"])

        try:
            # Generazione di 10 utenti fittizi
            for _ in range(10):
                nome = fake.first_name()
                cognome = fake.last_name()
                email = fake.email()
                telefono = fake.phone_number()
                ws.append([nome, cognome, email, telefono])

            try:
                # Salvataggio del file Excel
                wb.save("utenti.xlsx")
                print("File Excel 'utenti.xlsx' salvato con successo.")
            except Exception as e:
                print("Errore durante il salvataggio del file: " + str(e))

        except Exception as e:
            print("Errore durante la generazione dei dati: " + str(e))

    except Exception as e:
        print("Errore durante la creazione del workbook: " + str(e))

except Exception as e:
    print("Errore iniziale: " + str(e))
