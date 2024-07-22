set terminal png size 1024,768
set output 'DATA_THP/temphumpress.png'

set title "Temperature, Humidity, and Pressure over Time"
set xlabel "Time"
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set format x "%H:%M:%S"

set ylabel "Temperature (C)"
set y2label "Humidity (%)"
set y2tics
set grid

# Plot Temperature on the left y-axis, Humidity on the right y-axis
plot 'DATA_THP/temphumpress.csv' using 1:2 with lines title 'Temperature', \
     '' using 1:3 axes x1y2 with lines title 'Humidity', \
     '' using 1:4 axes x1y2 with lines title 'Pressure'
