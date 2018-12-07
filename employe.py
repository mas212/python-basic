employe = {
	"level" : {
		"level_name":['junior', "medium", "master"]
	},
	"position" : "backend developer",
	"point" : 10
}

def recuruite(vaule):
	pointTest = employe['point'] * vaule
	if pointTest > 50:
		print("anda master python dev")
	else:
		print("anda belajar python dev")

recuruite(10)
