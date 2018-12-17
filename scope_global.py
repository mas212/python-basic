#scope & global
namaKucing = "door"
makananKucing = "sego"

def kasihMakanKucing(nama, makanan):
	global namaKucing, makananKucing

	namaKucing = nama
	makananKucing = makanan

kasihMakanKucing('josBunder', 'sego-goreng')
print('nama nya kucing adalah', namaKucing, 'dan makan', makananKucing)

#scope global & return vulue
namaEmploye = "programmer"
positionEmploye = "backend developer"
salaryEmploye = "10000000"
def grid(employe, position, salary):
	global namaEmploye, positionEmploye, salaryEmploye

	namaEmploye = employe
	positionEmploye = positionEmploye
	salaryEmploye = salary
	return namaEmploye, positionEmploye, salaryEmploye
result = grid("mas", "fullstack", "2000000")
print(result)
# print("nama", namaEmploye, "position", positionEmploye, "salary", salaryEmploye)

jobTitle = "Backend develop"
position = "programmer"
skill = "python, djanggo, mysql"
salary = "3000 - 7000"

def newJobPythonDev(jobs, newPosition, newSkill, salaryPast):
	global jobTitle, position, skill, salary

	jobTitle 		= jobs
	position 		= newPosition
	skill 			= newSkill
	salary 			= salaryPast

	return jobTitle, position, skill, salary

postJobs = newJobPythonDev("backend developer", "python dev", "djanggo", "USD 3000")
print(postJobs)