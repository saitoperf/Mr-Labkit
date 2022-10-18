#!/bin/bash

if [ "$1" = 'vagrant' ]; then
    rm ~/.ssh/known_hosts
    vagrant destroy -f
    vagrant up --provider=libvirt
    ansible-playbook -bK -i inv.ini play-vagrant.yml
elif [ "$1" = 'generate' ]; then
    ./FileGenerator.py 
elif [ "$1" = 'ldap' ]; then
    ansible-playbook -bK -i inv.ini play-ldap-server.yml
elif [ "$1" = 'sssd' ]; then
    ansible-playbook -bK -i inv.ini play-sssd-client.yml
elif [ "$1" = 'samba' ]; then
    ansible-playbook -bK -i inv.ini play-samba-server.yml
elif [ "$1" = 'prom-server' ]; then
    ansible-playbook -bK -i inv.ini play-prom-server.yml
elif [ "$1" = 'prom-client' ]; then
    ansible-playbook -bK -i inv.ini play-prom-client.yml
elif [ "$1" = 'nfs-server' ]; then
    ansible-playbook -bK -i inv.ini play-nfs-server.yml
elif [ "$1" = 'nfs-client' ]; then
    ansible-playbook -bK -i inv.ini play-nfs-client.yml
elif [ "$1" = 'gitlab' ]; then
    ansible-playbook -bK -i inv.ini play-gitlab-server.yml
elif [ "$1" = 'all' ]; then
    ansible-playbook -bK -i inv.ini \
    play-ldap-server.yml \
    play-sssd-client.yml \
    play-samba-server.yml \
    play-prom-server.yml \
    play-prom-client.yml \
    play-nfs-server.yml \
    play-nfs-client.yml \
    play-gitlab-server.yml
else
    echo 'Usage: ./run.sh [OPTION]'
    echo 'options'
    echo '    generate: Run File generator'
    echo '    vagrant : Provision VM'
    echo '    all     : Install all services'
    echo '    ldap, sssd, samba, prom-server, prom-client, nfs-server, nfs-client, gitlab'
fi
