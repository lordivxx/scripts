#!/bin/bash -l

dnf update -y
systemctl enable --now cockpit.socket
dnf install -y cockpit-pcp cockpit-machines
adduser researchcomputing
echo researchcomputing:new_password | chpasswd
usermod -aG users,wheel researchcomputing
dnf install -y https://github.com/45Drives/cockpit-navigator/releases/download/v0.5.8/cockpit-navigator-0.5.8-1.el8.noarch.rpm
dnf install -y cockpit-pcp cockpit-packagekit cockpit-storaged
dnf install -y htop
rm /etc/systemd/system/rpcbind.service
systemctl enable rpcbind && systemctl start rpcbind
dnf install -y nfs-utils
systemctl start nfs-server.service
dnf install -y cockpit-file-sharing
wget http://www.ni-sp.com/wp-content/uploads/2019/10/SLURM_installation.sh
export VER=21.08.5
bash SLURM_installation.sh

systemctl enable libvirtd
systemctl start libvirtd

echo """
<network>
  <name>default</name>
  <uuid>6eba00f5-1ab3-4efa-971b-2621607edf10</uuid>
  <forward dev='eth0' mode='nat'>
    <interface dev='eth0'/>
  </forward>
  <bridge name='virbr0' stp='on' delay='0'/>
  <mac address='52:54:00:ae:72:e5'/>
  <domain name='default' localOnly='yes'/>
  <dns>
    <host ip='10.4.20.1'>
      <hostname>gateway</hostname>
    </host>
  </dns>
  <ip address='10.4.20.1' netmask='255.255.255.0' localPtr='yes'>
    <dhcp>
      <range start='10.4.20.10' end='10.4.20.20'/>
    </dhcp>
  </ip>
</network>
""" > default.xml


virsh net-define default.xml
virsh net-start default
virsh net-autostart default


mkdir -p /vhpc/opt/bin
mkdir -p /vhpc/storage-pool
mkdir -p /vhpc/opt/modules

virsh pool-create-as --name vhpc --type dir --target /vhpc/storage-pool --print-xml > vhpc-storage-pool-shorter.xml
virsh pool-define vhpc-storage-pool-shorter.xml && virsh pool-start vhpc && virsh pool-autostart vhpc

virsh vol-create-as --pool vhpc --name n1 --capacity 10G --format qcow2

