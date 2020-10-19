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

**Insert Picture**

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
