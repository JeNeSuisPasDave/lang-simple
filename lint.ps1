# Capture the file name of this powershell script
#
$SCRIPTNAME_ = $MyInvocation.InvocationName

# Check whether we are running in a python virtual environment
#
$VENV_RUNNING_ = Get-ChildItem env: | Where-Object {($_.Name -eq "VIRTUAL_ENV")}
If ($VENV_RUNNING_ -eq $null)
{
  echo "ERROR: Python virtual environment not running"
  echo ""
  echo "Try 'venv34\Scripts\Activate.ps1' to start the virtual environment, and"
  echo "then try '$SCRIPTNAME_' again."
  echo ""
  return False
}
$n = $VENV_RUNNING_.Name
$v = $VENV_RUNNING_.Value

# Check whether we are running Python 3.4
#
$rcmd = "python"
$rargs = "--version 2>&1" -split " "
$vsn = & $rcmd $rargs
if ($vsn -NotLike "Python 3.*")
{
  echo "ERROR: Python 3.4 or later is required. Found '$vsn'."
  echo ""
  echo "Deactivate the current virtual environment."
  echo "Try 'venv34\Scripts\Activate.ps1' to start the virtual environment, and"
  echo "then try '$SCRIPTNAME_' again."
  echo ""
  return False
}

# Check whether flake8 is installed
#
$rcmd = "pip"
$rargs = "list 2>&1" -split " "
$piplist = & $rcmd $rargs
$FLAKE8_INSTALLED_ = $piplist | Where-Object {($_ -Like "flake8 (*")}
If ($FLAKE8_INSTALLED_ -eq $null)
{
  echo "ERROR: flake8 is not installed"
  echo ""
  echo "Try 'pip install flake8' to install flake8, and"
  echo "then try '$SCRIPTNAME_' again."
  echo ""
  return False
}

# Check whether pep8-naming is installed
#
$PEP8NAMING_INSTALLED_ = $piplist | Where-Object {($_ -Like "pep8-naming (*")}
If ($PEP8NAMING_INSTALLED_ -eq $null)
{
  echo "ERROR: pep8-naming is not installed"
  echo ""
  echo "Try 'pip install pep8-naming' to install pep8-naming, and"
  echo "then try '$SCRIPTNAME_' again."
  echo ""
  return False
}

# Check whether pep257 is installed
#
$PEP257_INSTALLED_ = $piplist | Where-Object {($_ -Like "pep257 (*")}
If ($PEP257_INSTALLED_ -eq $null)
{
  echo "ERROR: pep257 is not installed"
  echo ""
  echo "Try 'pip install pep257' to install pep257, and"
  echo "then try '$SCRIPTNAME_' again."
  echo ""
  return False
}

# Check whether pyPEG2 is installed
#
$PYPEG2_INSTALLED_ = $piplist | Where-Object {($_ -Like "pyPEG2 (*")}
If ($PYPEG2_INSTALLED_ -eq $null)
{
  echo "ERROR: pyPEG2 is not installed"
  echo ""
  echo "Try 'pip install pyPEG2' to install pyPEG2, and"
  echo "then try '$SCRIPTNAME_' again."
  echo ""
  return False
}

# lint the source
#
$env:PYTHONPATH="$pwd\src"
#
cd src
$rcmd = "flake8"
$rargs = "--max-complexity=10 ." -split " "
& $rcmd $rargs | Out-File fixme.lint.txt 2>&1
$rcmd = "python"
$rargs = "..\run_pep257.py --match='(?!ez_setup).*\.py' ." -split " "
& $rcmd $rargs | Out-File -Append fixme.lint.txt 2>&1
cd ..
#
cd tests
$rcmd = "flake8"
$rargs = "--max-complexity=10 ." -split " "
& $rcmd $rargs | Out-File fixme.lint.txt 2>&1
$rcmd = "python"
$rargs = "..\run_pep257.py --match='.*\.py' ." -split " "
& $rcmd $rargs | Out-File -Append fixme.lint.txt 2>&1
cd ..

# Get out
#
return True
