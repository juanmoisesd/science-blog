import sys
import io

# Antes de nada, configura stdout/stderr
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Ahora carga y ejecuta el script original
with open('site_builder.py', 'r', encoding='utf-8') as f:
    script_content = f.read()

# Reemplaza todas las aperturas de archivo para forzar UTF-8 en MODO BINARIO
import re

# Cambiar: with io.open(..., "w", encoding="utf-8") as f:
# A: with io.open(..., "wb") as f:
script_content = re.sub(
    r'with io\.open\(([^)]+), "w", encoding="utf-8"\)',
    r'with io.open(\1, "wb")',
    script_content
)

# Luego cada f.write(texto) se convierte a f.write(texto.encode('utf-8'))
script_content = re.sub(
    r'(\s+)f\.write\(([^)]+)\)',
    r'\1f.write(\2.encode("utf-8") if isinstance(\2, str) else \2)',
    script_content
)

# Ejecuta el script modificado
exec(script_content)
