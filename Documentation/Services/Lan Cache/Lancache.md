Sure, I'll modify the documentation to use OMV instead of OMVV (assuming OMVV was a typo), and I'll update the Docker installation instructions as requested.

# OpenMediaVault Installation and Configuration Documentation


---

## 1. Introduction

This documentation provides step-by-step instructions for installing and configuring OpenMediaVault (OMV) and setting up a Lancache server on OMV to optimize game download speeds and manage network bandwidth more effectively.

### Prerequisites

- Hardware compatible with OMV and TrueNAS SCALE.
- Access to the OMV web interface.
- Access to a pfSense router.
- SSH access to OMV.

---

## 2. Installing OpenMediaVault

1. Install OpenMediaVault on your hardware following the official installation guide.

2. After installation, access the OMV web interface using a web browser. The default credentials are:
   - Username: `admin`
   - Password: `openmediavault`

---

## 3. Configuring Disks

1. In the OMV web interface, go to **Storage** > **Disks**.

2. Ensure that all your disks are detected and listed.

3. Select each disk and choose to wipe them to prepare for RAID configuration.

---

## 4. Creating a RAID 5

1. In the OMV web interface, go to **Storage** > **RAID Management**.

2. Create a new RAID 5 array and select all the wiped drives to be a part of it.

---

## 5. Creating a Filesystem

1. In the OMV web interface, go to **Storage** > **File Systems**.

2. Create a new filesystem of type EXT4 on the newly created RAID partition. This process may take a considerable amount of time.

3. Note the mount path of this filesystem. Enable the filter to show the mount point, and copy it (e.g., `/srv/dev-disk-by-uuid-5c3b05d6-ddcc-4bbe-be8d-4a25de3c1d39`).

---

## 6. Setting Static IP in pfSense

1. Access the pfSense router web interface.

2. Set a static IP address for the OMV server (e.g., `172.16.16.110`).

3. Restart the OMV server to apply the new IP configuration.

---

## 7. Installing Docker and Docker Compose

1. SSH into the OMV server using the command: `ssh admin@172.16.16.110` (replace with your server's IP).

2. Install Docker and Docker Compose using the following commands:

   ```bash
   sudo apt update
   sudo apt install docker.io
   sudo systemctl enable docker
   sudo systemctl start docker
   sudo apt install docker-compose
   sudo apt install apparmor
   sudo systemctl enable apprmor
   ```

---

## 8. Configuring Lancache

1. Navigate to the cache directory on OMV SCALE, typically located at `/srv/dev-disk-by-uuid-5c3b05d6-ddcc-4bbe-be8d-4a25de3c1d39`.

2. Clone the Lancache repository and navigate to it:

   ```bash
   git clone https://github.com/lancachenet/docker-compose lancache
   cd lancache
   ```

3. Edit the `.env` file with your preferred text editor (e.g., `sudo nano .env`) and set the necessary configurations:
   - `LANCACHE_IP` and `DNS_BIND_IP`: Set these to the static IP of OMV (e.g., `172.16.16.110`).
   - `UPSTREAM_DNS`: Set this to your Pi-hole or primary DNS server IP (e.g., `172.16.16.40`).
   - `CACHE_ROOT`: Point to your cache directory (e.g., `/mnt/NAS/Data/cache`).

---

## 9. Launching Lancache

1. Run the following command to start the Lancache Docker instance:

   ```bash
   sudo docker-compose up -d
   ```

---

## 10. Integrating with Network DNS

If you are using a Zentyal or AD/LDAP server:

1. Configure the DNS settings on your network to forward requests to the Lancache server.

2. Set Lancache's IP address (e.g., `172.16.16.110`) as the new forwarder.

---

## 11. Testing the Configuration

1. Test the Lancache configuration by running the following command on a client machine:

   ```bash
   nslookup steam.cache.lancache.net
   ```

   It should resolve to the IP address of the OMV server.

2. Ensure that you have connectivity to the internet and internal network resources, such as `cybersecurity.lan` or your AD/LDAP server.

---

## 12. Conclusion

Following these steps, you have successfully set up OpenMediaVault with RAID, Lancache and integrated it with your network's DNS. This configuration will optimize game download speeds and efficiently manage network bandwidth. Regularly check and update your Lancache configurations as needed to ensure optimal performance.