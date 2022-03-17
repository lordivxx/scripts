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
