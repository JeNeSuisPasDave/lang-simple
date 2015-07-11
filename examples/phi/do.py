from pypeg2 import parse
import parsing.parsing_simple as p

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
env = dict([])
env2 = smpl.evaluate(env)

# Print the result
#
print("phi is approximately {0}".format(env2['phi']))
