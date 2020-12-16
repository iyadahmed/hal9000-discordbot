import sys
import pip
from RestrictedPython import compile_restricted
from RestrictedPython import safe_globals

source_code = sys.argv[1]

byte_code = compile_restricted(source_code, '<inline>', 'exec')
exec(byte_code, safe_globals, {})
