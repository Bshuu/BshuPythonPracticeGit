import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#nsclpd-nrcdoc01
ssh.connect('10.41.2.41', username='brshuart',password='BshuBitcoin413!')

stdin, stdout, stderr = ssh.exec_command('history')
print(stdout.readlines())

ssh.close()