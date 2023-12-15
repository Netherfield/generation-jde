## Create project:
### upgrade pip
py -m pip install --upgrade pip

### we need a build backend
we use setuptools

### build
in the src/_myproject_ directory (or where pyproject.toml is located) run:
py -m build

### upload to TestPyPi through Twine
run inside the project folder:
py -m twine upload --repository testpypi dist/*


### to install
py -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-YOUR-USERNAME-H
