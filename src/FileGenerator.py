#!/bin/python3

import yaml
import ipaddress

class NomalFile:
    def __init__(self, vars_yml):
        with open(vars_yml, 'r') as f:
            self.vars = (yaml.safe_load(f))

    def replace_variable(self, filename):
        replaced = list()
        with open(filename, 'r') as f:
            for line in f:
                if '{{ user }}' in line:
                    line = line.replace('{{ user }}', self.vars['user'])
                if '{{ serverip }}' in line:
                    line = line.replace('{{ serverip }}', self.vars['serverip'])
                if '{{ subnet }}' in line:
                    line = line.replace('{{ subnet }}', self.vars['subnet'])
                if '{{ subnetmask }}' in line:
                    line = line.replace('{{ subnetmask }}', self.vars['subnetmask'])
                if '{{ k8s_masterip }}' in line:
                    line = line.replace('{{ k8s_masterip }}', self.vars['k8s']['masterip'])
                if '{{ gateway }}' in line:
                    line = line.replace('{{ gateway }}', self.vars['gateway'])
                if '{{ gitlab_name }}' in line:
                    line = line.replace('{{ gitlab_name }}', self.vars['gitlab']['name'])
                if '{{ gitlab_password }}' in line:
                    line = line.replace('{{ gitlab_password }}', self.vars['gitlab']['password'])
                replaced.append(line)
        return replaced
    
    def out_file(self, replaced, filename):
        with open(filename, 'w') as f:
            for r in replaced:
                f.write(r)

class PromFile(NomalFile):
    def replace_variable(self, filename):
        replaced = super().replace_variable(filename)
        new_replaced = list()
        for line in replaced:
            if '{{ client }}' in line:
                for i in range(self.vars['client']['nodes']):
                    ip = ipaddress.ip_address(int(ipaddress.ip_address(self.vars['client']['offset']))+i)
                    tmp = line.replace('{{ client }}', str(ip))
                    new_replaced.append(tmp)
                continue
            new_replaced.append(line)
        return new_replaced


class InvFile(NomalFile):
    def add(self, new_replaced, nodes, offset, hostname):
        for i in range(nodes):
            ip = ipaddress.ip_address(int(ipaddress.ip_address(offset))+i)
            new_replaced.append(hostname + str(i+1) + ' ansible_host=' + str(ip) + '\n')
            new_replaced.append(hostname + str(i+1) + ' ansible_ssh_private_key_file=".vagrant/machines/'+ hostname + str(i+1) + '/libvirt/private_key"\n')
    def replace_variable(self, filename):
        replaced = super().replace_variable(filename)
        new_replaced = list()
        for line in replaced:
            if '{{ client }}' in line:
                self.add(
                    new_replaced=new_replaced,
                    nodes=self.vars['client']['nodes'], 
                    offset=self.vars['client']['offset'], 
                    hostname='c'
                )
                continue
            if '{{ k8s_worker }}' in line:
                self.add(
                    new_replaced=new_replaced,
                    nodes=self.vars['k8s']['worker']['nodes'], 
                    offset=self.vars['k8s']['worker']['offset'], 
                    hostname='kw'
                )
                continue
            new_replaced.append(line)
        return new_replaced

class VagrantFile(NomalFile):
    def add(self, new_replaced, nodes, offset, hostname):
        new_replaced.append('    (0..' + str(nodes-1) + ').each do |i|'+'\n')
        new_replaced.append('        config.vm.define "' + hostname + '#{i+1}" do |server|'+'\n')
        new_replaced.append('            ip = "' + offset + '".split(".")[3].to_i + i'+'\n')
        new_replaced.append('            server.vm.hostname = "' + hostname + '#{i+1}"'+'\n')
        new_replaced.append('            server.vm.network :public_network, '+'\n')
        new_replaced.append('               :dev => "virbr0",'+'\n')
        new_replaced.append('               :mode => "bridge",'+'\n')
        new_replaced.append('               :type => "bridge",'+'\n')
        new_replaced.append('               :ip => "192.168.122.#{ip}"'+'\n')   # ここ変えたい
        new_replaced.append('        end'+'\n')
        new_replaced.append('    end'+'\n')
    def replace_variable(self, filename):
        replaced = super().replace_variable(filename)
        new_replaced = list()
        for line in replaced:
            if '{{ client }}' in line:
                self.add(
                    new_replaced=new_replaced, 
                    nodes=self.vars['client']['nodes'], 
                    offset=self.vars['client']['offset'], 
                    hostname='c')
                continue
            if '{{ k8s_worker }}' in line:
                self.add(
                    new_replaced=new_replaced,
                    nodes=self.vars['k8s']['worker']['nodes'], 
                    offset=self.vars['k8s']['worker']['offset'], 
                    hostname='kw'
                )
                continue
            new_replaced.append(line)
        return new_replaced

if __name__ == '__main__':
    vars_yml = "vars.yml"
    nomalfile = NomalFile(vars_yml)
    invfile = InvFile(vars_yml)
    vagrantfile = VagrantFile(vars_yml)
    promfile = PromFile(vars_yml)

    # ファイル生成
    replaced = nomalfile.replace_variable('./template/gitlab/docker-compose.yml')
    nomalfile.out_file(replaced, './files/gitlab/docker-compose.yml')
    
    replaced = nomalfile.replace_variable('./template/nfs/exports')
    nomalfile.out_file(replaced, './files/nfs/exports')

    replaced = nomalfile.replace_variable('./template/play-k8s-create-w.yml')
    nomalfile.out_file(replaced, './play-k8s-create-w.yml')

    replaced = nomalfile.replace_variable('./template/play-vagrant.yml')
    nomalfile.out_file(replaced, './play-vagrant.yml')
    
    replaced = promfile.replace_variable('./template/prometheus/server/prometheus.yml')
    nomalfile.out_file(replaced, './files/prometheus/server/prometheus.yml')
    
    replaced = invfile.replace_variable('./template/inv.ini')
    invfile.out_file(replaced, './inv.ini')
    
    replaced = vagrantfile.replace_variable('./template/Vagrantfile')
    vagrantfile.out_file(replaced, './Vagrantfile')
