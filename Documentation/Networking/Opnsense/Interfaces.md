# OPNsense Interface and DHCP Server Configuration Guide

This guide outlines the steps to configure interfaces and set up DHCP servers on OPNsense for four main interfaces: WAN, LAN (Sillynet/Cyber), and two virtual interfaces for Stemlab and Stemlabcafe.

## Step 1: Configure Virtual Interfaces

1. **Login to OPNsense Router:**
   - Ensure the LAN is correctly set up with the DHCP server during installation.
   - Access the router at `172.16.1.1`.

2. **Create VLAN Interfaces:**
   - Navigate to `Interfaces > Other Types > VLAN`.
   - Click the `Add` button and configure the VLAN interfaces as follows:

   **Stemlab Cafe Interface:**
   - Device: `vlan0.10`
   - Parent: `igb0` (LAN)
   - VLAN Tag: `10`
   - Description: `Stemlab Cafe`

   **Stemlab Interface:**
   - Device: `vlan0.100`
   - Parent: `igb0` (LAN)
   - VLAN Tag: `100`
   - Description: `Stemlab`

3. **Assign VLAN Interfaces:**
   - Go to `Interfaces > Assignments`.
   - Click `Add` twice to add both VLAN interfaces.
   - You should now see `OPT4` and `OPT5`. Note which interface corresponds to Stemlab and Stemlab Cafe.

## Step 2: Configure Interface Settings

1. **Stemlab Cafe (VLAN 10):**
   - Click on the interface `OPT4` or `OPT5` that corresponds to Stemlab Cafe.
   - Check `Enable Interface`.
   - Description: `igb010`
   - IPv4 Configuration Type: `Static IPv4`
   - IPv4 Address: `10.0.0.1/24`
   - Save and Apply.

2. **Stemlab (VLAN 100):**
   - Select the interface corresponding to Stemlab.
   - Check `Enable Interface`.
   - Description: `igb0100`
   - IPv4 Configuration Type: `Static IPv4`
   - IPv4 Address: `192.168.100.1/24`
   - Save and Apply.

## Step 3: Configure DHCP Servers

1. **Stemlab Cafe DHCP Server (VLAN 10):**
   - Navigate to `Services > ISC DHCPv4 > igb010`.
   - Enable DHCP Server.
   - Range: `10.0.0.20 - 10.0.0.254`
   - Save and Apply.

2. **Stemlab DHCP Server (VLAN 100):**
   - Go to `Services > ISC DHCPv4 > igb0100`.
   - Enable DHCP Server.
   - Range: `192.168.100.20 - 192.168.100.254`

  <div style="border: 1px solid red; padding: 10px; background-color: #f8d7da; color: #721c24;">
   <strong>WARNING:</strong>
   <ul>
      <li>Edit the DNS to point to your Active Directory server to resolve hostnames such as <code>cyber.lan</code>.</li>
      <li>This will bypass the captive portal redirection, meaning users will not log in through the captive portal. This is acceptable as this network is not intended for user access.</li>
      <li>Access the captive portal via <code>192.168.100.1</code>.</li>
      <li>Whitelist devices by MAC address to allow network access.</li>
   </ul>
</div>

   - Save and Apply.

## Conclusion

The configuration of the VLAN interfaces and DHCP servers on OPNsense is now complete. Ensure that the LAN interface was correctly set up during the installation, and no further adjustments are needed for it. If additional configurations or troubleshooting is required, refer to the OPNsense documentation or support resources.
