"""
    作者：Mr.Feng
    功能：模拟掷骰子，计算两个骰子的点数和及分布频率
    版本：1.0
    日期：2019/07/10
"""
from matplotlib import pyplot
import numpy as np
# import matplotlib.pyplot as plt
# 解决中文显示问题

pyplot.rcParams['font.sans-serif'] = ['SimHei']
pyplot.rcParams['axes.unicode_minus'] = False


def main():
    total_times = 100

    # 记录骰子的点数

    roll1_arr = np.random.randint(1, 7, size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)
    result_arr = roll1_arr + roll2_arr
    hist, bins = np.histogram(result_arr, range(2, 14))
    print(hist)
    print(bins)

    # 绘制直方图

    pyplot.hist(result_arr,range(2, 14), normed=1, edgecolor='black', color='brown', linewidth=1)
    xtick_label = ['2点', '3点', '4点', '5点', '6点', '7点', '8点', '9点',
                   '10点', '11点', '12点']
    xtick_pos = np.arange(2, 14) + 0.5
    pyplot.xticks(xtick_pos, xtick_label)
    pyplot.title('骰子点数统计')
    pyplot.xlabel('点数')
    pyplot.ylabel('频率')
    pyplot.show()


if __name__ == '__main__':
    main()