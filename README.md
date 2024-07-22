# Content of this repo

In this repo I am retrieving GNSS sensor data from a bunch of Raspberry Pi boards under different environments. Particularly, the R01 (first Raspberry, 3 model B) is running python code (using the libraries `serial`, and also `adafruit_bme280` and `RPi.GPIO` for other tests) in Raspbian OS 32 bit (a version from 2022).

# Done

I have managed to:
* open a serial port via hardware from the GPS6MV2 module to the RPi
* read NMEA sentences and split them into data fields
* store the file and scp it to my local machine
* plot a few data arrays

# Ongoing work

The [documentation](https://components101.com/sites/default/files/component_datasheet/NEO6MV2%20GPS%20Module%20Datasheet.pdf) of the hat has not yet clarified (or I have not yet come across it) some conditions for sufficient performance, namely:
* Signal intensity
* Transducer orientation
* Operation bands and satellites
* "Booting" time

At present, it takes some good 5 minutes to stabilise the messages received. By trial and error, I have established that the blue LED is blinking when the sensor is receiving signal (ergo, also correctly wired). This means that next points of interest to inspect are going to be:
* Check signal integrity
* Check received satellite's signal intensity/attenuation

## Example test: going shopping around the corner

![](DATA_GPS/ShoppingTest.png)

It appears that the data would be useless while getting the keys from inside the house and while inside the shop. The rest of the trajectory resembles the path to the shop (with correct axes scaling). What are we missing?
* The data has to be processed
* The quality of the transducer or the board components may be only sufficiently correct for DIY purposes


