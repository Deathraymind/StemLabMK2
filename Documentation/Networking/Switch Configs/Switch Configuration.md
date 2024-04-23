**Documentation**

---

**Trunked and Access Ports Configuration Guide**

This documentation provides step-by-step instructions for configuring trunked and access ports on a trunk switch (top switch) and a cyber switch (bottom Brocade switch) using Cisco and Brocade commands. It includes the setup of VLANs, tagging, and port configurations.

---

**1. Terminology**

- **Untagged**: Denotes access ports. Traffic on these ports is not encapsulated with VLAN tags.
- **Tagged**: Refers to trunked ports. Traffic on these ports is encapsulated with VLAN tags.
- **VLAN 10**: Represents a virtual interface configured for VLAN 10.

### **2. Configuration on Trunk Switch (Top Switch)**

**Red Ports (Multi-VLAN Ports for Switches and Routers)**:

```
enable
conf t
vlan 10
tagg e 1/1/1 to 1/1/6
interface e 1/1/1 to 1/1/6
dual-mode 1
exit
exit
write mem
```

**Green Ports (Multi-VLAN Ports with POE for APs)**:

```
enable
conf t
vlan 10
tagg e 1/1/7 to 1/1/12
exit
interface e 1/1/7 to 1/1/12
inline power
dual-mode 1
exit
exit
write mem
```

### **3. Configuration on Cyber Switch (Bottom Brocade Switch)**

**Red Ports**:

```
enable
conf t
vlan 10
tagg 1/1/1 to 1/1/6
exit
interface e 1/1/1 to 1/1/6
dual-mode 1
exit
exit
write mem
```

**Blue Ports (Untagged Interfaces for VLAN 10 Devices)**:

```
vlan 10
untagg e 1/1/13 to 1/1/24
exit
exit
write mem
```

**4. Additional Terminology and Tips for brocade**

- **Inline Power**: Enables Power over Ethernet (POE) on the specified ports.
- **Dual-Mode 1**: Sets the native VLANs on ports to VLAN 1 or the basic LAN configuration.
- **Module Configuration**: Modules must be configured one at a time, specifying `1/x/x` format for port identification.
- To view available interfaces: 
  ```
  enable
  show interfaces brief
  ```

### Cisco Switch Configuration

**Blue Ports (Configuring VLAN 10)**:

```
enable
configure terminal
vlan 10
name Cyber
exit
exit
wr mem
```

**Blue Ports (Configuring Untagged/Access Interface for VLAN 10)**:

```
enable
configure terminal
interface range g1/0/1 - g1/0/22
switchport mode access
switchport access vlan 10
exit
exit
wr mem
```

**Red Port (Configuring Tagged/Trunk Interface)**:

```
show ip interfaces brief

enable
configure terminal
interface gigabitethernet1/0/23
switchport trunk encapsulation dot1q
switchport mode trunk 
switchport trunk allowed vlan none
switchport trunk allowed vlan add 1
switchport trunk allowed vlan add 10
no shutdown
exit
exit
wr mem
```
**Side Note**: The "switchport trunk encapsulation dot1q" command may not be needed, though if this error message shows:
```
Command rejected: an interface whose trunk encapsulation is "auto" can not be configure
```
then type in the command.



