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
