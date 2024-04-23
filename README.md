# STEMlab Network Documentation Mk2

## Overview

The STEMlab Network Mk2 is designed to facilitate a physical network separation between STEMlab and Cyber, enhancing our operational capabilities. This new structure addresses the limitations of VLANs in our previous setup, offering a more adaptable and less disruptive environment. This is particularly beneficial for the Cyber team, who can now engage in networking experiments without affecting other lab functions.

## Network Composition

The lab is segmented into two distinct local networks, each with its own pfSense instance:

1. **Stemlab.lan**
2. **Cyber.lan**

### Stemlab.lan Network
- **DHCP Server**: Hosted on a physical computer within the server rack.
- **Network Range**: 192.168.100.x/24.
- **Wireless Access Point**: Named `stemlab24`.
- **Characteristics**: Features a basic setup with limited servers, tailored for general lab activities.

### Cyber.lan Network
- **DHCP Server**: Is a VLAN on pfsense.
- **Address Range**: 172.16.x.x/16.
- **Wireless SSID**: `sillynet`.
- **Core Objective**: Serves as an experimental sandbox for students, enabling them to undertake projects without impacting other lab sections.
- **Documentation Focus**: Detailed guidance on setting up a PXE server, Domain Controller, and OpenMediaVault server.
- **Additional Info**: This network is the primary subject of the GitHub documentation, due to its complex setup and educational purpose.

## Rationale for Physical Separation

Our transition away from VLANs was motivated by several factors:
- **Maintenance and Operational Challenges**: The complexity introduced by VLANs led to increased maintenance demands and potential network downtime.
- **Educational Impediments**: VLANs presented a steep learning curve, potentially limiting the ability of new students to effectively engage with the network.

## Conclusion

STEMlab Network Mk2's physically separated structure aims to overcome these challenges, providing a stable, user-friendly, and conducive learning environment. This documentation serves as a comprehensive guide for managing both networks, with a special emphasis on the intricacies of the Cyber.lan network.

---
