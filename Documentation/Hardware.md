# STEMlab Network Mk2: Hardware Configuration

## Overview

The STEMlab Network Mk2 is designed to optimize the functionality and reliability of the STEMlab and Cyber operations through two distinct network segments: `Stemlab.lan` and `Cyber.lan`. This setup ensures a seamless and efficient workflow, accommodating various activities within the lab.

## Network Segments and Hardware Components

### Stemlab.lan (192.168.100.x/24)
- **Purpose**: Dedicated to robotics and coding devices requiring constant uptime.
- **Components**:
  - **Stemlab.lan pfSense**: Manages network traffic and security.
  - **Stemlab.lan Main Switch**: Central hub for network connectivity.
  - **3D Printer Switch**: Dedicated switch for 3D printer connectivity.
  - **Cameras (3 units)**: Security and monitoring devices.
  - **Stemlab24 Linksys AP**: Wireless access point for network access.

### Cyber.lan (172.16.1.x/16)
- **Purpose**: Serves as a sandbox for student projects, networking experiments, and server operations.
- **Components**:
  - **Cyber.lan pfSense**: Manages network traffic and security for the Cyber segment.
  - **Cyber.lan Main Switch**: Central hub for Cyber network connectivity.
  - **PXE Switch**: Dedicated switch for PXE (Preboot Execution Environment) services.
  - **Cyber OpenWRT AP**: Advanced wireless access point, offering robust networking features.
  - **Proxmox and All Servers**: Virtualization environment and servers for various applications.
  - **Cyber Desktop Switch**: Dedicated switch for desktop connections.
  - **OMV (OpenMediaVault)**: Network-attached storage (NAS) solution.

## Connectivity

Both networks, `Stemlab.lan` and `Cyber.lan`, are connected to a shared switch which is also linked to the Starlink internet service. This setup ensures that both networks have reliable internet access while maintaining their operational independence.

---

![](https://app.diagrams.net/?src=about#HDeathraymind%2FStemLabMK2%2Fmain%2Fnetworking%2FUntitled%20Diagram.drawio.svg)
