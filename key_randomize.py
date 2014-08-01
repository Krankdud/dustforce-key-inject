from random import shuffle

# Change this to your levels folder, oh and make sure you make a backup
level_dir = 'c:/program files (x86)/steam/steamapps/common/dustforce/content/levels2/'

def set_key(filename, key_type):
	if key_type < 0 or key_type > 3:
		return

	try:
		f = open(filename, 'r+b')
	except IOError:
		print '*** Error: File was not found'
		return
	
	header = '\xB4\x9C\x34\x79\xE3\xA5\x4D\x9A\x33\x0E\x00'
	level = f.read()
	
	after_header = level.find(header) + len(header)
	# There are two possible combinations for the keys due to the bits for the keys
	# sometimes being offset by 1
	keys = ['\x14', '\x29',   # No keys
			'\x34', '\x69',   # Silver keys
			'\x54', '\xA9',   # Gold keys
			'\x74', '\xE9']   # Red keys
	
	key_index = None
	key_location = None
	for i in range(len(keys)):
		possible_key = level.find(keys[i] + '\x00\x00\x00', after_header)
		if possible_key != -1:
			if i / 2 == 0:
				print "Found no key"
			elif i / 2 == 1:
				print "Found silver key"
			elif i / 2 == 2:
				print "Found gold key"
			elif i / 2 == 3:
				print "Found red key"
			
			key_index = i
			key_location = possible_key
			break
	
	if key_index == None or key_location == None:
		print '*** ERROR: Could not find the key'
		return
			
	f.seek(key_location, 0)
	if key_type == 0:
		print 'Stripping key from map'
	elif key_type == 1:
		print 'Injecting silver key into map'
	elif key_type == 2:
		print 'Injecting gold key into map'
	elif key_type == 3:
		print 'Injecting red key into map'
	
	print 'Writing ' + hex(ord(keys[2 * key_type + key_index % 2])) + ' into map'
	print ''
	f.write(keys[2 * key_type + key_index % 2])
	f.close()
	
def randomize_keys():
	global level_dir

	keys = []
	for i in range(16):
		keys.append(1)
		keys.append(2)
		keys.append(3)
	shuffle(keys)
	
	levels = ['downhill', 'fireflyforest', 'momentum', 'momentum2',
				'suntemple', 'grasscave', 'ascent', 'summit',
				'garden', 'autumnforest', 'den', 'hyperdifficult',
				'courtyard', 'cliffsidecaves', 'library', 'cave',
				'precarious', 'treasureroom', 'arena', 'ramparts',
				'brimstone', 'parapets', 'observatory', 'moontemple',
				'chemworld', 'factory', 'park', 'boxes',
				'tunnel', 'basement', 'scaffold', 'cityrun',
				'clocktower', 'alley', 'hideout', 'concretetemple',
				'security', 'mary', 'venom', 'vat',
				'containment', 'pod', 'orb', 'wiring',
				'coretemple', 'dome', 'mary2', 'abyss']
				
	for i in range(len(levels)):
		set_key(level_dir + levels[i], keys[i])
	
if __name__ == '__main__':
	randomize_keys()
	print 'Done!'