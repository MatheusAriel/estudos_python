import subprocess
from timeit import timeit

# WINDOWS - ping ip
# LINUS - ping ip -c 4


proc = subprocess.run([
    'ping',
    '127.0.0.1',
], capture_output=True, text=True)

# print(proc.stdout)

# print('\n\n')
# print(proc.stderr)
# print(proc.returncode)
# print(proc.args)
