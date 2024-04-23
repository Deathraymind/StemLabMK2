# Configuring an OpenWrt Access Point

## Overview
This guide covers the steps to configure an OpenWrt router as a wireless access point (AP), including network settings, disabling unnecessary services, and finalizing the configuration.

## Steps

### 1. Disconnect the Wireless AP
- **Action**: Remove the AP from your network.

### 2. Connect to Computer
- **Action**: Use an Ethernet cable to connect your computer to a LAN port of the AP.

### 3. Access LuCI Interface
- **URL**: Navigate to `http://192.168.1.1` in your browser.
- **Login**: Log in and change the admin password if necessary.

### 4. Configure LAN Interface
- **Navigation**: Go to `Network → Interfaces`.
- **Edit LAN**: Click `Edit` on the LAN interface.
- **Set IP**: Under the `General Settings` tab, set a static IP address (e.g., 192.168.1.2).

### 5. Apply and Re-Navigate
- **Action**: Save and apply the new IP. Navigate to the new address (e.g., `http://192.168.1.2`).

### 6. Change IPv4 Gateway
- **Settings**: Go back to `Network → Interfaces → LAN interface → General Settings`.
- **Gateway IP**: Set the IPv4 gateway to your main router's IP (usually 192.168.1.1).

### 7. Configure DNS Settings
- **Location**: Go to the `Advanced Settings` tab.
- **DNS Server**: Enter your main router's IP in the `Use custom DNS servers` field.

### 8. Configure DHCP Server
- **Navigation**: Go to the `DHCP Server` tab → `General Setup`.
- **Disable DHCP**: Check the `Ignore interface` checkbox.

### 9. Disable IPv6 DHCP
- **Location**: In the `IPv6 Settings` sub-tab.
- **Disable Services**: Set `RA-Service`, `DHCPv6-Service`, and `NDP-Proxy` to disabled.

### 10. Physical Settings for Older OpenWrt Versions
- **Check**: If your OpenWrt version is older than 21.02.0, ensure "Bridge interfaces" is ticked under the `Physical Settings` tab.

### 11. Disable Unneeded Services
- **Navigation**: Go to `System → Startup`.
- **Disable Services**: Firewall, dnsmasq, and odhcpd services.

### 12. Adjust WAN Interfaces
- **Optional**: Remove or disable the WAN and WAN6 interfaces.

### 13. Configure Wireless Settings
- **Note**: Enable and configure your wireless settings if starting from a default installation.

### 14. Final Connections
- **Connection**: Use an Ethernet cable to connect a LAN port of your main router to a LAN port of the AP.

### 15. Reboot if Necessary
- **Action**: Reboot or power cycle the routers and connected devices if needed.

### 16. Finalization
- **Save**: Click `Save and Apply`. Your AP is now ready for use.

## Explanation

### Disconnecting the Wireless AP
This step ensures no network conflicts during configuration.

### Connecting to Computer
A direct Ethernet connection provides stable access to the router's settings.

### Accessing LuCI Interface
LuCI is the OpenWrt web interface. Changing the default password enhances security.

### Configuring LAN Interface
Assigning a static IP avoids IP conflicts. The IP should be in the same subnet as the main router but outside its DHCP range.

### Changing IPv4 Gateway and DNS Settings
These settings allow the AP to route traffic through the main router and use its DNS.

### DHCP and IPv6 DHCP Configuration
Disabling DHCP on the AP avoids IP conflicts, and disabling IPv6 is typically not needed for a simple AP setup.

### Physical Settings for Older OpenWrt Versions
For older versions, bridging interfaces is necessary for proper traffic flow.

### Disabling Unneeded Services and Adjusting WAN Interfaces
These steps simplify the setup and ensure the AP works solely as an access point.

### Wireless Settings and Final Connections
Configure wireless settings if needed and establish a physical connection between the main router and the AP.

### Rebooting if Necessary
Restarting ensures all settings are properly applied.

### Finalization
Saving and applying all changes completes the AP setup.
