rd web\build /s /q
rd web\pages /s /q
rd web\static\img\content /s /q
xcopy content web\pages\ /s /e

set PATH=git/bin;%PATH%
git config --global user.email "den-chi@qq.com"
git config --global user.name "denchi"
git clone https://github.com/den-chi/den-chi.github.io.git web/build

c:\python27\python.exe web/freeze.py

cd web/build
set PATH=../../git/bin;%PATH%
git add --all .
git commit -m "update website"
git push origin master
@pause