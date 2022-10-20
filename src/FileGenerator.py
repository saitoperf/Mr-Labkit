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
    def replace_variable(self, filename):
        replaced = super().replace_variable(filename)
        new_replaced = list()
        for line in replaced:
            if '{{ client }}' in line:
                for i in range(self.vars['client']['nodes']):
                    ip = ipaddress.ip_address(int(ipaddress.ip_address(self.vars['client']['offset']))+i)
                    new_replaced.append('c' + str(i+1) + ' ansible_host=' + str(ip) + '\n')
                    new_replaced.append('c' + str(i+1) + ' ansible_ssh_private_key_file=".vagrant/machines/c' + str(i+1) + '/libvirt/private_key"\n')
                continue
            new_replaced.append(line)
        return new_replaced

class VagrantFile(NomalFile):
    def replace_variable(self, filename):
        replaced = super().replace_variable(filename)
        new_replaced = list()
        for line in replaced:
            if '{{ client }}' in line:
                new_replaced.append('    (0..' + str(self.vars['client']['nodes']-1) + ').each do |i|'+'\n')
                new_replaced.append('        config.vm.define "c#{i+1}" do |host|'+'\n')
                new_replaced.append('            ip = "' + str(self.vars['client']['offset']) + '".split(".")[3].to_i + i'+'\n')
                new_replaced.append('            host.vm.hostname = "c#{i+1}"'+'\n')
                new_replaced.append('            host.vm.network :public_network, '+'\n')
                new_replaced.append('               :dev => "virbr0",'+'\n')
                new_replaced.append('               :mode => "bridge",'+'\n')
                new_replaced.append('               :type => "bridge",'+'\n')
                new_replaced.append('               :ip => "192.168.122.#{ip}"'+'\n')
                new_replaced.append('        end'+'\n')
                new_replaced.append('    end'+'\n')
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
    
    replaced = promfile.replace_variable('./template/prometheus/server/prometheus.yml')
    nomalfile.out_file(replaced, './files/prometheus/server/prometheus.yml')
    
    replaced = invfile.replace_variable('./template/inv.ini')
    invfile.out_file(replaced, './inv.ini')
    
    replaced = vagrantfile.replace_variable('./template/Vagrantfile')
    vagrantfile.out_file(replaced, './Vagrantfile')

