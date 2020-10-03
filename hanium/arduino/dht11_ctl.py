from pyfirmata import Arduino, util
import pymysql
import time
import threading

board = Arduino('/dev/ttyACM1')
board2 = Arduino('/dev/ttyACM2')
conn = pymysql.connect(host="localhost", user="root", port=3306, passwd="1234", db="mysql")
try:
	it = util.Iterator(board)
	it.start()
	time_ctl_p = 1
	time_ctl_l = 1
	led_avg = 0
	pump_avg = 0
	flag_1f = 1
	flag_2f = 1
	DELAY = 0.002
	stepPerResolution = 650

	with conn.cursor() as cur :
		sql_ctl = "select water_ctl,fan_ctl,light_ctl,slide,heat_ctl from smartfarm_ctl_values_1f"
		sql_ctl_2 = "select water_ctl,fan_ctl,light_ctl,slide,heat_ctl from smartfarm_ctl_values_2f"
		sql_ans = "select * from smartfarm_automaticsys"
		sql_data = "select tem_data,hum_data,light_data,sm_data from smartfarm_data_values_1f"
		sql_avg = "select avg(minled),avg(maxled), avg(minpump), avg(maxpump) from smartfarm_data_standard"

		cur.execute(sql_avg)
		avg = cur.fetchone()
		while True:
			cur.execute(sql_data)
			realtime = cur.fetchone()

			cur.execute(sql_ans)
			cmp = cur.fetchone()

			cur.execute(sql_ctl)
			datas = cur.fetchone()

			cur.execute(sql_ctl_2)
			datas2 = cur.fetchone()

			time_ctl_p = cmp[5]
			time_ctl_l = cmp[2]

			led_avg = int((avg[0]+avg[1])/2)
			pump_avg = int((avg[2]+avg[3])/2)
			cur.execute("update smartfarm_automaticsys set light_avg = '%s', sm_avg = '%s' where id=4",(led_avg, pump_avg))


			if cmp[1] == 1: #automatic
				if realtime[3] > pump_avg :   #water_ctl
					if time_ctl_p == 0:
						board.digital[10].write(1)
					if time_ctl_p == 1:
						board.digital[10].write(0)

				else:
					board.digital[10].write(0)
				if realtime[0]<cmp[3] or realtime[0]>cmp[4] and realtime[1] < cmp[9] or realtime[1]>cmp[8]:   #fan_ctl
					board.digital[8].write(1)
					board.digital[9].write(0)
				else:
					board.digital[8].write(0)
					board.digital[9].write(0)
				if realtime[2] < led_avg:   #light_ctl
					if time_ctl_l == 0:
						board.digital[12].write(1)
					if time_ctl_l == 1:
						board.digital[12].write(0)
				else:
					board.digital[12].write(0)


			if cmp[1] == 0: #passive
				if datas[0] == 1:   #water_ctl
					board.digital[10].write(1)
				else:
					board.digital[10].write(0)
				if datas[1] == 1:   #fan_ctl
					board.digital[9].write(1)
					board.digital[8].write(0)
				else:
					board.digital[9].write(0)
					board.digital[8].write(0)
				if datas[2] == 1:   #light_ctl
					board.digital[2].write(1)
					board.digital[3].write(1)
					board.digital[4].write(1)
					board.digital[5].write(1)

				else:
					board.digital[2].write(0)
					board.digital[3].write(0)
					board.digital[4].write(0)
					board.digital[5].write(0)

				if datas[3] == 1: # time
					if flag_1f == 1:  # direction
						for i in range(stepPerResolution):
							board.digital[7].write(1)
							board.digital[11].write(1)
							board.pass_time(DELAY)
							board.digital[11].write(0)
							board.pass_time(DELAY)
							flag_1f = 0
				else: 
					if flag_1f == 0:
						for i in range(stepPerResolution):
							board.digital[7].write(0)
							board.digital[11].write(1)
							board.pass_time(DELAY)
							board.digital[11].write(0)
							board.pass_time(DELAY)
							flag_1f = 1

				if datas[4] == 1:   # heat_ctl
					board.digital[12].write(1)
					board.digital[13].write(1)
				else:
					board.digital[12].write(0)
					board.digital[13].write(0)



# 2F
				if datas2[0] == 1:   #water_ctl
					board2.digital[10].write(1)
				else:
					board2.digital[10].write(0)
				if datas2[1] == 1:   #fan_ctl
					board2.digital[8].write(1)
					board2.digital[9].write(0)
				else:
					board2.digital[8].write(0)
					board2.digital[9].write(0)
				#if datas2[2] == 1:   #light_ctl
				#	board2.digital[13].write(1)
				#else:
				#	board2.digital[13].write(0)
				if datas2[3] == 1: # time
					if flag_2f == 1:  # direction
						for i in range(stepPerResolution):
							board2.digital[7].write(1)
							board2.digital[11].write(1)
							board2.pass_time(DELAY)
							board2.digital[11].write(0)
							board2.pass_time(DELAY)
							flag_2f = 0
				else: 
					if flag_2f == 0:
						for i in range(stepPerResolution):
							board2.digital[7].write(0)
							board2.digital[11].write(1)
							board2.pass_time(DELAY)
							board2.digital[11].write(0)
							board2.pass_time(DELAY)
							flag_2f = 1

				if datas2[4] == 1:
					board2.digital[12].write(1)
					board2.digital[13].write(1)
				else:
					board2.digital[12].write(0)
					board2.digital[13].write(0)




#                       cur.execute(sql_2)
#                       data = cur.fetchone()
#                        if cmp[0] == 0 and datas[0] == 1:   #water_ctl
#                                board.digital[6].write(1)
#                        else:
#                                board.digital[6].write(0)
#                        if cmp[0] == 0 and datas[1] == 1:   #fan_ctl
#                                board.digital[5].write(1)
#                                board.digital[4].write(0)
#                        else:
#                                board.digital[5].write(0)
#                                board.digital[4].write(0)
#                        if cmp[0] == 0 and datas[2] == 1:   #light_ctl
#                                board.digital[13].write(1)
#                        else:
#                                board.digital[13].write(0)
			conn.commit()
			time.sleep(0.1)


except KeyboardInterrupt :
	exit()
finally:
	conn.close()
