pip uninstall -y du2html
rm -rf build
rm -rf ./dist/*
python3 setup.py sdist bdist_wheel
pip install ./dist/du2html-0.0.6-py3-none-any.whl
# twine upload dist/*

# du2html -i ./test/du_20220413.txt -t 39997860216832
# du2html -i ./test/du_20220413.txt -t 39060410368K
# du2html -i ./test/du_20220413.txt -t 36.4T
# du2html -i ./test/du_20220413.txt