import socket, subprocess, json

proc = subprocess.Popen('octave --eval '+SOMA_AQUI,stdout = subprocess.PIPE, shell=True)
cmdOutput = proc.communicate()
cmdOutput = cmdOutput[0].decode('UTF-8').rstrip()

print(cmdOutput)
