# Installation Guide for FOG Server on Ubuntu Server

This guide will walk you through the installation process of setting up a FOG Server on an Ubuntu Server. FOG is an open-source cloning/imaging solution used for managing and deploying computer systems. Follow these steps carefully to ensure a successful installation.

## Before You Begin:

- Ensure that you have a fresh Ubuntu Server installation.
- Take a snapshot or backup of your virtual machine to ensure you can revert in case of issues.

## Step 1: Update Your System

```bash
sudo apt-get update
sudo apt-get dist-upgrade -y
```

## Step 2: Switch to Root User (Optional)

```bash
sudo -i
```

Switching to the root user allows you to execute commands without using 'sudo' repeatedly.

## Step 3: Navigate to /opt/ Directory

```bash
cd /opt/
```

Navigate to the /opt/ directory to perform the FOG Server installation in a clean location.

## Step 4: Download FOG Server

```bash
git clone https://github.com/fogproject/fogproject.git fogproject-master
```

This command downloads the FOG Server files from the GitHub repository.

## Step 5: Prepare for Installation

After downloading the FOG Server files, ensure you are in the correct directory:

```bash
cd /opt/fogproject-master/bin
```

Now, you are ready to install the FOG Server.

## Step 6: Launch FOG Server Installer

```bash
./installfog.sh
```

Follow the prompts carefully:

- Choose Installation Type: Choose 'N' for Normal installation.
- Enter IP Address: Use the IP address you set earlier.
- Change Network Interface: Choose 'N' to keep the default network interface.
- Router Address: Enter the IP address of your router/DHCP server.
- DHCP Handling of DNS: Choose 'Y'.
- DNS Address: Enter the IP address of your router or DNS server.
- Use FOG Server for DHCP: Choose 'N'.
- Internationalization Support: Choose 'N' unless you need it.
- HTTPS support: Choose 'N'.
- Confirm Installation: Verify the settings and confirm with 'Y'.

### MySQL Password (Optional)

In some cases, you may be asked to set a MySQL password during the installation process. If prompted, you can leave it empty and press Enter without a security risk. You can change it later if needed.

## Step 7: Update the Database

After the installation is complete, open a web browser on your local machine and access your FOG Server's management interface:

```
http://your_server_ip/fog/management/
```

Use the default credentials:

- Username: fog
- Password: password
  **KEEP DEFAULT TO MAKE IT EASY FOR FUTURE USERS**

Follow any prompts to update the database.

## Step 8: Reboot the Server

```bash
reboot now
```

After the server restarts, log in to the FOG Server's management interface again via your web browser.

## Step 9: Setting Netboot

For UEFI devices like the Latitude laptops, we'll need to utilize the "snponly.efi" file. The Z230 workstations, by default, are set to BIOS mode, but it's possible to switch to either Legacy or UEFI boot options by performing a quick online search.

To set up the PXE boot file, follow these steps:

- Access the web address of the newly created pfSense router, which, in our case, involves plugging into the PXE switch we've established and entering "192.168.4.1" in your browser.
- Login and navigate to "Services" > "DHCP Server."
- Scroll down to the "Network Booting" section and enable it.
- Enter the IP address of our FOG server
- Insert the "snponly.efi" file into the default BIOS file name.
- Save the settings, and you're all set. You should now be able to boot into the network interface and access the FOG boot file via Ethernet.