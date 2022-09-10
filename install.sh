ansible-playbook -bK -i inv.ini play-ldap.yml

ansible-playbook -bK -i inv.ini play-sssd-serv.yml
ansible-playbook -bK -i inv.ini play-sssd-calc.yml

ansible-playbook -bK -i inv.ini play-samba.yml

ansible-playbook -bK -i inv.ini play-nfs-serv.yml
ansible-playbook -bK -i inv.ini play-nfs-calc.yml