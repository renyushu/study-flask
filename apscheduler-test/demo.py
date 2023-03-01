from apscheduler.schedulers.background import BackgroundScheduler
import time

# 实例化一个调度器
scheduler = BackgroundScheduler()


def job1():
    print("%s: 执行任务" % time.asctime())


# 添加任务并设置触发方式为3s一次
scheduler.add_job(job1, 'interval', seconds=3)

# 开始运行调度器
scheduler.start()