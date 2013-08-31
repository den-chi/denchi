cd source
python.msi /qn
cd ..

cd source/distribute
c:/python27/python setup.py install
cd ../..

cd source/werkzeug
c:/python27/python setup.py install
cd ../..

cd source/markupsafe
c:/python27/python setup.py install
cd ../..

cd source/jinja
c:/python27/python setup.py install
cd ../..

cd source/itsdangerous
c:/python27/python setup.py install
cd ../..

cd source/flask
c:/python27/python setup.py install
cd ../..

cd source/markdown
c:/python27/python setup.py install
cd ../..

cd source/pyyaml
c:/python27/python setup.py install
cd ../..

cd source/flask-flatPages
c:/python27/python setup.py install
cd ../..

cd source/frozen-flask
c:/python27/python setup.py install
cd ../..

@pause