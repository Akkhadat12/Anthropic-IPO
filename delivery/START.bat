@echo off
setlocal DisableDelayedExpansion
cd /d "%~dp0"
if errorlevel 1 goto bad_folder
py -3 -I -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)" >nul 2>&1
if not errorlevel 1 goto use_py
python -I -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)" >nul 2>&1
if not errorlevel 1 goto use_python
python3 -I -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)" >nul 2>&1
if not errorlevel 1 goto use_python3
echo Python 3.10 or newer was not found.
echo Install Python once from https://www.python.org/downloads/windows/
echo Enable the Python launcher or add Python to PATH during installation.
echo Then reopen START.bat. See README_TH.md for Thai instructions.
pause
exit /b 2
:use_py
py -3 -I "%~dp0serve.py" start
goto result
:use_python
python -I "%~dp0serve.py" start
goto result
:use_python3
python3 -I "%~dp0serve.py" start
:result
set "RESULT=%ERRORLEVEL%"
if not "%RESULT%"=="0" pause
exit /b %RESULT%
:bad_folder
echo Could not open the package folder. Extract the ZIP to a writable local folder.
pause
exit /b 2
