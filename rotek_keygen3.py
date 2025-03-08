# keygen for some Rotek RX-22200 modems with ESSID WIFI-DOM.ru-DDDD (where DDDD are the last 4 digits of the SN)
# Based on reverse engineering of the algorithm  found in /bin/flash in the firmware attached to this
# youtube clip https://www.youtube.com/watch?v=gEuftTAWGVE
#
# the seeds are derived from an unknown hardware ID number found in /dev/mtdblock0
#
# seed 1 has a range of 0..0x763d
# seed 2 has a range of 0..0x7663
# seed 3 has a range of 0..0x7673
#
# however the real life range seems to be much smaller with most seed2 around 22000 and seed3=133

import argparse

def rotek_keygen3(seed1, seed2, seed3):
	charset = 'aaaaabcdeeeeefhiiiijkmnprstuuuuuvwxyyyyzAAAABCDEEEEFGHJKLMNPQRSTUUUUVWXYYYYZ12233445566778899'

	pos = 18
	pwd = ["" for i in range(18)]
	while pos > 0:
		seed1 = 171*seed1 % int('763d', 16)
		seed2 = 172*seed2 % int('7663', 16)
		seed3 = 170*seed3 % int('7673', 16)
		total = seed1+seed2+seed3
		letter = charset[total % len(charset)]
		pwd[pos-1] = letter

		if pos < 18:
			if pwd[pos-1] == pwd[pos]:
				pos = pos + 1

		if pos < 17:
			if pwd[pos-1] == pwd[pos+1]:
				pos = pos + 1

		if pos < 16:
			if pwd[pos-1] == pwd[pos+2]:
				pos = pos + 1

		pos = pos-1

	psk = pwd[8:18]
	print("PSK: %s" % "".join(psk))

parser = argparse.ArgumentParser(description='Keygen for some Rotek RX-22200 modems with ESSID WIFI-DOM.ru-DDDD (where DDDD are the last 4 digits of the SN)')
parser.add_argument('seed1', help='Seed1', type=int)
parser.add_argument('seed2', help='Seed2', type=int)
parser.add_argument('seed3', help='Seed3', type=int)
args = parser.parse_args()

rotek_keygen3(args.seed1, args.seed2, args.seed3)