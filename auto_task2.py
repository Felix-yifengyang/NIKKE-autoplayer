import time
import keyboard
from opencv import Player

my_player = Player(accuracy=0.8)


# Player默认accuracy为0.8
# Player默认鼠标点击间隔为2.5s


# 改变鼠标点击的模式，默认为模式1，在auto_task里提供一个修改Player属性的接口
def change_click(click_pattern):
    my_player.change_click(click_pattern)


def gain_diamond():
    if my_player.exist(['free_diamond']):
        my_player.find_touch(['free_diamond', 'REWARD'])


def home():
    while True:
        # 注意开局弹窗，以及中途的露菲广告，露菲广告会出现在每日收米后和爬塔后
        # if 有home图标，就点击
        if my_player.exist('home'):  # 如果不在home就回到home
            my_player.find_touch('home')
            time.sleep(my_player.interval)

        # 付费商店收米
        if my_player.exist('pay_shop'):
            my_player.find_touch(['pay_shop'])
            time.sleep(my_player.interval)
            if my_player.exist(["restrict"]):  # 查看是否有年龄限制
                my_player.find_touch_skewing(['restrict'], 90, 110)  # 点击已成年 # distance需要修改
                my_player.find_touch(['confirm_10'])  # 点击确认

                my_player.find_touch(['gift'])
                my_player.find_touch_skewing(['everyday'], 0, 120)
                gain_diamond()
                my_player.find_touch_skewing(['everyweek'], 0, 240)
                gain_diamond()
                my_player.find_touch_skewing(['everyweek'], 0, 360)
                gain_diamond()
                my_player.find_touch(['home'])

        # 商店收米
        if my_player.exist(['shop']):
            my_player.find_touch(['shop', '0'])
            my_player.find_touch(['buy', 'REWARD'])
            my_player.find_touch(['home'])
            time.sleep(my_player.interval)

        # 每日收米
        if my_player.exist(['mi']):
            my_player.find_touch('mi')
            my_player.find_touch(['destroy'])
            if my_player.exist(['start_destroy']):
                my_player.find_touch(['start_destroy', 'REWARD'])
            my_player.find_touch(['cancel', 'gain_reward', 'REWARD_2', 'REWARD', 'lobby'])

        # 友情点
        if my_player.exist(['friend']):
            my_player.find_touch(['friend', 'give', 'confirm', 'close'])

        # 邮箱
        if my_player.exist(['mail']):
            my_player.find_touch(['mail'])
            time.sleep(my_player.interval)
            my_player.find_touch(['gain_mail'])
            time.sleep(my_player.interval)
            my_player.find_touch(['REWARD', 'close_3'])


def base():
    # if 不在home就先回到home再点击base，else 点击base
    # 派遣
    # 每日收米
    # 咨询
    # 回到home

    return 0


def ark():
    # if 不在home就先回到home再点击ark，else 点击ark
    # 模拟室
    # 打boss
    # 竞技场
    # 爬塔
    # 回到home

    return 0


def normal_activity():
    # if 不在home就先回到home再点击activity，else 点击activity
    # 挑战
    # 闯关
    # 任务

    return 0


def single_raid():
    return 0
