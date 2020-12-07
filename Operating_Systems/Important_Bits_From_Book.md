# Chapter 1
* Why Study Operating Systems?

Although there are many practitioners of computer science, only a small 
percentage of them will be involved in the creation or modification of an 
operating system. Why, then, study operating systems and how they work? 
Simply because, as almost all code runs on top of an operating system, 
knowledge of how operating systems work is crucial to proper, efficient, 
effective, and secure programming. Understanding the fundamentals of operating systems,
how they drive computer hardware, and what they provide to 
applications is not only essential to those who program them but also highly
useful to those who write programs on them and use them.

* Storage Definitions and Notation

The basic unit of computer storage is the bit. A bit can contain one of two
values, 0 and 1. All other storage in a computer is based on collections of bits.
Given enough bits, it is amazing how many things a computer can represent:
numbers, letters, images, movies, sounds, documents, and programs, to name
a few. A byte is 8 bits, and on most computers it is the smallest convenient
chunk of storage. For example, most computers don’t have an instruction to
move a bit but do have one to move a byte. A less common term is word,
which is a given computer architecture’s native unit of data. A word is made
up of one or more bytes. For example, a computer that has 64-bit registers and
64-bit memory addressing typically has 64-bit (8-byte) words. A computer
executes many operations in its native word size rather than a byte at a time.
Computer storage, along with most computer throughput, is generally
measured and manipulated in bytes and collections of bytes. A kilobyte, or
KB, is 1,024 bytes; a megabyte, or MB, is 1,0242 bytes; a gigabyte, or GB, is
1,0243 bytes; a terabyte, or TB, is 1,0244 bytes; and a petabyte, or PB, is 1,0245
bytes. Computer manufacturers often round off these numbers and say that
a megabyte is 1 million bytes and a gigabyte is 1 billion bytes. Networking
measurements are an exception to this general rule; they are given in bits
(because networks move data a bit at a time).

* Definitions of Computer System Components

CPU—The hardware that executes instructions.

Processor—A physical chip that contains one or more CPUs.

Core—The basic computation unit of the CPU.

Multicore— Including multiple computing cores on the same CPU.

Multiprocessor— Including multiple processors.

Although virtually all systems are now multicore, we use the general term
CPU when referring to a single computational unit of a computer system and
core as well as multicore when specifically referring to one or more cores on
a CPU.

* PC Motherboard

Consider the desktop PC motherboard with a processor socket shown below:

![PC Motherboard](https://github.com/Spencer-Kotys/help/blob/main/Operating_Systems/PC_Pic1.PNG)

This board is a fully functioning computer, once its slots are populated.
It consists of a processor socket containing a CPU, DRAM sockets, PCIe bus
slots, and I/O connectors of various types. Even the lowest-cost generalpurpose CPU contains multiple cores. Some motherboards contain multiple
processor sockets. More advanced computers allow more than one system
board, creating NUMA systems.

* Hadoop

Hadoop is an open-source software framework that is used for distributed
processing of large data sets (known as big data) in a clustered system containing simple, low-cost hardware components. Hadoop is designed to scale
from a single system to a cluster containing thousands of computing nodes.
Tasks are assigned to a node in the cluster, and Hadoop arranges communication between nodes to manage parallel computations to process and coalesce
results. Hadoop also detects and manages failures in nodes, providing an
efficient and highly reliable distributed computing service.
Hadoop is organized around the following three components:
1. A distributed file system that manages data and files across distributed computing nodes.

2. The YARN (“Yet Another Resource Negotiator”) framework, which manages
resources within the cluster as well as scheduling tasks on nodes in the
cluster.

3. The MapReduce system, which allows parallel processing of data across
nodes in the cluster.

Hadoop is designed to run on Linux systems, and Hadoop applications
can be written using several programming languages, including scripting
languages such as PHP, Perl, and Python. Java is a popular choice for
developing Hadoop applications, as Hadoop has several Java libraries that
support MapReduce. More information on MapReduce and Hadoop can
be found at https://hadoop.apache.org/docs/r1.2.1/mapred tutorial.html
and https://hadoop.apache.org

* Linux Timers

On Linux systems, the kernel configuration parameter HZ specifies the frequency of timer interrupts. An HZ value of 250 means that the timer generates
250 interrupts per second, or one interrupt every 4 milliseconds. The value
of HZ depends upon how the kernel is configured, as well the machine type
and architecture on which it is running. A related kernel variable is jiffies,
which represent the number of timer interrupts that have occurred since the
system was booted. A programming project in Chapter 2 further explores
timing in the Linux kernel.

* Linux Kernel Data Structures

The data structures used in the Linux kernel are available in the kernel source
code. The include file <linux/list.h> provides details of the linked-list
data structure used throughout the kernel. A queue in Linux is known as a
kfifo, and its implementation can be found in the kfifo.c file in the kernel
directory of the source code. Linux also provides a balanced binary search tree
implementation using red-black trees. Details can be found in the include file
<linux/rbtree.h>.

* The Study of Operating Systems

There has never been a more interesting time to study operating systems,
and it has never been easier. The open-source movement has overtaken operating systems, 
causing many of them to be made available in both source and
binary (executable) format. The list of operating systems available in both
formats includes Linux, BSD UNIX, Solaris, and part of macOS. The availability of source
code allows us to study operating systems from the inside out.
Questions that we could once answer only by looking at documentation or
the behavior of an operating system we can now answer by examining the
code itself.
Operating systems that are no longer commercially viable have been
open-sourced as well, enabling us to study how systems operated in a
time of fewer CPU, memory, and storage resources. An extensive but
incomplete list of open-source operating-system projects is available from
http://dmoz.org/Computers/Software/Operating Systems/Open Source/.
In addition, the rise of virtualization as a mainstream (and frequently free)
computer function makes it possible to run many operating systems on top
of one core system. For example, VMware (http://www.vmware.com) provides a free “player” for 
Windows on which hundreds of free “virtual appliances” can run. Virtualbox (http://www.virtualbox.com) provides a free,
open-source virtual machine manager on many operating systems. Using
such tools, students can try out hundreds of operating systems without dedicated hardware.
In some cases, simulators of specific hardware are also available, allowing the operating system to run on “native” hardware, all within the confines of a modern computer and modern operating system. For example,
a DECSYSTEM-20 simulator running on macOS can boot TOPS-20, load the
source tapes, and modify and compile a new TOPS-20 kernel. An interested
student can search the Internet to find the original papers that describe the
operating system, as well as the original manuals.
The advent of open-source operating systems has also made it easier to
make the move from student to operating-system developer. With some
knowledge, some effort, and an Internet connection, a student can even create
a new operating-system distribution. Not so many years ago, it was difficult
or impossible to get access to source code. Now, such access is limited only
by how much interest, time, and disk space a student has.

* Summary

An operating system is software that manages the computer hardware, as
well as providing an environment for application programs to run.

Interrupts are a key way in which hardware interacts with the operating
system. A hardware device triggers an interrupt by sending a signal to the
CPU to alert the CPU that some event requires attention. The interrupt is
managed by the interrupt handler.

For a computer to do its job of executing programs, the programs must be
in main memory, which is the only large storage area that the processor
can access directly.

The main memory is usually a volatile storage device that loses its contents
when power is turned off or lost

Nonvolatile storage is an extension of main memory and is capable of
holding large quantities of data permanently.

The most common nonvolatile storage device is a hard disk, which can
provide storage of both programs and data.

The wide variety of storage systems in a computer system can be organized
in a hierarchy according to speed and cost. The higher levels are expensive,
but they are fast. As we move down the hierarchy, the cost per bit generally
decreases, whereas the access time generally increases.

Modern computer architectures are multiprocessor systems in which each
CPU contains several computing cores.

To best utilize the CPU, modern operating systems employ multiprogramming, which allows several jobs to be in memory at the same time, thus
ensuring that the CPU always has a job to execute.

Multitasking is an extension of multiprogramming wherein CPU scheduling algorithms rapidly switch between processes, providing users with a
fast response time.

To prevent user programs from interfering with the proper operation of
the system, the system hardware has two modes: user mode and kernel
mode.

Various instructions are privileged and can be executed only in kernel
mode. Examples include the instruction to switch to kernel mode, I/O
control, timer management, and interrupt management.

A process is the fundamental unit of work in an operating system. Process management includes creating and deleting processes and providing
mechanisms for processes to communicate and synchronize with each
other.

An operating system manages memory by keeping track of what parts of
memory are being used and by whom. It is also responsible for dynamically allocating and freeing memory space.

Storage space is managed by the operating system; this includes providing
file systems for representing files and directories and managing space on
mass-storage devices.

Operating systems provide mechanisms for protecting and securing the
operating system and users. Protection measures control the access of
processes or users to the resources made available by the computer system.

Virtualization involves abstracting a computer’s hardware into several
different execution environments.

Data structures that are used in an operating system include lists, stacks,
queues, trees, and maps.

Computing takes place in a variety of environments, including traditional
computing, mobile computing, client–server systems, peer-to-peer systems, cloud computing, and real-time embedded systems.

Free and open-source operating systems are available in source-code format. Free software is licensed to allow no-cost use, redistribution, and
modification. GNU/Linux, FreeBSD, and Solaris are examples of popular
open-source systems.

# Chapter 2
* Example of Standard API

As an example of a standard API, consider the ``read()`` function that is available in UNIX and Linux systems. The API for this function is obtained from the man page by invoking the command

``man read``

on the command line. A description of this API appears below:

![API Call](https://github.com/Spencer-Kotys/help/blob/main/Operating_Systems/Pictures/OS2.1.PNG)

A program that uses the ``read()`` function must include the ``unistd.h`` header
file, as this file defines the ``ssize_t`` and ``size_t`` data types (among other
things). The parameters passed to ``read()`` are as follows:

* ``int fd`` — the file descriptor to be read
* ``void *buf`` — a buffer into which the data will be read
* ``size t count`` — the maximum number of bytes to be read into the buffer

On a successful read, the number of bytes read is returned. A return value of
0 indicates end of file. If an error occurs, ``read()`` returns −1.

* Examples of Windows and Unix System Calls

The following illustrates various equivalent system calls for Windows and UNIX operating systems.

| System Call | Windows | Unix |
| --- | --- | --- |
| Process control | ``CreateProcess()`` <br> ``ExitProcess()`` <br> ``WaitForSingleObject()`` | ``fork()`` <br> ``exit()`` <br> ``wait()`` |
| File management | ``CreateFile()`` <br> ``ReadFile()`` <br> ``WriteFile()`` <br> ``CloseHandle()`` | ``open()`` <br> ``read()`` <br> ``write()`` <br> ``close()`` |
| Device management | ``SetConsoleMode()`` <br> ``ReadConsole()`` <br> ``WriteConsole()`` | ``ioctl()`` <br> ``read()`` <br> ``write()`` |
| Information maintenance | ``GetCurrentProcessID()`` <br> ``SetTimer()`` <br> ``Sleep()`` | ``getpid()`` <br> ``alarm()`` <br> ``sleep()`` |
| Communications | ``CreatePipe()`` <br> ``CreateFileMapping()`` <br> ``MapViewOfFile()`` | ``pipe()`` <br> ``shm_open()`` <br> ``mmap()`` |
| Protection | ``SetFileSecurity()`` <br> ``InitlializeSecurityDescriptor()`` <br> ``SetSecurityDescriptorGroup()`` | ``chmod()`` <br> ``umask()`` <br> ``chown()`` |

* The Standard C Library

The standard C library provides a portion of the system-call interface for many versions of UNIX and Linux. As an example, let’s assume a C program invokes the ``printf()`` statement. The C library intercepts this call and invokes the necessary system call (or calls) in the operating system—in this instance, the ``write()`` system call. The C library takes the value returned by ``write()`` and passes it back to the user program:

![C Call](https://github.com/Spencer-Kotys/help/blob/main/Operating_Systems/Pictures/OS2.2.PNG)

* ELF Format

Linux provides various commands to identify and evaluate ELF files. For example, the ``file`` command determines a file type. If ``main.o`` is an object file, and ``main`` is an executable file, the command

``file main.o``

will report that ``main.o`` is an ELF relocatable file, while the command

``file main``

will report that ``main`` is an ELF executable. ELF files are divided into a number of sections and can be evaluated using the ``readelf`` command.

* Windows Subsytem for Linux

Windows uses a hybrid architecture that provides subsystems to emulate different operating-system environments. These user-mode subsystems communicate with the Windows kernel to provide actual services. Windows 10 adds a Windows subsystem for Linux (WSL), which allows native Linux applications (specified as ELF binaries) to run on Windows 10. The typical operation is for a user to start the Windows application ``bash.exe``, which presents the user with a bash shell running Linux. Internally, the WSL creates a Linux instance consisting of the ``init`` process, which in turn creates the bash shell running the native Linux application ``/bin/bash``. Each of these processes runs in a Windows Pico process. This special process loads the native Linux binary into the process’s own address space, thus providing an environment in which a Linux application can execute.

Pico processes communicate with the kernel services LXCore and LXSS to translate Linux system calls, if possible using native Windows system calls. When the Linux application makes a system call that has no Windows equivalent, the LXSS service must provide the equivalent functionality. When there is a one-to-one relationship between the Linux and Windows system calls, LXSS forwards the Linux system call directly to the equivalent call in the Windows kernel. In some situations, Linux and Windows have system calls that are similar but not identical. When this occurs, LXSS will provide some of the functionality and will invoke the similar Windows system call to provide the remainder of the functionality. The Linux ``fork()`` provides an illustration of this: The Windows ``CreateProcess()`` system call is similar to ``fork()`` but does not provide exactly the same functionality. When ``fork()`` is invoked in WSL, the LXSS service does some of the initial work of ``fork()`` and then calls ``CreateProcess()`` to do the remainder of the work. The figure below illustrates the basic behavior of WSL.

![WSL](https://github.com/Spencer-Kotys/help/blob/main/Operating_Systems/Pictures/OS2.3.PNG)

* *Kernighan’s Law*

“Debugging is twice as hard as writing the code in the first place. Therefore,
if you write the code as cleverly as possible, you are, by definition, not smart
enough to debug it.”

* Summary

An operating system provides an environment for the execution of programs by providing services to users and programs.

The three primary approaches for interacting with an operating system are (1) command interpreters, (2) graphical user interfaces, and (3) touchscreen interfaces.

System calls provide an interface to the services made available by an operating system. Programmers use a system call’s application programming interface (API) for accessing system-call services.

System calls can be divided into six major categories: (1) process control, (2) file management, (3) device management, (4) information maintenance, (5) communications, and (6) protection.

The standard C library provides the system-call interface for UNIX and Linux systems.

Operating systems also include a collection of system programs that provide utilities to users.

A linker combines several relocatable object modules into a single binary executable file. A loader loads the executable file into memory, where it becomes eligible to run on an available CPU.

There are several reasons why applications are operating-system specific. These include different binary formats for program executables, different instruction sets for different CPUs, and system calls that vary from one operating system to another.

An operating system is designed with specific goals in mind. These goals ultimately determine the operating system’s policies. An operating system implements these policies through specific mechanisms.

A monolithic operating system has no structure; all functionality is provided in a single, static binary file that runs in a single address space. Although such systems are difficult to modify, their primary benefit is efficiency.

A layered operating system is divided into a number of discrete layers, where the bottom layer is the hardware interface and the highest layer is the user interface. Although layered software systems have had some success, this approach is generally not ideal for designing operating systems due to performance problems.

The microkernel approach for designing operating systems uses a minimal kernel; most services run as user-level applications. Communication takes place via message passing.

A modular approach for designing operating systems provides operatingsystem services through modules that can be loaded and removed during run time. Many contemporary operating systems are constructed as hybrid systems using a combination of a monolithic kernel and modules.

A boot loader loads an operating system into memory, performs initialization, and begins system execution.

The performance of an operating system can be monitored using either counters or tracing. Counters are a collection of system-wide or perprocess statistics, while tracing follows the execution of a program through the operating system.
