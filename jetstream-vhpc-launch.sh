#!/bin/bash -l

dnf update -y
systemctl enable --now cockpit.socket
dnf install -y cockpit-pcp cockpit-machines
adduser researchcomputing
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
<network connections='3'>
  <name>default</name>
  <uuid>6eba00f5-1ab3-4efa-971b-2621607edf10</uuid>
  <forward dev='eth0' mode='nat'>
    <nat>
      <port start='1024' end='65535'/>
    </nat>
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
      <host mac='52:54:00:b8:21:17' ip='10.4.20.11'/>
      <host mac='52:54:00:55:d3:1e' ip='10.4.20.12'/>
      <host mac='52:54:00:09:1b:34' ip='10.4.20.13'/>
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

#virsh vol-create-as --pool vhpc --name n1 --capacity 10G --format qcow2
#virsh vol-create-as --pool vhpc --name n2 --capacity 10G --format qcow2
#virsh vol-create-as --pool vhpc --name n3 --capacity 10G --format qcow2

echo """
10.4.20.1 vhpc
10.4.20.11 n1
10.4.20.12 n2
10.4.20.13 n3
""" >> /etc/hosts

dnf -y install pdsh pdsh-rcmd-ssh environment-modules

echo "/vhpc/opt/modules" > /etc/environment-modules/modulespath

pip install gdown 

gdown https://drive.google.com/drive/folders/1170b6nraaleesZqaLksft6XauyoZ96pZ?usp=sharing -O ./ --folder

cd jetstream-vhpc && tar -zxvf n1.tar.gz && cd ..

cp jetstream-vhpc/n1 /vhpc/storage-pool/n1
cp jetstream-vhpc/n1 /vhpc/storage-pool/n2
mv jetstream-vhpc/n1 /vhpc/storage-pool/n3

virsh define jetstream-vhpc/n1.xml
virsh define jetstream-vhpc/n2.xml
virsh define jetstream-vhpc/n3.xml

virsh autostart n1 
virsh autostart n2 
virsh autostart n3 

virsh start n1
virsh start n2
virsh start n3

sleep 30

cp jetstream-vhpc/vhpc /root/.ssh/vhpc
chmod 400 /root/.ssh/vhpc
cp jetstream-vhpc/vhpc.pub /root/.ssh/vhpc.pub
cp jetstream-vhpc/config /root/.ssh/config
cat .ssh/vhpc.pub >> .ssh/authorized_keys

