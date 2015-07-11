from pypeg2 import parse
import parsing.parsing_simple as p
from simple.simple_expressions import Number

import sys
import io

# Load the source file
#
fn = sys.argv[1]
src = None
with open(fn, "r", encoding="utf-8") as f:
    src = f.read()

# Parse and compile the program
#
ast = parse(src, p.Program)
smpl = ast.to_simple()

# Execute the program
#
env = dict([
    ('phi', Number(0)),
    ('x0', Number(0)),
    ('x1', Number(4567)),
    ('x2', Number(7654)),
    ('i', Number(0)),
    ('limit', Number(24))])
env1 = dict(env)
env2 = smpl.evaluate(env1)

# Print the result
#
print("phi is approximately {0}".format(env2['phi']))
