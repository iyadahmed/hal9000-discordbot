import sys

from RestrictedPython import compile_restricted

from RestrictedPython import safe_builtins

from RestrictedPython.PrintCollector import PrintCollector

_print_ = PrintCollector
_getattr_ = getattr

source_code = sys.argv[1]
source_code = source_code + "\nresult=printed"
byte_code = compile_restricted(
source_code,
filename='<string>',
mode='exec'
)
exec(byte_code)
print(result)
