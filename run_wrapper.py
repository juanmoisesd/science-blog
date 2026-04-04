import sys
import io
import builtins

# Fuerza UTF-8 en stdout/stderr
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Guarda la función original open()
original_open = builtins.open

# Crea una versión que fuerza UTF-8
def open_utf8(*args, **kwargs):
    # Si el modo es 'w' o 'r' y no tiene encoding especificado
    if len(args) >= 2 and isinstance(args[1], str) and 'b' not in args[1]:
        kwargs['encoding'] = 'utf-8'
        kwargs['errors'] = 'replace'
    return original_open(*args, **kwargs)

# Reemplaza la función global open()
builtins.open = open_utf8

# Ahora ejecuta el script
with open('site_builder.py', 'r', encoding='utf-8') as f:
    exec(f.read())
