import urllib.request
from datetime import datetime

url = 'https://github.com'
try:
    response = urllib.request.urlopen(url, timeout=10)
    status = response.getcode()
    resultado = "en línea" if status == 200 else f"código {status}"
except Exception as e:
    resultado = f"error: {e}"

ahora = datetime.now()
fecha = ahora.strftime("%Y-%m-%d")
hora = ahora.strftime("%H:%M:%S")

with open("reporte.txt", "w") as f:
    f.write(f"Fecha: {fecha}\n")
    f.write(f"Hora: {hora}\n")
    f.write(f"Resultado: {resultado}\n")
