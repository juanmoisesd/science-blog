with open('site_builder.py', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Reemplaza with open(..., "w", encoding="utf-8") as f:
# Con: with open(..., "wb") as f: (modo binario)

# Y cada f.write(algo) se convierte a f.write(algo.encode('utf-8'))

# Primero, cambia todas las aperturas de archivo a modo binario
content = re.sub(
    r'with open\(([^)]+), "w", encoding="utf-8"\) as f:',
    r'with open(\1, "wb") as f:',
    content
)

# Luego, envuelve todos los f.write() con .encode('utf-8')
content = re.sub(
    r'f\.write\(([^)]+)\)',
    lambda m: f'f.write({m.group(1)}.encode("utf-8") if isinstance({m.group(1)}, str) else {m.group(1)})',
    content
)

with open('site_builder.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Modo binario activado para todas las escrituras')
