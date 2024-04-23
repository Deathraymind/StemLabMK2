# TFTP Server Setup on Linux using Tftpd-hpa

This documentation provides step-by-step instructions for setting up a TFTP (Trivial File Transfer Protocol) server on a Linux system using the Tftpd-hpa package. TFTP is commonly used for network booting and transferring files between devices.

## Step 1: Install Tftpd-hpa

1. Open a terminal window on your Linux machine.

2. Install the Tftpd-hpa package using the following command:

   ```bash
   sudo apt-get install tftpd-hpa
   ```

   If you're using a different Linux distribution, use its package manager to install Tftpd-hpa.

## Step 2: Configure Tftpd-hpa

1. Edit the Tftpd-hpa configuration file located at `/etc/default/tftpd-hpa` using your preferred text editor. In this example, we'll use the `nano` text editor:

   ```bash
   sudo nano /etc/default/tftpd-hpa
   ```

2. Inside the configuration file, configure the following options:

   ```bash
   # /etc/default/tftpd-hpa

   TFTP_USERNAME="tftp"
   TFTP_DIRECTORY="/tftp"
   TFTP_ADDRESS=":69"
   TFTP_OPTIONS="--secure --create"
   ```

   - `TFTP_USERNAME`: Set the TFTP server's username, which is typically "tftp."
   - `TFTP_DIRECTORY`: Specify the directory from which TFTP will serve files. In this example, we've set it to `/tftp`.
   - `TFTP_ADDRESS`: Specify the TFTP server's listening address and port. The default port is 69.
   - `TFTP_OPTIONS`: Configure any additional TFTP options. In this example, we use `--secure` to enable security checks and `--create` to allow file creation.

3. Save the changes and exit the text editor.

## Step 3: Create the TFTP Directory

1. Create the directory specified in the `TFTP_DIRECTORY` variable. In this example, we use `/tftp`:

   ```bash
   sudo mkdir -p /tftp
   ```

## Step 4: Set Permissions

1. Adjust the permissions on the TFTP directory to ensure that files can be read and written by the TFTP server:

   ```bash
   sudo chown -R nobody:nogroup /tftp
   ```


   ```bash 
   sudo ufw allow 69
   ```

To move the files to the /tftp directory use this command

   ```bash
   mv ArubaInstant_Taurus_6.5.4.25_86114 /tftp
   ```

## Step 5: Restart Tftpd-hpa

1. After configuring and creating the TFTP directory, restart the Tftpd-hpa service to apply the changes:

   ```bash
   sudo systemctl restart tftpd-hpa
   ```

## Step 6: Test the TFTP Server

1. To test your TFTP server, you can use a TFTP client. In this example, we use the `tftp` command to test it locally:

   ```bash
   tftp localhost
   ```

2. Within the TFTP client, you can use the `get` and `put` commands to retrieve or send files to the TFTP server:

   - To retrieve a file from the TFTP server:

     ```bash
     tftp> get testfile.txt
     ```

   - To send a file to the TFTP server:

     ```bash
     tftp> put testfile.txt
     ```

   Replace `localhost` with the IP address or hostname of your TFTP server if you're testing from a different machine. Ensure that the file you're trying to retrieve or send exists in the TFTP directory.

## Step 7: Managing File Permissions

1. To avoid errors, ensure that the file you add to the TFTP directory has appropriate permissions. You can use the following command to set permissions on a specific file, for example, `file.bin`:

   ```bash
   sudo chmod 666 /tftp/file.bin
   ```

Your TFTP server is now set up and ready to serve files. You can use it for tasks such as network booting or transferring configuration files to network devices.