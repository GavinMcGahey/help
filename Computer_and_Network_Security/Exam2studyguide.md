# Exam 2 Topics

## Threat Reports -- Specifically Crowdstrike

Some cyber attacks come from more sophistocated actors. These are called Advanced Persistent Threats (APT). Threat reports are drawn up to describe there activities. Crowdstrike is one of many companies that uses knowlegde of APTs to protect against cyber attacks.

Crowdstrike
-2011
-intelligence
-APT (class 27) : different threat groups 
-techniques 
-ATP1: peoples liberation army 

[Crowdstrike](https://www.crowdstrike.com/about-crowdstrike/)

[Class 13](https://github.com/Spencer-Kotys/help/blob/main/Computer_and_Network_Security/CNS_Classes.md#class-13----intro-to-cyber)

[Class 17](https://github.com/Spencer-Kotys/help/blob/main/Computer_and_Network_Security/CNS_Classes.md#class-17-intrusion-detection-and-intrusion-prevention-systems)

[Class 27](https://github.com/Spencer-Kotys/help/blob/main/Computer_and_Network_Security/CNS_Classes.md#class-27---cyber-threats-and-defenses)

## MITRE ATT&CK -- Understand the TTPs and what might illustrate different Techniques

TTPs: tactics, techniques, and procedures 
Pyramid of Pain: how hard it is for a threat actor to change their identifier 

-TTP (hardest to change)
-Tools
-Network
-Domain
-IP address
-Hash values (easiest to change)

TTPs: used to track and figure out ATPs, whos who?

ATT & CK : method to organize TTPs into categories



[Class 6](https://github.com/Spencer-Kotys/help/blob/main/Computer_and_Network_Security/CNS_Classes.md#class-06-mitre-attck)

[Class 13](https://github.com/Spencer-Kotys/help/blob/main/Computer_and_Network_Security/CNS_Classes.md#class-13----intro-to-cyber)

[Class 27](https://github.com/Spencer-Kotys/help/blob/main/Computer_and_Network_Security/CNS_Classes.md#class-27---cyber-threats-and-defenses)

## Domain Names -- Find registration info and IPs and DNS data

commands:
whois
nslookup

[whois](https://www.tecmint.com/whois-command-get-domain-and-ip-address-information/)

## SQL Injections -- Lab on SQL

SQL: structure query language 

user = 'username'

Prepared Statement: how you prevent a SQL injection
var username 
user = username 
prepared = input 
* won't be able to run as code

[SQL Injection](https://github.com/macee/cns/blob/2020f/labs/lab_09_SQL_inject/lab_09.md#test-sql-injection-string)

## Vuln Mgmt -- Tools like ACAS (Nessus and SC from Tenable) 

ACAS: assured compliance assessment solution

Tenable: parent company of NESSUS and SC (tenable.com)

NESSUS: propriety vulnerability scanner developed by tennable, product, vulnerability assessment solution 
SC: "security center", product of tenable, scanner

What are they installed on? networks that you want to scan ("networks that have bad behavior" -Niles)



[Class 29](https://github.com/Spencer-Kotys/help/blob/main/Computer_and_Network_Security/CNS_Classes.md#class-29-logging-and-vuln-management)

## DNSSEC -- What does it protect against

DNSSEC: Domain Name System Security Exetentions (class 25)

What does it protect against? 
-DNS cache poisoning 

-validates DNS response 
-helps with integrity 
-does not provide confidentiality 
-digitally signs DNS lookup records with public key crypto 

[DNSSEC](https://github.com/Spencer-Kotys/help/blob/main/Computer_and_Network_Security/CNS_Classes.md#dnssec)

## Windows Executable -- Where do they live on a system

[Windows PE](https://github.com/Spencer-Kotys/help/blob/main/Computer_and_Network_Security/CNS_Classes.md#windows-pe-file)

[Windows Logs](https://github.com/Spencer-Kotys/help/blob/main/Computer_and_Network_Security/CNS_Classes.md#windows-logs)

[Class 30](https://github.com/Spencer-Kotys/help/blob/main/Computer_and_Network_Security/CNS_Classes.md#class-30---windows-logging-the-files-are-in-the-computer)

## Sigcheck

Sigcheck is a command-line utility that shows file version number, timestamp information, and digital signature details, including certificate chains.

[Sigcheck Docs](https://docs.microsoft.com/en-us/sysinternals/downloads/sigcheck#:~:text=Sigcheck%20is%20a%20command%2Dline,signature%20details%2C%20including%20certificate%20chains.)

## Log analysis -- Windows, Linux, Nginx, access logs

### Windows Logs:

Old (NT,2000,XP,Server 2003):

.evt files located in `C:\Windows\System32\config`, examples are SecEvent.evt, AppEvent.evt, SysEvent.evt

New (Vista onwards):

.evtx files located in `C:\Windows\System32\winevt\logs` and are able to do remote logging, examples are Security.evtx, Application.evtx, System.evtx

Different logon types (2,3,4,5,7,8,9,10,11)

4624 = Successful Logon

### Linux Logs:

.log files located in `/var/log` 

`var/log/syslog` and `/var/log/messages` store all system logs

`var/log/auth.log` and `var/secure` store all security logs

[Class 29](https://github.com/Spencer-Kotys/help/blob/main/Computer_and_Network_Security/CNS_Classes.md#class-29-logging-and-vuln-management)

[Class 30](https://github.com/Spencer-Kotys/help/blob/main/Computer_and_Network_Security/CNS_Classes.md#class-30---windows-logging-the-files-are-in-the-computer)

[Class 31](https://github.com/Spencer-Kotys/help/blob/main/Computer_and_Network_Security/CNS_Classes.md#class-31---syslog)
