import subprocess, os, base64, time, threading
workfile = subprocess.getoutput("pwd")
settings = [int(subprocess.getoutput("cat "+workfile+"/config.txt | grep 'DMF: '").replace("DMF: ", "")), int(subprocess.getoutput("cat "+workfile+"/config.txt | grep 'SSH: '").replace("SSH: ", "")), int(subprocess.getoutput("cat "+workfile+"/config.txt | grep 'HID: '").replace("HID: ", "")), int(subprocess.getoutput("cat "+workfile+"/config.txt | grep 'DOS: '").replace("DOS: ", "")), int(subprocess.getoutput("cat "+workfile+"/config.txt | grep 'DPP: '").replace("DPP: ", ""))]
pastlog, logs = "", []
connectsshIp_output, connectsshIp = "", ""
nums = [0,0,0]
spaces = []
pastlognum = 1
lognums = ["N0", "N1", "N2", "N3", "N4", "N5", "N6"]
mainscantarget = []
dangerouscmdlist = [b'cm0gLXJm', b'Oigpezp8OiZ9Ozo=', b'PiAvZGV2L3NkYQ==', b'bXYgL2hvbWUvdXNlci8qIC9kZXYvbnVsbA==', b'LU8tIHwgc2g=', b'bWtmcy5leHQxIC9kZXYvc2Rh', b'bWtmcy5leHQyIC9kZXYvc2Rh', b'bWtmcy5leHQzIC9kZXYvc2Rh', b'bWtmcy5leHQ0IC9kZXYvc2Rh', b'bWtmcy54ZnMgL2Rldi9zZGE=', b'bWtmcy5idHJmcyAvZGV2L3NkYQ==', b'PiAv', b'XmZvb15iYXI=', b'ZGQgaWY9L2Rldi9yYW5kb20gb2Y9L2Rldi9zZGE=', b'Q2htb2QgLVIgNzc3IC8=']
for i in range(7): logs.append("                                                                                                                           ")
for i in range(7): spaces.append("         ")
os.system("ulimit -S -u 4000")
def shield(type):
	if type == "hcfsearch":
		subprocess.getoutput("echo $(cd ~/ ; find `pwd` -maxdepth 3000>/dev/ttys002)>search.txt")
	if type == "ssh":
		if settings[2] == 1:
			if not subprocess.getoutput("pidof ssh") == "":
				logs.append("\x1b[31;40;1m[!] /1\x1b[0m\x1b[37m Detect (SSH):   Detected REVERSE SHELL! Kill right now by: \x1b[31;40;1mkillssh\x1b[37m")
		if settings[2] == 2:
			connectsshIp = subprocess.getoutput("who -a | grep ')'")
			if not connectsshIp == "":
				for i in range(3):
					os.system('kill '+str(subprocess.getoutput('pidof ssh')))
				if str(os.system('kill '+str(subprocess.getoutput('pidof ssh')))) == '0':
					connectsshIp_output = "   > "+connectsshIp
					for i in range(81-len(connectsshIp_output)):
						connectsshIp_output = connectsshIp_output + " "
					logs.append(connectsshIp_output)
					logs.append("\x1b[31;40;1m[!] /2\x1b[0m\x1b[37m Log&Kl (SSH):   Detected REVERSE SHELL! IP:                                 \x1b[37m")
		if settings[2] == 3:
			for i in range(3):
				os.system('kill '+str(subprocess.getoutput('pidof ssh')))
			if str(os.system('kill '+str(subprocess.getoutput('pidof ssh')))) == '0':
				logs.append("\x1b[31;40;1m[!] /3\x1b[0m\x1b[37m Killed (SSH):   Killed REVERSE SHELL! If intended, turn off in settings!\x1b[37m")
	if type == "hcf":
		s = subprocess.getoutput("cat search.txt")
		mainscantarget = s.splitlines()
		for i in range(len(mainscantarget)):
			for j in range(len(dangerouscmdlist)):
				if str(base64.b64decode(dangerouscmdlist[j-1]).decode()) in subprocess.getoutput("cat "+mainscantarget[i-1]):
					if settings[1] == 1:
						logs.append("\x1b[32;40;1m[!] /1\x1b[0m\x1b[37m Detect (HCF):  Detected HARMFUL COMMAND FILE!  Detected: "+mainscantarget[i-1])
					if settings[1] == 2:
						logs.append("\x1b[33;40;1m[!] /2\x1b[0m\x1b[37m De-Arm (HCF): Neutralized HARMFUL COMMAND FILE! Dearmed: "+mainscantarget[i-1])
						os.system("echo " + str(base64.b64encode(subprocess.getoutput("cat "+mainscantarget[i-1]).encode()))+" > ~"+mainscantarget[i-1])
					if settings[1] == 3:
						logs.append("\x1b[31;40;1m[!] /3\x1b[0m\x1b[37m Delete (HCF):     Deleted HARMFUL COMMAND FILE! Deleted: "+mainscantarget[i-1])
						os.system(str(base64.b64decode(dangerouscmdlist[0].decode()))[1:]+" ~"+mainscantarget[i-1])
shield("hcfsearch")
while True:
	os.system("clear")
	for i in range(7):                                 
		if len(lognums[i]) == 3: spaces[i] = "        "
		if len(lognums[i]) == 4: spaces[i] = "       "
		if len(lognums[i]) == 5: spaces[i] = "      "
	print("\x1b[37m           A         VV      VV      fff      SSSSSS       y   y   sss   t    ee     m   m       \n          AAA        VV      VV     ff ff    SS     SS      y y   ss    ttt  eeeee  m m m m      \n         AA AA       VV      VV     ff ff   SS       SS      y     sss   t   e      m m m m      \n        AA   AA       VV    VV      ff      SS              y     sss    t    eee   m  m  m      \n       AA     AA      VV    VV      ff       SSSSSSSS     ----------------------------------     \n      AAAAAAAAAAA      VV  VV     ffffff            SS      ee    r r   v   v   ee    r r        \n     AA         AA      V  V        ff      SS      SS     eeeee  rr r  v   v  eeeee  rr r       \n     AA         AA      VVVV        ff       SS    SS      e      r      v v   e      r          \n     AA         AA       VV         ff        SSSSSS        eee   r       v     eee   r          \n\n\x1b[39;40;1;4mMonitoring:\x1b[0m                                                                                      \x1b[37m\n\x1b[39;40;1;4mLog:\x1b[0m\x1b[37m                                                                                             \x1b[0m\n\x1b[37m\n----------------------------------------------------------------------------------------------------------------------------------------+\n\x1b[37m"+str(lognums[0]).replace("N", str(spaces[0]))+"| "+logs[len(logs)-1]+"\x1b[0m\n\x1b[37m"+str(lognums[1]).replace("N", str(spaces[1]))+"| "+logs[len(logs)-2]+"\x1b[0m\n\x1b[37m"+str(lognums[2]).replace("N", str(spaces[2]))+"| "+logs[len(logs)-3]+"\x1b[0m\n\x1b[37m"+str(lognums[3]).replace("N", str(spaces[3]))+"| "+logs[len(logs)-4]+"\x1b[0m\n\x1b[37m"+str(lognums[4]).replace("N", str(spaces[4]))+"| "+logs[len(logs)-5]+"\x1b[0m\n\x1b[37m"+str(lognums[5]).replace("N", str(spaces[5]))+"| "+logs[len(logs)-6]+"\x1b[0m\n\x1b[37m"+str(lognums[6]).replace("N", str(spaces[6]))+"| "+logs[len(logs)-7]+"\x1b[0m\n\x1b[37m----------------------------------------------------------------------------------------------------------------------------------------+\n\n\n\x1b[39;40;1;4mWorkspace:\x1b[0m\x1b[37m                                                                                       \x1b[0m\x1b[37m\n+---------------------------------------------------------------------------------------------------------------------------------------+\x1b[0m")
	hcfs = threading.Thread(target=shield("hcfsearch"))
	hcf = threading.Thread(target=shield("hcf"))
	ssh = threading.Thread(target=shield("ssh"))
	hcfs.start()
	hcf.start()
	ssh.start()
	pastlog = str(logs)
	if len(logs)-7 >= pastlognum:
		pastlognum += 1
		for i in range(7):
			lognums[i] = "N"+str(int(lognums[i].replace("N","")) + 1)
