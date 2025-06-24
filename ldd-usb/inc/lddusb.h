#ifndef SIMPLE_DRIVER_H
#define SIMPLE_DRIVER_H

#include <linux/fs.h>

/* LINUX KERNEL macros */
MODULE_LICENSE("GPL");
MODULE_AUTHOR("name");
MODULE_DESCRIPTION("lddusb driver template");

/* generic defines */

#define DEVICE_NAME "lddusb"
#define MAJOR_NUM 240

// Function prototypes
static int device_open(struct inode *inode, struct file *file);
static int device_release(struct inode *inode, struct file *file);
static ssize_t device_read(struct file *filp, char __user *buffer, size_t length, loff_t *offset);
static ssize_t device_write(struct file *filp, const char __user *buffer, size_t length, loff_t *offset);

#endif // SIMPLE_DRIVER_H