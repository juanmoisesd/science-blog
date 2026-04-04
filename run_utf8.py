import sys
import io

# Fuerza UTF-8 en stdout/stderr
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if sys.stderr.encoding != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Abre el archivo con encoding UTF-8 explícito
with open('site_builder.py', 'r', encoding='utf-8') as f:
    exec(f.read())
