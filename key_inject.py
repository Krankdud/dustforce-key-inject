import sys

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
	
if __name__ == '__main__':
	if len(sys.argv) == 3:
		set_key(sys.argv[1], int(sys.argv[2]))
	else:
		print 'Type in filename of the level to inject/strip a key from:'
		level = raw_input()
		print 'Which key to inject?\n0: No key\n1: Silver key\n2: Gold key\n3: Red key\n(Type 0-3 for the key)'
		key = input()
		while key < 0 or key > 3:
			key = input()
		set_key(level, key)