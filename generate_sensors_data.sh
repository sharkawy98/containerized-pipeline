#!/bin/bash
sensors=( "sensor_0|50|100" "sensor_1|100|150" "sensor_2|200|300" "sensor_3|1000|1500" )
start="12:00:00 2021-01-01"
days=$((1*365))

create_sensor_data () {
  i=0
  while [[ $i -lt $days ]] 
  do
    echo -ne "$1... $i"\\r
    echo "$1,$(date -d"$start +$i days" +"%Y-%m-%d %H:%M:%S"),$(($2 + $RANDOM % ($3-$2)))" >> sensors_data.csv
    i=$((i+1))
  done
}

rm -f sensors_data.csv
echo "Generating sensors data..."

echo "sensor,timestamp,value" > sensors_data.csv
for elm in ${sensors[@]}; do
  sensor=$(echo $elm | cut -d '|' -f 1)
  from=$(echo $elm | cut -d '|' -f 2)
  to=$(echo $elm | cut -d '|' -f 3)
  create_sensor_data $sensor $from $to
  echo "$sensor... $days days"
done
echo "Done."
