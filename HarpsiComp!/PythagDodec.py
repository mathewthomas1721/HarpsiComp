#Mathew Thomas - N15690387
#Music Software Projects, NYU Courant, Fall 2016
#Implementation of Pythagorean Dodecaphonic Scale

class pythagorean:					#Class implementing PythagDodec scale
	
	def __init__(self, intn, bf):
	
		if (intn==0):
			self.base = bf
			self.intn = float(intn)
			self.degree = 0
			self.let = ""
			self.type = ""
			self.num = ""
			self.denom = ""
			self. factor = ""
			self.intfreq = ""
			self.octave = ""
			self.octfact = ""
			self.newnum = ""
			self.newdenom = ""
			self.factoctadj = 1.0
			self.finfreq = float(bf)
			self.filename = ""
			'''self.stringoctadj = "\"" + str(Fraction(1,1))+"\""
			self.cents = 0'''

		elif (intn<0):
			self.base = bf
			self.intn = float(intn)
			self.degree = 0
			self.let = ""
			self.type = ""
			self.num = float(2) ** (intn * -1)
			self.denom = float(3) ** (intn * -1)
	
			self.factor = float(self.num) / float(self.denom)

			self.intfreq = float(self.base) * float(self.factor)
	        
			self.octave = float(self.lasttpowerof2(self.intfreq,self.base))
	
			self.octfact = float(2**(-1*self.octave))

			self.newnum = self.num * self.octfact
			self.newdenom = self.denom

			self.factoctadj = float(self.newnum)/float(self.newdenom)
		
			self.finfreq = self.hz()
			self.filename = ""
		
			'''self.stringoctadj = self.get_interval_ratio()
			self.cents = int(round(abs(1200 * mp.log(self.factoctadj,2))))'''
			
		else :
			self.base = bf
			self.intn = float(intn)
			self.degree = 0
			self.let = ""
			self.type = ""
			self.num = float(3) ** intn
			self.denom = float(2) ** intn
	
			self.factor = float(self.num) / float(self.denom)

			self.intfreq = float(self.base) * float(self.factor)
	        
			self.octave = float(self.lasttpowerof2(self.intfreq,self.base))
	
			self.octfact = float(2**self.octave)

			self.newnum = self.num 
			self.newdenom = self.denom * self.octfact

			self.factoctadj = float(self.newnum)/float(self.newdenom)
		
			self.finfreq = self.hz()
			self.filename = ""
		
			'''self.stringoctadj = self.get_interval_ratio()
			self.cents = int(round(abs(1200 * mp.log(self.factoctadj,2))))'''
			
	def __repr__(self):
		return '{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n\n'.format(self.degree,self.intn,self.num,self.denom,self.factor,self.intfreq,self.octave,self.octfact,self.newnum,self.newdenom,self.factoctadj,self.finfreq,self.let,self.type)

	def lasttpowerof2(self,intfreq,base):
		i = 0
		if intfreq>base : 
			while(base<intfreq):
				base = float(base) * 2;
				i = i+1;
			i = i-1;
		else :
			while(base>intfreq):
				base = float(base)/2;
				i = i-1;
			
					
		return i
	
	'''def get_interval_ratio(self):
		y = (float(self.denom) * float(self.octfactor))
		x = float(self.num)/float(y)
		return x'''

	def hz(self):
		x = self.factoctadj * self.base
		return x

def getKey(meantone):				#Obtains the key for sorting the scale
	return meantone.finfreq

def dodec(bf,filenameDict):							#generates pythagorean dodecaphonic list
	

	LetterDict = {0 : "C", 1 : "Db/C#", 2 : "D", 3 : "Eb/(D#)", 4 : "E", 5 : "F", 6 : "Gb/F#", 7 : "Gb/F#", 8 : "G", 9 : "Ab/G#", 10 : "A", 11 : "Bb/A#", 12 : "B"}
	TypeDict = {0 : "1.0", 1 : "m2", 2 : "2.0", 3 : "m3", 4 : "M3", 5 : "4.0", 6 : "b5 (-)", 7 : "b5 (+)", 8 : "5.0", 9 : "m6", 10 : "M6", 11 : "m7", 12 : "M7"}
	'''filenameDict = { 0 :'PythagDodecScale/C.wav', 1 : 'PythagDodecScale/C#.wav', 2 : 'PythagDodecScale/D.wav', 3 : 'PythagDodecScale/D#.wav', 4 : 'PythagDodecScale/E.wav', 5 : 'PythagDodecScale/F.wav', 6 : 'PythagDodecScale/F#1.wav', 7 :'PythagDodecScale/F#2.wav', 8 :'PythagDodecScale/G.wav', 9 : 'PythagDodecScale/G#.wav', 10 : 'PythagDodecScale/A.wav', 11 : 'PythagDodecScale/A#.wav', 12 : 'PythagDodecScale/B.wav'}'''


	PythagoreanList = []
	for i in range(-6, 7) :
		x = pythagorean(i,bf)
		PythagoreanList.append(x)
	
	
	PythagoreanList = sorted(PythagoreanList, key=getKey)
	for i in range (len(PythagoreanList)):
		PythagoreanList[i].degree = i + 1
		PythagoreanList[i].let = LetterDict[i]
		PythagoreanList[i].type = TypeDict[i]
		PythagoreanList[i].filename = filenameDict[i]
		#print(PythagoreanList[i].intn, PythagoreanList[i].finfreq)
		#regtestD(PythagoreanList[i],i)
		#playsound(PythagoreanList[i].finfreq, 1)
	'''ProperPythag = {}
	for i in range(len(PythagoreanList)):
		if PythagoreanList[i].let in ["C","D","E","F","G","A","B"] :
			
			ProperPythag.update({PythagoreanList[i].let : PythagoreanList[i].finfreq})'''
	
	return PythagoreanList;

