#Mathew Thomas - N15690387
#Music Software Projects, NYU Courant, Fall 2016
#Implementation of Even Tempered Scale

class evenTempered : 						#class implementing ET scale
	def __init__(self, intn, bf):
		self.base = bf
		self.intn = intn
		power = intn/12.0
		factor = 2**power
      		self.finfreq = bf * factor
		self.cents = 100 * intn
		self.let = ""
		self.filename = ""
	
	def __repr__(self):
		return '{}\n{}\n{}\n\n'.format(self.intn,self.finfreq,self.cents)

def ET(bf,filenameDict):											#generates even tempered list
	LetterDict = { 0 :"C", 1 : "C#", 2 : "D", 3 : "D#", 4 : "E", 5 : "F", 6 : "F#", 7 :"G", 8 : "G#", 9 : "A", 10 : "A#", 11 : "B" }
	'''filenameDict = { 0 :"EvenTemperedScale/C.wav", 1 : "EvenTemperedScale/C#.wav", 2 : "EvenTemperedScale/D.wav", 3 : "EvenTemperedScale/D#.wav", 4 : "EvenTemperedScale/E.wav", 5 : "EvenTemperedScale/F.wav", 6 : "EvenTemperedScale/F#.wav", 7 :"EvenTemperedScale/G.wav", 8 : "EvenTemperedScale/G#.wav", 9 : "EvenTemperedScale/A.wav", 10 : "EvenTemperedScale/A#.wav", 11 : "EvenTemperedScale/B.wav"  }'''
	evenTemperedList = []						
	for i in range(12):
		x = evenTempered(i,bf)
		x.let = LetterDict[i]
		x.filename = filenameDict[i]
		#regressiontestET1(x,i)
		evenTemperedList.append(x)
	'''ProperET = {}
	for i in range(len(evenTemperedList)):
		if evenTemperedList[i].let in ["C","D","E","F","G","A","B"] :
			
			ProperET.update({evenTemperedList[i].let : evenTemperedList[i].finfreq})'''
	
	return evenTemperedList;
