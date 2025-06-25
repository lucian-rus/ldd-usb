# todo:
#   * handle input arguments
#   * check if sandbox exists, if not, create virtual env
#   * run requirements installation

source ./tools/sandbox/bin/active

# run python pre_build script
python tools/scripts/pre_build.py

cd ldd-usb
make 
cd ..

# run python post_build script
python tools/scripts/post_build.py
