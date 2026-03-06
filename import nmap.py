import nmap
import datetime

# Netzbereich & Ports definieren
netzwerk = "192.168.1.0/24"   # Passe diesen Bereich ggf. an dein Netzwerk an
ports = "22,80,443"           # Standardports: SSH, HTTP, HTTPS

# Zeitstempel
zeit = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"[{zeit}] Starte Netzwerkscan auf {netzwerk} (Ports: {ports})\n")

# Scanner initialisieren
scanner = nmap.PortScanner()

# Scan starten
scanner.scan(hosts=netzwerk, arguments=f"-p {ports} --open")

# Ergebnisse verarbeiten
for host in scanner.all_hosts():
    if scanner[host].state() == "up":
        print(f"🟢 {host} ist aktiv:")
        for proto in scanner[host].all_protocols():
            portliste = scanner[host][proto].keys()
            for port in sorted(portliste):
                status = scanner[host][proto][port]['state']
                print(f"   └ Port {port}/{proto} → {status}")
print("\n✅ Scan abgeschlossen.")
