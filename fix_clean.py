import re

with open('site_builder.py', 'r', encoding='utf-8') as f:
    content = f.read()

# SOLO reemplaza 'with open(..., "w")' CON 'with open(..., "w", encoding="utf-8")'
# SIN tocar f.write()

content = re.sub(
    r'with\s+open\(([^)]+?),\s*["\']w["\']\s*\)',
    r'with open(\1, "w", encoding="utf-8")',
    content
)

content = re.sub(
    r'with\s+open\(([^)]+?),\s*["\']r["\']\s*\)',
    r'with open(\1, "r", encoding="utf-8")',
    content
)

with open('site_builder.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Fixes aplicados correctamente')
