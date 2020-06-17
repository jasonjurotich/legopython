import spikesumpython.py

# EXAMPLES


def testsp():
	print(sgv())
	sb(60, 0.5)
	sb(67, 0.5)
	sb(60, 0.5)

# testsp()


def testmo():
	print(mgg())

# testmo()


def testButtonLight():
	while True:
		lbwup()
		lsi('SKULL',100)
		wait(5)
		lo()    

# test()


def testlight():
	lsi('HAPPY')
	wait(5)
	lo()

# testlight()


def motionLightApp(): 
	while True:
		ori = mwno()
		if ori == 'front':
			lsi('ASLEEP')
			soundst('Snoring')
		elif ori == 'up':
			lsi('HAPPY')
			soundst('Triumph')

motionLightApp()


# abs() is absolute value, it works similar to int() or float()
def lightAngle():
	while True:
		angle = abs(mgpa()) * 2
		lsi('HAPPY', angle)

# lightAngle()


def testco():
	print(cgc())
  clu('A',20,30,50)
  wait(5)
  clua('A',100)
  print(cgal())

# testco()


def testdis():
	print(dcm())
  dlua('C', 100)
  wait(5)
  dlua('C', 0)

# testdis()


def testfor():
	while True:
		fwup()
		print(fgfp())
		print(mgg())
		ssb(44)

# testfor()



def runMoterForSeconds():
	mrfs('E', 2.0, 75)

runMoterForSeconds()


def runMoterForDegrees():
	mrfd('E', 360, 50)

runMoterForDegrees()


def runToPosition():
	wait(1)
	mrtp('E', 0, 'shortest path', 30)
	wait(1)
	mrtp('E', 90, 'clockwise', 100)

# runToPosition()

''' 
Create a short program to run 2 motors according to a beat, 
something like both motors in one direction, both in the other 
direction, one motor in opposite direction of the other. 

'''


def testForceMotor1():
	msds(25)
	fwup()
	mstt()
	fwur()
	mstp()
	
# testForceMotor1()


def testForceMotor2():
	msds(25)
	fwup()
	fwur()
	mstt()
	fwup()
	fwur()
	mstp()
	
# testForceMotor2()


def forceMotorWhileCount():
	count = 1
	msds(25)
	while count < 5:
		fwup()
		mstt()
		fwur()
		mstp()
		count += 1

# forceMotorWhileCount()


def forceMotorWhileTrue():
	while True:
		mstt('E', fgfp())

# forceMotorWhileTrue()

def colorMotor():
	while timer.now() < 30:
		color = cwnc()
		if color == 'violet':
			mrfr('E',1,100)
		elif color == 'yellow':
			mrfr('F',1,100)

# colorMotor()


def colorReflectMotor():
	while True:
		color = cwnc()

		if color == 'magenta':
			mrfr('E',1,per)
		elif color == 'yellow':
			mrfr('F',1,per)

# colorReflectMotor()


def distanceMotor():
	while True:
		dwdft('B', 20, 'cm')
		mstt()
		dwdct('B', 20, 'cm')
		mstp()

# distanceMotor()


def distancePerMotor():
	while True:
		per = dper()
		if per is not None:
			mstt('E', 100 - per)

# distancePerMotor()


def motorPair():
	mpsds('E','F',50)
	mpm('E','F',2,'seconds')

	mpsds('E','F',-50)
	mpm('E','F',2,'seconds')

	mpmt('E','F',10,'cm',25,75)
	mpmt('E','F',1,'rotations',-50,50)

# motorPair()


def hand():
	mrfs('E', 1, 75)
	while True:
		lbwup()
		mssd('E', False)
		mstt('E', -75)
		lbwur()
		mssd('E', True) 
	# There’s a missing a line of code here

# hand()


def testsound():
	sound('Alert', 3)

# testsound()
