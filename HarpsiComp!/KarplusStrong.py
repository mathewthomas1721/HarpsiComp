#Mathew Thomas - N15690387
#Music Software Projects, NYU Courant, Fall 2016
#Karplus-Strong algorithm for generating string sounds
#Credit for this approach to the implementation of the Karplus-Strong algorithm goes to saracogluhamet, as posted on https://saracogluahmet.wordpress.com/. 

from random import random
from array import array
import wave
 
fs=44100 #standard sampling frequency value
 
nchannels,swdth,frame_rate,nframes=1,2,44100,44100
 
max_val=32767
 
def Generate(f,nsamples,filename):
 
    N=fs//f
     
    buffer=[random()-0.5 for i in range(int(N))]
    samples=[]
 
    for i in range(nsamples):
        samples.append(buffer[0])
        avg=0.997*0.5*(buffer[0]+buffer[1])
        buffer.append(avg)
        buffer.pop(0)
 
    tempbuffer=[int(x*max_val) for x in samples]
    #print (tempbuffer)
    stringdata=array('h',tempbuffer).tostring()
    file=wave.open(filename,'wb')
    file.setparams((nchannels,swdth,frame_rate,nframes,'NONE','nonecompressed'))    
    file.writeframes(stringdata)
    file.close()
   
	
#Generate(528,44100//1,'C.wav')
	


