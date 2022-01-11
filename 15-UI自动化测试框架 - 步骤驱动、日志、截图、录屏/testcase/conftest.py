#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/11 17:43
import os
import shlex
import signal
import subprocess
import time

import allure
import pytest


@pytest.fixture(scope="module", autouse=True)
def record():
    cmd = shlex.split("scrcpy --record tmp.mp4")
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)
    time.sleep(2)
    allure.attach.file(file_path="tmp.mp4",name="tmp", attachment_type=allure.attachment_type.MP4)

