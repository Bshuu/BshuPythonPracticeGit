import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.18.0.1', username='brshuart',password='')

stdin, stdout, stderr = ssh.exec_command('pwd')
print(stdout.readlines())

ssh.close()