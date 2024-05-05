@ECHO OFF
CHCP 65001 > NUL

REM // ウインドウを非表示にする
REM _EDCBX_HIDE_

REM // パラメータを環境変数に渡す
REM _EDCBX_DIRECT_

REM // 視聴予約なら終了
if "%RecMode%" == "4" (
  goto :eof
)

REM // edcb-notifier.py を実行
CD %~dp0\edcb-notifier
.\python-3.9.13-embed-amd64\python.exe .\edcb-notifier.py --PostAddReserve

exit
