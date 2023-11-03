import paramiko
import scp

# サーバに繋ぐ
with paramiko.SSHClient() as sshc:
  sshc.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  sshc.connect(hostname='192.168.3.36', port=22, username='pi', password='raspberry')

  # SSHClient()の接続設定を合わせてあげる
  with scp.SCPClient(sshc.get_transport()) as scpc:
    scpc.put('images/grad_cam0.png', 'que')

