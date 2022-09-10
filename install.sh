#!/bin/bash

ansible-playbook -bK -i inv.ini play-ldap-server.yml

ansible-playbook -bK -i inv.ini play-sssd-client.yml

ansible-playbook -bK -i inv.ini play-samba-server.yml

ansible-playbook -bK -i inv.ini play-nfs-server.yml
ansible-playbook -bK -i inv.ini play-nfs-client.yml

ansible-playbook -bK -i inv.ini play-prom-client.yml
ansible-playbook -bK -i inv.ini play-prom-server.yml
