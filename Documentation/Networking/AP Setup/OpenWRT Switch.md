# OpenWrt Firmware Installation Guide for Linksys E2500

This documentation provides step-by-step instructions for flashing your Linksys E2500 router with OpenWrt firmware and configuring essential settings using the LuCI web interface.

## Flashing OpenWrt Firmware

1. **Prepare the Router:** Locate the recessed reset button on the back of your Linksys E2500 router. Use a pin or similar tool to press and hold the reset button for 10 seconds.

2. **Connect to the Router:** Disconnect the WAN (yellow) port and connect your computer to one of the LAN (blue) ports on the router using an Ethernet cable. Ensure your computer is disconnected from any wireless networks.

3. **Access Router Interface:** Open a web browser and enter `192.168.1.1` into the address bar. Choose the unsecure configuration option to bypass initial setup.

4. **Login:** Enter `admin` as both the username and password to access the router's interface.

5. **Upgrade Firmware:** Navigate to the Administration section and select the option to upgrade firmware. Download the OpenWrt firmware for Linksys E2500 from [https://openwrt.org/toh/linksys/e2500_v3](https://openwrt.org/toh/linksys/e2500_v3) and upload the file.

## Configuring OpenWrt Settings

1. **Access LuCI Interface:** Open a web browser and go to `http://192.168.1.1`. Log in with your username and password (default is `admin`). Change the admin password if prompted.

2. **Configure LAN Interface:**
   - Navigate to `Network → Interfaces`.
   - Click on the edit icon for the LAN interface.
   - Under the General Settings tab, assign a static IP address (e.g., `192.168.1.2`).

3. **Apply Changes:** Save and apply the new IP address settings. Navigate to the new IP address (e.g., `http://192.168.1.2`).

4. **Change IPv4 Gateway:**
   - Return to `Network → Interfaces → LAN interface → General Settings`.
   - Change the Gateway IP setting from static to DHCP client.

5. **Configure DNS Settings:**
   - Go to the Advanced Settings tab.
   - Uncheck "Use DNS servers advertised by peer."
   - Enter your main router's IP address in the Use custom DNS servers field.

6. **Configure DHCP Server:**
   - Navigate to the DHCP Server tab → General Setup.
   - Check the Ignore interface checkbox to disable DHCP.

7. **Disable IPv6 DHCP:**
   - Under IPv6 Settings sub-tab, disable RA-Service, DHCPv6-Service, and NDP-Proxy.

8. **Physical Settings for Older OpenWrt Versions:**
   - If your OpenWrt version is older than 21.02.0, ensure "Bridge interfaces" is enabled under the Physical Settings tab.

9. **Disable Unneeded Services:**
   - Navigate to System → Startup.
   - Disable Firewall, dnsmasq, and odhcpd services.
