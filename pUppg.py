# -- Carl Säflund 18/11 2015
# -- Aritmatrisen
# -- DD1310

from random import randint #hämtar randintklassen från ramdom-modulen
from colorama import Fore, Back #hämtat från stack overflow, en modul för färgerna till markeringen. ('bakgrundsbelysningen')
from colorama import init
init()
import sys
import re

class Matrix:	#klassen
	def __init__(self, size):
		self.size = size
		self.xPos = randint(0,size-1)
		self.yPos = randint(0,size-1)
		self.matrix = self.createMatrix() #behöver inte ett värde
		self.points = self.matrix[self.xPos][self.yPos]
		self.target = randint(1, 300)
		self.action = None

	def createMatrix(self):		#metod som skapar matrisen 
		matrix = [None]*self.size #en kolumn med size:st None element
		for i in range(self.size): #loop som multiplicerar kolumnerna med size för att skaa rader som blir en matris
			matrix [i]= [None]*self.size #skapar subgrupper till None-elementen
		for x in range(self.size): #kolumner
			for y in range(self.size): #rader
				matrix[x][y] = randint(1, 99) #matrix[kolumn][rad]
		return matrix #returnerar matrisen

	def printMatrix(self):		#metod som printar matrisen
		print(chr(27)+'[2J')	#tömmer terminalen
		for y in range(self.size):
			for x in range(self.size):
				if x == self.xPos and y == self.yPos:	#om den skriver ut den rutan man är på körs koden under
					print(Fore.BLACK + Back.WHITE + str(self.matrix[x][y]).rjust(5), end='   ' + Fore.WHITE + Back.BLACK) #Byter bakgrundsfär till vit och textfärg till svart och sen tillbaka till normalt
				else:
					print (str(self.matrix[x][y]).rjust(5), end='   ') # formatering. skriver ut mellanrum mellan siffrorna
			print ('\n')

	def movePlayer(self, input):	#metod som styr spelaren!
		for i in str(input):
			if i == 'N':
				if not self.yPos == 0:
					self.yPos -= 1
				else:
					print("Goodbye")
					sys.exit()
			elif i == 'S':
				if not self.yPos == self.size-1:
					self.yPos += 1
				else:
					print("Goodbye")
					sys.exit()
			elif i == 'W':
				if not self.xPos == 0:
					self.xPos -= 1
				else:
					print("Goodbye")
					sys.exit()
			elif i == 'E':
				if not self.xPos == self.size-1:
					self.xPos += 1
				else:
					print("Goodbye")
					sys.exit()
		if self.action == '+':
			self.points += self.matrix[self.xPos][self.yPos]
		if self.action == '-':
			self.points -= self.matrix[self.xPos][self.yPos]
#---------------------------------------------------------------------------------- Slut på klass!


def program(instance):	#programmedelandet 
	message = '''
______________________________________

	   You have {0} points
	   You need {1} points
______________________________________

	'''.format(instance.points, instance.target)
	instance.printMatrix()	#skriver ut matrisen
	print (message)			#skrive ut meddelandet (poäng och mål)

def gamefunc(instance):		#funktionsfunktion
		program(instance)	#kör programutskriften
		while True:			#alla inputs
			c = input('Vill du 1:addera eller 2:subtrahera?: ')
			if c == '1':
				instance.action = '+'
				break
			elif c == '2':
				instance.action = '-'
				break
			else:
				print('Försök igen')
		while True:
			b = input('Vilken rikting vill du röra dig? (N,S,E,W): ')
			if (1 == len(b) or len(b) == 2) and (re.search(b, 'NN|NE|NW|SS|SE|SW|EN|ES|EE|WN|WS|WW')):
				instance.movePlayer(str(b))
				if instance.points == instance.target:	#om dina poäng är samma som målet blir det sysExit och så vinner du
					print('Grattis du vann!')
					sys.exit()
				break

		else:
			print('Försök igen')

def intro():		#introprinten
	titel = '''

          :::     ::::::::: ::::::::::: :::::::::::   :::   :::       ::: ::::::::::: :::::::::  ::::::::::: ::::::::  :::::::::: ::::    ::: 
       :+: :+:   :+:    :+:    :+:         :+:      :+:+: :+:+:    :+: :+:   :+:     :+:    :+:     :+:    :+:    :+: :+:        :+:+:   :+:  
     +:+   +:+  +:+    +:+    +:+         +:+     +:+ +:+:+ +:+  +:+   +:+  +:+     +:+    +:+     +:+    +:+        +:+        :+:+:+  +:+   
   +#++:++#++: +#++:++#:     +#+         +#+     +#+  +:+  +#+ +#++:++#++: +#+     +#++:++#:      +#+    +#++:++#++ +#++:++#   +#+ +:+ +#+    
  +#+     +#+ +#+    +#+    +#+         +#+     +#+       +#+ +#+     +#+ +#+     +#+    +#+     +#+           +#+ +#+        +#+  +#+#+#     
 #+#     #+# #+#    #+#    #+#         #+#     #+#       #+# #+#     #+# #+#     #+#    #+#     #+#    #+#    #+# #+#        #+#   #+#+#      
###     ### ###    ###    ###     ########### ###       ### ###     ### ###     ###    ### ########### ########  ########## ###    ####       

										                Press enter to begin!!!!

	'''
	print (titel)
	#input('')

	regler = '''
_________________________________________________________________________________________________________________________________________


					Du kan röra dig i de fyra vädersträcken, N, S, W, E

					 	Du kan hoppa max två steg åt gången						

		  t.ex (NN), (NW) eller (E). Du kan inte hoppa norr och söder samtidigt samt öst och väst.

_________________________________________________________________________________________________________________________________________

'''
	print(regler)
	input('')


if __name__ == '__main__':
	a = Matrix(5) #skapar klassinstans (matrisen)
	intro()
	while True:
		gamefunc(a)