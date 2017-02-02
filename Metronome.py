#Mathew Thomas - N15690387
#Music Software Projects, NYU Courant, Fall 2016
#Metronome function that can be used for different accents. Didn't use the accent functionality in this application, implemented polyrhythms instead
import time
import pygame

def metronome(bpm, accent, normal,timesignum,timesigdenom,accentposition):
	pygame.mixer.pre_init(44100, -16, 2, 512)
	pygame.mixer.init()
	pygame.init()
	A = pygame.mixer.Sound(accent)
	if normal !='silent':
		B = pygame.mixer.Sound(normal)					
	interval = 60/(float(bpm)*(timesigdenom/4))
	x = interval - int(A.get_length())
	y = interval
	#print x
	if normal != 'silent':
		y = interval - int(B.get_length())
	i = 1
	
	if len(accentposition) == 0 :
		
		screen = pygame.display.set_mode((400, 300))
		titlewin = str(bpm) + " bpm, " + str(int(timesignum)) + "/" + str(int(timesigdenom))
		pygame.display.set_caption(titlewin)
		done = False

		while not done:
			font = pygame.font.Font(None, 300)
			text = font.render(str((i%int(timesignum))+1), True, (128, 128, 128))
			screen.fill((0, 0, 0))
			screen.blit(text,(200 - text.get_width() // 2, 150 - text.get_height() // 2))		
		
			A.play()	
			time.sleep(x)
			i = i+1
	
	        	for event in pygame.event.get():
                		if event.type == pygame.QUIT:
                        		done = True
        	
        		pygame.display.flip()
			
	else:	
	
		screen = pygame.display.set_mode((400, 300))
		done = False

		while not done:
			font = pygame.font.Font(None, 300)
			text = font.render(str((i%int(timesignum))+1), True, (128, 128, 128))
			screen.fill((0, 0, 0))
			screen.blit(text,(200 - text.get_width() // 2, 150 - text.get_height() // 2))		
		
			if i % timesignum in accentposition:
				A.play()	
				time.sleep(x)
				i = i + 1
			elif normal == 'silent':
				time.sleep(y)
				i = i+1
				
			else :
				B.play()
				time.sleep(y)
				i = i+1
	
	        	for event in pygame.event.get():
                		if event.type == pygame.QUIT:
                        		done = True
        	
        		pygame.display.flip()
'''x = sys.argv[6]
x = x.split()
#print x
for i in range(len(x)):
	x[i] = float(x[i])
metronome(int(sys.argv[1]), sys.argv[2], sys.argv[3], float(sys.argv[4]),float(sys.argv[5]),x,float(sys.argv[7]))	
#print sys.argv[1]'''
#metronome(90, 'tabla.wav', 'chick.wav',7,8,[1])
