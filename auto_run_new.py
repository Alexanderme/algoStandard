# @Time : 2020/9/8 16:08 
# @modele : auto_run_new.py
# @Author : zhengzhong
# @Software: PyCharm
import os
import time
import json
import unittest
from config import Terminal, Config_file
from utls.subprocess_test import runcmd

mounted_dir = "/tmp/standard"
path = "/tmp/standard/sh/zz.sh"
algo_config = "/usr/local/ev_sdk/config/algo_config.json"


class Auto_run(unittest.TestCase):
    def setUp(self):
        pass

    @staticmethod
    def file_config_setting(content):
        with open(algo_config, "r") as f:
            json_str = json.load(f)
        for key, vaule in content.items():
            json_str[key] = vaule
        with open(algo_config, "w") as f2:
            json.dump(json_str, f2)

    def reduction_config(self):
        runcmd(f"cp /{mounted_dir}/config/algo_config.json /usr/local/ev_sdk/config/")

    def test00001_not_function(self):
        """验证未授权返回-999"""
        code, connet = runcmd(f"bash  {path}  {Terminal.main_not_function}")
        write_res(connet + '\n')

    def test00002_yes_function(self):
        """授权"""
        code, connet = runcmd(f"bash {path} {Terminal.main_yes_function}")
        write_res(connet + '\n')

    def test00003_ev_license(self):
        """ev_license版本是否一致"""
        code, connet = runcmd(f"bash {path}  {Terminal.main_ev_license}")
        write_res(connet + '\n')

    def test00004_project_path(self):
        """验证工程路径与规范一致"""
        code, connet = runcmd(f"bash {path}  {Terminal.main_project_path}")
        write_res(connet + '\n')

    def test00005_make_file(self):
        """验证test.cpp和makefile"""
        code, connet = runcmd(f"bash {path}  {Terminal.main_make_file}")
        write_res(connet + '\n')

    def test00006_catalogue(self):
        """test-ji-api和license.txt移动到任意目录，都需要能够正常运行目录"""
        code, connet = runcmd(f"bash {path}  {Terminal.main_catalogue}")
        write_res(connet + '\n')

    def test00007_libji_connect(self):
        """libjo.so链接所有库"""
        code, connet = runcmd(f"bash {path}  {Terminal.main_libji_connect}")
        write_res(connet + '\n')

    def test00008_verification_pem(self):
        """# 公私钥位置，名称验证"""
        code, connet = runcmd(f"bash {path}  {Terminal.main_verification_pem}")
        write_res(connet + '\n')

    def test000091_algo_config(self):
        """生成不同的结果图片"""
        runcmd(f"cp {algo_config} /{mounted_dir}/config/")
        config = Config_file.config
        for con in config:
            file_name = ''
            for a, b in config[con].items():
                file_name += a + "_" + str(b)
            self.file_config_setting(config[con])
            code, conten = runcmd(f"bash {path}  {Terminal.main_run_sdk} {file_name}")
            write_res(conten + '\n')
            self.reduction_config()

    def test000092_dynamiv_config(self):
        """动态传参生成不同的结果图片"""
        config = Config_file.config
        for con in config:
            file_name = ''
            for a, b in config[con].items():
                file_name += a + "_" + str(b)
            code, conten = runcmd(
                f"bash {path}  {Terminal.main_run_sdk_dynamiv} {file_name} {config[con]}")
            write_res("动态传参" + conten + '\n')

    def test000093_function(self):
        """实现的接口测试"""
        for i in range(1, 5):
            code, conten = runcmd(f"bash {path}  {Terminal.main_function} {i}")
            write_res(conten + '\n')


# 运行的接口
# 传入参数是接口对应的数字
def write_res(res):
    with open(f"/{mounted_dir}/project_res.txt", "a") as f:
        f.write(res)


def time_time():
    t = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    return t


if __name__ == "__main__":
    unittest.main()
