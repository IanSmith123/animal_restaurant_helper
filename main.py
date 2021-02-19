import re
import os
import time
import subprocess
from concurrent.futures import ThreadPoolExecutor


def get_screen_size():
    cmd = "adb shell wm size"
    p = subprocess.run(cmd, capture_output=True)
    stdout = p.stdout.decode()
    out = re.findall(r'\d+', stdout)
    width, height = [int(i) for i in out]
    print(width, height)
    return width, height


def send_ad():
    screen_x_percent = 0.9
    screen_y_percent = 0.92
    run_adb_tap(screen_x_percent, screen_y_percent)


def touch_consumer():
    x1, y1 = 0.3, 0.4
    run_adb_tap(x1, y1, )
    x2, y2 = 0.5, 0.4
    run_adb_tap(x2, y2, )
    x3, y3 = 0.8, 0.4
    run_adb_tap(x3, y3, )

    x4, y4 = 0.3, 0.6
    run_adb_tap(x4, y4, )
    x5, y5 = 0.5, 0.6
    run_adb_tap(x5, y5, )
    x6, y6 = 0.8, 0.6
    run_adb_tap(x6, y6, )


def run_adb_tap(screen_x_percent, screen_y_percent, duration=1):
    """
    adb shell input tap x y duration
    """
    cmd = 'adb shell input tap {} {} {}'.format(int(screen_width * screen_x_percent),
                                                int(screen_height * screen_y_percent), duration)

    # print(cmd)
    os.system(cmd)


def send_ad_inf():
    count = 0
    while True:
        count += 1
        print("\rtouch count: {}".format(count), end='')
        send_ad()


def touch_consume_inf():
    while True:
        touch_consumer()
        time.sleep(1)


def single_thread_main_scheduler():
    count = 0
    while True:
        count += 1
        print("\rtouch count: {}".format(count), end='')
        send_ad()
        if count % 15 == 0:
            time.sleep(0.2)
            touch_consumer()
            print()
            print("touch consumer")


def multi_thread_scheduler():
    pool_size = 5
    pool = ThreadPoolExecutor(pool_size)
    for i in range(pool_size - 1):
        pool.submit(send_ad_inf)
        time.sleep(1)
    pool.submit(touch_consume_inf)
    print("the end")


if __name__ == '__main__':
    screen_width, screen_height = get_screen_size()
    # main_scheduler()
    multi_thread_scheduler()
