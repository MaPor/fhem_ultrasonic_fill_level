# fhem_ultrasonic_fill_level

This is how to connect a ultrasonic device for a raspi. The ultrasonic device is mounted inside a rain water cistern to monitor the height of the water inside the cistern.
During hot summers without rain there is the danger of missing water and because the water is used in the toilet.... :-)

# Installation / Prerequisites

- Running Raspi
- wired ultrasonic device (4 wires: 2 power supply (5V), 2 wires signals -> GPIO)
- running FHEM for house automation -> calling python script out of fhem in recurring time distances...

# Usage

- Measuring the distance from sensor to water level by time of flight
- known mounting heigt -> calculation of fill level possible

# Issues

- Sometimes weird measuring value due to multipath reflexions or swimming ball inside of cistern. -> quick solution: take 5 measurements and collect a mean value. every mearuement value far away from this mean value is not valid.
