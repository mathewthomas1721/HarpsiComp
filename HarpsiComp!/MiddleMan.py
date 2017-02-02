#Mathew Thomas - N15690387
#Music Software Projects, NYU Courant, Fall 2016
#Intermediate function between the TkInter window and PyGame functions

from multiprocessing import Process
from Metronome import metronome
from HarpsiComp import Harpsichord

def middleman(bpm,numlist,denom,scale):
	#Harpsichord("EvenTempered")
	bpms = []
	bpms.append(bpm)
	for i in range(1,len(numlist)):
		x = (float(numlist[i])/numlist[0]) * bpm
		bpms.append(x)
	Process(target=Harpsichord, args=(scale,)).start()
	if len(numlist)==1:
		Process(target=metronome, args=(bpms[0], 'PercSounds/Cowbell.wav', 'PercSounds/HatClosed.wav',float(numlist[0]),float(denom),[1])).start()	
	
	if len(numlist)>1:
		Process(target=metronome, args=(bpms[0], 'PercSounds/Cowbell.wav', 'silent',float(numlist[0]),4,[])).start()
		Process(target=metronome, args=(bpms[1], 'PercSounds/Snare1.wav', 'silent',float(numlist[1]),4,[])).start()
	if len(numlist)>2:
		Process(target=metronome, args=(bpms[2], 'PercSounds/HatClosed.wav', 'silent',float(numlist[2]),4,[])).start()
	if len(numlist)>3:
		Process(target=metronome, args=(bpms[3], 'PercSounds/Kick1.wav', 'silent',float(numlist[3]),4,[])).start()
