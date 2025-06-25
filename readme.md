# LDD-USB
simple LDD project to better understand how to develop ldds

> because building LDDs requires make, the build system will be implemented in python. once finished, this will be ported to the `build_pf` repo and imported as a proper submodule 

### Altering the behaviour 
the behaviour of the build script can be altered via `config.json` and the pre-build and post-build python scripts which are found in the `tools/scripts` directory
* pre_build_create_dirs -> files to be created in the pre-build process
* output_cleaner_exceptions -> specifies which files are omitted from the post-build clean process
* output_mover_exceptions -> specifies which files are omitted from the move process 
* output_mover_target_dir -> where to put the generated files

> names are subject to change