Nmap Netzwerkscanner
Python-Skripte zum Scannen lokaler Netzwerke mit python-nmap.
Erkennt aktive Hosts und zeigt den Status ausgewählter Ports an.

Projektstruktur
text
nmap-scanner/
├── import-nmap.py        # Einfacher Scan, Ausgabe in der Konsole
├── netzwerkscan-2.py     # Scan mit Log-Datei und Fehlerbehandlung
└── README.md
Voraussetzungen
Python 3.8+

Nmap installiert und im PATH verfügbar → https://nmap.org/download.html

Python-Bibliothek python-nmap

bash
pip install python-nmap
Skripte
import-nmap.py
Scannt einen Netzwerkbereich auf offene Ports und gibt die Ergebnisse in der Konsole aus.

bash
python import-nmap.py
Standardwerte:

Netzwerk: 192.168.1.0/24

Ports: 22, 80, 443

netzwerkscan-2.py
Zweistufiger Scan:

Host Discovery im Netzwerk (-sn)

Port-Scan auf jedem gefundenen Host

Ergebnisse werden in der Konsole angezeigt und in einer Log-Datei gespeichert.

bash
python netzwerkscan-2.py
Standardwerte:

Netzwerk: 192.168.178.0/24

Ports: 22, 80, 443

Logs: LogsNetzwerkscan/scan_YYYY-MM-DD.txt (wird automatisch erstellt)

Konfiguration
Am Anfang jedes Skripts können folgende Variablen angepasst werden:

Variable	Beschreibung	Beispiel
netzwerk	IP-Bereich (CIDR)	"10.0.0.0/24"
ports	Ports (kommagetrennt)	"21,22,80,443,3389"
logordner	Pfad für Log-Dateien	"C:\\Logs\\Scan"
Beispielausgabe
text
[2026-03-06 09:30:00] Starte Netzwerkscan auf 192.168.178.0/24 (Ports: 22,80,443)
🔎 3 aktive Geräte gefunden. Starte Port-Scan...

🟢 192.168.178.1 ist aktiv:
   └ Port 80/tcp → open
   └ Port 443/tcp → open

✅ Scan abgeschlossen.

Hinweis
Nur in Netzwerken verwenden, für die eine Genehmigung vorliegt.
Unautorisiertes Scannen fremder Netzwerke ist strafbar.
