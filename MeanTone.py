#Mathew Thomas - N15690387
#Music Software Projects, NYU Courant, Fall 2016
#Implementation of Mean Tone Scale
class MeanTone:					#Class implementing Mean Tone Scale
	
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

			self.factoctadj = float(self.newnum)/float(self.newdenom) * ((float(80)/81)**(self.intn/4))
		
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

			self.factoctadj = float(self.newnum)/float(self.newdenom) * ((float(80)/81)**(self.intn/4))
		
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

def meantone(bf,filenameDict):
	

	LetterDict = {0 : "C", 1 : "C#", 2 : "Db", 3 : "D", 4 : "D#", 5 : "Eb", 6 : "E", 7 : "F", 8 : "F#", 9 : "Gb", 10 : "G", 11 : "G#", 12 : "Ab", 13 : "A", 14 : "A#", 15 : "Bb", 16 : "B"}
	'''filenameDict = {0 : 'MeanToneScale/C.wav', 1 : 'MeanToneScale/C#.wav', 2 : 'MeanToneScale/Db.wav', 3 : 'MeanToneScale/D.wav', 4 : 'MeanToneScale/D#.wav', 5 : 'MeanToneScale/Eb.wav', 6 : 'MeanToneScale/E.wav', 7 : 'MeanToneScale/F.wav', 8 : 'MeanToneScale/F#.wav', 9 : 'MeanToneScale/Gb.wav', 10 : 'MeanToneScale/G.wav', 11 : 'MeanToneScale/G#.wav', 12 : 'MeanToneScale/Ab.wav', 13 : 'MeanToneScale/A.wav', 14 : 'MeanToneScale/A#.wav', 15 : 'MeanToneScale/Bb.wav', 16 : 'MeanToneScale/B.wav'}'''
	TypeDict = {0 : "1.0", 1 : "", 2 : "", 3 : "2.0", 4 : "", 5 : "", 6 : "M3", 7 : "4.0", 8 : "", 9 : "", 10 : "5.0", 11 : "", 12 : "", 13 : "M6", 14 : "", 15 : "", 16 : "M7"}




	MeanToneList = []
	for i in range(-6, 11) :
		x = MeanTone(i,bf)
		MeanToneList.append(x)
		#regtestD(x,i+6);
	
	MeanToneList = sorted(MeanToneList, key=getKey)
	for i in range (len(MeanToneList)):
		MeanToneList[i].degree = i + 1
		MeanToneList[i].let = LetterDict[i]
		MeanToneList[i].type = TypeDict[i]
		MeanToneList[i].filename = filenameDict[i]
		#RegTestM(MeanToneList[i],i)
		#print(MeanToneList[i].intn, MeanToneList[i].factoctadj)
		#regtestD(PythagoreanList[i],i)
		#playsound(MeanToneList[i].finfreq, 1)
	#playsound(bf*2,1)
	'''ProperMeanTone = {}
	for i in range(len(MeanToneList)):
		if MeanToneList[i].let in ["C","D","E","F","G","A","B"] :
			
			ProperMeanTone.update({MeanToneList[i].let : MeanToneList[i].finfreq})'''
	return MeanToneList;
	#print (ProperMeanTone)
