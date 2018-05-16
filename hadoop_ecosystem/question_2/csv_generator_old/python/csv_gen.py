import csv
import time
import random

col_three = ['arturo','pedro','felipe','gerardo','jack','nikita']
col_four = [20,21,23,25,53,67,68,69,80]
col_five = ['TCP','TCP','Telnet','SMTP','DNS','DHCP','DHCP','TFTP']
time_stamp = lambda: int(round(time.time() * 1000))

def gen_csv():
	with open('log.csv', 'w') as csv_file:
		csv_writer = csv.writer(csv_file, delimiter=",")
		for i in range(1000):
			print("Record {} created!".format(i+1))
			ran_one = random.randint(0,5)
			ran_two = random.randint(0,7)
			int_to_binary = "{0:08b}".format(i+1)
			csv_writer.writerow([time_stamp(), int_to_binary, col_three[ran_one], col_four[ran_two], col_five[ran_two]])

gen_csv()