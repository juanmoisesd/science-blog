import re

with open('site_builder.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Encuentra la línea donde se escribe con la plantilla y asegúrate que sea UTF-8
# Busca: f.write(root_template.render(...))
# y cámbiala a: f.write(root_template.render(...).encode('utf-8').decode('utf-8'))

# Mejor aún: cambia la apertura de archivo para usar io.open
content = content.replace(
    'with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:',
    'import io\nwith io.open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:'
)

# Agrega import io al inicio del archivo si no existe
if 'import io' not in content:
    content = content.replace('import time', 'import time\nimport io')

with open('site_builder.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Site builder actualizado con io.open')
