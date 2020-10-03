import time 
import serial 
import pymysql


def main():
    port = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=None)
    conn = pymysql.connect(host="localhost", user="root", port=3306, passwd="1234", db="mysql")
    row_data = [0] * 10


    try :
        with conn.cursor() as cur :
            sql_1="insert into smartfarm_data_values_1f(name, created_at, hum_data,tem_data,light_data,sm_data,co2) values(%s,%s,%s,%s,%s,%s,%s)"
            sql_2="insert into smartfarm_data_values_2f(name, created_at, hum_data,tem_data,light_data,sm_data,co2) values(%s,%s,%s,%s,%s,%s,%s)"
            sql_cnt="select count(*) from smartfarm_data_values_1f"
            sql_del_1 ="DELETE FROM smartfarm_data_values_1f WHERE id <= (SELECT * FROM (SELECT id FROM smartfarm_data_values_1f order by id desc limit 51,1 ) as P)"
            sql_del_2 ="DELETE FROM smartfarm_data_values_2f WHERE id <= (SELECT * FROM (SELECT id FROM smartfarm_data_values_2f order by id desc limit 51,1) as p)"
            
            while True:
                line = port.readline()
                arr= line.split()
                if len(arr) < 3:
                    continue
                dataType = arr[2]
                data = float(arr[1])

                ''' 1 floor '''
                if dataType == b'%1':
                    print("1F_Humidity: %.1f %%" % data)
                    row_data[0] = data
                elif dataType == b'C1':
                    print("1F_Temperature: %.1f C" % data)
                    row_data[1] = data
                elif dataType == b'LX1':
                    print("1F_cds: %.1f LX" % data)
                    row_data[2] = data
                elif dataType == b'SM1' :
                    print("1F_soil: %.1f SM" % data)
                    row_data[3] = data
                elif dataType == b'PPM1':
                    print("1F_co2: %.1f PPM" % data)
                    row_data[4] = data 


                ''' 2 floor '''
                if dataType == b'%2':
                    print("2F_Humidity: %.1f %%" % data)
                    row_data[5] = data
                elif dataType == b'C2':
                    print("2F_Temperature: %.1f C" % data)
                    row_data[6] = data
                elif dataType == b'LX2':
                    print("2F_cds: %.1f LX" % data)
                    row_data[7] = data
                elif dataType == b'SM2' :
                    print("2F_soil: %.1f SM" % data)
                    row_data[8] = data
                elif dataType == b'PPM2': 
                    print("2F_co2: %.1f PPM" % data)
                    row_data[9] = data


                cur.execute(sql_1,('smartfarm_1F',time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),row_data[0],row_data[1],row_data[2],row_data[3],row_data[4]))
                cur.execute(sql_2,('smartfarm_2F',time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),row_data[5],row_data[6],row_data[7],row_data[8],row_data[9]))
                cur.execute(sql_del_1)
                cur.execute(sql_del_2)
                conn.commit()
                time.sleep(0.1)

    except KeyboardInterrupt :
        exit()
    finally :
        conn.close()




if __name__=="__main__":
    main()
