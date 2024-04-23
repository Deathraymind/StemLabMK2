**Documentation**

---

**Enabling SSH on Cisco Devices Guide**

This document provides a step-by-step guide for configuring Secure Shell Protocol (SSH) on Cisco switches and routers using Cisco commands.
Also you must configure the VLANS before enabling SSH.

---

**1. Terminology**

- **VTY**: Stands for Virtual teleTYpe. VTY is a command line interface that gives users access to a device’s control plane, most often in network devices like routers and switches. It enables users to connect to a device and configure it via its virtual interface (VTY).
- **Secret**: A command that creates an encrypted password.

### **2. Configuring a Management IP on a Switch**

**This is required before setting up SSH**

```
enable
configure terminal
interface vlan 10
ip address 172.16.254.10 255.255.0.0
no shut
exit
ip default-gateway 172.16.1.1
exit
wr mem
```

### **3. Configuring SSH on a Switch**

**This will be configured only for VLAN10 access**

```
enable
configure terminal
enable secret 1234qwer!@#$QWER
username admin secret amongus
access-list 1 permit 172.16.0.0 0.0.255.255
ip domain name silly.net
hostname CiscoCyberSW
crypto key generate rsa
2048
ip ssh version 2
line vty 0 15
login local
exec-timeout 5 0
transport input ssh
access-class 1 in
exit
exit
wr mem
```