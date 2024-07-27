# STEMlab Network Documentation Mk2

## Overview

The STEMlab Network Mk2 is designed to facilitate a physical network separation between STEMlab and Cyber, enhancing our operational capabilities. This new structure addresses the limitations of VLANs in our previous setup, offering a more adaptable and less disruptive environment. This is particularly beneficial for the Cyber team, who can now engage in networking experiments without affecting other lab functions.

## Network Composition



1. **Stemlab**
2. **Silly**
3. **Stemlab Cafe**

### Silly Network
- **VLAN**: `1`
- **DHCP Server**: `172.16.1.20 - 172.16.1.254`
- **Address Range**: `172.16.1.x/24`
- **Wireless SSID**: `sillynet` (HIDDEN OR OFF).
- **Core Objective**: Serves as an experimental sandbox for students, enabling them to undertake projects without impacting other lab sections.
- **Documentation Focus**: Detailed guidance on setting up a PXE server, Domain Controller, and OpenMediaVault server.
- **Additional Info**: This is where alot of servcies will be hosted with more strict firewall rules.

### Stemlab Cafe Network
- **VLAN**: `10`
- **DHCP Server**: `10.0.0.10 - 10.0.0.254`
- **Network Range**: `10.0.0.x/24`
- **Wireless Access Point**: Named `Stemlab Cafe`.
- **Characteristics**: Has a captive portal so we can sell internet logins.


### Stemlab24 Network
- **VLAN**: `100`
- **DHCP Server**: `192.168.100.20 - 192.168.100.254`
- **Network Range**: `192.168.100.x/24`
- **Wireless Access Point**: Named `stemlab24`.
- **Characteristics**: This will hold all IOT projects and clients that need to connect to the AD server aka laptops.




## Conclusion

STEMlab Network Mk2's physically separated structure aims to overcome these challenges, providing a stable, user-friendly, and conducive learning environment. This documentation serves as a comprehensive guide for managing both networks, with a special emphasis on the intricacies of the Cyber.lan network.

---
