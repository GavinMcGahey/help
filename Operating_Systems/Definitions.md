# Chapter 1

* Operating system: Software that manages a computer's hardware.
* Hardware: The central processing unit (CPU), the memory, and the input/ouput (I/O) devices.
* Application programs: Such as word processors, spreadsheets, web browsers, define the ways in which these resources are used.
* Four components of a computer system: Hardware, Operating system, application programs, and user.
* Ease of use: How easily the operating system is to use for the end user.
* Resource utilization: how various hardware and software resources are shared.
* Touch screen: A system where the user interacts by pressing and swiping fingers acreoss the screen.
* Voice Recognition: A system that allows interaction by recongnising a users voice.
* Siri: Apple Inc's voice recognition software.
* Embedded computers: Computers with little or no user view, part of a system like home devices and automobiles.
* Resource allocator: An operating system manages avalible resources.
* Control program: Manages the execution of user programs to prevent errors and improper use.
* Moore's Law: Predicts that the number of transistors on an integrated circuit will double every 18 months.
* Kernel: One program that is always running on the computer, base of the operating system.
* System Programs: Associated with the operating system, but not part of the kernel.
* Middleware: A set of software frameworks that provide additional services to application developers.
* Interrupt: A signal sent to the CPU that my stop the system bus, usually at the completion of a program.
* Interrupt vector: An array of addresses that hold the interrupt service routines indexed by a unique number.
* Interrupt-request line: A wire on the CPU that is checked after executing every instruction.
* Interrupt-handler routine: The instruction set that the CPU jumps to after reading the interrupt number.
* Random-access memory (RAM): Rewritable memory that computers run programs off of. Also called main memory.
* Bit: A bit is the building block of computer storage and can be either 0 or 1.
* Byte: 8 bits, most common size of data to manipulate.
* Word: Number of bytes dependent on computer architecture. On a 64-bit computer, a word is 64 bits or 8 bytes.
* Secondary storage: An extention of main memory (RAM), able to hold data permanently.
* Hard-disk drives (HDDs): Spinning discs that are encoded with information, think CDs or DVDs.
* Nonvolatile memory (NVM): Circits that store data, generally called SSDs, think flash drives.
* Tertiary storage: Data storage used for special purposes like backup. Could be stored on optical disk or magnetic tape.
* Memory: In this book, volatile storage is referred to as memory. 
* Nonvolatile storage (NVS): It retains its contents when power is lost, usually secondary storage.
* Mechanical storage: HDDS, optical disks, etc. (generally larger and less expensive per byte)
* Electrical storage (NVM) : Flash memory, FRAM, NRAM, and SSD.
* **CPU: The hardware that executes instructions.**
* **Processor: A physical chip that contains one or more CPUs.**
* **Core: The basic computation unit of the CPU.**
* **Multicore: Including multiple computing cores on the same CPU.**
* **Multiprocessor: Including multiple processors.**
* Clustered system: A system which combines multiple CPUS.
* Loosely coupled: Clustered systems are considered loosely coupled because theay are composed of two  or more individual systems.
* High-availability service: Service that will continue evein if one or more failures occur.
* Graceful degradation: The ability to continue providing service proportional to the level of surviving hardware after a failure.
* Fault tolerant: Goes beyond graceful degradation because any single component can fail without affecting operations.
* Asymmetric clustering: One machine is in hot-standby mode where it is ready to jump in if the other machine fails.
* Symmetric clustering: Two or more machines are running programs and monitoring each other. 
* Parallelization: Dividing a program into sepate parts that run in parallel on different cores of the computer.
* Distributed lock manager (DLM): Access controal and locking for parallelization.
* Storage-area networks (SANs): Allow many systems to attach to a pool of storage.
* System daemons: System services that are loaded at boot and run the entire time the kernel is running.
* Trap (exception): Another form of an interrupt which is a software-generated kind caused by and error or a specific request.
* Multiprogramming: Organizes programs so that the CPU is always executing one.
* Process: A program in execution
* Multitasking: An extension of multiprogramming wherein CPU scheduling algorithms rapidly switch between processes
* Response time: The amount of time it takes a process to respond to user input.
* User mode: LImited in the instructions that can be executed.
* Kernel mode (supervisor mode, system mode, etc): Can exectue any instruction.
* Privileged instructions: Machine instruction that may cause harm so only a privileged account can execute them.
* Protection rings: Varying levels of privilge.
* Virtual machine manager (VMM): Manages virtual machine, has privilge between user an kernel.
* Timer: An interrupt that can be set for a specified period of time, used to prevent infinite loops.
* Variable timer: A timer set to a number of clock cycles.
* Progarm counter: Specifies the next instruction to execute.
* Caching: Copying information from a slower storage system to a the cache which is a faster storage system.
* Cache management: The managing of information stored in the cache.
* List: A representation of collections of data values in a sequence.
* Linked list: A list in which items are linked to one another.
* Singly linked list: Each item points to its successor.
* Doubly linked list: Item can refer to either its predecessor or its successor.
* Circularly linked list: The last element in the list refers to the first element.* Stack: A sequentially ordered data structure that used LIFO for adding and removing items.
* Last in, first out (LIFO): The last item in is the first item removed.
* Queue: A sequentially ordered data structure that uses FIFO.
* First in, first out (FIFO): items are removed in the order in which they came.
* Tree: A data structure that can represent data hierarchically. Data linked through parent-child relationships.
* General tree: A parent may have an unlimited number of children.
* Binary tree, a parent may have at most two children.
* Hash function: Takes data as its input, performs an operation on the data, and returns a value.
* Hash collision: When two different inputs result in the same hash output.
* Hash map: Associates key and value pairs using a hash function.
* Bitmap: A string of n binary digits that can be used to represent the status of n items.
* Disk blocks: The individual units on a storage disk.
* Portals: Provide web accessibility to internal servers.
* Wireless networks: A network that does not use wires to propagate network connections.
* Firewall: Controls information that is passed in, out, and on the network.
* Mobile Computing: Computing on handheld smartphones and tablet computers.
* Client-Server Computing: Where there is a designated server or servers for clients to connect to.
* Computer-server system: Provides an interface to which a client can send a request to perform an action. The server then executes the action and sends the results to the client. 
* File-server system: Provides a file-system interface where clients can create, update, read, and delte files.
* Peer-to-Peer Computing: Where there is not distingtion between clients and servers.
* Discovery protocol: A protocol that allows peers to discover services provided by other peers.
* Cloud computing: Computing that delivers computing, storage, applications as a service across a network.
* Public cloud: cloud available via the internet to anyone willing to pay
* Private cloud: available for and ran by a company
* Hybrid cloud: a cloud with public and private cloud components
* SaaS: one or more applications available via the internet
* PaaS: a software stack ready for application use via the internet
* IaaS: servers or storage available over the internet 
* Application-specific integrated circuits (ASICs): Hardware created to perform specific tasks.
* Free software: Makes source code availabe and is licensed to allow no-cost use, redistribution, and modification.
* Open-source software: Source code is availabe but not the same licencing as free software.
* Closed-source: Where source code is not released.
* Proprietary software: Owned and sometimes created by a company, usually heavily restricted.
* Reverse engineering: Taking binary code and turing it into  the source code.
* GNU's not unix! (GNU): A Unix compatible operating system started by Richard Stallman in 1984.
* Linux: The kernel created by Linus Torvals and others released in 1991.
* GNU/Linux: Combination of GNU and teh Linux kernel, commonly refered to as Linux.
* BSD UNIX: A derivated of AT&T's UNIX from Berkely. Started in 1978, became open source in 1994.
* Version control system: Allow a user to pull entire source code and push changed back.
* Git: A version control system, is what Github is based on.
* Solaris: Commmercial UNIX-based operating system of Sun Microsystems.

# Chapter 2

* User interface
* Graphical user interface (GUI)
* Touch-screnn interface
* Command-line interface (CLI)
* Shared memory
* Message passing
* Command interpreter
* Shells
* Desktop
* Icons
* Folder
* Gestures
* Springboard
* System administrators
* Power users
* Shell scripts
* System calls
* Application programming interface (API)
* libc
* Run=time environment (RTE)
* System-call interface
* Pushed
* Stack
* Popped
* Process control
* File management
* Device management
* Information maintenance
* Communications
* Protection
* Debugger
* Bugs
* Lock
* Sketch
* Boot loader
* Single step
* Message-passing model
* Host name
* Process name
* Daemons
* Client
* Server
* Shared-memory model
* System services aka system utilities
* Registry
* Application programs
* Relocatable object file
* Linker
* Executable
* Loader
* Relocation
* Dynamically linked libraries (DLLs)
* Executable and Linkable Format (ELF)
* Portable Executable (PE)
* Mach-O
* Applicatin binary interface (ABI)
* User goals
* System goals
* Policy
* Mechanism
* Monolithic
* Tightly coupled
* Loosely coupled
* Layerd approach
* Mach
* Micro-kernel
* Loadable kernel modules (LKMs)
* User experience layer
* Application frameworks layer
* Core Frameworks
* Kernel environment
* Darwin
* Traps
* Krnel abstractions
* Kernel extensions or kexts
* Ahead-of-time (AOT)
* Bionic
* WSL
* Pico
* System build
* Booting
* Bootstrap program or boot loader
* BIOS
* Boot block
* UEFI
* GRUB
* Recovery mode
* Single-user mode
* Debugging
* Performance tuning
* Botlenecks
* Log file
* Core dump
* Crash
* Crash dump
* BPF Compiler Collection (BCC)
* Verifie

