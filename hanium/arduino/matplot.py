import datetime
import time
import pymysql
import matplotlib.pyplot as plt
import matplotlib.legend as legend
conn= pymysql.connect(host="localhost", user="root",passwd="1234", db="mysql")
current=datetime.datetime.now()
last_time=current-datetime.timedelta(minutes=1)

try :
    tmep1 = 0
    tmep2 = 0
    lstx=[]
    lst_tmp=[]
    lst_hum=[]
    lst_soil=[]
    lst_light=[]
    standard_tmp_min=[]
    standard_tmp_max=[]
    standard_hum_min=[]
    standard_hum_max=[]
    standard_sm=[]
    standard_light=[]
    fig=plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    fig.show()
    fig.canvas.draw()
    with conn.cursor() as cur :
            sql="select * from smartfarm_data_values_1f where created_at > %s"
            sql_ans="select mintmp,maxtmp,minhum,maxhum from smartfarm_automaticsys"
            sql_std="select light_avg,sm_avg from smartfarm_automaticsys"
            cur.execute(sql_std)
            std = cur.fetchone()
            light_std = std[0]
            sm_std = std[1]
            while True :
                    i=0
                    cur.execute(sql_ans)
                    cmp =cur.fetchone()

                    cur.execute(sql,(last_time))
                    for row in cur.fetchall():
                        lstx.append(row[7])
                        lst_tmp.append(row[2])
                        lst_hum.append(row[3])
                        lst_soil.append(row[5])
                        lst_light.append(row[4])
                        last_time=row[7]
                        standard_tmp_min.append(cmp[0])
                        standard_tmp_max.append(cmp[1])
                        standard_hum_min.append(cmp[2])
                        standard_hum_max.append(cmp[3])
                        standard_light.append(light_std)
                        standard_sm.append(sm_std)
                        i=i+1
                    conn.commit()
                    if i==0 :
                        plt.pause(0.01)
                        fig.canvas.draw()
                        time.sleep(0.5)
                        continue
                   # plt.ylim(0,100)
                    plt.subplot(2,2,1)
                    tmp,=plt.plot(lstx,lst_tmp,'r.-')
                    standard_tmp1, = plt.plot(lstx,standard_tmp_min,'r--')
                    standard_tmp2, = plt.plot(lstx,standard_tmp_max,'r--')
                    plt.subplot(2,2,2)
                    hum,=plt.plot(lstx,lst_hum,'b.-')
                    standard_hum1, = plt.plot(lstx,standard_hum_min,'b--')
                    standard_hum2, = plt.plot(lstx,standard_hum_max,'b--')
                    plt.subplot(2,2,3)
                    soil,=plt.plot(lstx,lst_soil,'g.-')
                    standard_sm1, = plt.plot(lstx,standard_sm,'g--')
                    plt.subplot(2,2,4)
                    light,=plt.plot(lstx,lst_light,'c.-')
                    standard_light1, = plt.plot(lstx,standard_light,'c--')
                    plt.legend([tmp, hum, soil, light], ['Temperature', 'Humidity', 'soil', 'light'], loc=4)
                    plt.pause(0.01)
                    fig.canvas.draw()
                    time.sleep(0.5)
except KeyboardInterrupt :
    exit()
finally :
    conn.close()
