with open('site_builder.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Reemplaza TODAS las líneas f.write(template.render(...)) 
# con f.write(template.render(...).encode('utf-8').decode('utf-8', errors='replace'))

import re

# Patrón: f.write(X.render(...))
pattern = r'f\.write\(([^)]+?\.render\([^)]*\))\)'
replacement = r'f.write(\1.encode("utf-8").decode("utf-8", errors="replace"))'

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('site_builder.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Todas las escrituras de plantillas ahora usan UTF-8')
