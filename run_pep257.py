"""This is a shim to access pep257.

Windows only.

Under ActiveState Pytyon 3.4.10, when pep257 installs (via pip)
it doesn't lay down an exe, but rather a shell script. But that
file has no extension and is a bit suspect. I created this file
to do something similar, but more reliable w.r.t the lint.ps1
script.

"""

from pep257 import main

if __name__ == '__main__':
    main()
