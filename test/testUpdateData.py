from time import sleep

import controller.updateData as up
import data.dumpToDailyData as dump
if __name__ == '__main__':
    up.update(dump.getStockList())
    # while True:
    #     up.update()
    #     sleep(60)