# rotek_keygen3
Keygen for some Rotek RX-22200 modems

Keygen for some Rotek RX-22200 modems with ESSID WIFI-DOM.ru-DDDD (where DDDD are the last 4 digits of the SN)\
Based on reverse engineering of the algorithm  found in /bin/flash in the firmware attached to this youtube clip https://www.youtube.com/watch?v=gEuftTAWGVE
\
\
The seeds are derived from an unknown hardware ID number found in /dev/mtdblock0\
\
seed 1 has a range of 0..0x763d\
seed 2 has a range of 0..0x7663\
seed 3 has a range of 0..0x7673\
\
However the real life range seems to be much smaller with most seed2 around 22000 and seed3=133\

Usage: python3 rotek_keygen3.py 15809 22845 133

Credit to drsnooker for his Matlab script that this was converted from: https://forum.hashkiller.io/index.php?threads/unpublished-wpa-key-algorithms.19944/post-354135
