#set datafile separator ","
#set xdata time
#set timefmt "%Y-%m-%d %H:%M:%S"
#set format x "%H:%M:%S"
#set term png
#set output 'gps_plot.png'

#set title "GPS Data"
#set xlabel "Time"
#set ylabel "Latitude"
#set y2label "Longitude"

#set ytics nomirror
#set y2tics
#set style data linespoints
#set missing ""

#plot 'DATA_GPS/gps_data.csv' using 1:($4/100) with lines title 'Latitude', \
#     'DATA_GPS/gps_data.csv' using 1:($6/100) axes x1y2 with lines title 'Longitude'

set datafile separator ","
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set format x "%H:%M:%S"
set term png
set output 'gps_plot.png'

set title "GPS Data"
set xlabel "Time"
set ylabel "Latitude"
set y2label "Longitude"

set ytics nomirror
set y2tics
set style data linespoints

plot 'DATA_GPS/gps_dataEdit.csv' using 1:(($3 == "A" && $5 != "") ? ($4/100) : 1/0) with lines title 'Latitude', \
     'DATA_GPS/gps_dataEdit.csv' using 1:(($3 == "A" && $7 != "") ? ($6/100) : 1/0) axes x1y2 with lines title 'Longitude'
