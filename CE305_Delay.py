# --- BEGIN IMPORTS ---

import pygame
import datetime

# ---  END  IMPORTS ---


# --- BEGIN INITILIZATION ---

# initialize pygame package
pygame.init()

# set two helper variables
init = True # enables the initialization loop
looper = False # disables the main program loop

# stores recorded data
lines = []

print 'CE 305: Delay Assessment'
print '        Data Logger'

# instruction output
print 'press `b` to begin'
print '      `p` to quit'

# ---  END  INITILIZATION ---


# --- BEGIN USER INTERACTION ---

# initialization loop
while init:

	# loop over events occuring within current iteration
	for event in pygame.event.get():

		# if the event is a key press...
		if event.type == pygame.KEYDOWN and event.key == pygame.K_b:

			# if the key pressed is 'b' (beginning time)
			if event.key == pygame.K_b:

				# if so, store the current time
				rn = datetime.datetime.now()

				# create a new line with the key press and the current timestamp, modified
				# to match the existing program's output
				line = '%s %s' % (rn.strftime('%H %M %S %f')[:-4], pygame.key.name(event.key))
				
				# add this line to the data array
				lines.append(line)
				
				# print the line for the user to see
				print line
				
				# kill the initilization loop by
				# setting init to False
				init = False

				# begin the primary loop by
				# setting looper to True
				looper = True

# primary data gathering loop
while looper:

	# loop over all events within the current iteration
	for event in pygame.event.get():

		# if the event is a key press...
		if event.type == pygame.KEYDOWN:

			# if the key pressed is 'p' (quitting time)
			if event.key == pygame.K_p:

				# print message for user
				print 'saving, hang tight...'

				# generate filename as traffic_{current_time}.txt
				fn = 'traffic_' + datetime.datetime.now().strftime('%H%M%S') + '.txt'

				# create new file with generated name
				with open(fn, 'w') as f:

					# write each line from the data array
					# to the text file
					for line in lines:
						f.write('%s\n' % line)

				# alert the user that saving is complete
				# and give them the filename
				print 'file saved: %s' % fn

				# kill the primary loop (program exits)
				looper = False

			# if the key pressed is anything else...
			else:

				# get current timestamp
				rn = datetime.datetime.now()

				# create a new line with the key press and the current timestamp, modified
				# to match the existing program's output
				line = '%s %s' % (rn.strftime('%H %M %S %f')[:-4], pygame.key.name(event.key))

				# add this line to the data array
				lines.append(line)

				# print the line for the user to see
				print line

# ---  END USER INTERACTION ---

# inform the user that the run is complete
print 'program complete'