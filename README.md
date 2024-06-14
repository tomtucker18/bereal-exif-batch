# BeReal Exif Batch

Dieses Script wird gebraucht um das Aufnahmedatum des jeweiligen BeReals in die Exif Daten zu schreiben. Das Datum wird automatischaus dem Dateinamen herausgelesen. Für die Uhrzeit wird immer 12:00 verwendet, da die Zeit beim Export aus der App nicht angegeben wird.

## Usage

1. `pip install -r requirements.txt`
2. Alle BeReals mit Hilfe der Autoklicker App exportieren und in den **photos** Ordner kopieren.
3. main.py ausführen

Nun sollten alle Bilder das korrekte Aufnahmedatum haben.