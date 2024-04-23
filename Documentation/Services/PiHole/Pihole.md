

# Setting Up Pi-hole on Ubuntu

It is recommended to have a dedicated device to this sinkhole as we are going to be messing with the DNS name servers of the host device, which could conflict with other services. 

## Check Port 53 Usage

Before setting up Pi-hole, make sure port 53 is available by checking which process is currently using it.

```bash
sudo lsof -i -P -n | grep LISTEN
```

It is likely that `systemd-resolved` is listening on port 53. To free up the port, disable and stop `systemd-resolved`:

```bash
sudo systemctl disable systemd-resolved.service
sudo systemctl stop systemd-resolved
```

## Configure DNS for Your Host

Edit the `/etc/resolv.conf` file to specify your DNS server. For example, using Google's DNS server:

```bash
sudo nano /etc/resolv.conf
```

Add the following line to the file:

```plaintext
nameserver 8.8.8.8
```

If there are other nameservers listed, consider commenting them out to avoid conflicts.

## Install Pi-hole with Docker

To install Pi-hole with Docker, run the following command:

```bash
curl -sSL https://install.pi-hole.net | bash
```

To change the Pi-hole admin password, use the following command:

```bash
sudo pihole -a -p
```

# Configuring pfSense

## Configure DNS Servers in pfSense

1. Log in to pfSense's web interface: https://172.16.0.1/ (Use your pfSense server's IP address).

2. Navigate to `System` > `General Setup`.

3. In the "DNS Server Settings" section, set the top DNS server to the IP address of your Pi-hole (e.g., 172.16.16.40).

4. Set the secondary DNS server to a reliable external DNS server, such as Google's DNS (e.g., 8.8.8.8).

## Configure DHCP Server in pfSense

1. Go to `Server` > `DHCP Server`.

2. Scroll down to "Server Options."

3. Set the top DNS server to the IP address of your Pi-hole (e.g., 172.16.16.40).

4. Set the secondary DNS server to a reliable external DNS server (e.g., 8.8.8.8).

5. Save, apply, and refresh the DHCP settings on your devices.

# Verify Pi-hole Operation

After completing these steps, Pi-hole should be blocking queries. For example, when visiting a website like cnn.com, you should see blocked queries on the Pi-hole dashboard.

**Note:** Ensure that your Pi-hole container is running and configured to bind port 53 to the host machine.

This documentation provides a step-by-step guide for setting up Pi-hole on Ubuntu and configuring DNS settings in pfSense. Users can follow these instructions to create a working Pi-hole setup for network-wide ad-blocking.