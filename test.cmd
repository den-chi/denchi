rd web\build /s /q
rd web\pages /s /q
rd web\static\img\content /s /q
xcopy content web\pages\ /s /e

cd web
c:\python27\python.exe app.py
@pause