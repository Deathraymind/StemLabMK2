On opnsense you have to make specific interfaces first, we have 4 main interfaces we need to create. WAN which sould be good to go already and then LAN for Sillynet aka cyber and two virtual interfaces for Stemlab and Stemlabcafe.

So lets start by making the virtual interfaces. login to the opnsense router which sould be 172.16.1.1 if you set the LAN correctly and DHCP server while installing.

Go to interfaces>Other types>VLAN and select the add button and configure the two VLAN interfaces as shown below

Device:Vlan0.10
parent:igb0 aka LAN
vlan tag:10 
Descritption: stemlab cafe

Device vlan0.100 
Parent:igb0 aka LAN
VLAN tag:100
Description:stemlab cafe

Now we need to make these actual interfaces we can apply services too.

goto interfaces>Assignments

simply click add two times so that both of our interfaces are added

Now you sould see OPT4 and OPT5 please look at which interface is stemlab and cafe to procede to the next steps

click on the interface OPT4 or OPT5 that is stemlab cafe or vlan 10

check enable interface
description:igb010
IPv4 Configuration: Type Static ipv4
IPv4 Address: 10.0.0.1/24

save apply
Now select the interface that corolates to the stemlab

enable the interface
description: igb0100
IPv4 Configuration Type: static IPv4
IPv4 address 192.168.100.1/24 

save apply

Now were done with the actaul vlan interfaces note that LAN sould already be set up correctly during the install process so we dont have to touch it. 


DHCP Servers


We want to create a dhcp server so we can hand out IPs to newly connected devices so to do this go to Services>ISC DHCPv4>igb010

this was our vlan10 interface aka stemlab cafe

enable dhcp server
range:10.0.0.20 - 10.0.0.254

save apply were not going to need to edit DNS or else captive portal will not work 

now go to Services>ISC DHCPv4>igb0100

Enable DHCP Server
192.168.100.20 - 192.168.100.254

WARNING
you are going to need to edit the DNS to point to youre active directory server so its hostname such as cyber.lan can be resolved. Now the issue with this is it will bypass the captive portal redirection meaning that the user will not be able to login, this however is perfectly fine as we dont really want users to be accsessing this network. The login for the captive portal will ofcourse still be accsessed via 192.168.100.1. However devices on this network sould be whitelisted via mac address. So when you join a new DELL laptop or ardiono it will not be able to accsess the internet and parts of the network until it is whitelisted in the captive portal area. 
END OF WARNING

Save and Apply




