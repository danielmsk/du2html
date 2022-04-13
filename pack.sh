pip uninstall -y du2html
rm -rf build
rm -rf ./dist/*
python3 setup.py sdist bdist_wheel
pip install ./dist/du2html-0.0.4-py3-none-any.whl
# twine upload dist/*

# du2html -i ./test/du_20220411.txt -o test.html -t 37T
# du2html -i home2_20220413_1.txt