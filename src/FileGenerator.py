#!/bin/python3

import yaml

class FileGenerator:
    def __init__(self, vars_yml):
        with open(vars_yml, 'r') as f:
            self.vars = (yaml.safe_load(f))
        # print(self.vars['allip'][1])

    def replace_variable(self, filename):
        replaced = list()
        with open(filename, 'r') as f:
            for line in f:
                # line = line.replace('\n', '')
                if '{{ user }}' in line:
                    line = line.replace('{{ user }}', self.vars['user'])
                if '{{ serverip }}' in line:
                    line = line.replace('{{ serverip }}', self.vars['serverip'])
                if '{{ clientip }}' in line:
                    line = line.replace('{{ clientip }}', self.vars['clientip'])
                if '{{ allip }}' in line:
                    tmp = line  # tmp：リプレース後の文字列、line：変数で記述されている文字列
                    for ip in self.vars['allip']:
                        tmp = line.replace('{{ allip }}', ip)
                        replaced.append(tmp)
                    continue
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

if __name__ == '__main__':
    fg = FileGenerator("vars.yml")

    # ファイル生成
    replaced = fg.replace_variable('./files_template/gitlab/docker-compose.yml')
    fg.out_file(replaced, './files/gitlab/docker-compose.yml')
    
    replaced = fg.replace_variable('./files_template/nfs/exports')
    fg.out_file(replaced, './files/nfs/exports')
    
    replaced = fg.replace_variable('./files_template/prometheus/server/prometheus.yml')
    fg.out_file(replaced, './files/prometheus/server/prometheus.yml')
    
    replaced = fg.replace_variable('./files_template/inv.ini')
    fg.out_file(replaced, './inv.ini')
