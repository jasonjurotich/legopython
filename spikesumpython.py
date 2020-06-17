import math

from spike import App

from spike import(
	PrimeHub, LightMatrix, Button, StatusLight, 
  ForceSensor, MotionSensor, Speaker, ColorSensor, 
  App, DistanceSensor, Motor, MotorPair)

from spike.control import(
  wait_for_seconds, wait_until, Timer)

app = App()
hub = PrimeHub()
timer = Timer()

def wait(numseconds=1):
	return wait_for_seconds(numseconds)

def waitu(condition):
	# can have more than one condition
	return wait_until(condition)



# BUTTONS

def lbwup():
	return hub.left_button.wait_until_pressed()

def lbwur(): 
	return hub.left_button.wait_until_released()

def lbwp():
	return hub.left_button.was_pressed()

def lbip():
	return hub.left_button.is_pressed()

def rbwup():
	return hub.right_button.wait_until_pressed()

def rbwur(): 
	return hub.right_button.wait_until_released()

def rbwp():
	return hub.right_button.was_pressed()

def rbip():
	return hub.right_button.is_pressed()



# SPEAKER

def sb(note=60, seconds=0.2):
	# notes (44-123), default 60
	# any number, default 0.2
	return hub.speaker.beep(note, seconds)

def ssb(note=60):
	# notes (44-123), default 60
	# stops with sst()
	return hub.speaker.start_beep(note)

def sst():
	return hub.speaker.stop()

def sgv():
	return hub.speaker.get_volume()

def ssv(volume=100): 
	# volume (0-100), default 100
	return hub.speaker.set_volume(volume)



# LIGHTS

# 25 LEDS

def lsi(image='SMILE', brightness=100):
	light = hub.light_matrix
	# image is obligatory, default made SMILE
	# brightness (0-100), default is 100
	# use lo to stop it
	return light.show_image(image, brightness)

def lsp(x_axel=1, y_axel=1, brightness=100):
	light = hub.light_matrix
	# x and y axels obligatory, default made 1
	# brightness (0-100), default is 100
	# axels (1-5)
	return light.set_pixel(x_axel, y_axel, brightness)

def lw(text='Hi'):
	# any text, obligatory, default made Hi
	return hub.light_matrix.write(text)

def lo():
	return hub.light_matrix.off()

# IMAGE POSSIBILITIES
"""
YES, XMAS, ANGRY, ARROW_E, ARROW_N, ARROW_NE, ARROW_NW, 
ARROW_S, ARROW_SE, ARROW_SW, ARROW_W, ASLEEP, BUTTERFLY,
CHESSBOARD, CLOCK1, CLOCK2, STICKFIGURE, CLOCK3, CLOCK4,
CLOCK5, CLOCK6, CLOCK7, CLOCK8, CLOCK9, CONFUSED,COW, 
DIAMOND, DIAMOND_SMALL, DUCK, FABULOUS, GHOST, GIRAFFE,
GO_RIGHT, GO_LEFT, GO_IP, GO_DOWN, HAPPY, HEART, SNAKE,
HEART_SMALL, HOUSE, MEH, MUSIC_CROTCHET, MUSIC_QUAVER,
MUSIC_QUAVERS, NO, PACMAN,PITCHFORK, RABBIT, 
ROLLERSKATE, SAD, SILLY, SKULL, SMILE, SQUARE
"""

# STATUS LIGHT

def slon(color='white'):
	# Options: black, violet, blue, cyan, green, yellow, red, white
	# obligatory, default is white
	return hub.status_light.on(color)

def sloff():
	return hub.status_light.off()



# MOTION

def mgg():
	# Returns: shaken, tapped, doubletapped, falling, None
	return hub.motion_sensor.get_gesture()

def mwng():
	motion = hub.motion_sensor
	# Returns: shaken, tapped, doubletapped, falling, None
	return motion.wait_for_new_gesture()

def mgo():
	# Returns: front, back, up, down, left side, right side
	return hub.motion_sensor.get_orientation()

def mwno():
	motion = hub.motion_sensor
	# Returns: front, back, up, down, left side, right side
	return motion.wait_for_new_orientation()

def mgra():
	return hub.motion_sensor.get_roll_angle()

def mgpa():
	return hub.motion_sensor.get_pitch_angle()

def mgya():
	return hub.motion_sensor.get_yaw_angle()

def mrya():
	return hub.motion_sensor.reset_yaw_angle()

def mwg(gesture=None):
	# Options: shaken, tapped, doubletapped, falling, None
	return hub.motion_sensor.was_gesture(gesture)





# SENSORS

# DISTANCE

def dcm(port='C'):
	distance = DistanceSensor(port)
	return distance.get_distance_cm()

def din(port='C'):
	distance = DistanceSensor(port)
	return distance.get_distance_inches()

def dper(port='C'):
	distance = DistanceSensor(port)
	return distance.get_distance_percentage()

def dwdft(port='C', distance=0.1, unit='cm', short_range=False):
	distance = DistanceSensor(port)
	# distance (any num), default made 0.1
	# unit ('in', 'cm','%'), default cm
	# short_range (True, False) default False
	return distance.wait_for_distance_farther_than(distance, unit, short_range)

def dwdct(port='C', distance=1, unit='cm', short_range=False):
	distance = DistanceSensor(port)
	# distance (any num),
	# unit ('in', 'cm''%'), default cm
	# short_range (True, False) default False
	return distance.wait_for_distance_closer_than(distance, unit, short_range)

def dlu(port='C', right_top=100, left_top=100, right_bottom=100, left_botton=100):
	distance = DistanceSensor(port)
	# brightness (0-100)
	return distance.light_up(right_top, left_top, right_bottom, left_botton)

def dlua(port='C', brightness=100):
	distance = DistanceSensor(port)
	# brightness (0-100)
	return distance.light_up_all(brightness)



# COLOR

def cgc(port='A'):
	color = ColorSensor(port)
	return color.get_color()

def cgal(port='A'):
	color = ColorSensor(port)
	return color.get_ambient_light()

def cgrl(port='A'):
	color = ColorSensor(port)
	return color.get_reflected_light()

def cgri(port='A'):
	color = ColorSensor(port)
	return color.get_rgb_intensity()

def cgr(port='A'):
	color = ColorSensor(port)
	return color.get_red()

def cgg(port='A'):
	color = ColorSensor(port)
	return color.get_green()

def cgb(port='A'):
	color = ColorSensor(port)
	return color.get_blue()

def cwnc(port='A'):
	color = ColorSensor(port)
	return color.wait_for_new_color()

def cwuc(port='A', color=None):
	color = ColorSensor(port)
	# Options: black, violet, blue, cyan, green, yellow, red, white
	return color.wait_until_color(color)

def clua(port='A', brightness=100):
	color = ColorSensor(port)
	# brightness (0-100)
	return color.light_up_all(brightness)

def clu(port='A', light_1=100, light_2=100, light_3=100):
	color = ColorSensor(port)
	# brightness (0-100)
	return color.light_up(light_1, light_2, light_3)



# FORCE

def fip(port='B'):
	force = ForceSensor(port)
	return force.is_pressed()

def fgfn(port='B'):
	force = ForceSensor(port)
	return force.get_force_newton()

def fgfp(port='B'):
	force = ForceSensor(port)
	return force.get_force_percentage()

def fwup(port='B'):
	force = ForceSensor(port)
	return force.wait_until_pressed()

def fwur(port='B'):
	force = ForceSensor(port)
	return force.wait_until_released()



# MOTOR

# SINGLE MOTOR

def msdc(port='E', degrees=0):
	motor = Motor(port)
	# any number, no default
	return motor.set_degrees_counted(degrees)

def msdp(port='E', speed=100):
	motor = Motor(port)
	# back/forward (-100 to 100), no default
	return motor.set_default_speed(speed)

def mstt(port='E', speed=100):
	motor = Motor(port)
	# back/forward (-100 to 100), default using msdp
	# use mstp to stop
	return motor.start(speed)

def mstap(port='E', power=100):
	motor = Motor(port)
	# power (-100 to 100), no default
	# use mstp to stop
	return motor.start_at_power(power)

def mwi(port='E'):
	motor = Motor(port)
	return motor.was_interrupted()

def mssd(port='E', boolean=True):
	motor = Motor(port)
	# Only takes True or False, default True
	return motor.set_stall_detection(boolean)

def mws(port='E'):
	motor = Motor(port)
	return motor.was_stalled()

def mssa(port='E', action='coast'):
	motor = Motor(port)
	# Only takes 'coast', 'brake', or 'hold', default coast
	return motor.set_stop_action(action)

def mstp(port='E'):
	motor = Motor(port)
	# use mssa for action
	return motor.stop()

def mgs(port='E'):
	motor = Motor(port)
	return motor.get_speed()

def mgp(port='E'):
	motor = Motor(port)
	return motor.get_position()

def mgdc(port='E'):
	motor = Motor(port)
	return motor.get_degrees_counted()

def mgds(port='E'):
	motor = Motor(port)
	return motor.get_dfault_speed()


def mrtp(port='E', degrees=0, direction='shortest path', speed=100):
	motor = Motor(port)
	# degrees (0 to 359), no default, obligatory
	# shortest path, clockwise, counterclockwise
	# speed (0 to 100) or use msdp for default
	# if degrees is 0 then direction and speed are optional
	return motor.run_to_position(degrees, direction, speed)

def mrtdg(port='E', degrees=0, speed=100):
	motor = Motor(port)
	# degrees (0 to 359) obligatory
	# speed (0 to 100) obligatory
	return motor.run_to_degrees_counted(degrees, speed)

def mrfd(port='E', degrees=0, speed=100):
	motor = Motor(port)
	# any number, obligatory
	# back/forward (-100 to 100) default to msdp
	return motor.run_for_degrees(degrees, speed)

def mrfr(port='E', rotations=1, speed=100):
	motor = Motor(port)
	# any number, obligatory
	# back/forward (-100 to 100) default to msdp
	return motor.run_for_rotations(rotations, speed)

def mrfs(port='E', seconds=0.2, speed=100):
	motor = Motor(port)
	# any number, obligatory
	# back/forward (-100 to 100) default to msdp
	return motor.run_for_seconds(seconds, speed)


# MOTOR PAIRS

def mpgds(port1='E', port2='F'):
	motorp = MotorPair(port1, port2)
	return motorp.get_default_speed()

def mpsmr(port1='E', port2='F', amount=17.6, unit='cm'):
	motorp = MotorPair(port1, port2)
	# any number, default 17.6
	# unit ('in', 'cm'), default cm
	return motorp.set_motor_rotation(amount, unit)

def mpsds(port1='E', port2='F', speed=100):
	motorp = MotorPair(port1, port2)
	# back/forward (-100 to 100) default 100
	return motorp.set_default_speed(speed)

def mpm(port1='E', port2='F', amount=1, unit='cm', steering=0, speed=100):
	motorp = MotorPair(port1, port2)
	# any number,
	# unit ('in', 'cm', 'rotations, 'degrees', 'seconds'),
	# steering (-100 to 100), default is 0, add manually
	# speed (-100 to 100), add manually
	# use mpsds for default speed
	return motorp.move(amount, unit, steering, speed)

def mpstt(port1='E', port2='F', steering=0, speed=100):
	motorp = MotorPair(port1, port2)
	# steering (-100 to 100), default is 0, add manually
	# speed (-100 to 100) add manually
	# use mpsds for default speed and mpstp to stop
	return motorp.start(steering, speed)

def mpsap(port1='E', port2='F', power=100, steering=0):
	motorp = MotorPair(port1, port2)
	# power[back/forward] (-100 to 100), default is 100
	# steering (-100 to 100), default is 0, add manually
	# use mpstp to stop
	return motorp.start_at_power(power, steering)

def mpssa(port1='E', port2='F', action='coast'):
	motorp = MotorPair(port1, port2)
	# Only options are 'coast', 'brake', or 'hold'
	# Default is coast
	return motorp.set_stop_action(action)

def mpstp(port1='E', port2='F'):
	motorp = MotorPair(port1, port2)
	# should be used with mpssa
	return motorp.stop()

def mpmt(port1='E', port2='F', amount=1, unit='cm', left_speed=100, right_speed=100):
	motorp = MotorPair(port1, port2)
	# any number,
	# unit ('in', 'cm', 'rotations, 'degrees', 'seconds'),
	# left_speed (-100 to 100), right_speed (-100 to 100)
	# use mpsds for default speed instead of left and right
	return motorp.move_tank(amount, unit, left_speed, right_speed)

def mpsta(port1='E', port2='F', left_speed=100, right_speed=100):
	motorp = MotorPair(port1, port2)
	# left_speed (-100 to 100), right_speed (-100 to 100)
	return motorp.start_tank(left_speed, right_speed)

	def mpstap(port1='E', port2='F', left_power=100, right_power=100):
	motorp = MotorPair(port1, port2)
	# left_power (-100 to 100), right_power (-100 to 100)
	return motorp.start_tank_at_power(left_power, right_power)



# SOUND

def sound(name='Alert', volume=100):
	# Options for name: only from list below
	# Volume (0-100) default 100
	return app.play_sound(name, volume)

def soundst(name='Alert', volume=100):
	# Options for name: only from list below
	# Volume (0-100) default 100
	return app.start_sound(name, volume)

# Values for names
'''
		Alert, Applause1, Applause2,
		Applause3, Baa, Bangi, Bang2,
		BasketballBounce, BigBoing, Bird,
		Bite, Boat Horni, Boat Horn2, Bonk,
		BoomCloud, BoopBingBop,
		BowlingStrike, Burp1, Burp2, Burp3,
		CarAcceleratel, CarAccelerating2,
		Car Horn, Carldle, CarReverse,
		CarSkidi, CarSkid2, CarVroom,
		CatAngry, CatHappy, CatHiss,
		CatMeowl, CatMeow2, CatMeow3,
		CatPurring, CatWhining, Chatter,
		Chirp, Clang, ClockTicking,
		Clown Honki, Clown Honk2,
		Clown Honk3, Coin, Collect,
		Connect, Crank, CrazyLaugh,
		Croak, CrowdGasp, Crunch,
		Cuckoo, CymbalCrash, Disconnect,
		DogBarki, Dog Bark2, DogBark3,
		DogWhining1, DogWhining2,
		Doorbelli, Doorbell2, Doorbell3,
		DoorClosing, DoorCreeki,
		DoorCreek2, Door Handle,
		Doorknock, DoorSlaml, DoorSlam2,
		Drum Roll, DunDunDunnn,
		Emotional Piano, Fart1, Fart2, Fart3,
		Footsteps, Gallop, GlassBreaking,
		Glug, GoalCheer, Gong, Growl,
		Grunt, HammerHit, HeadShake,
		HighWhoosh, Jump, JungleFrogs,
		Lasert, Laser2, Laser3,
		Laughing Babyl, LaughingBaby2,
		Laughing Boy, LaughingCrowd1,
		Laughing Crowd2, Laughing Girl,
		Laughing Male, Lose, LowBoing,
		LowSqueak, LowWhoosh,
		MagicSpell, MaleJumpi,
		Male Jump2, Moo, Ocean Wave,
		Oops, Orchestra Tuning,
		PartyBlower, Pew, PingPongHit,
		PlaingFlyingBy,
		PlaneMotor Running, PlaneStarting,
		Pluck, Police Sireni, Police Siren2,
		Police Siren3, Punch, Rain,
		Ricochet, Rimshot, Ring Tone, Rip,
		Robot1, Robot2, Robot3,
		RocketExplosion Rumble, Rooster,
		ScramblingFeet, Screech, Seagulls,
		ServiceAnnouncement,
		Sewing Machine, ShipBell,
		SirenWhistle, Skid, SlideWhistlel,
		SlideWhistle2, Sneaker Squeak,
		Snoring, Snort, SpaceAmbience,
		SpaceFlyby, SpaceNoise, Splash,
		SportWhistle1, SportWhistle2,
		Squeaky Toy, Squish Pop,
		SuctionCup, Tada, TelephoneRing2,
		TelephoneRing, Teleport2,
		Teleport3, Teleport, TennisHit,
		ThunderStorm, TolietFlush,
		ToyHonk, ToyZing, Traffic,
		TrainBreaks, Train Horni,
		Train Horn2, Train Horn3,
		TrainOnTracks, TrainSignali,
		TrainSignal2, TrainStart,
		Train Whistle, Triumph,
		TropicalBirds, Wand, WaterDrop,
		WhistleThump, Whizi, Whiz2,
		WindowBreaks, Win, Wobble,
		WoodTap, Zip
'''



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

''' Create a short program to run 2 motors according to a beat, something like both motors in one direction, both in the other direction, one motor in opposite direction of the other. '''


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