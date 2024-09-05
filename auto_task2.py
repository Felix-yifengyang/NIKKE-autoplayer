import time
from opencv import Player
import pygetwindow as gw
import pyautogui
import keyboard

my_player = Player(accuracy=0.8)


# Player默认accuracy为0.8
# Player默认鼠标点击间隔为2.5s


# 改变鼠标点击的模式，默认为模式1，在auto_task里提供一个修改Player属性的接口
def change_click(click_pattern):
    my_player.change_click(click_pattern)


# 点击NIKKE边缘处的地方，用于退出弹窗
def click_edge(window_title='NIKKE'):
    # 获取窗口
    window = gw.getWindowsWithTitle(window_title)[0]
    # 获取窗口的位置和大小
    left, top, width, height = window.left, window.top, window.width, window.height
    # 计算顶部中间位置
    x = left + width // 2 - 50
    y = top + 50  # 边缘稍微下面一点
    # 移动鼠标并点击
    pyautogui.click(x, y)
    print("已点击边缘位置")


# 点击某个固定位置
def click_here(x, y):
    pyautogui.click(x, y)


# 返回大厅
def check_home():
    click_edge()
    # if 有home图标，就点击
    if my_player.exist('home'):  # 如果不在home就回到home
        my_player.find_touch('home')
        time.sleep(my_player.interval * 2.5)
    elif my_player.exist('close'):
        my_player.find_touch('close')


# 激活NIKKE窗口
def activate_window():
    # 获取指定窗口并激活
    window = gw.getWindowsWithTitle('NIKKE')[0]
    window.activate()
    window.resizeTo(1037, 811)


# 处理模拟室中获得的buff
def gain_buff():
    # if my_player.exist(['SSR']):
    #     my_player.find_touch(['SSR', 'confirm', 'confirm_2'])
    # elif my_player.exist(['SR']):
    #     my_player.find_touch(['SR', 'confirm', 'confirm_2'])
    # elif my_player.exist(['R']):
    #     my_player.find_touch(['R', 'confirm', 'confirm_2'])
    if my_player.exist(['no_choose_2']):
        my_player.find_touch(['no_choose_2', 'confirm'])


def home():
    # 注意开局弹窗，以及中途的露菲广告，露菲广告会出现在每日收米后和爬塔后
    check_home()

    # 付费商店收米
    if my_player.exist('pay_shop'):
        my_player.find_touch(['pay_shop'])
        time.sleep(my_player.interval)

        if my_player.exist(["restrict"]):  # 查看是否有年龄限制
            my_player.find_touch_skewing(['restrict'], 90, 110)  # 点击已成年 # distance需要修改
            my_player.find_touch(['confirm_10'])  # 点击确认

        my_player.find_touch(['gift'])
        my_player.find_touch(['everyday'])
        my_player.find_touch(['everyday_free', 'REWARD'])
        my_player.find_touch(['home'])
        time.sleep(my_player.interval)
        check_home()

    # 商店收米
    if my_player.exist(['shop']):
        my_player.find_touch(['shop', '0'])
        my_player.find_touch(['buy', 'REWARD'])
        my_player.find_touch(['home'])
        time.sleep(my_player.interval)
        check_home()

    # 每日收米
    if my_player.exist(['outpost']):
        my_player.find_touch('outpost')
        my_player.find_touch(['destroy'])
        if my_player.exist(['start_destroy']):
            my_player.find_touch(['start_destroy', 'REWARD'])
        my_player.find_touch(['cancel', 'gain_reward', 'REWARD_2'])
        check_home()

    # 友情点
    if my_player.exist(['friend']):
        my_player.find_touch(['friend', 'give', 'confirm', 'close'])
        check_home()

    # 邮箱
    if my_player.exist(['mail']):
        my_player.find_touch(['mail'])
        my_player.find_touch(['gain_mail'])
        my_player.find_touch(['REWARD', 'close'])


def base():
    # if 不在home就先回到home再点击base，else 点击base
    check_home()
    if my_player.exist('base'):
        my_player.find_touch('base')
        time.sleep(my_player.interval * 2.5)

        # 派遣
        my_player.find_touch(['board', 'gain_all', 'REWARD', 'dispatch_all', 'dispatch'])
        click_edge()

        # 第二次收米
        if my_player.exist('outpost_ark'):
            my_player.find_touch('outpost_ark')
            my_player.find_touch(['gain_reward', 'REWARD_2'])

        # 咨询
        if my_player.exist('center'):
            my_player.find_touch(['center', 'enter', 'consult'])
            my_player.find_touch(['taolesi', 'fast_consult', 'confirm', 'back'])
            my_player.find_touch(['huangguan', 'fast_consult', 'confirm', 'back'])


def ark():
    # if 不在home就先回到home再点击ark，else 点击ark
    check_home()
    if my_player.exist('ark'):
        my_player.find_touch('ark')
        time.sleep(my_player.interval)
        # 模拟室
        # 进入
        my_player.find_touch(['simulation_room', 'start_simulation_1', 'difficulty_5',
                              'grade_C', 'start_simulation_2'])
        # 开打
        # normal battle 和 hard battle 经常弄错
        while True:
            if my_player.exist('normal_battle'):
                my_player.find_touch('normal_battle')
                if my_player.exist('quick_battle_2'):
                    my_player.find_touch('quick_battle_2')
                else:
                    my_player.find_touch('enter_battle')
                    time.sleep(my_player.interval * 16)
                    while True:
                        if my_player.exist('next_step'):
                            my_player.find_touch('next_step')
                            time.sleep(my_player.interval)
                            break
                gain_buff()

            elif my_player.exist('cure_room'):
                my_player.find_touch(['cure_room', 'cure', 'confirm',
                                      'confirm_2', 'confirm'])

            elif my_player.exist('boss_battle'):
                my_player.find_touch(['boss_battle', 'enter_battle'])
                time.sleep(my_player.interval * 16)
                while True:
                    if my_player.exist('next_step'):
                        my_player.find_touch('next_step')
                        time.sleep(my_player.interval * 1.5)
                        my_player.find_touch(['end_simulation', 'confirm', 'no_choose', 'confirm_3', 'confirm'])
                        break
                break

        # 拦截战
        my_player.find_touch('back')
        if my_player.exist('interception'):
            my_player.find_touch(['interception', 'challenge', 'enter_battle_3'])
            time.sleep(my_player.interval * 16)
            while True:
                if my_player.exist('next_step'):
                    my_player.find_touch('next_step')
                    break
            for i in range(0, 2):
                time.sleep(my_player.interval)
                my_player.find_touch(['quick_battle', 'next_step', 'next_step'])

        # 竞技场
        my_player.find_touch('back')
        if my_player.exist('special_reward'):
            my_player.find_touch(['special_reward', 'gain_reward_2', 'REWARD'])
        if my_player.exist('arena'):
            my_player.find_touch(['arena', 'rookie_arena', 'rookie_arena'])
            for i in range(0, 5):
                while True:
                    if my_player.exist('update_menu'):
                        my_player.find_touch_skewing('update_menu', 90, 250)
                        break
                my_player.find_touch(['enter_battle_2', 'enter_battle_2'])
                while True:
                    if my_player.exist('next_step_3'):
                        keyboard.press_and_release('Esc')
                        break

            keyboard.press_and_release('Esc')

            # 特殊竞技场
            my_player.find_touch(['special_arena', 'special_arena'])
            for i in range(0, 2):
                while True:
                    if my_player.exist('update_menu'):
                        my_player.find_touch_skewing('update_menu', 90, 250)
                        break
                my_player.find_touch('enter_battle_2')
                while True:
                    if my_player.exist('next_step_2'):
                        my_player.find_touch('next_step_2')
                        break
        # 爬塔，待修工
    # 回到home


if __name__ == '__main__':
    activate_window()


