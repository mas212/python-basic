player   = {"name": "player-1", "point": 200, "record": 5}
player2  = {"name": "player-2", "point": 300, "record": 7}

def attack(attacker, defender):
	if(attacker['point'] < defender['point']):
		print('selamat bro', player['point'])
	else:
		print('serangan gagal')

def trackRecord(record):
	if(record['record'] < record['record']):
		print('oke recor', player2['record'])

attack(player, player2)
trackRecord(player2)