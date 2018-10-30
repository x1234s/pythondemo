#! encoding=utf-8
import threadpool
import time


def demo_run(str):
    print str
    time.sleep(1)


if __name__ == '__main__':
    # 线程会遍历str_中的内容
    str_ = ['11', '22', 'aa']
    pool = threadpool.ThreadPool(10)
    requests = threadpool.makeRequests(demo_run, str_)
    [pool.putRequest(req) for req in requests]
    pool.wait()
    exit(0)