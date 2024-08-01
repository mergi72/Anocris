if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit
    python C:\Users\merhautr\python_projects\Anocris\batch_anocris.py
    start C:\Windows\System32\scrnsave.scr /s
exit