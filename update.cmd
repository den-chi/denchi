rd web\build /s /q
rd web\pages /s /q
rd web\static\img\upload /s /q
mkdir web\pages
xcopy content web\pages\ /s /e
xcopy content\image web\static\img\upload\ /s /e
rd web\pages\image /s /q

set PATH=git/bin;%PATH%
git config user.email "den-chi@qq.com"
git config user.name "denchi"
git clone https://github.com/den-chi/den-chi.github.io.git web/build

cd web\build
del * /q
for /d %%d in (*) do (
    rd /q/s "%%~d"
)
cd ..\..

c:\python27\python.exe web/freeze.py

cd web/build
echo denchi.cn > CNAME
set PATH=../../git/bin;%PATH%
git add --all .
git commit -m "update website"
git push origin master
@pause