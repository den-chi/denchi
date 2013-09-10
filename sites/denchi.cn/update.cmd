@echo off

echo ���������ʱ���ļ�...
if exist web\build\.git\index.lock del web\build\.git\index.lock /s/q > nul
if exist web\pages rd web\pages /s /q > nul
if exist web\static\img\upload rd web\static\img\upload /s /q > nul
mkdir web\pages
xcopy content web\pages\ /s /e > nul
xcopy content\image web\static\img\upload\ /s /e > nul
rd web\pages\image /s /q > nul

set PATH=../../git/bin;%PATH%
set PATH=../../../../git/bin;%PATH%
echo ����ͬ�����°汾���ļ�...
if exist web\build (
    cd web\build
    git reset --hard
    git pull origin master
    cd ..\..
) else (
    git config --global user.email "den-chi@qq.com"
    git config --global user.name "denchi"
    git clone https://github.com/den-chi/den-chi.github.io.git web/build
)

if not exist web\build (
    echo �����������ʧ���ˣ�����д��ʲô�أ����ͼ����user@ufoym.com�ɣ�
    @pause
    exit
)

cd web\build
del * /q
for /d %%d in (*) do (
    rd /q/s "%%~d"
)
cd ..\..

c:\python27\python.exe web/freeze.py

cd web/build
echo denchi.cn > CNAME
set PATH=../../../../git/bin;%PATH%
git add --all .
git commit -m "update website"
echo �������ûʲô���⣬��ô����������den-chi��Ȼ����������Ӧ������
git push origin master
@pause