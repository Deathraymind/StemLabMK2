

## Overview

This document provides detailed steps to set up captive portals for VLAN 10 (Stemlab Cafe) and VLAN 100 (Stemlab24). The Stemlab Cafe portal will use a voucher system for user authentication, while Stemlab24 will use MAC address whitelisting to grant access to devices.

## Step 1: Adding Voucher Server

1. **Navigate to System > Servers**:
   - Go to the System menu and select Servers.
2. **Add a New Voucher Server**:
   - Click on the "Add" button to create a new server.
   - **Server Type**: Voucher.
   - **Description**: Stemlab Cafe Voucher Server.
   - **Username Length**: 4 (can be higher for increased security).
   - **Password Complexity**: Use a simple password to ensure ease of use for the users.
   - **Voucher Duration**: Set the duration as needed (e.g., one week, one month, one year).
3. **Save the Voucher Server**:
   - Click on the "Save" button to add the server.

4. **Add a Local Database Server**:
   - Click on the "Add" button again to create another server.
   - **Server Type**: Local Database.
   - **Description**: Local Database for Network Admins.
   - **Username Length**: 4 (or higher if needed).
   - **Password Complexity**: Ensure it is easy to use but secure.
   - Click on the "Save" button to add the server.

## Step 2: Configuring the Captive Portal for Stemlab Cafe

1. **Navigate to Services > Captive Portal**:
   - Go to the Services menu and select Captive Portal.
2. **Add a New Captive Portal**:
   - Click on the "Add" button to create a new captive portal.
   - **Name**: Stemlab Cafe.
   - **Interface**: Select the interface corresponding to VLAN 10 (e.g., igb010).
   - **Authentication**: Select the Stemlab Cafe Voucher Server created earlier.
   - **Concurrent user logins**: Uncheck this so that vouchers are one time use. 
   - **Description**: Stemlab Cafe.
3. **Save the Captive Portal Configuration**:
   - Click on the "Save" button to activate the captive portal for Stemlab Cafe.

## Step 3: Configuring the Captive Portal for Stemlab24

1. **Add a New Captive Portal for VLAN 100**:
   - While still in the Captive Portal menu, click on the "Add" button to create another captive portal.
   - **Name**: Stemlab24.
   - **Interface**: Select the interface corresponding to VLAN 100.
   - **Authentication**: Leave it blank unless a group of network admins is to be created. If so, select the Local Database server.
   - **Description**: Stemlab24.
2. **Configure MAC Address Whitelisting**:
   - Ensure that the devices that need access to this network are manually added to the MAC address whitelist.
   - This can be done in the Captive Portal settings under the MAC Authentication tab.
3. **Save the Captive Portal Configuration**:
   - Click on the "Save" button to activate the captive portal for Stemlab24.

## Step 4: Managing Vouchers and Whitelist

1. **Generating Vouchers**:
   - Go to the Voucher server settings to generate and manage vouchers for Stemlab Cafe users.
   - Print or distribute the vouchers as needed.
2. **Managing MAC Addresses**:
   - Regularly update the MAC address whitelist to ensure only authorized devices have access to Stemlab24.
   - This can be done through the Captive Portal settings under the MAC Authentication tab.

## Conclusion

By following these steps, you will have successfully set up captive portals for both VLAN 10 (Stemlab Cafe) using a voucher system and VLAN 100 (Stemlab24) using MAC address whitelisting. Ensure regular maintenance and monitoring to keep the network secure and accessible to authorized users.

---
