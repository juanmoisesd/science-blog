import re

with open('site_builder.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Reemplaza todos los 'with open(' para incluir encoding='utf-8'
content = re.sub(r'with open\(([^,]+), "[wa]"\)', r'with open(\1, "w", encoding="utf-8")', content)
content = re.sub(r'with open\(([^,]+), "[ra]"\)', r'with open(\1, "r", encoding="utf-8")', content)

with open('site_builder.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Archivo corregido con encoding UTF-8')
