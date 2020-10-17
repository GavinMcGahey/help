# Quiz 1
1. What is the purpose of a Security Technical Implementation Guide (STIG)?:

**Provide system specific security configurations**

2. What is the purpose of a SCC Tool?

**Provide an automated tool for testing system security configuration**

3. What is the purpose of a NIST 800-53?

**Provide a holistic approach to information security**

4. What is Defense in Depth most similar to?

**A medieval castle**

5. What would you use as a baseline to develop a hardening policy for all firewalls in an environment of 40000 users with 3 different brands of firewall?

**SRG**

6. What is the SHA256 hash of the word "CAT" (not including the quotes, upper case without a trailing new line)?

**15b89a569474240a616f9a94dd045b2711d445dde955b62bf4b8f2a2afaf0f6b**

7. What does V-72161 stipulate you audit?

**sudo**

8. The RHEL 7 STIG V-71905 would be what in the Win 10 STIG

**V-63427**

9. What would you use to correlate Vul ID's across system STIGs

**CCI**

10. AC-17 deals with

**Remote Access**

11. In NIST 800-53 Rev 4 the control: AC-17 (1) deals with monitoring and controlling remote access systems. Select the related controls

**V-63459, V-63405, V-63657, V-77103**

12. Who (github user) made the commit "6a49097e3f51e3a9a04f685dfd1a9dd6e805418c" in macee/cns

**(soups)**

13. What is Linus Torvalds Public SSH Key on GitHub

**(ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCoQ9S7V+CufAgwoehnf2TqsJ9LTsu8pUA3FgpS2mdVwcMcTs++8P5sQcXHLtDmNLpWN4k7NQgxaY1oXy5e25x/4VhXaJXWEt3luSw+Phv/PB2+aGLvqCUirsLTAD2r7ieMhd/pcVf/HlhNUQgnO1mupdbDyqZoGD/uCcJiYav8i/V7nJWJouHA8yq31XS2yqXp9m3VC7UZZHzUsVJA9Us5YqF0hKYeaGruIHR2bwoDF9ZFMss5t6/pzxMljU/ccYwvvRDdI7WX4o4+zLuZ6RWvsU6LGbbb0pQdB72tlV41fSefwFsk4JRdKbyV3Xjf25pV4IXOTcqhy+4JTB/jXxrF)**

14. ESXi is an example of:

**Software on "Bare Metal"**

15. What does the vagrant file (below link) do?
https://cga.sfo2.digitaloceanspaces.com/Vagrantfile

**Free Response**

I put: *It configures Vagrant to version 2.
It then configures a box for centos 7.
It gives the IP address of 127.0.0.1 to use.
It then configures a vm provision for ansible
then sets ansible.playbook to "playbook.yml"*

**[Quiz 1 Walkthrough](https://youtu.be/MM-OO18PwEQ)**

# Quiz 2
1. What protocol can Ansible use to connect to remote hosts?

**SSH**

2. Terraform can be used to manage assets in Google Cloud

**True**

3. Stateless packet filtering is performed on a per-packet basis? 

**True**

4. A typical enterprise firewall has at minimum the following interfaces?

**Outside, Inside, and DMZ**

5. Which Vagrant providers are not shipped with the software?

**Nutanix**

6. What does the following do in Vagrant?

config.vm.provision "shell",

 inline: "sudo apt install lynx"
 
 **Installs a web browser**
 
 7. Vagrant is a Type 2 Hypervisor
 
 **False**
 
 8. Vagrant is a configuration managment tool
 
 **False**
 
 9. Security engineers will usually build firewall rules with netfilter
 
 **False**
 
 10. What tool would you use to scan for open ports

**nmap**

11. If you want to be able to telnet into a server you need to install what package in Ubuntu Linux?

**telnetd**

12. What group can execute this script?

-rw-rw-r-- 1 constantine bananas 626 Sep 30 22:27 exploit.py

**no one**

13. What type of script is this?

-rw-rw-r-- 1 constantine bananas 626 Sep 30 22:27 exploit.py

**Python**

14. A firewall passes or blocks traffic based upon:

**Port number and IP address**

15. A firewall is typically located at only one position in an organization?

**False**
