# lang-simple

This is experimental code for investigating [PEG parsing](https://en.wikipedia.org/wiki/Parsing_expression_grammar) and operational semantics. The *simple* language that is used as the target for the experiments is inspired by the SIMPLE language introduced in the second chapter of [Tom Stuart's book *Understanding Computation*](http://shop.oreilly.com/product/0636920025481.do).

## Dependencies

The primary code depends on the standard Python 3.4 library and upon [pyPEG2](https://pypi.python.org/pypi/pyPEG2/2.15.1).

## Development

lang-simple is written in Python, targeting Python 3.4 or later. The primary source code is in the `src/` folder and there are unit tests in the `tests/` folder.

There is a lint script, `lint.sh`, that is used to ensure the Python code follow PEP guidelines for style and usage. The lint output is reported in `src\fixme.lint.txt` and `tests\fixme.lint.txt`. If these files are empty after running the script, then no issues were detected.

### OS X

To run the linter:

~~~bash
$ ./lint.sh
~~~

### Windows 8.1

To run the linter:

~~~powershell
> .\lint.ps1
~~~

## Testing

To run the tests:

### OS X

~~~bash
$ ./test.sh
~~~

### Windows 8.1

To run the linter:

~~~powershell
> .\test.ps1
~~~

## Virtual Environment

Both the linter and test scripts check that a Python virtual environment is in place.

### OS X

On my OS X machine I setup the virtual environment as follows, starting from a Terminal window in the root of the project directory tree:

~~~bash
$ /opt/local/Library/Frameworks/Python.framework/Versions/3.4/bin/virtualenv venv34
$ . venv34/bin/activate
(venv34)$ pip install -U setuptools
(venv34)$ pip install -U pip
(venv34)$ pip install pyPEG2
~~~

To leave the virtual environment, I do this:

~~~bash
(venv34)$ deactivate
$
~~~

### Windows 8.1

On my Windows 8.1 machine I have ActiveState Python installed. I set up the viritual environment as follows, starting from a Powershell prompt in the root of the project directory tree:

~~~powershell
> c:\Python34\python -m venv venv34
> .\venv34\Scripts\Activate.ps1
(venv34)> pip install -U setuptools
(venv34)> pip install pyPEG2
~~~

To leave the virtual environment, I do this:

~~~powershell
(venv34)> deactivate
>
~~~

## Contributing

Similar to the contribution guidance from <https://github.com/github/markup>:

1. Fork it.
1. Create a branch (`git checkout -b my_lang-simple`)
1. Commit your changes (`git commit -am "Added some magics"`)
1. Push to the branch (`git push origin my_lang-simple`)
1. Open a [Pull Request](http://github.com/jenesuispasdave/lang-simple/pulls)
1. Enjoy a refreshing beverage and wait

## License and Copyright

lang-simple is licensed with the [Mozilla Public License Version 2.0][mpl].

Copyright 2015 Dave Hein

[mpl]: http://www.mozilla.org/MPL/2.0/
