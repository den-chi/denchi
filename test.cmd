rd web\build /s /q
rd web\pages /s /q
rd web\static\img\upload /s /q
mkdir web\pages
xcopy content web\pages\ /s /e
xcopy content\image web\static\img\upload\ /s /e
rd web\pages\image /s /q

cd web
start c:\python27\python.exe app.py
start http://127.0.0.1:5000