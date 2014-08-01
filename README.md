<<<<<<< HEAD
A quick Python script for injecting keys into a Dustforce map.
This let's you add or remove keys from custom maps, which can be useful if you
are using a stock level as a base, or if you are designing a custom hub.

If you run key_inject.py without any arguments, it will ask you for the file name
and which key to inject.

For command-line folks:
Usage: python key_inject.py <filename> <key>
- <filename> is the name of the file for the level you want to inject a key into.
             Path should be included if it isn't in the same folder as this script.
- <key> is a number from 0 to 3 which determines which key to inject
	0: No key
	1: Silver key
	2: Gold key
	3: Red key
	

The Python scripts were made for 2.7. If you use 3.0, you probably just need to
change the print statements and change the divisions to use // instead of /
	
There's a little bonus script included that randomizes the keys for all the
stock levels. If you use it, make sure you set level_dir to be the directory
where your levels are.
There's no guarantee that all the levels will be unlockable if you use it,
it was mainly made as a fun way to test the key injection.