# Networks terminology
## Definitions

**IP address** -  a unique address that identifies a device on the internet or a local network. 
IP stands for "Internet Protocol," which is the set of rules governing the format of data sent via the internet or local network.

**IP version 4 and version 6** - IP version 4 addresses are 32-bit integers that can be expressed in hexadecimal notation. IPv4 was the first version 
deployed for production in January 1983 by ARPANET(Advanced Research Projects Agency Networks). It still routes most Internet traffic today, despite the ongoing deployment of a successor protocol, IPv6.
IPv4 uses a 32-bit address space which provides 4,294,967,296 (232) unique addresses, but large blocks are reserved for special networking methods.

**SSH** - SSH or Secure Shell Protocol is a cryptographic network protocol for operating network services securely over an unsecured network. 
The SSH protocol uses encryption to secure the connection between a client and a server. 
All user authentication, commands, output, and file transfers are encrypted to protect against attacks in the network. 
SSH is widely used by network administrators for managing systems and applications remotely, enabling them to log in to another computer over a network, execute commands and move files from one computer to another.

**SCP** - The Secure Copy Protocol or “SCP” helps to transfer computer files securely from a local to a remote host. 
It is somewhat similar to the File Transfer Protocol “FTP”, but it adds security and authentication. 
The RCP is used to transfer the files, and the SSH protocol provides authentication and encryption, so SCP can be considered a mixture of these two protocols.
The SCP can also benefit from using SSH because it allows the inclusion of permissions and timestamps for the file that needs to be uploaded.

### Terminal commands
1. **LS** -  ls is used for listing directory contents or file information in a terminal.

1. **CAT** - cat allows us to create single or multiple files, view contain of file, concatenate files and redirect output in terminal or files.

1. **ECHO** - echo command writes(outputs) an argument in a terminal

1. **CD** - changes directory or which folder we are in. Ex: cd~ takes us to a home directory.

1. **CHMOD** - allows us to change the file permissions.




**Server** - A server is a computer that provides data to other computers. It may serve data to systems on a local area network (LAN) or a wide area
network (WAN) over the Internet. Many types of servers exist, including web servers, mail servers, and file servers.
Each type runs software specific to the purpose of the server. For example, a Web server may run Apache HTTP Server or Microsoft IIS, which
both provide access to websites over the Internet. 

**Router** - A router is a hardware device that routes(forwards) data(packets) from a local area network (LAN) to another network
connection. It can be a separate hardware device or software loaded
onto a server. 

**Switch** - A network switch is a hardware device and it connects devices within a network (often a local area network, or LAN*) 
and forwards data packets to and from those devices.
Unlike a router, a switch only sends data to the single device it is intended for (which may be another switch, a router, or a user's computer), not to networks of multiple devices.

**wLAN** - Stands for "Wireless Local Area Network." A WLAN, or wireless LAN, is a network that allows devices to 
connect and communicate wirelessly. Unlike a traditional wired LAN, in which devices communicate over Ethernet cables, 
devices on a WLAN communicate via Wi-Fi.
While a WLAN may look different than a traditional LAN, it functions the same way.

**LAN** - A local area network (LAN) is a collection of devices connected together in one physical location, 
such as a building, office, or home. A LAN can be small or large, 
ranging from a home network with one user to an enterprise network with thousands of users and devices in an office or school.
Regardless of size, a LAN's single defining characteristic is that it connects devices that are in a single, limited area.

**UDP** - User data protocol one of the core members of the Internet protocol suite. With UDP, computer applications can send messages, in this case referred to as datagrams, to other hosts on an Internet Protocol network. It speeds up communications by not formally establishing a connection before data is transferred. This allows data to be transferred very quickly, but it can also cause packets to become lost in transit — and create opportunities for exploitation in the form of DDoS attacks.

**TCP** - Transmission Control Protocol is a transport protocol that is used on top of IP to ensure reliable transmission of packets. TCP includes mechanisms to solve many of the problems that arise from packet-based messaging, such as lost packets, out of order packets, duplicate packets, and corrupted packets.
Since TCP is the protocol used most commonly on top of IP, the Internet protocol stack is sometimes referred to as TCP/IP.

**NAS** - network-attached storage device is a data storage device that connects to and is accessed through a network, instead of connecting directly to a computer. NAS devices contain a processor and operating system so it can run applications and provide the intelligence needed for files to be easily shared by authorized people. The advantage of a NAS device is that it can be easily accessed by multiple people, multiple computers, mobile devices, or even remotely (if set up properly).  

**RJ45** - The eight-pin RJ45 connector is a standardised interface which often connects a computer to a local area network (LAN).
