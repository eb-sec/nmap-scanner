import nmap
import datetime
import os

# Netzbereich & Ports definieren
netzwerk = "192.168.178.0/24"
ports = "22,80,443"


# 📁 Log-Datei vorbereiten
datum = datetime.datetime.now().strftime("%Y-%m-%d")
zeit = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
logordner = r"Your\Logordner"
os.makedirs(logordner, exist_ok=True)
logpfad = os.path.join(logordner, f"scan_{datum}.txt")

# 📝 Einstieg in Log schreiben
with open(logpfad, "a", encoding="utf-8") as logfile:
    logfile.write(f"[{zeit}] Starte Netzwerkscan auf {netzwerk} (Ports: {ports})\n")

scanner = nmap.PortScanner()

try:
    # 🔍 Schritt 1: Aktive Hosts finden
    scanner.scan(hosts=netzwerk, arguments="-sn")
    aktive_hosts = [host for host in scanner.all_hosts() if scanner[host].state() == "up"]

    if not aktive_hosts:
        print("ℹ️  Keine aktiven Geräte gefunden.")
        with open(logpfad, "a", encoding="utf-8") as logfile:
            logfile.write("Keine aktiven Geräte gefunden.\n\n")
    else:
        print(f"🔎 {len(aktive_hosts)} aktive Geräte gefunden. Starte Port-Scan...\n")
        with open(logpfad, "a", encoding="utf-8") as logfile:
            logfile.write(f" {len(aktive_hosts)} aktive Geräte gefunden. Starte Port-Scan...\n")

        # 🚪 Schritt 2: Ports auf jedem Host scannen
        for host in aktive_hosts:
            scanner.scan(hosts=host, arguments=f"-p {ports} --open -Pn")
            print(f"🟢 {host} ist aktiv:")
            with open(logpfad, "a", encoding="utf-8") as logfile:
                logfile.write(f"🟢 {host} ist aktiv:\n")
                for proto in scanner[host].all_protocols():
                    for port in sorted(scanner[host][proto].keys()):
                        status = scanner[host][proto][port]['state']
                        zeile = f"   └ Port {port}/{proto} → {status}\n"
                        print(zeile.strip())
                        logfile.write(zeile)

        print("\n✅ Scan abgeschlossen.")
        with open(logpfad, "a", encoding="utf-8") as logfile:
            logfile.write("✅ Scan abgeschlossen.\n\n")

except Exception as e:
    fehlermeldung = f"❌ Fehler beim Scan: {e}\n"
    print(fehlermeldung.strip())
    with open(logpfad, "a", encoding="utf-8") as logfile:
        logfile.write(fehlermeldung)


