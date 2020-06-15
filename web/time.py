import schedule
import time
import sys

sys.path.append("../parser/")
from scrapper import run as parser
sys.path.append("../tomita/")
from tomita import findFact as tomita 
sys.path.append("../tonality/")
from dos import main as tonality 
import os


def run():
    parser()
    tomita()
    tonality()

run()
schedule.every(60).minutes.do(run)
while True:
    schedule.run_pending()
    time.sleep(1)




