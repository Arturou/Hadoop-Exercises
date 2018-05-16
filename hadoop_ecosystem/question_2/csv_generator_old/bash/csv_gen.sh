#! /bin/bash

col_three=('arturo' 'pedro' 'felipe' 'gerardo' 'jack' 'nikita');
col_four=(20 21 23 25 53 67 68 69 80);
col_five=('TCP' 'TCP' 'Telnet' 'SMTP' 'DNS' 'DHCP' 'DHCP' 'TFTP');
for ((i=0; i<1000;i++))
do
	echo "Record $((i+1)) created!"
	timestamp=`date +%s%3N`;
	ran_one=$RANDOM%6;
	ran_two=$RANDOM%8;
	printf "$timestamp,$((i+1)),${col_three[ran_one]},${col_four[ran_two]},${col_five[ran_two]}\n" >> log.csv
done