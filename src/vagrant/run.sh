#!/bin/bash

rm ~/.ssh/known_hosts
vagrant up --provider=libvirt
ansible-playbook -bK -i inv.ini play.yml
