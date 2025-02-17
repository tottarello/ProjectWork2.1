Descrizione

Quest script Python  utenti.py  genera 10 utenti fittizi utilizzando la libreria Faker e li esporta in un file Excel utilizzando la libreria openpyxl (https://openpyxl.readthedocs.io/en/stable/).
 
Segue poi lo script db.py utilizza la libreria sqlite3 per gestire il database SQL e openpyxl per leggere i dati dal file Excel.

Requisiti

Prima di eseguire lo script, assicurati di avere installate le seguenti dipendenze:

Python 3.x 
Faker
openpyxl (per la gestione dei file Excel)

Esecuzione

Eseguendo lo script Python: utenti.py verrà generato un file utenti.xlsx contenente i dati degli utenti fittizi.
Eseguendo lo script Python: db.py verrà generato un db utenti.db contenente i dati degli utenti fittizi presenti in utenti.xlsx.

Esempio

Sono allegati 2 file utenti.xlsx contente le inormazioni dei 10 utenti fittizzi generati dallo script utenti.py e un file utenti.db con una tabella popolata dal file precedentemente generato utenti.xlsx

Autore

Script sviluppato da Tiziano Carduci
