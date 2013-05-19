#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    netscan.py
#
#    Copyright 2013 Mike Harley <VestedSkeptic@gmail.comm>
#		
#    netscan is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    netscan is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with netscan.  If not, see <http://www.gnu.org/licenses/>.

import threading, getopt, sys, time

# *********************************************************
def usage():
	"""
	
	print out usage
	
	"""
	print ""
	print "netscan.py [COMANDS]"
	print "  -l              --   Listen mode, gets packets and prints data"
	print "  -s [data]       --   Send mode, sends packets over and over"
	print "  -m              --   Passive profiling of all the channels (1-11)"
	print "  -c [UserName]   --   Chat client mode"
	print "  -r              --   Reloop shows the mod/remainder of the specified channel"
	print "  -p              --   Ping/Pong testing, Run this on one machine and it will"
	print "                       respond with a pong."
	print "  -k              --   Ping server mode, will repsond to pings with pong and current time"

# *********************************************************
def main():
	listen_mode = send_mode = scan_chans_mode = chat_mode = ping_mode_serv = ping_mode_client = reloop_mode = False
	
	# parse arguments
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hlrmkpc:s:f:")
	except getopt.GetoptError, err:
		print str(err)
		usage()
		sys.exit(1)
	for opt, arg in opts:
		if opt == "-h":
			usage()
			sys.exit(0)
		elif opt == "-f":
			config_file = arg
		elif opt == "-l": 
			listen_mode = True
		elif opt == "-r":
			reloop_mode = True
		elif opt == "-s":
			send_mode = True
			send_data = arg
		elif opt == "-m":
			scan_chans_mode = True
		elif opt == "-c":
			UserName = arg
			chat_mode = True
		elif opt == "-k":
			ping_mode_serv = True
		elif opt == "-p":
			ping_mode_client = True
			
	if listen_mode:
		pass
		
	elif reloop_mode:
		pass
		
	elif send_mode:
		pass
			
	elif chat_mode:
		pass
		
	elif scan_chans_mode:
		pass
			
	elif ping_mode_serv:
		print "Ping Server mode"
		pass
	
	elif ping_mode_client:
		pass
		
	else:
		usage()
		sys.exit()

				
# *********************************************************		
if __name__ == "__main__":
	main()
