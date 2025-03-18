# 例子1：随机验证码
# 设计一个生成随机验证码的函数，验证码由数字和英文大小写字母构成，长度可以通过参数设置。
# random模块的sample和choices函数都可以实现随机抽样，sample实现无放回抽样；choices实现有放回抽样
import random
import string
# 定义一个包含所有可能字符的字符串，包括数字和大小写字母
# string模块的digits代表0到9的数字构成的字符串'0123456789'，string模块的ascii_letters代表大小写英文字母构成的字符串'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
code = string.digits + string.ascii_letters
# 当*出现在函数参数列表中时，它表示之后的所有参数都必须以关键字参数的形式传递，而不能以位置参数的形式传递。
def generate(*,code_num = 5):
    # ''.join()将随机选择的字符列表拼接成一个字符串
    return ''.join(random.choices(code,k = code_num))
# 生成5组随机验证码
for _ in range(5):
    print(generate())

# 例子2：判断素数
# 设计一个判断给定的大于1的正整数是不是质数的函数。质数是只能被1和自身整除的正整数（大于1），如果一个大于1的正整数N是质数，那就意味着在2到 N-1之间都没有它的因子。
def test(n):
    if n < 2:
        print(f"{n}不是素数")
        return False
    for i in range(2, int(n ** 0.5) + 1):  # 只需检查到 sqrt(n)
        if n % i == 0:  # 如果 n 能被 i 整除
            print(f"{n}不是素数")
            return False
    print(f"{n}是素数")
    return True
test(23)

# 例子3：最大公约数和最小公倍数
# 设计计算两个正整数最大公约数和最小公倍数的函数。x和y的最大公约数是能够同时整除x和y的最大整数, x和y的最小公倍数是能够同时被x和y整除的最小正整数
# def lcm(x: int, y: int) -> int:
#     """求最小公倍数"""
#     return x * y // gcd(x, y)
# def gcd(x: int, y: int) -> int:
#     """求最大公约数"""
#     while y % x != 0:
#         x, y = y % x, x
#     return x
def max_num(x, y):
    # 从较大的数开始递减，寻找最大公约数
    for i in range(min(x, y), 0, -1):
        if x % i == 0 and y % i == 0:
            print(f"{x}与{y}的最大公约数为：{i}")
            break
def min_num(x, y):
    # 从较大的数开始递增，寻找最小公倍数
    for i in range(max(x, y), x * y + 1):
        if i % x == 0 and i % y == 0:
            print(f"{x}与{y}的最小公倍数为：{i}")
            break
max_num(14, 36)
min_num(14, 36)

# 例子4：数据统计
# 假设样本数据保存一个列表中，设计计算样本数据描述性统计信息的函数。描述性统计信息通常包括：算术平均值、中位数、极差（最大值和最小值的差）、方差、标准差、变异系数等
def ptp(data):
    """
    计算极差（全距）。
    """
    return max(data) - min(data)

def mean(data):
    """
    计算算术平均值。
    算术平均值是所有数据之和除以数据的个数。
    """
    return sum(data) / len(data)

def median(data):
    """
    计算中位数。
    中位数是将数据从小到大排序后位于中间位置的值。
    如果数据个数为偶数，则中位数为中间两个数的平均值。
    """
    temp, size = sorted(data), len(data)  # 对数据排序并获取数据个数
    if size % 2 != 0:  # 如果数据个数为奇数
        return temp[size // 2]  # 返回中间位置的值,注意是索引值
    else:  # 如果数据个数为偶数
        return mean(temp[size // 2 - 1:size // 2 + 1])  # 返回中间两个数的平均值


def var(data, ddof=1):
    """
    计算方差。
    方差是衡量数据离散程度的统计量，计算公式为：
    方差 = Σ(x_i - x̄)^2 / (n - ddof)
    其中，x̄ 是数据的平均值，ddof 是自由度调整参数（默认为1，表示样本方差）。
    参数:
        ddof (int): 自由度调整参数，默认为1。
    """
    x_bar = mean(data)  # 计算数据的平均值
    temp = [(num - x_bar) ** 2 for num in data]  # 计算每个数据与平均值的差的平方
    return sum(temp) / (len(temp) - ddof)  # 返回方差

def std(data, ddof=1):
    """
    计算标准差。
    标准差是方差的平方根，用于衡量数据的离散程度。
    """
    return var(data, ddof) ** 0.5  # 返回方差的平方根


def cv(data, ddof=1):
    """
    计算变异系数。
    变异系数是标准差与平均值的比值，用于衡量数据的相对离散程度。
    参数:
        ddof (int): 自由度调整参数，默认为1。
    """
    return std(data, ddof) / mean(data)  # 返回标准差与平均值的比值


def describe(data):
    """
    输出描述性统计信息。
    打印数据的均值、中位数、极差、方差、标准差和变异系数。
    """
    print(f'均值: {mean(data)}')
    print(f'中位数: {median(data)}')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    print(f'极差: {ptp(data)}')
    print(f'方差: {var(data)}')
    print(f'标准差: {std(data)}')
    print(f'变异系数: {cv(data)}')

# 例子5：双色球随机选号
# 将生成随机号码和输出一组号码的功能分别封装到两个函数中，然后通过调用函数实现机选N注号码的功能。
import random
RED_BALLS = [i for i in range(1, 34)]
BLUE_BALLS = [i for i in range(1, 17)]
def choose():
    """
    生成一组随机号码，模拟双色球的选号过程。
    从红球中随机选择6个号码，并从蓝球中随机选择1个号码。
    返回:
        list: 一个包含6个红球号码和1个蓝球号码的列表。
    """
    # 从红球中随机选择6个不重复的号码
    selected_balls = random.sample(RED_BALLS, 6)
    # 对红球号码进行排序
    selected_balls.sort()
    # 添加一个随机选择的蓝球号码
    selected_balls.append(random.choice(BLUE_BALLS))
    return selected_balls

def display(balls):
    """
    格式化输出一组号码，红球用红色显示，蓝球用蓝色显示。
    参数:
        balls (list): 保存随机号码的列表，前6个为红球，最后1个为蓝球。
    """
    # 遍历红球号码（前6个）
    for ball in balls[:-1]:
        # 使用ANSI转义码将红球号码以红色显示，并左填充到两位数
        # \033[031m和\033[0m这是 ANSI 转义码，用于控制终端的显示属性，比如文字颜色和样式。\033：这是转义字符（ASCII码为27，十六进制为\x1b），用于标识 ANSI 转义码的开始。
        # [031m：这是ANSI转义码的一部分，表示设置文字颜色为红色。
        # \033[0m：这是ANSI转义码的结束标记，用于重置所有属性，恢复默认的文字颜色和样式。
        # end = ' '这是 print() 函数的一个参数，用于指定在输出内容后附加的字符串。在这里，end=' ' 表示在输出后附加一个空格
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
        # {ball: 0 > 2d}这是 f-string 中的格式化表达式，用于格式化变量 ball 的输出。并左填充到两位数。用0填充，右对齐，总宽度为2个字符，d表示十进制整数
    # 使用ANSI转义码将蓝球号码以蓝色显示
    print(f'\033[034m{balls[-1]:0>2d}\033[0m')

# 从用户输入中获取需要生成的号码注数
n = int(input('生成几注号码: '))
# 循环生成并显示指定数量的随机号码
for _ in range(n):
    display(choose())