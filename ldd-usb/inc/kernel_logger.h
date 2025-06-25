#ifndef KERNEL_LOGGER_H
#define KERNEL_LOGGER_H

#define LOG_INFO(str)       printk(KERN_INFO str)
#define LOG_WARN(str)       printk(KERN_WARNING str)
#define LOG_ERROR(str)      printk(KERN_ERR str)

#endif