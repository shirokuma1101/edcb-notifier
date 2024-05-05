@ECHO OFF
CHCP 65001 > NUL

REM // Hide the command prompt window
REM _EDCBX_HIDE_

REM // Pass parameters to environment variables
REM _EDCBX_DIRECT_

REM // If you have booked a viewing, it is not executed
if "%RecMode%" == "4" (
  goto :eof
)

REM // Execute edcb-notifier.py
CD %~dp0\edcb-notifier
.\python-3.9.13-embed-amd64\python.exe .\edcb-notifier.py --PostRecStart

exit
