"""
    #  @ModuleName: algoPerformance
    #  @Function: 
    #  @Author: Ljx
    #  @Time: 2020/9/14 10:35
"""
import os
import time
from config import Terminal
from utls.subprocess_test import runcmd
from auto_run_new import path, mounted_dir

def write_top(res):
    with open(f"/{mounted_dir}/top.txt", "a") as f:
        f.write(res)

"""测试接口1和接口5是否存在内存显存泄露"""
os.system(f"bash {path} {Terminal.main_free_num1} &")
time.sleep(5)
code, pid = runcmd("pidof test-ji-api")
write_top("接口1资源占用情况" + str(pid) + '\n')
for i in range(10):
    time.sleep(120)
    cmd_cpu = "top -n 1 -p %s |grep test  |awk '{print $10}'" % pid
    cmd_mem = "top -n 1 -p %s |grep test  |awk '{print $11}'" % pid
    cmd_nvidia = "nvidia-smi |grep Default |awk '{print $9}'|awk 'NR==1'"
    _, nvidia = runcmd(cmd_nvidia)
    _, cpu = runcmd(cmd_cpu)  # cpu占用
    _, mem = runcmd(cmd_mem)  # 内存占用
    t = time_time()  # 当前时间
    write_top("当前时间:%s \n cpu占用:%s \n 内存占用:%s \n 显存占用:%s" % (t, cpu, mem, nvidia))
os.system("kill -9 %s" % pid)
time.sleep(5)
os.system(f"bash {path} {Terminal.main_free_num5}")
code, pid = runcmd("pidof test-ji-api")
write_top("接口5资源占用情况" + str(pid) + '\n')
for i in range(10):
    time.sleep(120)
    cmd_cpu = "top -n 1 -p %s |grep test  |awk '{print $10}'" % pid
    cmd_mem = "top -n 1 -p %s |grep test  |awk '{print $11}'" % pid
    cmd_nvidia = "nvidia-smi |grep Default |awk '{print $9}'|awk 'NR==1'"
    _, nvidia = runcmd(cmd_nvidia)
    _, cpu = runcmd(cmd_cpu)  # cpu占用
    _, mem = runcmd(cmd_mem)  # 内存占用
    t = time_time()  # 当前时间
    write_top("当前时间:%s \n cpu占用:%s \n 内存占用:%s \n 显存占用:%s" % (t, cpu, mem, nvidia))