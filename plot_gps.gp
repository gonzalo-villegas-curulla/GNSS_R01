set datafile separator ","
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set format x "%H:%M\n%d-%b"
set term png
set output 'gps_plot.png'


set title "GPS Data"
set xlabel "Time"
set ylabel "Latitude"
set y2label "Longitude"

set ytics nomirror
set y2tics
set style data linespoints
#set missing ""

set terminal pngcairo size 1280,720
set grid

plot "dataGPS/gps_dataEdit.csv" using 1:($4 == "N" ? $5 : -$5) with lines title "Latitude"#, \
#     "dataGPS/gps_dataEdit.csv" using 1:($7 == "E" ? $8 : -$8) axes x1y2 with lines title "Longitude"

#plot 'data/gps_data.csv' using 1:($4/100) with lines title 'Latitude', \
#     'data/gps_data.csv' using 1:($6/100) axes x1y2 with lines title 'Longitude'
