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

# Check whether pyPEG2 is installed
#
$rcmd = "pip"
$rargs = "list 2>&1" -split " "
$piplist = & $rcmd $rargs
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

# Run the test
#
$env:PYTHONPATH="$pwd\src"
$rcmd = "python"
$rargs = "-m unittest discover -s ./tests/simple" -Split " "
& $rcmd $rargs
$rcmd = "python"
$rargs = "-m unittest discover -s ./tests/parsing" -Split " "
& $rcmd $rargs

# Get out
#
return True
