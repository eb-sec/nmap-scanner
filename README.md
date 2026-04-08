# Nmap Network Scanner

Python scripts for scanning local networks using python-nmap.
Detects active hosts and displays the status of selected ports.

---

## Project Structure

```
nmap-scanner/
├── import-nmap.py        # Simple scan with console output
├── netzwerkscan-2.py     # Scan with log file and error handling
└── README.md
```

---

## Requirements

- Python 3.8+
- Nmap installed and available in PATH → https://nmap.org/download.html
- Python library `python-nmap`

```bash
pip install python-nmap
```

---

## Scripts

### import-nmap.py

Scans a network range for open ports and prints the results to the console.

```bash
python import-nmap.py
```

**Defaults:**
- Network: `192.168.1.0/24`
- Ports: `22, 80, 443`

---

### netzwerkscan-2.py

Two-stage scan:
1. Host discovery across the network (`-sn`)
2. Port scan on each discovered host

Results are printed to the console and saved to a log file.

```bash
python netzwerkscan-2.py
```

**Defaults:**
- Network: `192.168.178.0/24`
- Ports: `22, 80, 443`
- Logs: `LogsNetzwerkscan/scan_YYYY-MM-DD.txt` (created automatically)

---

## Configuration

The following variables can be adjusted at the top of each script:

| Variable | Description | Example |
|---|---|---|
| `netzwerk` | IP range (CIDR) | `"10.0.0.0/24"` |
| `ports` | Ports (comma-separated) | `"21,22,80,443,3389"` |
| `logordner` | Path for log files | `"C:\\Logs\\Scan"` |

---

## Sample Output

```
[2026-03-06 09:30:00] Starting network scan on 192.168.178.0/24 (Ports: 22,80,443)
🔎 3 active devices found. Starting port scan...
🟢 192.168.178.1 is active:
   └ Port 80/tcp → open
   └ Port 443/tcp → open
✅ Scan complete.
```

---

## Legal Notice

Only use this tool on networks you are authorized to scan.
Unauthorized scanning of third-party networks is illegal.
