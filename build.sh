# run python pre_build script
python3 tools/scripts/pre_build.py

cd ldd-usb
make 
cd ..

# run python post_build script
python3 tools/scripts/post_build.py