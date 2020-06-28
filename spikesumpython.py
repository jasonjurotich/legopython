# SPIKE HUB POR IOS OR ANDROID APP

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

hub.left_button()
hub.right_button()

hub.[left/right].wait_until_pressed()
hub.[left/right].is_pressed()
hub.[left/right].was_pressed()


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
hub.speaker.beep()
hub.speaker.stop()
hub.speaker.start_beep()
hub.speaker.get_volume()
hub.speaker.set_volume()


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
hub.light_matrix()

hub.light_matrix.show_image()
hub.light_matrix.set_pixel()
hub.light_matrix.write()
hub.light_matrix.off()



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

hub.status_light.on()
hub.status_light.off()


def slon(color='white'):
	# Options: black, violet, blue, cyan, green, yellow, red, white
	# obligatory, default is white
	return hub.status_light.on(color)

def sloff():
	return hub.status_light.off()



# MOTION
hub.motion_sensor()

hub.motion_sensor.get_gesture()
hub.motion_sensor.was_gesture()
hub.motion_sensor.wait_for_new_gesture()
hub.motion_sensor.get_orientation()
hub.motion_sensor.wait_for_new_orientation()
hub.motion_sensor.get_roll_angle()
hub.motion_sensor.get_pitch_angle()
hub.motion_sensor.get_yaw_angle()
hub.motion_sensor.reset_yaw_angle()



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
DistanceSensor(port)

DistanceSensor('A').get_distance_cm()
DistanceSensor('A').get_distance_inches()
DistanceSensor('A').get_distance_percentage()
DistanceSensor('A').wait_for_distance_farther_than()
DistanceSensor('A').wait_for_distance_closer_than()
DistanceSensor('A').light_up()
DistanceSensor('A').light_up_all()



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
ColorSensor(port)

ColorSensor('C').get_color()
ColorSensor('C').get_ambient_light()
ColorSensor('C').get_reflected_light()
ColorSensor('C').get_rgb_intensity()
ColorSensor('C').get_red()
ColorSensor('C').get_green()
ColorSensor('C').get_blue()
ColorSensor('C').wait_for_new_color()
ColorSensor('C').wait_until_color()
ColorSensor('C').light_up()
ColorSensor('C').light_up_all()

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
ForceSensor(port)
ForceSensor('D').is_pressed()
ForceSensor('D').get_force_newton()
ForceSensor('D').get_force_percentage()
ForceSensor('D').wait_until_pressed()
ForceSensor('D').wait_until_released()


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
Motor(port)

Motor('E').set_degrees_counted()
Motor('E').set_default_speed()
Motor('E').start()
Motor('E').start_at_power()
Motor('E').stop()
Motor('E').set_stop_action()
Motor('E').set_stall_detection()
Motor('E').was_interrupted()
Motor('E').was_stalled()
Motor('E').get_speed()
Motor('E').get_position()
Motor('E').get_degrees_counted()
Motor('E').get_default_speed()
Motor('E').run_to_position()
Motor('E').run_to_degrees_counted()
Motor('E').run_for_degrees()
Motor('E').run_for_rotations()
Motor('E').run_for_seconds()



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
MotorPair(port1, port2)

MotorPair('E','F').get_default_speed()
MotorPair('E','F').set_motor_rotation()
MotorPair('E','F').set_default_speed()
MotorPair('E','F').move()
MotorPair('E','F').start()
MotorPair('E','F').start_at_power()
MotorPair('E','F').stop()
MotorPair('E','F').set_stop_action()
MotorPair('E','F').move_tank()
MotorPair('E','F').start_tank()
MotorPair('E','F').start_tank_at_power()


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
app.play_sound()
app.start_sound()

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







# HUB MICROPYTHON POR TERMINAL
# Review callback options in each method
# hub.motion.callback(beep())
# Need to put the method, then period and then tab to see the options. 
# Options in brackets. Take brackets out and put option for method. 


hub()
utime()

utime.sleep(1)


# ONE COMMAND
hub.power_off()
hub.info()
hub.temperature()
hub.status()
hub.repl_restart()
hub.supervision.info()
hub.file_transfer()
hub.led() # 3 args


# MULTIPLE COMMANDS
hub.bluetooth()
hub.ble()
hub.battery()
hub.USB_VCP()
hub.button()
hub.sound()
hub.display()
hub.Image()
hub.motion()
hub.port()




# BLUETOOTH	
hub.bluetooth.discoverable()
hub.bluetooth.info()

hub.ble.connect()
hub.ble.scan()
hub.ble.scan_result()
hub.ble.mac()
hub.ble.rssi()




# BATTERY

hub.battery.BATTERY_BAD_BATTERY()
hub.battery.BATTERY_HUB_TEMPERATURE_CRITICAL_OUT_OF_RANGE()   
hub.battery.BATTERY_NO_ERROR()
hub.battery.BATTERY_TEMPERATURE_OUT_OF_RANGE()
hub.battery.BATTERY_TEMPERATURE_SENSOR_FAIL()
hub.battery.BATTERY_VOLTAGE_TOO_LOW()
hub.battery.CHARGER_STATE_CHARGING_COMPLETED()
hub.battery.CHARGER_STATE_CHARGING_ONGOING()  
hub.battery.CHARGER_STATE_DISCHARGING()
hub.battery.CHARGER_STATE_FAIL()              
hub.battery.USB_CH_PORT_CDP()
hub.battery.USB_CH_PORT_DCP()            
hub.battery.USB_CH_PORT_NONE()
hub.battery.USB_CH_PORT_SDP()

# from_bytes to_bytes

hub.battery.info()
hub.battery.capacity_left()
hub.battery.charger_detect()
hub.battery.current()         
hub.battery.temperature()     
hub.battery.voltage()




# USB
hub.USB_VCP.any()
hub.USB_VCP.init()
hub.USB_VCP.readline()
hub.USB_VCP.readlines()
hub.USB_VCP.readinto()
hub.USB_VCP.setinterupt()
hub.USB_VCP.close()
hub.USB_VCP.send()
hub.USB_VCP.CTS()
hub.USB_VCP.isconnected()
hub.USB_VCP.read()
hub.USB_VCP.write()
hub.USB_VCP.RTS()
hub.USB_VCP.recv()




# BUTTON
hub.button.left()
hub.button.right()
hub.button.center()
hub.button.connect()

hub.button.[left/right/center].presses()
hub.button.[left/right/center].is_pressed()
hub.button.[left/right/center].was_pressed()
hub.button.[left/right/center].on_change()




# SOUND

hub.sound.play()
hub.sound.volume() # 0 - 10 
hub.sound.beep() # 3 args
# freq, time, waveform (sin,square,triangle, sawtooth)
# hub.sound.beep(2000, 500, 3)  

hub.sound.SOUND_SIN()
hub.sound.SOUND_SQUARE()
hub.sound.SOUND_TRIANGLE()
hub.sound.SOUND_SAWTOOTH()

# from_bytes to_bytes




# DISPLAY

hub.display.show()
hub.display.clear()
hub.display.rotation() # takes two arguments
hub.display.pixel() # takes two arguments



		
# IMAGE

hub.Image.get_pixel() # 3 args      
hub.Image.set_pixel() # 4 args
hub.Image.height()     
hub.Image.width()      
hub.Image.shift_left() # 2 args     
hub.Image.shift_right() # 2 args   
hub.Image.shift_up() # 2 args  
hub.Image.shift_down() # 2 args

image = hub.Image("90004\n06090\n00900\n09090\n90009")
image = hub.Image('90009:90009:99999:09640:00900')
image = hub.Image("90009\n09090\n00900\n09090\n90009")
image = hub.Image(2, 2, b'\x08\x08\x08\x08')


'''
hub.Image.HEART, hub.Image.HEART_SMALL, hub.Image.HAPPY, 
hub.Image.SMILE, hub.Image.SAD, hub.Image.CONFUSED, 
hub.Image.ANGRY, hub.Image.ASLEEP, hub.Image.SURPRISED, 
hub.Image.SILLY, hub.Image.FABULOUS, hub.Image.MEH,
hub.Image.CLOCK12, hub.Image.CLOCK11, hub.Image.CLOCK10, 
hub.Image.CLOCK9, hub.Image.CLOCK8, hub.Image.CLOCK7, 
hub.Image.CLOCK6, hub.Image.CLOCK5, hub.Image.CLOCK4, 
hub.Image.CLOCK3, hub.Image.CLOCK2, hub.Image.CLOCK1,
hub.Image.ARROW_N, hub.Image.ARROW_NE, hub.Image.ARROW_E, 
hub.Image.ARROW_SE, hub.Image.ARROW_S, hub.Image.ARROW_SW, 
hub.Image.ARROW_W, hub.Image.ARROW_NW, hub.Image.TRIANGLE, 
hub.Image.TRIANGLE_LEFT, hub.Image.CHESSBOARD, hub.Image.DIAMOND, 
hub.Image.DIAMOND_SMALL, hub.Image.SQUARE, hub.Image.SQUARE_SMALL, 
hub.Image.RABBIT, hub.Image.COW, hub.Image.MUSIC_CROTCHET, 
hub.Image.MUSIC_QUAVER, hub.Image.MUSIC_QUAVERS, hub.Image.PITCHFORK, 
hub.Image.XMAS, hub.Image.PACMAN, hub.Image.TARGET, 
hub.Image.TSHIRT, hub.Image.ROLLERSKATE, hub.Image.DUCK, 
hub.Image.HOUSE, hub.Image.TORTOISE, hub.Image.BUTTERFLY, 
hub.Image.STICKFIGURE, hub.Image.GHOST, hub.Image.SWORD, 
hub.Image.GIRAFFE, hub.Image.SKULL, hub.Image.UMBRELLA, 
hub.Image.SNAKE, hub.Image.ALL_CLOCKS, hub.Image.ALL_ARROWS, 
hub.Image.YES, hub.Image.NO
'''


# The \n are separators by line. Each number is for each pixel/block on the screen. 
# Each number, 0-9, sets the brightness of that pixel via pwm.

# You use display with image:

hub.display.show(hub.Image.YES)




# MOTION

hub.motion.FREEFALL()
hub.motion.SHAKE()
hub.motion.LEFTSIDE()        
hub.motion.RIGHTSIDE()
hub.motion.FRONT()    
hub.motion.BACK()     
hub.motion.UP()
hub.motion.DOWN()
hub.motion.TAPPED()         
hub.motion.DOUBLETAPPED()    
hub.motion.NONE()

hub.motion.[BACK,UP,etc].

__class__       
hub.motion.[BACK,UP,etc].count()           
hub.motion.[BACK,UP,etc].endswith()        
hub.motion.[BACK,UP,etc].find()
hub.motion.[BACK,UP,etc].format()      
hub.motion.[BACK,UP,etc].index()        
hub.motion.[BACK,UP,etc].isalpha()         
hub.motion.[BACK,UP,etc].isdigit()
hub.motion.[BACK,UP,etc].islower()         
hub.motion.[BACK,UP,etc].isspace()         
hub.motion.[BACK,UP,etc].isupper()         
hub.motion.[BACK,UP,etc].join()
hub.motion.[BACK,UP,etc].lower()         
hub.motion.[BACK,UP,etc].lstrip()         
hub.motion.[BACK,UP,etc].replace()        
hub.motion.[BACK,UP,etc].rfind()
hub.motion.[BACK,UP,etc].rindex()       
hub.motion.[BACK,UP,etc].rsplit()        
hub.motion.[BACK,UP,etc].rstrip()        
hub.motion.[BACK,UP,etc].split()
hub.motion.[BACK,UP,etc].startswith()      
hub.motion.[BACK,UP,etc].strip()    
hub.motion.[BACK,UP,etc].upper()         
hub.motion.[BACK,UP,etc].center()
hub.motion.[BACK,UP,etc].encode()         
hub.motion.[BACK,UP,etc].partition()       
hub.motion.[BACK,UP,etc].rpartition()     
hub.motion.[BACK,UP,etc].splitlines()



hub.motion.accelerometer() # tuple with (x,y,z) axis
hub.motion.accelerometer_filter()
hub.motion.gyroscope() # tuple with (x,y,z) axis in degrees      
hub.motion.gyroscope_filter()
hub.motion.orientation() # string with gesture Upper or lower case???
hub.motion.position() # tuple with (x,y,z) axis in degrees
hub.motion.preset_yaw()      
hub.motion.reset_yaw()
hub.motion.was_gesture() # boolean: was GESTURE since last call
hub.motion.gesture() # boolean: is currently GESTURE

# GESTURES
LEFTSIDE, RIGHTSIDE, UP, DOWN, FRONT, BACK
TAPPED, DOUBLETAPPED, SHAKE, FREEFALL




# PORT

hub.port.ATTACHED        
hub.port.DETACHED        
hub.port.MODE_DEFAULT
hub.port.MODE_GPIO       
hub.port.MODE_FULL_DUPLEX                
hub.port.MODE_HALF_DUPLEX

# from_bytes to_bytes

hub.port.A
hub.port.B               
hub.port.C               
hub.port.D
hub.port.E               
hub.port.F               


hub.port.[A,B,C,D,E,F].
  
hub.port.[A,B,C,D,E,F].info
hub.port.[A,B,C,D,E,F].mode            
hub.port.[A,B,C,D,E,F].pwm  # PowerMeter??
hub.port.[A,B,C,D,E,F].device



# ONLY APPEARS WHEN MOTOR IS CONNECTED  
hub.port.[A,B,C,D,E,F].motor.

             
hub.port.[A,B,C,D,E,F].motor.BUSY_MODE()       
hub.port.[A,B,C,D,E,F].motor.BUSY_MOTOR()
hub.port.[A,B,C,D,E,F].motor.EVENT_COMPLETED()                 
hub.port.[A,B,C,D,E,F].motor.EVENT_INTERRUPTED()
hub.port.[A,B,C,D,E,F].motor.FORMAT_PCT()
hub.port.[A,B,C,D,E,F].motor.FORMAT_RAW()    
hub.port.[A,B,C,D,E,F].motor.FORMAT_SI()    
hub.port.[A,B,C,D,E,F].motor.PID_POSITION()
hub.port.[A,B,C,D,E,F].motor.PID_SPEED()  
hub.port.[A,B,C,D,E,F].motor.STOP_BRAKE()     
hub.port.[A,B,C,D,E,F].motor.STOP_FLOAT()    
hub.port.[A,B,C,D,E,F].motor.STOP_HOLD()


hub.port.[A,B,C,D,E,F].motor.brake()         
hub.port.[A,B,C,D,E,F].motor.busy()           
hub.port.[A,B,C,D,E,F].motor.float()       
hub.port.[A,B,C,D,E,F].motor.hold()   

hub.port.[A,B,C,D,E,F].motor.default()
'''{'pid': (0, 0, 0), 'max_power': 0, 'speed': 0, 'stall': True, 'deceleration': 150, 'stop': 1, 'callback': <bound_method>, 'acceleration': 100}'''

hub.port.[A,B,C,D,E,F].motor.get()  # [0, 0, 175, 0]      
hub.port.[A,B,C,D,E,F].motor.mode()  # [(1, 0), (2, 2), (3, 1), (0, 0)]        
hub.port.[A,B,C,D,E,F].motor.pid()   # (0, 0, 0)         
hub.port.[A,B,C,D,E,F].motor.run_at_speed() # speed arg
''' 
speed = 50, max_power = 100, acceleration = 100, deceleration = 100, stall = False
'''
hub.port.[A,B,C,D,E,F].motor.run_for_degrees() # 1 arg, can 2               
hub.port.[A,B,C,D,E,F].motor.run_for_time() # 1 arg, can 3, time - msec and speed
hub.port.[A,B,C,D,E,F].motor.run_to_position() # 1 arg, can 2, position and speed

hub.port.[A,B,C,D,E,F].motor.preset()  # 2 args          
hub.port.[A,B,C,D,E,F].motor.pwm()  # 2 args, from -100 to 100    
hub.port.[A,B,C,D,E,F].motor.pair() # 2 args 
# hub.port.A.motor.pair(hub.port.B.motor)




#MOTOR ENCODER
hub.port.A.device.get() --> returns integer array with [0,relative position,absolute position,0].

"""
hub.port.At': {'datasets': 1, 'type': 0, 'figures': 1, 'decimals': 0}, 'capability': b' @\x00\x00\x01\x04', 'map_out': 8, 'name': 'LOAD', 'pct': (0.0, 100.0), 'map_in': 8, 'si': (0.0, 127.0), 'raw': (0.0, 127.0)}, {'symbol': '\x01\x04\x01', 'format': {'datasets': 0, 'type': 0, 'figures': 0, 'decimals': 194}, 'capability': b'\x00\x00\x00\x00\x00\x00', 'map_out': 0, 'name': 'K', 'pct': (3444.96, 1.12104e-43), 'map_in': 0, 'si': (0.0, 2.24208e-44), 'raw': (5.73972e-42, 5.73972e-42)}], 'speed': 115200, 'hw_version': 4096, 'combi_modes': (14, 15), 'type': 48}
"""

#COLOR
hub.port.F.device.get() --> returns integer array [reflected light, color id]; color id can be type None
# [1, None, 5, 5, 5]
# [32, 0, 150, 153, 153]
# [46, 4, 135, 259, 312]

"""
hub.port.D'DEBUG', 'pct': (0.0, 100.0), 'map_in': 16, 'si': (0.0, 65535.0), 'raw': (0.0, 65535.0)}, {'symbol': '', 'format': {'datasets': 7, 'type': 1, 'figures': 5, 'decimals': 0}, 'capability': b'@@\x00\x00\x04\x84', 'map_out': 0, 'name': 'CALIB', 'pct': (0.0, 100.0), 'map_in': 0, 'si': (0.0, 65535.0), 'raw': (0.0, 65535.0)}], 'speed': 115200, 'hw_version': 268435456, 'combi_modes': (99,), 'type': 61}
"""



#FORCE
hub.port.E.device.get() --> returns integer array [(raw) pressure, pressed, (SI) pressure?];
# [9, 1, 663]

"""
hub.port.Fres': 4, 'decimals': 0}, 'capability': b'\x00\x00\x00\x00\x04\x84', 'map_out': 0, 'name': 'FRAW', 'pct': (0.0, 100.0), 'map_in': 16, 'si': (0.0, 1023.0), 'raw': (0.0, 1023.0)}, {'symbol': 'RAW', 'format': {'datasets': 1, 'type': 1, 'figures': 4, 'decimals': 0}, 'capability': b'\x00\x00\x00\x00\x04\x84', 'map_out': 0, 'name': 'FPRAW', 'pct': (0.0, 100.0), 'map_in': 16, 'si': (0.0, 1023.0), 'raw': (0.0, 1023.0)}, {'symbol': '', 'format': {'datasets': 8, 'type': 1, 'figures': 4, 'decimals': 0}, 'capability': b'\x00@\x00\x00\x04\x84', 'map_out': 0, 'name': 'CALIB', 'pct': (0.0, 100.0), 'map_in': 0, 'si': (0.0, 1023.0), 'raw': (0.0, 1023.0)}], 'speed': 115200, 'hw_version': 268435456, 'combi_modes': (63,), 'type': 63}
"""


#The first entry ranges from 0-10 and appears to be the pressure in Newtons. 
#The second entry is 0 or 1 for released or pressed. 
#The third entry appears to also be pressure, but ranging from 382-687. 
#It is labelled as SI_PRESSURE, but does not appear to be in Newtons or grams.


#Ultrasonic Distance sensor:	off by about 1 cm
hub.port.F.device.get() --> returns integer array [distance (cm)] with a single entry (distance in cm)
# [15]
""" 
'pct': (0.0, 100.0), 'map_in': 0, 'si': (0.0, 255.0), 'raw': (0.0, 255.0)}], 'speed': 115200, 'hw_version': 268435456, 'combi_modes': (), 'type': 62} 
"""






	
# EXAMPLES

import hub, utime	
def on_start(vm, stack):
  hub.led(255, 0, 0) # red  (r,g,b)
  hub.led(3) # blue   (colors 0 - 10)
  hub.led
  for i in range(11):
      hub.led(i)
      utime.sleep(1)	



def on_start():
  while True:
      if hub.button.left.is_pressed():
          hub.display.show(hub.Image.YES)
      elif hub.button.right.is_pressed():
          hub.display.show(hub.Image.NO)
		
  

def on_start():
  hub.port.A.motor.mode(1)
  hub.port.A.motor.get()
  hub.port.A.motor.pwm(100) 
  utime.sleep(1)
  hub.port.A.motor.float()
  hub.port.A.motor.brake()
  
  hub.port.A.motor.run_at_speed(
  	speed = 50, 
  	max_power = 100, 
  	acceleration = 100, 
  	deceleration = 100, 
  	stall = False)
  	
  hub.port.A.motor.run_for_degrees(degrees = 90, speed = 50)
  hub.port.A.motor.run_to_position(90, 50)  
  hub.port.A.motor.default()
  hub.port.A.motor.run_for_time(100, 50)   
  
  # only works if motors are connected
  p = hub.port.A.motor.pair(hub.port.B.motor)
  p.pwm(40,-40)   # drive straight
  p.run_for_time(200,40,-40)




	
