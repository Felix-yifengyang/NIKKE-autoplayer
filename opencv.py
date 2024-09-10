import time, os, random, math
import cv2, numpy, pyautogui
from PIL import ImageGrab
import pygetwindow as gw

# 桌面模式下的鼠标操作延迟，程序已经设置随机延迟这里无需设置修改
pyautogui.PAUSE = 0.001
cwd = __file__.replace('opencv.py', '')  # 当前文件目录
wanted_path = f'{cwd}\\wanted'  # 目标图片目录


class Player(object):
    """docstring for Player"""

    # accuracy 匹配精准度 0~1
    def __init__(self, accuracy=0.8):
        super().__init__()
        self.accuracy = accuracy
        self.interval = 2.5
        self.click_pattern = 1
        self.target_map = None
        self.screen = None
        self.load_target()
        w, h = pyautogui.size()
        print(f'Physical size: {w}x{h}')

    # 读取要查找的目标图片，名称为文件名
    # 返回字典{name1:[cv2_image1, name1], name2:...}
    def load_target(self):
        target_map = {}
        path = wanted_path
        file_list = os.listdir(path)
        for file in file_list:
            name = file.split('.')[0]
            file_path = path + '/' + file
            content = [cv2.imread(file_path), name]
            target_map[name] = content
        print(target_map.keys())
        self.target_map = target_map
        return target_map

    # 截屏并发送到目录./screen, 默认返回cv2读取后的图片
    def screen_shot(self, name='screen'):
        screen = ImageGrab.grab()
        if name != 'screen':
            screen.save(f'{cwd}\\screen\\{name}.jpg')
        screen = cv2.cvtColor(numpy.array(screen), cv2.COLOR_RGB2BGR)
        print('截图已完成 ', time.ctime())
        self.screen = screen
        return self.screen

    # 随机位置偏移，默认左右5个像素
    def random_offset(self, position, range=5):
        x, y = position
        x += random.randint(-range, range)
        y += random.randint(-range, range)
        return (x, y)

    # 点击NIKKE边缘处的地方，用于退出弹窗
    def click_edge(self):
        left, top, width, height = self.get_size()
        pyautogui.click(left + width // 2, top + 100)
        print("已点击边缘位置")

    # 点击某个固定位置
    def click_here(self, x, y):
        pyautogui.click(x, y)
        print(f"已点击位置{x},{y}")

    # 返回大厅
    def check_home(self):
        self.click_edge()
        # if 有home图标，就点击
        if self.exist('home'):  # 如果不在home就回到home
            self.find_touch('home')
            time.sleep(self.interval * 2.5)
        elif self.exist('close'):
            self.find_touch('close')

    def get_size(self):
        window = gw.getWindowsWithTitle('NIKKE')[0]
        left, top, width, height = window.left, window.top, window.width, window.height
        return left, top, width, height

    # 激活NIKKE窗口
    def activate_window(self):
        # 获取指定窗口并激活
        window = gw.getWindowsWithTitle('NIKKE')[0]
        window.activate()
        window.resizeTo(1037, 811)
        print('已打开NIKKE')

    # 或pyautogui鼠标点击，带偏移与延迟
    def touch(self, position):
        x, y = self.random_offset(position)  # 对position坐标进行随机偏移
        origin = pyautogui.position()  # 记录鼠标当前的位置
        dt = random.uniform(0.01, 0.02)
        pyautogui.moveTo(x, y, duration=dt)  # 将鼠标移动到 (x, y) 坐标，移动时间为 dt 秒
        if self.click_pattern == 1:
            # 单击
            pyautogui.doubleClick()
        elif self.click_pattern == 2:
            # 双击
            pyautogui.click()
        else:
            # 按压释放
            pyautogui.mouseDown(button='left')
            time.sleep(0.4)
            pyautogui.mouseUp(button='left')

        time.sleep(0.13)

        pyautogui.moveTo(*origin, duration=dt)

    # 拖动或长按
    def drag(self, position_start, end, second=0.2):
        sx, sy = self.random_offset(position_start)
        ex, ey = self.random_offset(end)
        origin = pyautogui.position()  # 记录原位，点完返回
        dt = random.uniform(0.01, 0.02)
        pyautogui.moveTo(sx, sy, duration=dt)
        pyautogui.dragTo(ex, ey, duration=second + dt)
        pyautogui.moveTo(*origin, duration=dt)

    # 在图上标记位置p1左上，p2右下
    def mark(self, background, p1, p2):
        cv2.rectangle(background, p1, p2, (0, 0, 255), 3)

    # 计算两点距离
    def distance(self, a, b):
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    # 核心功能， 在background大图片上定位target_name对应的小图片位置
    # debug开启则会以图片形式显示查找结果
    def locate(self, background, target_name, debug=0):
        loc_pos = []
        target, c_name = self.target_map[target_name]  # [cv2_target_image, target_name]
        h, w, _ = target.shape
        result = cv2.matchTemplate(background, target, cv2.TM_CCOEFF_NORMED)  # result存储了所有位置的匹配分数，通常是一个二维数组
        location = numpy.where(result >= self.accuracy)  # 在background大图片上的坐标位置，大于accuracy的即为匹配成功，将会有多个值
        for y, x in zip(*location):
            center = x + int(w / 2), y + int(h / 2)  # background上匹配成功的图像的中心坐标
            if loc_pos and self.distance(loc_pos[-1], center) < 20:  # 忽略邻近重复的点
                continue
            else:
                loc_pos.append(center)
                p2 = x + w, y + h
                self.mark(background, (x, y), p2)

        if debug:  # 在图上显示寻找的结果，调试时开启
            cv2.imshow(f'result for {target_name}:', background)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        res = len(loc_pos)
        msg = f'查找结果：{c_name} 匹配到 {res} 个位置'
        print(msg)
        return loc_pos

    # 裁剪Img以加速检测， 从给定图像中裁剪出一个指定区域的子图像，area[h1,h2,w1,w2]为高宽范围百分比
    # 选中区域为高h1%到h2% 宽w1%到w2%，返回裁剪后图片与左上角位置
    def cut(self, img, area=[0, 50, 0, 50]):
        h1, h2, w1, w2 = [e / 100 for e in area]
        h, w, c = img.shape
        h1, h2 = int(h * h1), int(h * h2)
        w1, w2 = int(w * w1), int(w * w2)
        small = img[h1:h2, w1:w2, :]
        start = [w1, h1]
        return small, start

    # 判断name_list中哪些目标存在，但不点击，全部目标遍历，返回同长度真假列表
    # 输入[name1,name2...]返回[name1_result, name2_result...]
    def exist(self, name_list, area=None):
        background = self.screen_shot()
        if area:
            background, start = self.cut(background, area)
        re = []
        name_list = name_list if type(name_list) == list else [name_list, ]
        for name in name_list:
            loc_pos = self.locate(background, name)
            cur = len(loc_pos) > 0
            re.append(cur)
        re = re[0] if len(re) == 1 else re
        time.sleep(0.2)
        return re

    # 寻找name_list中的目标，并点击第一个找到的目标，然后中止
    # 注意有优先级顺序，找到了前面的就不会再找后面的
    # 只返回第一个找到并点击的name，都没找到返回false
    def find_touch_same_screen(self, name_list, area=None):
        background = self.screen_shot()
        if area:
            background, start = self.cut(background, area)
        re = False
        name_list = name_list if type(name_list) == list else [name_list, ]
        for name in name_list:
            loc_pos = self.locate(background, name)
            if len(loc_pos) > 0:
                if area:  # 从裁剪后的坐标还原回裁前的坐标
                    loc_pos[0][0] += start[0]
                    loc_pos[0][1] += start[1]
                self.touch(loc_pos[0])  # 同一目标多个结果时只点第一个
                re = name
                break
        return re

    # 尝试查找所有目标图像，并依次点击每个找到的目标图像。
    def find_touch(self, name_list, area=None):
        re = False
        name_list = name_list if type(name_list) == list else [name_list, ]
        for name in name_list:
            background = self.screen_shot()
            if area:
                background, start = self.cut(background, area)
            loc_pos = self.locate(background, name)
            if len(loc_pos) > 0:
                if area:  # 从裁剪后的坐标还原回裁前的坐标
                    loc_pos[0][0] += start[0]
                    loc_pos[0][1] += start[1]
                self.touch(loc_pos[0])  # 同一目标多个结果时只点第一个
                re = name
            time.sleep(self.interval)
        return re

    # 寻找目标，点击偏移指定方向距离的目标
    def find_touch_skewing(self, name_list, direction, distance):
        re = False
        name_list = name_list if type(name_list) == list else [name_list, ]
        for name in name_list:
            background = self.screen_shot()
            loc_pos = self.locate(background, name)
            if len(loc_pos) > 0:
                t = loc_pos[0]
                new_t = (t[0] + distance * math.cos(math.radians(direction)),
                         t[1] + distance * math.sin(math.radians(direction)))
                loc_pos[0] = new_t
                self.touch(loc_pos[0])  # 同一目标多个结果时只点第一个
                re = name
            time.sleep(self.interval)
        return re

    @staticmethod
    def continuous_click():
        pyautogui.mouseDown()
        time.sleep(0.23)
        pyautogui.mouseUp()
        time.sleep(0.021)

    # 修改精确度
    def change_accuracy(self, new_accuracy):
        self.accuracy = new_accuracy

    # 修改时间间隔
    def change_interval(self, new_interval):
        self.interval = new_interval

    # 修改点击模式
    def change_click(self, click_pattern):
        self.click_pattern = click_pattern
