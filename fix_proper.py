import re

with open('site_builder.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # Si la línea contiene f.write( y NO está ya codificada
    if 'f.write(' in line and '.encode(' not in line:
        # Busca el patrón: f.write(ALGO)
        # Lo reemplaza con: f.write(str(ALGO).encode('utf-8'))
        line = re.sub(r'f\.write\((.+?)\)$', r'f.write(str(\1).encode("utf-8"))', line)

    new_lines.append(line)

with open('site_builder.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('✅ Script reparado correctamente')
