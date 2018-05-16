import time
import random
import pandas as pd
import numpy as np

col_three = ['arturo','pedro','felipe','gerardo','jack','nikita']
col_four = [20,21,23,25,53,67,68,69,80]
col_five = ['TCP','TCP','Telnet','SMTP','DNS','DHCP','DHCP','TFTP']
time_stamp = lambda: int(round(time.time() * 1000))
today=time.strftime("%Y_%m_%d__%H_%M_%S")
file_name="log_"+today+".csv"
def gen_csv():
	arr=[]
	for i in range(1000):
		ran_one = random.randint(0, 5)
		ran_two = random.randint(0, 7)
		arr.append([i + 1, time_stamp(), col_three[ran_one], col_four[ran_two], col_five[ran_two]])
	df = pd.DataFrame(np.array(arr))
	df.to_csv(file_name, sep=',')

gen_csv()
