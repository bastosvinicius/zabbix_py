#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: vinicius bastos
# version: 0.1
# mail: bastosvinicius@live.com

print ("\n" * 100)
from termcolor import colored
print colored('ola', 'blue'), ("d(-_-)b"), colored('mundo', 'blue')
print("\n bem vindo ao script de utilidades do time de automacao"
"\n"
"\n compartilhe conhecimento"
)
amb=True
while amb:
    print ("""
    1 - zabbix
    2 - tws
    3 - sair
    """)
    amb=raw_input("selecione o ambiente desejado: ")
    if amb=="1":
        mzbx=True
        while mzbx:
            print("""
            1 - extracao de dados
            2 - consulta de disponibilidade de servidores
            3 - instalacao em massa
            4 - menu anterior
            5 - sair
            """)
            mzbx=raw_input("\n escolha uma opcao: ")
            if mzbx=="1":
                print("\n ferramenta de utilidades do zabbix do time de automacao cpfl \n")
                print ("autenticao de usuario\n")
                from zabbix_api import ZabbixAPI
                import getpass
                zapi = ZabbixAPI(server="http://<zabbix_host>.com.br/zabbix/")
                usuario = raw_input("usuario: ")
                senha = getpass.getpass("senha: ")
                zapi.login(usuario, senha)
                print("Conectado ao Zabbix %s" % zapi.api_version())
                zbxextrac=True
                while zbxextrac:
                    print("""
                    1 - extrair lista de servidores no zabbix
                    2 - extrair lista de hostgroups no zabbix
                    3 - extrair lista de servidores em determinado template no zabbix
                    4 - extrair lista de servidores em determinado hostgroup no zabbix
                    5 - extrair lista de usuarios no zabbix
                    6 - menu anterior
                    7 - sair
                    """)
                    zbxextrac=raw_input("\n escolha uma opcao: ")

                    if zbxextrac=="1":
                        print("\n extraindo lista de servidores cadastrados no zabbix \n")
                        print("\n")
                        hosts = zapi.host.get({"output": ["hostid","name"], "sortfield": "name"}) 
                        hosts
                    elif zbxextrac=="2":
                        print("extraindo lista de hostgroups cadastrados no zabbix")

                    elif zbxextrac=="3":
                        print("extraindo lista de servidores cadastrados para o template no zabbix")

                    elif zbxextrac=="4":
                        print("extraindo lista de servidores cadastrados no hostgroup no zabbix")
                        grp = raw_input("nome do grupo: \n")

                        def get_hostgroups_id(grupo):
                            groupId = zapi.hostgroup.get({"output": "extend","filter":{"name":grupo}})[0]['groupid']
                            return groupId

                        def get_hosts(grupo):
                            hosts_grupo = zapi.host.get({"groupids":get_hostgroups_id(grupo),"output":["host"]})
                            listaHosts = []
                            for x in hosts_grupo:
                                print x['host']
                                listaHosts += [x['host']]
                            return listaHosts

                        get_hosts('%s' % grp)
                        print("\n")

                    elif zbxextrac=="5":
                        print("extraindo lista de usuarios cadastrados no zabbix")

                    elif zbxextrac=="6":
                        break

                    elif zbxextrac=="7":
                        print("abraco"); quit()

                    elif zbxextrac !="":
                        print("opcao invalida")

            elif mzbx=="2":
                print("consulta de disponibilidade do zabbix")
            elif mzbx=="3":
                print("instalacao em massa do zabbix")
            elif mzbx=="4":
                break
            elif mzbx=="5":
                print("abraco"); quit()
            elif mzbx !="":
                print("opcao invalida")
    elif amb=="2":
        print("\n em desenvolvimento")
    elif amb=="3":
        print("\n abraco") ; quit()
    elif amb !="":
        print("\n opcao invalida")