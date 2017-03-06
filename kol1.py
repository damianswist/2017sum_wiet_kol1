import random

# returns current orientation
def get_current_orientation():
	current_orientation = random.randint(0,360)
	return current_orientation


# returns corrected orientation
def correct_orientation(current_orientation, max_correction_step):
	new_orientation = 0
	
	if 180 - max_correction_step < current_orientation < 180 + max_correction_step:
		new_orientation = 180
	elif current_orientation > 180:
		new_orientation = current_orientation - max_correction_step
	elif current_orientation < 180:
		new_orientation = current_orientation + max_correction_step	
	return new_orientation

		

if __name__=="__main__":
	max_correction_step = 3
	
	while True:
		current_orientation = get_current_orientation()
		corrected_orientation = correct_orientation(current_orientation, max_correction_step)
		print "Current orientation {0}: ".format(current_orientation)
		print "Corrected orientation {0}: ".format(corrected_orientation)
		print
		
		
		
		
