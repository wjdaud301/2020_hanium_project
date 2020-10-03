from pyfirmata import Arduino, util
import pymysql
import time
import threading

conn = pymysql.connect(host="localhost", user="root", port=3306, passwd="1234", db="mysql")
board = Arduino('/dev/ttyACM0')
flag = 1
DELAY = 0.002
stepPerResolution = 1000


try:
    with conn.cursor() as cur :
        sql_ctl = "select water_ctl,fan_ctl,light_ctl,slide from smartfarm_ctl_values_1f"

        while True:

            cur.execute(sql_ctl)
            datas = cur.fetchone()

            if datas[3] == 1:
                if flag == 1:  # direction
                    for i in range(stepPerResolution):
                            board.digital[2].write(1)
                            board.digital[3].write(1)
                            board.pass_time(DELAY)
                            board.digital[3].write(0)
                            board.pass_time(DELAY)
                            flag = 0


            if datas[3] == 0:
                if flag == 0:
                    for i in range(stepPerResolution):
                            board.digital[2].write(0)
                            board.digital[3].write(1)
                            board.pass_time(DELAY)
                            board.digital[3].write(0)
                            board.pass_time(DELAY)
                            flag = 1

            conn.commit()
except KeyboardInterrupt :
        exit()

