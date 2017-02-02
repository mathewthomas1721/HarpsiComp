#Mathew Thomas - N15690387
#Music Software Projects, NYU Courant, Fall 2016
#Maps keys to notes of a given scale system

import pygame
#from  PlayWavSound import playsound
from Metronome import metronome
from threading import Thread

	
	
def Harpsichord(scale):
	pygame.mixer.pre_init(44100, -16, 2, 512)
	pygame.mixer.init()
	pygame.init()
	screen = pygame.display.set_mode((400, 300))
	done = False
#is_blue = True
	
	
	font = pygame.font.Font(None, 300)
	textC0 = font.render("C0", True, (0, 128, 0))
	textD0 = font.render("D0", True, (0, 128, 0))
	textE0 = font.render("E0", True, (0, 128, 0))
	textF0 = font.render("F0", True, (0, 128, 0))
	textG0 = font.render("G0", True, (0, 128, 0))
	textA0 = font.render("A0", True, (0, 128, 0))
	textB0 = font.render("B0", True, (0, 128, 0))
	textCsharp0 = font.render("C#0", True, (0, 128, 0))
	textDsharp0 = font.render("D#0", True, (0, 128, 0))
	textFsharp0 = font.render("F#0", True, (0, 128, 0))
	textGsharp0 = font.render("G#0", True, (0, 128, 0))
	textAsharp0 = font.render("A#0", True, (0, 128, 0))
	texttest = font.render("CMajor", True, (0, 128, 0))
	textC1 = font.render("C1", True, (0, 128, 0))
	textD1 = font.render("D1", True, (0, 128, 0))
	textE1 = font.render("E1", True, (0, 128, 0))
	textF1 = font.render("F1", True, (0, 128, 0))
	textG1 = font.render("G1", True, (0, 128, 0))
	textA1 = font.render("A1", True, (0, 128, 0))
	textB1 = font.render("B1", True, (0, 128, 0))
	textCsharp1 = font.render("C#1", True, (0, 128, 0))
	textDsharp1 = font.render("D#1", True, (0, 128, 0))
	textFsharp1 = font.render("F#1", True, (0, 128, 0))
	textGsharp1 = font.render("G#1", True, (0, 128, 0))
	textAsharp1 = font.render("A#1", True, (0, 128, 0))

	textC2 = font.render("C2", True, (0, 128, 0))
	textD2 = font.render("D2", True, (0, 128, 0))
	textE2 = font.render("E2", True, (0, 128, 0))
	textF2 = font.render("F2", True, (0, 128, 0))
	textG2 = font.render("G2", True, (0, 128, 0))
	textA2 = font.render("A2", True, (0, 128, 0))
	textB2 = font.render("B2", True, (0, 128, 0))
	textCsharp2 = font.render("C#2", True, (0, 128, 0))
	textDsharp2 = font.render("D#2", True, (0, 128, 0))
	textFsharp2 = font.render("F#2", True, (0, 128, 0))
	textGsharp2 = font.render("G#2", True, (0, 128, 0))
	textAsharp2 = font.render("A#2", True, (0, 128, 0))
	
	textC3 = font.render("C3", True, (0, 128, 0))
	textD3 = font.render("D3", True, (0, 128, 0))
	textE3 = font.render("E3", True, (0, 128, 0))
	textF3 = font.render("F3", True, (0, 128, 0))
	textG3 = font.render("G3", True, (0, 128, 0))
	textA3 = font.render("A3", True, (0, 128, 0))
	textB3 = font.render("B3", True, (0, 128, 0))
	textCsharp3 = font.render("C#3", True, (0, 128, 0))
	textDsharp3 = font.render("D#3", True, (0, 128, 0))
	textFsharp3 = font.render("F#3", True, (0, 128, 0))
	textGsharp3= font.render("G#3", True, (0, 128, 0))
	textAsharp3 = font.render("A#3", True, (0, 128, 0))

	textC4 = font.render("C4", True, (0, 128, 0))
	textD4 = font.render("D4", True, (0, 128, 0))
	textE4 = font.render("E4", True, (0, 128, 0))
	textF4 = font.render("F4", True, (0, 128, 0))
	textG4 = font.render("G4", True, (0, 128, 0))
	textA4 = font.render("A4", True, (0, 128, 0))
	textB4 = font.render("B4", True, (0, 128, 0))
	textCsharp4 = font.render("C#4", True, (0, 128, 0))
	textDsharp4 = font.render("D#4", True, (0, 128, 0))
	textFsharp4 = font.render("F#4", True, (0, 128, 0))
	textGsharp4 = font.render("G#4", True, (0, 128, 0))
	textAsharp4 = font.render("A#4", True, (0, 128, 0))

	test = 0
	C = pygame.mixer.Sound(scale + "Scale/C.wav")
	D = pygame.mixer.Sound(scale + "Scale/D.wav")
	E = pygame.mixer.Sound(scale + "Scale/E.wav")
	F = pygame.mixer.Sound(scale + "Scale/F.wav")
	G = pygame.mixer.Sound(scale + "Scale/G.wav")
	A = pygame.mixer.Sound(scale + "Scale/A.wav")
	B = pygame.mixer.Sound(scale + "Scale/B.wav")
	Csharp = pygame.mixer.Sound(scale + "Scale/C#.wav")
	Dsharp = pygame.mixer.Sound(scale + "Scale/D#.wav")
	Fsharp = pygame.mixer.Sound(scale + "Scale/F#.wav")
	Gsharp = pygame.mixer.Sound(scale + "Scale/G#.wav")
	Asharp = pygame.mixer.Sound(scale + "Scale/A#.wav")
	COctave = pygame.mixer.Sound(scale + "Scale/Octave1C.wav")
	DOctave = pygame.mixer.Sound(scale + "Scale/Octave1D.wav")
	EOctave = pygame.mixer.Sound(scale + "Scale/Octave1E.wav")
	FOctave = pygame.mixer.Sound(scale + "Scale/Octave1F.wav")
	GOctave = pygame.mixer.Sound(scale + "Scale/Octave1G.wav")
	AOctave = pygame.mixer.Sound(scale + "Scale/Octave1A.wav")
	BOctave = pygame.mixer.Sound(scale + "Scale/Octave1B.wav")
	CsharpOctave = pygame.mixer.Sound(scale + "Scale/Octave1C#.wav")
	DsharpOctave = pygame.mixer.Sound(scale + "Scale/Octave1D#.wav")
	FsharpOctave = pygame.mixer.Sound(scale + "Scale/Octave1F#.wav")
	GsharpOctave = pygame.mixer.Sound(scale + "Scale/Octave1G#.wav")
	AsharpOctave = pygame.mixer.Sound(scale + "Scale/Octave1A#.wav")
	COctave1 = pygame.mixer.Sound(scale + "Scale/Octave2C.wav")
	DOctave1 = pygame.mixer.Sound(scale + "Scale/Octave2D.wav")
	EOctave1 = pygame.mixer.Sound(scale + "Scale/Octave2E.wav")
	FOctave1 = pygame.mixer.Sound(scale + "Scale/Octave2F.wav")
	GOctave1 = pygame.mixer.Sound(scale + "Scale/Octave2G.wav")
	AOctave1 = pygame.mixer.Sound(scale + "Scale/Octave2A.wav")
	BOctave1 = pygame.mixer.Sound(scale + "Scale/Octave2B.wav")
	CsharpOctave1 = pygame.mixer.Sound(scale + "Scale/Octave2C#.wav")
	DsharpOctave1 = pygame.mixer.Sound(scale + "Scale/Octave2D#.wav")
	FsharpOctave1 = pygame.mixer.Sound(scale + "Scale/Octave2F#.wav")
	GsharpOctave1 = pygame.mixer.Sound(scale + "Scale/Octave2G#.wav")
	AsharpOctave1 = pygame.mixer.Sound(scale + "Scale/Octave2A#.wav")
	COctave2 = pygame.mixer.Sound(scale + "Scale/Octave3C.wav")
	DOctave2 = pygame.mixer.Sound(scale + "Scale/Octave3D.wav")
	EOctave2 = pygame.mixer.Sound(scale + "Scale/Octave3E.wav")
	FOctave2 = pygame.mixer.Sound(scale + "Scale/Octave3F.wav")
	GOctave2 = pygame.mixer.Sound(scale + "Scale/Octave3G.wav")
	AOctave2 = pygame.mixer.Sound(scale + "Scale/Octave3A.wav")
	BOctave2 = pygame.mixer.Sound(scale + "Scale/Octave3B.wav")
	CsharpOctave2 = pygame.mixer.Sound(scale + "Scale/Octave3C#.wav")
	DsharpOctave2 = pygame.mixer.Sound(scale + "Scale/Octave3D#.wav")
	FsharpOctave2 = pygame.mixer.Sound(scale + "Scale/Octave3F#.wav")
	GsharpOctave2 = pygame.mixer.Sound(scale + "Scale/Octave3G#.wav")
	AsharpOctave2 = pygame.mixer.Sound(scale + "Scale/Octave3A#.wav")
	COctave3 = pygame.mixer.Sound(scale + "Scale/Octave4C.wav")
	DOctave3 = pygame.mixer.Sound(scale + "Scale/Octave4D.wav")
	EOctave3 = pygame.mixer.Sound(scale + "Scale/Octave4E.wav")
	FOctave3 = pygame.mixer.Sound(scale + "Scale/Octave4F.wav")
	GOctave3 = pygame.mixer.Sound(scale + "Scale/Octave4G.wav")
	AOctave3 = pygame.mixer.Sound(scale + "Scale/Octave4A.wav")
	BOctave3 = pygame.mixer.Sound(scale + "Scale/Octave4B.wav")
	CsharpOctave3 = pygame.mixer.Sound(scale + "Scale/Octave4C#.wav")
	DsharpOctave3 = pygame.mixer.Sound(scale + "Scale/Octave4D#.wav")
	FsharpOctave3 = pygame.mixer.Sound(scale + "Scale/Octave4F#.wav")
	GsharpOctave3 = pygame.mixer.Sound(scale + "Scale/Octave4G#.wav")
	AsharpOctave3 = pygame.mixer.Sound(scale + "Scale/Octave4A#.wav")
	while not done:
		#if is_blue: color = (0, 128, 255)
		#else: color = (255, 100, 0)
		#pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
		titlewin = "HarpsiComp! " + scale
		#C E G -C major, F A C - F major , G B D - G Major
		#A C E - A Minor, D F A - D Minor , E G# B - E major
		pygame.display.set_caption(titlewin)
        	for event in pygame.event.get():
        	        if event.type == pygame.QUIT:
        	                done = True
			if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
				screen.fill((0, 0, 0))
				screen.blit(textC0,(200 - textC0.get_width() // 2, 150 - textC0.get_height() // 2))
				C.play()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
				screen.fill((0, 0, 0))
				screen.blit(textD0,(200 - textD0.get_width() // 2, 150 - textD0.get_height() // 2))
				D.play()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
				screen.fill((0, 0, 0))
				screen.blit(textE0,(200 - textE0.get_width() // 2, 150 - textE0.get_height() // 2))
				E.play()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
				screen.fill((0, 0, 0))
				screen.blit(textF0,(200 - textF0.get_width() // 2, 150 - textF0.get_height() // 2))
				F.play()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
				screen.fill((0, 0, 0))
				screen.blit(textG0,(200 - textG0.get_width() // 2, 150 - textG0.get_height() // 2))
				G.play()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
				screen.fill((0, 0, 0))
				screen.blit(textA0,(200 - textA0.get_width() // 2, 150 - textA0.get_height() // 2))
				A.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
				screen.fill((0, 0, 0))
				screen.blit(textB0,(200 - textB0.get_width() // 2, 150 - textB0.get_height() // 2))
				B.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
				screen.fill((0, 0, 0))
				screen.blit(textC1,(200 - textC1.get_width() // 2, 150 - textC1.get_height() // 2))
				COctave.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
				screen.fill((0, 0, 0))
				screen.blit(textD1,(200 - textD1.get_width() // 2, 150 - textD1.get_height() // 2))
				DOctave.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_o:
				screen.fill((0, 0, 0))
				screen.blit(textE1,(200 - textE1.get_width() // 2, 150 - textE1.get_height() // 2))
				EOctave.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
				screen.fill((0, 0, 0))
				screen.blit(textF1,(200 - textF1.get_width() // 2, 150 - textF1.get_height() // 2))
				FOctave.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFTBRACKET:
				screen.fill((0, 0, 0))
				screen.blit(textG1,(200 - textG1.get_width() // 2, 150 - textG1.get_height() // 2))
				GOctave.play()
		
			if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHTBRACKET:
				screen.fill((0, 0, 0))
				screen.blit(textA1,(200 - textA1.get_width() // 2, 150 - textA1.get_height() // 2))
				AOctave.play()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSLASH:
				screen.fill((0, 0, 0))
				screen.blit(textB1,(200 - textB1.get_width() // 2, 150 - textB1.get_height() // 2))
				BOctave.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
				screen.fill((0, 0, 0))
				screen.blit(textC2,(200 - textC2.get_width() // 2, 150 - textC2.get_height() // 2))
				COctave1.play()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
				screen.fill((0, 0, 0))
				screen.blit(textD2,(200 - textD2.get_width() // 2, 150 - textD2.get_height() // 2))
				DOctave1.play()
				
			if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
				screen.fill((0, 0, 0))
				screen.blit(textE2,(200 - textE2.get_width() // 2, 150 - textE2.get_height() // 2))
				EOctave1.play()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
				screen.fill((0, 0, 0))
				screen.blit(textF2,(200 - textF2.get_width() // 2, 150 - textF2.get_height() // 2))
				FOctave1.play()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
				screen.fill((0, 0, 0))
				screen.blit(textG2,(200 - textG2.get_width() // 2, 150 - textG2.get_height() // 2))
				GOctave1.play()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
				screen.fill((0, 0, 0))
				screen.blit(textA2,(200 - textA2.get_width() // 2, 150 - textA2.get_height() // 2))
				AOctave1.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_j:
				screen.fill((0, 0, 0))
				screen.blit(textB2,(200 - textB2.get_width() // 2, 150 - textB2.get_height() // 2))
				BOctave1.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
				screen.fill((0, 0, 0))
				screen.blit(textC3,(200 - textC3.get_width() // 2, 150 - textC3.get_height() // 2))
				COctave2.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
				screen.fill((0, 0, 0))
				screen.blit(textD3,(200 - textD3.get_width() // 2, 150 - textD3.get_height() // 2))
				DOctave2.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SEMICOLON:
				screen.fill((0, 0, 0))
				screen.blit(textE3,(200 - textE3.get_width() // 2, 150 - textE3.get_height() // 2))
				EOctave2.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_QUOTE:
				screen.fill((0, 0, 0))
				screen.blit(textF3,(200 - textF3.get_width() // 2, 150 - textF3.get_height() // 2))
				FOctave2.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
				screen.fill((0, 0, 0))
				screen.blit(textG3,(200 - textG3.get_width() // 2, 150 - textG3.get_height() // 2))
				GOctave2.play()
		
			if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
				screen.fill((0, 0, 0))
				screen.blit(textA3,(200 - textA3.get_width() // 2, 150 - textA3.get_height() // 2))
				AOctave2.play()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
				screen.fill((0, 0, 0))
				screen.blit(textB3,(200 - textB3.get_width() // 2, 150 - textB3.get_height() // 2))
				BOctave2.play()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
				screen.fill((0, 0, 0))
				screen.blit(textC4,(200 - textC4.get_width() // 2, 150 - textC4.get_height() // 2))
				COctave3.play()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
				screen.fill((0, 0, 0))
				screen.blit(textD4,(200 - textD4.get_width() // 2, 150 - textD4.get_height() // 2))
				DOctave3.play()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
				screen.fill((0, 0, 0))
				screen.blit(textE4,(200 - textE4.get_width() // 2, 150 - textE4.get_height() // 2))
				EOctave3.play()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
				screen.fill((0, 0, 0))
				screen.blit(textF4,(200 - textF4.get_width() // 2, 150 - textF4.get_height() // 2))
				FOctave3.play()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
				screen.fill((0, 0, 0))
				screen.blit(textG4,(200 - textG4.get_width() // 2, 150 - textG4.get_height() // 2))
				GOctave3.play()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
				screen.fill((0, 0, 0))
				screen.blit(textA4,(200 - textA4.get_width() // 2, 150 - textA4.get_height() // 2))
				AOctave3.play()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_COMMA :
				screen.fill((0, 0, 0))
				screen.blit(textB4,(200 - textB4.get_width() // 2, 150 - textB4.get_height() // 2))
				BOctave3.play()
		
	
			
			if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKQUOTE:
				screen.fill((0, 0, 0))
				screen.blit(textCsharp0,(200 - textCsharp0.get_width() // 2, 150 - textCsharp0.get_height() // 2))
				Csharp.play()
			
			if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
				screen.fill((0, 0, 0))
				screen.blit(textDsharp0,(200 - textDsharp0.get_width() // 2, 150 - textDsharp0.get_height() // 2))
				Dsharp.play()
			
			if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
				screen.fill((0, 0, 0))
				screen.blit(textFsharp0,(200 - textFsharp0.get_width() // 2, 150 - textFsharp0.get_height() // 2))
				Fsharp.play()
			
			if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
				screen.fill((0, 0, 0))
				screen.blit(textGsharp0,(200 - textGsharp0.get_width() // 2, 150 - textGsharp0.get_height() // 2))	
				Gsharp.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
				screen.fill((0, 0, 0))
				screen.blit(textAsharp0,(200 - textAsharp0.get_width() // 2, 150 - textAsharp0.get_height() // 2))	
				Asharp.play()



	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
				screen.fill((0, 0, 0))
				screen.blit(textCsharp1,(200 - textCsharp1.get_width() // 2, 150 - textCsharp1.get_height() // 2))
				CsharpOctave.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_6:
				screen.fill((0, 0, 0))
				screen.blit(textDsharp1,(200 - textDsharp1.get_width() // 2, 150 - textDsharp1.get_height() // 2))
				DsharpOctave.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_7:
				screen.fill((0, 0, 0))
				screen.blit(textFsharp1,(200 - textFsharp1.get_width() // 2, 150 - textFsharp1.get_height() // 2))
				FsharpOctave.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_8:
				screen.fill((0, 0, 0))
				screen.blit(textGsharp1,(200 - textGsharp1.get_width() // 2, 150 - textGsharp1.get_height() // 2))
					
				GsharpOctave.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_9:
				screen.fill((0, 0, 0))
				screen.blit(textAsharp1,(200 - textAsharp1.get_width() // 2, 150 - textAsharp1.get_height() // 2))
				AsharpOctave.play()




	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
				screen.fill((0, 0, 0))
				screen.blit(textCsharp2,(200 - textCsharp2.get_width() // 2, 150 - textCsharp2.get_height() // 2))
				CsharpOctave1.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_MINUS:
				screen.fill((0, 0, 0))
				screen.blit(textDsharp2,(200 - textDsharp2.get_width() // 2, 150 - textDsharp2.get_height() // 2))
				DsharpOctave1.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_EQUALS:
				screen.fill((0, 0, 0))
				screen.blit(textFsharp2,(200 - textFsharp2.get_width() // 2, 150 - textFsharp2.get_height() // 2))
				FsharpOctave1.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
				screen.fill((0, 0, 0))
				screen.blit(textGsharp2,(200 - textGsharp2.get_width() // 2, 150 - textGsharp2.get_height() // 2))
				GsharpOctave1.play()
			
			'''if event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
				screen.fill((0, 0, 0))
				screen.blit(textC0,(200 - textC0.get_width() // 2, 150 - textC0.get_height() // 2))
				GsharpOctave1.play()'''
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
				screen.fill((0, 0, 0))
				screen.blit(textAsharp2,(200 - textAsharp2.get_width() // 2, 150 - textAsharp2.get_height() // 2))
				AsharpOctave1.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F2:
				screen.fill((0, 0, 0))
				screen.blit(textCsharp3,(200 - textCsharp3.get_width() // 2, 150 - textCsharp3.get_height() // 2))
				CsharpOctave2.play()
			
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F3:
				screen.fill((0, 0, 0))
				screen.blit(textDsharp3,(200 - textDsharp3.get_width() // 2, 150 - textDsharp3.get_height() // 2))
				DsharpOctave2.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F4:
				screen.fill((0, 0, 0))
				screen.blit(textFsharp3,(200 - textFsharp3.get_width() // 2, 150 - textFsharp3.get_height() // 2))
				FsharpOctave2.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F5:
				screen.fill((0, 0, 0))
				screen.blit(textGsharp3,(200 - textGsharp3.get_width() // 2, 150 - textGsharp3.get_height() // 2))
				GsharpOctave2.play()
			
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F6:
				screen.fill((0, 0, 0))
				screen.blit(textAsharp3,(200 - textAsharp3.get_width() // 2, 150 - textAsharp3.get_height() // 2))
				AsharpOctave2.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F7:
				screen.fill((0, 0, 0))
				screen.blit(textCsharp4,(200 - textCsharp4.get_width() // 2, 150 - textCsharp4.get_height() // 2))
				CsharpOctave3.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F8:
				screen.fill((0, 0, 0))
				screen.blit(textDsharp4,(200 - textDsharp4.get_width() // 2, 150 - textDsharp4.get_height() // 2))
				DsharpOctave3.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F9:
				screen.fill((0, 0, 0))
				screen.blit(textFsharp4,(200 - textFsharp4.get_width() // 2, 150 - textFsharp4.get_height() // 2))
				FsharpOctave3.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
				screen.fill((0, 0, 0))
				screen.blit(textGsharp4,(200 - textGsharp4.get_width() // 2, 150 - textGsharp4.get_height() // 2))
				GsharpOctave3.play()
	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
				screen.fill((0, 0, 0))
				screen.blit(textAsharp4,(200 - textAsharp4.get_width() // 2, 150 - textAsharp4.get_height() // 2))
				AsharpOctave3.play()
	
			
			
        	pygame.display.flip()		

#Harpsichord("PythagDodec")	
