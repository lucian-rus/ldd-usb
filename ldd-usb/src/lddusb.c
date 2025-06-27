#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/fs.h>

#include "lddusb.h"

/* if logger support is defined, import kernel logger*/
#if defined(LOGGER_ENABLED)
#include "kernel_logger.h"
#endif

static struct file_operations fops = {
    .owner = THIS_MODULE,
    .open = device_open,
    .release = device_release,
    .read = device_read,
    .write = device_write,
};

static int __init lddusb_init(void)
{
#if defined(LOGGER_ENABLED)
    LOG_WARN("got it");
#endif
    printk("lddusb: registered with major number %d\n", LDDUSB_MAJOR_NUM);
    return 0;
}

static void __exit lddusb_exit(void)
{
    // unregister_chrdev(LDDUSB_MAJOR_NUM, LDDUSB_DEVICE_NAME);
    printk("lddusb: unregistered\n");
}

module_init(lddusb_init);
module_exit(lddusb_exit);

static int device_open(struct inode *inode, struct file *file)
{
    printk("lddusb: device opened\n");
    return 0;
}

static int device_release(struct inode *inode, struct file *file)
{
    printk("lddusb: device closed\n");
    return 0;
}

static ssize_t device_read(struct file *filp, char __user *buffer, size_t length, loff_t *offset)
{
    printk("lddusb: read\n");
    return 0;
}

static ssize_t device_write(struct file *filp, const char __user *buffer, size_t length, loff_t *offset)
{
    printk("lddusb: write\n");
    return length;
}
