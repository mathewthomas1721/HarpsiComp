#Mathew Thomas - N15690387
#Music Software Projects, NYU Courant, Fall 2016
#Implementation of Ptolemy's Scale

from PythagDodec import dodec
from fractions import Fraction

def ptolemy(bf,filenameDict):
	x = dodec(bf,filenameDict)
	#print x
	y = []
	AdjNum = [1,81,1,81,80,1,0,32768,1,81,80,1,80]
	AdjDenom = [1,80,1,80,81,1,1,32805,1,80,81,1,81]
	y.append(x[0])
	for i in range (1,len(x)) :
		tempnum = int(x[i].newnum) * AdjNum[i]
		tempdenom = int(x[i].newdenom) * AdjDenom[i]
		#print (tempnum , tempdenom)
		temp = Fraction(tempnum,tempdenom)
		x[i].newnum = float(temp.numerator)
		x[i].newdenom = float(temp.denominator)
		if x[i].newnum != 0:
			
			x[i].factoctadj = float(x[i].newnum)/float(x[i].newdenom)
			x[i].finfreq = x[i].hz()
			y.append(x[i])
		
        return y;

'''PtolemyfilenameDict = { 0 :'PtolemyScale/C.wav', 1 : 'PtolemyScale/C#.wav', 2 : 'PtolemyScale/D.wav', 3 : 'PtolemyScale/D#.wav', 4 : 'PtolemyScale/E.wav', 5 : 'PtolemyScale/F.wav', 6 : 'PtolemyScale/F#.wav', 7 :'PtolemyScale/F#2.wav', 8 :'PtolemyScale/G.wav', 9 : 'PtolemyScale/G#.wav', 10 : 'PtolemyScale/A.wav', 11 : 'PtolemyScale/A#.wav', 12 : 'PtolemyScale/B.wav'}
ptolemy(66,PtolemyfilenameDict)'''
