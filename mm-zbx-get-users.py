#!/bin/python3.4
# author: bastosvinicius
# version: 1.0

import pymysql.cursors, sys, csv, datetime, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

cnx = pymysql.connect(host='<DATABASE HOSTNAME>', user='zabbix', password='<ZABBIX DB PASSWORD>', db='zabbix', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

server = smtplib.SMTP('<SMTP MAIL SERVER>',25)

sql = "SELECT usr.alias AS 'alias', usr.name AS 'name', usr.surname AS 'surname', CASE WHEN usr.type = '1' THEN 'Zabbix User' WHEN usr.type = '2' THEN 'Zabbix Admin' WHEN usr.type = '3' THEN 'Zabbix Super Admin' END AS type, GROUP_CONCAT(grp.name ORDER BY grp.name ASC SEPARATOR'/') AS 'groups' FROM users AS usr INNER JOIN users_groups AS usrg ON usr.userid = usrg.userid INNER JOIN usrgrp AS grp ON grp.usrgrpid = usrg.usrgrpid GROUP BY usr.alias ORDER BY usr.name"

today = str(datetime.date.today())

cursor = cnx.cursor()

cursor.execute(sql)

result = cursor.fetchall()

output = open("/tmp/zabbix_users.csv", "w")

print('Matricula,Nome,Sobrenome,Tipo do Usuario,Grupos do usuario', file=output)
print('',file=output)

def results():
        for row in result:
                print(row["alias"], row["name"], row["surname"], row["type"], row["groups"], sep=',',file=output)

def sendmail():
        subject = "[ZBX] - Relatorio de usuarios cadastrados no Zabbix"
        sender = "m3g4z0rd@m3g4z0rd.com.br"
        recipients = ['m3g4z0rd@m3g4z0rd.com.br', 'bastosvinicius@live.com']
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)
        part = MIMEText("""Senhores,

Segue em anexo relatorio de usuarios cadastrados no Zabbix extraido em """+today+"""

Att.

m3g4z0rd""")
        msg.attach(part)
        part = MIMEApplication(open(str('/tmp/zabbix_users.csv'),"rb").read())
        part.add_header('Content-Disposition', 'attachment', filename=str('zabbix_users.csv'))
        msg.attach(part)
        server.sendmail(sender, recipients, msg.as_string())

results()
output.close()
sendmail()
server.close()
quit()
