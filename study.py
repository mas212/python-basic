
monster = {
	'name' : 'bang point',
	'point' : '1000'
}

def startGame():
	choice = input(' mau game apa ? 1.mobile legend 2.pubg 3.exit')

	if choice == "1":
		goGame()
	elif choice == "2":
		goPubg()
	else:
		goExit()
		

def goGame():
	print('oke point')

def goPubg():
	print('pubg new star game')

def goExit():
	print('keluarlah' + monster['point'])

startGame()