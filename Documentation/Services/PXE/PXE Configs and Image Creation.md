Images Required:
Robotics Windows 11 VMware, Arduino, Chrome
Cyber Windows 11
Cyber Ubuntu Latest Version

### 1. Accessing the PXE Server
- First, determine the IP address of your PXE server. This can usually be found in the server's documentation or by checking the network topology. If you're using Proxmox, you can obtain the IP by running `ip a` in the proxy VM.
- Open a web browser and navigate to `http://<YourPXEIP>/fog` to access the PXE server's interface.

### 2. Login
- Use the username `fog` and the password `password` to log in.

### 3. Configure Server Settings
- Click on the wrench icon to open the **FOG Configuration**.
- Navigate to **FOG Settings** on the left panel.
- Click **Expand All** and scroll down to **FOG Boot Settings**.
- Change the **PXE Menu Timeout** setting from 3 to 0. This prevents the PXE from exiting if no key is pressed within 3 seconds, which is useful when managing multiple devices.

### 4. Registering a Laptop
- Connect the laptop to a switch that is part of VLAN1 or any other VLAN where PXE is available (refer to your network configurations for details).
- Turn on the laptop and repeatedly press F12 to enter the boot menu. Select **NIC IPV4**.
- The screen should display a message from https://IPXE.org and then boot into the FOG menu.
- Perform a full check-in and registration. Assign the computer a name according to its tag (e.g., RB14).
- Do not change other default settings or deploy an image yet.

### 5. Creating and Capturing Images
- Return to the FOG web panel.
- Click on the **Images** icon and choose **Create New Image**.
- Name the image appropriately (e.g., Windows10/11 or Ubuntu23) and select the operating system from the dropdown.
- Most settings should be left at their defaults. Scroll down and click **Add**.
- Go to **Hosts** (the computer icon), select **List All**.
- Click the orange **Capture** icon next to the desired host, select the appropriate image from the dropdown (e.g., Windows 10), and leave all other settings default. Click **Update**.
- Select the host you want to capture (e.g., RB14), go to **Basic Task** at the top, and choose **Capture Image**. Leave the settings default and click the **Task** button.
- Plug the computer back into the PXE switch, restart it, press F12, and boot from NIC IPV4. It should immediately start capturing the image.

