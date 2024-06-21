**Documentation**

---

**Trunked and Access Ports Configuration Guide**

This documentation provides step-by-step instructions for configuring trunked and access ports on RackSW (bottom switch) and RackSW-2 (top switch) using Cisco commands. It includes the setup of VLANs, tagging, and port configurations.

***Note:** Please refer to "Rack Switch Mapping" and "Rack Switch-2 Mapping" (Network Diagrams) to confirm how the devices' ports should be configured. Contact your Chief Network Engineer for any other questions.*

---

**1. Terminology**

- **Access**: Denotes access/untagged ports. Traffic on these ports are not encapsulated with VLAN tags.
- **Trunk**: Refers to trunk/tagged ports. Traffic on these ports are encapsulated with VLAN tags.
- **VLAN**: Stands for Virtual Local Area Network (LAN). 

### **2. Configuration on RackSW (Bottom Switch)**

**Creating VLANS**

```
enable
configure terminal
vlan 10
name Cyber
vlan 100
name Stemlab
vlan 254
name Management
exit
```

**Trunk Ports**

```
interface range g1/0/1 - 8
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan none
switchport trunk allowed vlan add 1,10,100,254
```

**POE enabled Trunk Ports**

```
interface range g1/0/9 - 16
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan none
switchport trunk allowed vlan add 1,10,100,254
power inline auto
```

**VLAN10 Access Ports**

```
interface range g1/0/17 - 24
switchport mode access
swtichport access vlan 10
interface range g1/0/37 - 48
switchport mode access
switchport access vlan 10
```

**VLAN100 Access Ports**

```
interface range g1/0/25 - 36
switchport mode access
switchport access vlan 100
exit
exit
wr mem
```

**Configuring SSH**

```
enable 
configure terminal
ip domain name goon.lan
hostname RackSW
enable secret 1234qwer!@#$QWER
username administrator secret amongus
crypto key generate rsa
2048
ip ssh version 2
interface vlan 254
ip address 172.16.254.11 255.255.255.0 
no shut
exit
ip default-gateway 172.16.254.1
access-list 1 permit 172.16.254.0 0.0.0.255
access-list 1 permit 172.16.10.0 0.0.0.255
line vty 0 15 
login local
exec-timeout 5 0
transport input ssh
access-class 1 in
exit
exit
wr mem
```

### **3. Configurations on RackSW-2 (Top switch)**

**Creating VLANS**

```
enable
configure terminal
hostname RackSW-2
vlan 10
name Cyber
vlan 100
name Stemlab
vlan 254
name Management
exit
```

**Trunk Ports**

```
interface range g0/1 - 8
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan none
switchport trunk allowed vlan add 1,10,100,254
```

**Access Ports**

```
interface range g0/9 - 16
switchport mode access
switchport access vlan 10
interface range g0/17 - 24
switchport mode access 
switchport access vlan 100
exit
```

**Configuring SSH**

```
interface vlan 254
ip address 172.16.254.12 255.255.255.0
no shut
exit
ip default-gateway 172.16.254.1
exit
enable secret 1234qwer!@#$QWER
username administrator secret amongus
access-list 1 permit 172.16.254.0 0.0.0.255
access-list 1 permit 172.16.10.0 0.0.0.255
ip domain name goon.lan
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
