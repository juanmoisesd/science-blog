import re

with open('site_builder.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Reemplaza TODOS los with open con encoding='utf-8'
# Busca: with open(..., "w") as f:
# Busca: with open(..., "r") as f:
# Busca: with open(..., "a") as f:

# Primero, reemplaza con comillas dobles "w"
content = content.replace('with open(', 'with open(')

# Usa regex más específico
content = re.sub(
    r'with\s+open\(([^)]+?),\s*(["\'])([rwa])(["\'])\s*\)',
    lambda m: f'with open({m.group(1)}, "{m.group(3)}", encoding="utf-8")',
    content
)

with open('site_builder.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Archivo corregido correctamente')
