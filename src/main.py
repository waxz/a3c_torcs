
	
#-*- coding:utf-8 -*-
from flask import Flask,request
import random,os,time
import subprocess
import docker
app=Flask(__name__)
 
# test_list=[]  #本教程的目的就是要在多进程下，取代类似这样子的对象

from controller import controller
#读取数据库里test_list
class cmd_lock():
    def __init__(self):
        self.lock=False
    def get_lock(self):
        self.lock=True
    def release_lock(self):
        self.lock=False

Locker=cmd_lock()

@app.route('/cmd_api', methods=['POST','GET'])
def register():
    global game_controller
    # print (request.headers)
    # print  (request.form)
    # print  (request.form['name'])
    # print  (request.form.get('name'))
    # print ( request.form.getlist('name'))
    # print  (request.form.get('nickname', default='little apple'))
    # cmd_buff=conn.get("cmd_buff")
    # print('buff \n',cmd_buff)

    worker=request.form.get('worker')
    # port=request.form.get('port')
    print("get worker :{} ".format(worker))
    cmd_dict={worker:{"cmd":"start"}}

    # Locker.get_lock()
    game_controller.create(worker)
    # cmd_buff.update(cmd_dict)
    # conn.set('cmd_buff',cmd_buff)

    # print('buff \n',cmd_buff)
    
    # controller()
    # os.system('torcs -nofuel -nolaptime -p {} &'.format(port) )
    # os.system('sh autostart.sh')

    return 'start'

           


                
    


game_controller=controller()

if __name__ =="__main__":
    # clear_redis()
    
    
    app.run(threaded=False)
    print("shut down "*5)
    os.system('sh kill_docker.sh')

    # app.run(processes=3)
    