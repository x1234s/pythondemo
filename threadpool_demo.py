#! encoding=utf-8
import threadpool
import time


def demo_run(str):
    print str
    time.sleep(1)


def demo_run_multi(a, b, c):
    print a,b,c
    time.sleep(1)


def one_param():
    # 线程会遍历str_中的内容
    str_ = ['11', '22', 'aa']
    pool = threadpool.ThreadPool(10)
    requests = threadpool.makeRequests(demo_run, str_)
    [pool.putRequest(req) for req in requests]
    pool.wait()
    exit(0)


def multi_param():
    # 多个参数的情况，函数调用时第一个解包list，第二个解包dict
    # 方法1
    lst_vars_1 = ['1', '2', '3']
    lst_vars_2 = ['4', '5', '6']
    func_var = [(lst_vars_1, None), (lst_vars_2, None)]
    # 方法2
    dict_vars_1 = {'m': '1', 'n': '2', 'o': '3'}
    dict_vars_2 = {'m': '4', 'n': '5', 'o': '6'}
    func_var = [(None, dict_vars_1), (None, dict_vars_2)]

    pool = threadpool.ThreadPool(2)
    requests = threadpool.makeRequests(demo_run_multi, func_var)
    [pool.putRequest(req) for req in requests]
    pool.wait()