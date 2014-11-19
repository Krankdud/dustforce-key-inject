import sys

def set_nexus(filename, nexusify):
	try:
		f = open(filename, 'r+b')
	except IOError:
		print '*** Error: File was not found'
		return
	
	header = '\xB4\x9C\x34\x79\xE3\xA5\x4D\x9A\x33\x0E\x00'
	level = f.read()
	
	after_header = level.find(header) + len(header)
	
	# Like with keys, there are two possibilities. Not sure why though.
	nexus_flags = ['\xA7\x53', '\xA7\x00',	# Not a nexus
					'\xA7\xD3', '\xA7\x01']	# Is a nexus
	
	nexus_index = None
	nexus_location = None
	for i in range(len(nexus_flags)):
		possible_nexus = level.find(nexus_flags[i] + '\x00\x00\x00', after_header)
		if possible_nexus != -1:
			if i / 2 == 0:
				print "Found a normal level"
			else:
				print "Found a nexus"
			
			nexus_index = i
			nexus_location = possible_nexus
	
	if nexus_index == None or nexus_location == None:
		print '*** Error: Could not find nexus'
		return
	
	f.seek(nexus_location, 0)
	if nexusify == True:
		print 'Making the level a nexus...'
		f.write(nexus_flags[2 + nexus_index % 2])
	else:
		print 'Making the nexus a level...'
		f.write(nexus_flags[nexus_index % 2])
		
	print ''
	f.close()
	
if __name__ == '__main__':
	if len(sys.argv) == 3:
		set_nexus(sys.argv[1], bool(int(sys.argv[2])))
	else:
		print 'Type in the filename of the level to nexusify / denexusify:'
		level = raw_input()
		print 'Do you want to make it a nexus?\n0: No\n1: Yes'
		key = input()
		while key < 0 or key > 1:
			key = input()
		set_nexus(level, bool(key))
