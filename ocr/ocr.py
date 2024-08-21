# coding: utf-8
from paddleocr import PaddleOCR
import time, random
import cv2, numpy, pyautogui
from PIL import ImageGrab


class PlayerOCR(object):
    def __init__(self, accuracy=0.6):
        super().__init__()
        self.screen = None
        self.accuracy = accuracy
        self.ocr = PaddleOCR()
        w, h = pyautogui.size()
        print(f'Physical size: {w}x{h}')

    def screen_shot(self):
        """获得屏幕截图"""
        screen = ImageGrab.grab()  # 屏幕截图
        screen = cv2.cvtColor(numpy.array(screen), cv2.COLOR_RGB2BGR)  # 将RGB转换成BGR
        print('截图已完成', time.ctime())
        self.screen = screen  # 赋值为Player的属性
        return screen

    def read(self):
        img = self.screen_shot()
        results = self.ocr.ocr(img)
        if results is None or len(results) == 0:
            raise ValueError("OCR 识别失败")
        print(results)

        data = []
        for result in results:
            for item in result:
                box = item[0]  # 获取矩形框坐标
                text, confidence = item[1]  # 获取文本和置信度
                data.append({'text': text, 'confidence': confidence, 'text_box_position': box})
        return data

    def random_offset(self, position, range=5):
        x, y = position
        x += random.randint(-range, range)
        y += random.randint(-range, range)
        return (x, y)

    def touch(self, position):
        x, y = self.random_offset(position)  # 对position坐标进行随机偏移
        origin = pyautogui.position()  # 记录鼠标当前的位置
        dt = random.uniform(0.01, 0.02)
        pyautogui.moveTo(x, y, duration=dt)  # 将鼠标移动到 (x, y) 坐标，移动时间为 dt 秒
        pyautogui.mouseDown(button='left')  # 模拟鼠标左键按下
        time.sleep(dt)  # 暂停 dt 秒
        pyautogui.mouseUp(button='left')
        pyautogui.moveTo(*origin, duration=dt)

    def find_touch(self, key_list):
        """查找并点击"""
        data = self.read()
        # 如果 key_list 是一个字符串，则将其转换为包含一个字符串的列表
        key_list = [key_list, ] if type(key_list) == str else key_list
        re = False
        for key in key_list:
            if key[0] == 's':
                key = key[1:]
                # 使用列表推导来查找 data 中与 key 匹配的文字信息
                found = [e for e in data if key == e['text']]
            else:
                found = [e for e in data if key in e['text']]
            msg = f'目标：{key},  找到数量：{len(found)}'
            print(msg)
            if found:
                p1, _, p2, _ = found[0]['text_box_position']
                (x1, y1), (x2, y2) = p1, p2
                center = (int((x1 + x2) / 2), int((y1 + y2) / 2))
                self.touch(center)
                re = key
                break
        return re

    def exist(self, key_list):
        """查找但是不点击"""
        data = self.read()
        key_list = [key_list, ] if type(key_list) == str else key_list
        re = []
        for key in key_list:
            if key[0] == 's':
                key = key[1:]
                found = [e for e in data if key == e['text']]
            else:
                found = [e for e in data if key in e['text']]
            msg = f'目标：{key},  找到数量：{len(found)}'
            print(msg)
            re.append(len(found))
        re = re[0] if len(re) == 1 else re
        return re



