# Build the CLI tooling
WHEELHOUSE='wheelhouse_linux'

python setup.py bdist_wheel --plat-name=manylinux1_x86_64
cp dist/bigquery_python_utils-0.1-py3-none-manylinux1_x86_64.whl ${WHEELHOUSE}
rm -r dist
rm -r build
rm -r bigquery_python_utils.egg-info

# Gather the dependencies to allow install on servers that don't have access to the internet
pip download  --no-deps  --platform=manylinux_x86_64 --dest ${WHEELHOUSE} --no-cache -r requirements.txt
