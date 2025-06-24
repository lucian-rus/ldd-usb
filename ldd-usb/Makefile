obj-m += lddusb.o

SRC_DIR := src
INC_DIR := inc
KDIR := /lib/modules/$(shell uname -r)/build
PWD := $(shell pwd)

# Tell kbuild to look for source and headers in the right place
ccflags-y := -I$(PWD)/$(INC_DIR)

# Build rule for the object file from the src directory
lddusb-objs := $(SRC_DIR)/lddusb.o

all:
	make -C $(KDIR) M=$(PWD) modules

clean:
	make -C $(KDIR) M=$(PWD) clean