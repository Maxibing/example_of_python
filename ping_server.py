import os
import time

UE_ADDRESS = "10.1.187.231"

INTERVAL_TIME = 120

PING_CMD = "ping %s -l 200 -w 100000 -n 1" % UE_ADDRESS


def write_log(log):
    with open("ping.log", "a+", encoding="utf-8") as f:
        cur_time = str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        f.write(cur_time + ":" + log + "\n")
        f.close()


def main():
    while True:
        write_log("START PING")
        if os.system(PING_CMD):
            write_log("START FAILED\n")
        else:
            write_log("START SUCCESS\n")
        time.sleep(INTERVAL_TIME)


if __name__ == "__main__":
    main()