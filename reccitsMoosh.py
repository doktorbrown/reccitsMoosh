
import commands

#pass these to main()
aStat='arecord -l' #list ALSA devices
bStat='arecord -L'  #list ALSA devices verbose
cStat='arecord --version'  #arecord version
#this does recording to USB after capture device is set with ALSA mixer
dStat='arecord -D sysdefault:CARD=AK5370  -f cd  -t wav --max-file-time 30 --use-strftime ~/usbdrv/recordings/%Y%m%d/%Y%m%d_BigEar_%H-%M-%v.wav'

def runCommandLine(cmd):
    a=commands.getstatusoutput(cmd)
    return a


def main(stuff):
    print('recording')
    a=runCommandLine(stuff)    
    return a


main(dStat)

