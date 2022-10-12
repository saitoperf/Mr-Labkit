#!/bin/bash

ansible-playbook -bK -i inv.ini \
    play-ldap-server.yml \
    play-sssd-client.yml \
    play-samba-server.yml \
    play-prom-server.yml \
    play-prom-client.yml \
    play-nfs-server.yml \
    play-nfs-client.yml \
    play-gitlab-server.yml

# ansible-playbook -bK -i inv.ini play-ldap-server.yml
# ansible-playbook -bK -i inv.ini play-sssd-client.yml

# ansible-playbook -bK -i inv.ini play-samba-server.yml
# ansible-playbook -bK -i inv.ini play-prom-server.yml
# ansible-playbook -bK -i inv.ini play-prom-client.yml

# ansible-playbook -bK -i inv.ini play-nfs-server.yml
# ansible-playbook -bK -i inv.ini play-nfs-client.yml
# ansible-playbook -bK -i inv.ini play-gitlab-server.yml

# 冪等性
## ok
### ldap, gitlab

## not
###