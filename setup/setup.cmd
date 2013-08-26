cd source
python.msi /qn
cd ..

cd source/distribute
python setup.py install
cd ../..

cd source/werkzeug
python setup.py install
cd ../..

cd source/markupsafe
python setup.py install
cd ../..

cd source/jinja
python setup.py install
cd ../..

cd source/itsdangerous
python setup.py install
cd ../..

cd source/flask
python setup.py install
cd ../..

cd source/markdown
python setup.py install
cd ../..

cd source/pyyaml
python setup.py install
cd ../..

cd source/flask-flatPages
python setup.py install
cd ../..

cd source/frozen-flask
python setup.py install
cd ../..

@pause