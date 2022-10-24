#!/bin/bash

k8s-create(){
    ansible-playbook -bK -i inv.ini \
        play-k8s-create-common.yml \
        play-k8s-create-m.yml \
        play-k8s-create-w.yml
}

k8s-delete(){
    ansible-playbook -bK -i inv.ini \
        play-k8s-delete-m.yml \
        play-k8s-delete-w.yml
}

baremetal(){
    ansible-playbook -bK -i inv.ini \
        play-ldap-server.yml \
        play-sssd-client.yml \
        play-samba-server.yml \
        play-prom-server.yml \
        play-prom-client.yml \
        play-gitlab-server.yml \
        play-nfs-server.yml \
        play-nfs-client.yml
    sed -i -e "s/\/c[1-99]\//\/s1\//g" inv.ini
}

if [ "$1" = 'vagrant' ]; then
    rm ~/.ssh/known_hosts
    vagrant destroy -f
    vagrant up --provider=libvirt
    yes yes | ansible-playbook -bK -i inv.ini play-vagrant.yml
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
    # 認証に使う秘密鍵のディレクトリを変える
    sed -i -e "s/\/c[1-99]\//\/s1\//g" inv.ini
elif [ "$1" = 'gitlab' ]; then
    if [ "$2" = "get-pass" ]; then
        vagrant ssh s1 -- docker exec gitlab grep 'Password:' /etc/gitlab/initial_root_password
    else
        ansible-playbook -bK -i inv.ini play-gitlab-server.yml
    fi
elif [ "$1" = 'baremetal' ]; then
    baremetal
elif [ "$1" = 'k8s-create' ]; then
    k8s-create
elif [ "$1" = 'k8s-delete' ]; then
    k8s-delete
elif [ "$1" = 'all' ]; then
    baremetal
    k8s
else
    echo 'Usage: ./run.sh [OPTION]'
    echo 'options'
    echo '    generate      : Run File generator'
    echo '    vagrant       : Provision VM'
    echo '    baremetal     : Install baremetal services'
    echo '    k8s-create    : Provisioning k8s cluster'
    echo '    k8s-delete    : Delete k8s cluster'
    echo '    all           : Install all services'
    echo '    ldap          :'
    echo '    sssd          :'
    echo '    samba         :'
    echo '    prom-server   :'
    echo '    prom-client   :'
    echo '    nfs-server    :'
    echo '    nfs-client    :'
    echo '    gitlab        : get-pass'
fi
