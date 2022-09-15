import pyautogui
import time
import math
import os

MAX_RANGE = 200
MAX_RANGE_AMA = 300
CUR_X = 1197
CUR_Y = 595

ring_list = ['sample/Ring_0.png', 'sample/Ring_1.png', 'sample/Ring_2.png',
             'sample/Ring_3.png', 'sample/Ring_4.png']

rune_list = ['sample/Rune_0.png', 'sample/Rune_1.png', 'sample/Rune_2.png',
             'sample/Rune_3.png', 'sample/Rune_4.png']

key_1_list = ['sample/KeyOfTerror.png']
key_2_list = ['sample/KeyOfHate.png', 'sample/KeyOfHate2.png']
key_3_list = ['sample/KeyofDestruction.png']
boss_5_list = ['sample/boiact5.png', "sample/item/TicketSavaltion.png"]

# amulet_list = ['sample/Amulet1.png', 'sample/Amulet2.png', 'sample/botact3.png']

enemy_list = ['sample/enemy1.png', 'sample/enemy2.png', 'sample/enemy3.png']
boss_5 = ['sample/boss_available.png']


def range_ret(x, y, a, b):
    num1 = x - a
    num2 = y - b
    num3 = pow(num1, 2) + pow(num2, 2)
    ret = math.sqrt(num3)
    return int(ret)


def ring_available():
    for ring in ring_list:
        ring_location = pyautogui.locateOnScreen(ring, confidence=0.7)
        print(ring)
        if str(ring_location) != "None":
            x, y = pyautogui.center(ring_location)
            return x, y
    return None, None


def item_available(sample_list):
    for sample in sample_list:
        item_location = pyautogui.locateOnScreen(sample, confidence=0.7)
        print(sample)
        if str(item_location) != "None":
            x, y = pyautogui.center(item_location)
            return x, y
    return None, None


def enemy_available():
    for enemy in enemy_list:
        enemy_location = pyautogui.locateOnScreen(enemy, confidence=0.7)
        print(enemy)
        if str(enemy_location) != "None":
            x, y = pyautogui.center(enemy_location)
            return x, y
    return None, None


def boss_available(boss_list):
    for enemy in boss_list:
        enemy_location = pyautogui.locateOnScreen(enemy, confidence=0.7)
        print(enemy)
        if str(enemy_location) != "None":
            x, y = pyautogui.center(enemy_location)
            return x, y
    return None, None


def rm_popup():
    popup = pyautogui.locateOnScreen('sample/popup_teamview.PNG', confidence=0.7)
    if str(popup) != "None":
        okbutton = pyautogui.locateOnScreen('sample/OK_button_TV.PNG', confidence=0.7)
        if str(okbutton) != "None":
            x, y = pyautogui.center(okbutton)
            pyautogui.moveTo(x, y, 1)
            time.sleep(0.1)
            pyautogui.click(x, y)


def collect_ring():
    ret = False
    pyautogui.moveTo(20, 20, 0.5)
    cur_time = time.time()
    while ret:
        x, y = ring_available()
        if str(x) != 'None' and int(time.time() - cur_time) < 20:
            pyautogui.moveTo(x, y, 1)
            time.sleep(0.1)
            pyautogui.click(x, y)
            time.sleep(3)
            print("click on location ", x, " and ", y)
        else:
            ret = False
            print("Can not find item on screen")
        # time.sleep(0.2)
    return ret


def collect_items(list_item):
    ret = True
    pyautogui.moveTo(20, 20, 0.5)
    cur_time = time.time()
    while ret:
        x, y = item_available(list_item)
        if str(x) != 'None' and int(time.time() - cur_time) < 20:
            pyautogui.moveTo(x, y, 1)
            time.sleep(0.1)
            pyautogui.click(x, y)
            time.sleep(3)
            print("click on location ", x, " and ", y)
        else:
            ret = False
            print("Can not find item on screen")
        # time.sleep(0.2)
    return ret


def collect_items_one_time(list_item):
    pyautogui.moveTo(20, 20, 0.2)
    cur_time = time.time()
    x, y = item_available(list_item)
    if str(x) != 'None' and int(time.time() - cur_time) < 20:
        pyautogui.moveTo(x, y, 1)
        time.sleep(0.1)
        pyautogui.click(x, y)
        print("click on location ", x, " and ", y)
    else:
        print("Can not find item on screen")


def confirm_close():
    close_img = pyautogui.locateOnScreen('sample/confirm_close.png', confidence=0.9)
    if str(close_img) != "None":
        return False
    else:
        return True


def confirm_open():
    open_img = pyautogui.locateOnScreen('sample/confirm_open.png', confidence=0.9)
    if str(open_img) != "None":
        return False
    else:
        return True


def close_app():
    pyautogui.press("=")
    print("App Closing")
    # time.sleep(1)
    while confirm_close():
        time.sleep(0.5)
    print("App Close Completed")


def pre_run_condition():
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)


def start_run():
    pyautogui.hotkey('alt', 'z')
    print("App Starting")
    # time.sleep(2)
    while confirm_open():
        time.sleep(0.5)
    print("App started")


def waiting_for_complete(sample_img):
    sample_img = pyautogui.locateOnScreen(sample_img, confidence=0.7)
    if str(sample_img) != "None":
        return False
    else:
        return True


def click_image(img, check_img, cfd):
    click_img = pyautogui.locateOnScreen(img, confidence=cfd)
    if str(click_img) != "None":
        x, y = pyautogui.center(click_img)
        pyautogui.click(x, y)
        cur_time = time.time()
        while waiting_for_complete(check_img) and int(time.time() - cur_time) < 10:
            time.sleep(0.5)


def click_image_without_check(img):
    click_img = pyautogui.locateOnScreen(img, confidence=90)
    if str(click_img) != "None":
        x, y = pyautogui.center(click_img)
        pyautogui.click(x, y)


def auto_tele(c, check_img):
    while waiting_for_complete(check_img):
        time.sleep(0.5)
        pyautogui.press(c)
        # time.sleep(0.5)
    # pause auto teleport
    pyautogui.press("F2")


def start_game():
    click_image('sample/Create_button.png', 'sample/Create_Game_Button.png', 0.9)
    click_image('sample/Create_Game_Button.png', 'sample/confirm_open.png', 0.9)
    print("Start Completed")


def buff():
    pyautogui.press("F3")
    time.sleep(0.3)
    pyautogui.click(button='right', x=521, y=409)
    time.sleep(0.2)
    pyautogui.press("F4")
    time.sleep(0.3)
    pyautogui.click(button='right', x=521, y=409)
    time.sleep(0.2)
    pyautogui.press("F5")
    time.sleep(0.3)
    pyautogui.click(button='right', x=521, y=409)
    time.sleep(0.2)
    pyautogui.press("F6")
    time.sleep(0.3)
    pyautogui.click(button='right', x=521, y=409)
    time.sleep(0.2)


def buffsor():
    pyautogui.press("F4")
    time.sleep(0.7)
    pyautogui.click(button='right', x=521, y=409)
    time.sleep(0.2)
    pyautogui.press("F3")
    time.sleep(0.5)
    pyautogui.click(button='right', x=521, y=409)
    time.sleep(0.2)
    pyautogui.press("F5")
    time.sleep(0.5)
    pyautogui.click(button='right', x=521, y=409)
    time.sleep(0.2)


def buffama():
    pyautogui.press("W")
    time.sleep(0.3)
    pyautogui.press("F4")
    time.sleep(0.3)
    pyautogui.click(button='right', x=1299, y=635)
    time.sleep(0.2)
    pyautogui.click(button='right', x=1299, y=635)
    time.sleep(0.2)
    pyautogui.press("F5")
    time.sleep(0.3)
    pyautogui.click(button='right', x=1299, y=635)
    time.sleep(0.2)
    pyautogui.click(button='right', x=1299, y=635)
    time.sleep(0.2)
    pyautogui.press("F6")
    time.sleep(0.3)
    pyautogui.click(button='right', x=1299, y=635)
    time.sleep(0.2)
    pyautogui.press("F7")
    time.sleep(0.3)
    pyautogui.click(button='right', x=1299, y=635)
    time.sleep(0.2)


# act 1 only
def teleport_to_waypoint_act1_11():
    # set tele skill
    pyautogui.press("F1")
    # step tele to waypoint
    pyautogui.click(button='right', x=1330, y=504)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1385, y=548)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1367, y=619)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1410, y=681)
    time.sleep(0.5)
    pyautogui.moveTo(1178, 589, 0.5)
    time.sleep(0.1)
    pyautogui.click(x=1178, y=589)
    time.sleep(0.5)
    # waypoint tab open
    click_image('sample/blackMarshWp.png', 'sample/bMConfirm.png', 0.9)
    print("Teleported to Black Marsh")


def teleport_to_waypoint_act1_125():
    # set tele skill
    pyautogui.press("F1")
    # step tele to waypoint
    pyautogui.click(button='right', x=888, y=453)
    time.sleep(0.5)
    pyautogui.click(button='right', x=833, y=317)
    time.sleep(0.5)
    # pyautogui.click(button='right', x=1098, y=504)
    # time.sleep(0.5)
    pyautogui.moveTo(496, 357, 0.5)
    time.sleep(1)
    pyautogui.click(x=467, y=365)
    time.sleep(1)
    # waypoint tab open
    click_image('sample/blackMarshWp.png', 'sample/bMConfirm.png', 0.9)
    print("Teleported to Black Marsh")
    time.sleep(1)


def sor_teleport_to_waypoint_act1_125():
    # set tele skill
    pyautogui.press("F1")
    # step tele to waypoint
    time.sleep(1)
    pyautogui.click(button='right', x=888, y=453)
    time.sleep(0.3)
    pyautogui.click(button='right', x=833, y=317)
    time.sleep(100)


def tele_pit():
    pyautogui.press("g")
    time.sleep(6)
    print("Teleported to Tamoa Highland")
    pyautogui.press("v")
    time.sleep(6)
    print("Teleported to Pit Level 1")


def tele_key1():
    pyautogui.press("v")
    time.sleep(2)
    print("Teleported Tower")
    pyautogui.press("v")
    time.sleep(2)
    print("Teleported Tower Level 1")
    pyautogui.press("v")
    time.sleep(3)
    print("Teleported Tower Level 2")
    pyautogui.press("v")
    time.sleep(4)
    print("Teleported Tower Level 3")
    pyautogui.press("v")
    time.sleep(3)
    print("Teleported Tower Level 4")
    pyautogui.press("v")
    time.sleep(3)
    print("Teleported Tower Level 5")
    pyautogui.click(button='right', x=186, y=188)
    time.sleep(0.5)
    pyautogui.click(button='right', x=186, y=188)
    time.sleep(0.5)
    pyautogui.click(button='right', x=186, y=188)
    time.sleep(0.5)
    pyautogui.click(button='right', x=186, y=188)
    time.sleep(0.5)
    pyautogui.click(button='right', x=186, y=188)
    time.sleep(0.5)
    pyautogui.click(button='right', x=186, y=188)
    time.sleep(0.5)
    # pyautogui.click(button='right', x=640, y=321)
    # time.sleep(0.5)
    # pyautogui.click(button='right', x=822, y=421)
    # time.sleep(0.5)


def teleport_to_waypoint_act3():
    # set tele skill
    pyautogui.press("F1")
    # step tele to waypoint
    pyautogui.click(button='right', x=1497, y=553)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1471, y=379)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1471, y=379)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1412, y=470)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1470, y=526)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1460, y=450)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1237, y=574)
    time.sleep(0.5)
    # pyautogui.click(button='right', x=1354, y=499)
    # time.sleep(0.5)
    # pyautogui.click(button='right', x=1419, y=656)
    # time.sleep(0.5)
    # pyautogui.click(button='right', x=1435, y=568)
    # time.sleep(0.5)
    # pyautogui.click(button='right', x=1381, y=523)
    # time.sleep(0.5)
    # pyautogui.click(button='right', x=1407, y=533)
    # time.sleep(0.5)
    # pyautogui.click(button='right', x=1345, y=521)
    # time.sleep(0.5)
    # pyautogui.click(button='right', x=1430, y=598)
    # time.sleep(0.5)
    pyautogui.moveTo(1063, 563, 0.5)
    time.sleep(0.1)
    pyautogui.click(x=1063, y=563)
    time.sleep(0.5)
    # waypoint tab open
    click_image('sample/DuranceWp.png', 'sample/DuranceConfirm.png', 0.9)
    print("Teleported to Durance of Hate Level 2")
    pyautogui.press("v")
    time.sleep(2)
    pyautogui.press("v")
    time.sleep(3)
    pyautogui.click(x=758, y=412)
    time.sleep(0.5)
    # pyautogui.click(x=1058, y=517)
    # time.sleep(0.5)


def teleport_to_waypoint_act3_ama():
    # set tele skill
    pyautogui.press("F1")
    # step tele to waypoint
    pyautogui.click(button='right', x=1349, y=664)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1394, y=539)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1393, y=537)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1372, y=514)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1367, y=527)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1352, y=511)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1361, y=502)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1354, y=499)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1419, y=656)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1435, y=568)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1381, y=523)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1407, y=533)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1345, y=521)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1430, y=598)
    time.sleep(0.5)
    pyautogui.moveTo(1199, 597, 0.5)
    time.sleep(0.1)
    pyautogui.click(x=1199, y=597)
    time.sleep(0.5)
    # waypoint tab open
    click_image('sample/DuranceWp.png', 'sample/DuranceConfirm.png', 0.9)
    print("Teleported to Durance of Hate Level 2")
    time.sleep(0.5)
    pyautogui.press("w")
    time.sleep(0.3)
    pyautogui.press("v")
    time.sleep(2)
    pyautogui.press("v")
    time.sleep(3)
    pyautogui.click(x=1003, y=495)
    time.sleep(0.5)


def teleport_to_waypoint_act2():
    # set tele skill
    pyautogui.press("F1")
    # step tele to waypoint
    pyautogui.click(button='right', x=1254, y=385)
    time.sleep(0.5)
    pyautogui.click(button='right', x=978, y=464)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1037, y=438)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1158, y=366)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1404, y=460)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1441, y=503)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1338, y=440)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1092, y=414)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1214, y=383)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1391, y=480)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1439, y=587)
    time.sleep(0.5)
    pyautogui.moveTo(1199, 597, 0.5)
    time.sleep(0.1)
    pyautogui.click(x=1199, y=597)
    time.sleep(0.5)
    # waypoint tab open
    click_image('sample/ArcaneSanctuary.png', 'sample/ArcaneConfirm.png', 0.9)
    print("Teleported to Arcane Sanctuary")


def teleport_to_waypoint_act5(img, img_confirm):
    # set tele skill
    pyautogui.press("F1")
    # step tele to waypoint
    pyautogui.click(button='right', x=1070, y=752)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1037, y=674)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1105, y=749)
    time.sleep(0.5)
    pyautogui.click(button='right', x=1100, y=686)
    time.sleep(0.5)
    pyautogui.moveTo(1197, 598, 0.5)
    time.sleep(0.1)
    pyautogui.click(x=1197, y=598)
    time.sleep(0.5)
    # waypoint tab open
    click_image(img, img_confirm, 0.9)
    print("Teleported to Hall of Pain")


def tele_boss_cuoi():
    pyautogui.moveTo(1200, 523, 0.5)
    time.sleep(0.1)
    pyautogui.click(x=1200, y=523)
    time.sleep(0.5)
    pyautogui.click(button='right', x=933, y=597)
    time.sleep(0.5)
    pyautogui.click(button='right', x=898, y=721)
    time.sleep(0.5)
    pyautogui.click(button='right', x=829, y=361)
    time.sleep(0.5)


def tele_key2():
    pyautogui.press("v")
    time.sleep(8)
    print("Teleported boss")


def tele_key3():
    pyautogui.press("v")
    time.sleep(5)
    print("Teleported boss")
    pyautogui.press("v")
    time.sleep(4)
    print("Teleported boss")


def tele_boss_act5():
    pyautogui.press("v")
    time.sleep(4)
    print("Teleported WorldStone Level 3")
    pyautogui.press("v")
    time.sleep(3)
    print("Teleported Throne of Destruction")
    pyautogui.press("v")
    time.sleep(3)
    print("Teleported boss")
    pyautogui.click(button='right', x=922, y=396)
    time.sleep(0.5)


def auto_skill(a, b):
    # pyautogui.press("W")
    # # time.sleep(0.3)
    pyautogui.press("F2")
    with pyautogui.hold('shift'):
        pyautogui.click(button='right', x=a, y=b)
        time.sleep(0.5)
        pyautogui.click(button='right', x=a, y=b)
        time.sleep(0.5)
        pyautogui.click(button='right', x=a, y=b)
        time.sleep(0.5)
        pyautogui.click(button='right', x=a, y=b)
        time.sleep(0.5)
        pyautogui.click(button='right', x=a, y=b)
        time.sleep(0.5)


def teleport(x, y):
    pyautogui.press("F1")
    time.sleep(0.3)
    pyautogui.click(button='right', x=x, y=y)
    time.sleep(0.1)


def auto_attack(time_set):
    ret = True
    cur_time = time.time()
    while ret:
        x, y = enemy_available()
        if str(x) != 'None' and int(time.time() - cur_time) < time_set:
            distance = range_ret(CUR_X, CUR_Y, x, y)
            auto_skill(x, y)
            if distance < MAX_RANGE_AMA:
                auto_skill(x, y)
            else:
                teleport(int((CUR_X + x) / 2), int((CUR_Y + y) / 2))
        else:
            ret = False
            if int(time.time() - cur_time) > time_set:
                pyautogui.press("esc")
                print("You have Died")
            else:
                print("Can not find enemy on screen")
        time.sleep(0.3)
    return ret


def auto_attack_ama(time_set):
    ret = True
    cur_time = time.time()
    while ret:
        x, y = enemy_available()
        if str(x) != 'None' and int(time.time() - cur_time) < time_set:
            distance = range_ret(CUR_X, CUR_Y, x, y)
            auto_skill(x, y)
            if distance < MAX_RANGE:
                auto_skill(x, y)
            else:
                teleport(int((CUR_X + x) / 2), int((CUR_Y + y) / 2))
        else:
            ret = False
            if int(time.time() - cur_time) > time_set:
                pyautogui.press("esc")
                print("You have Died")
            else:
                print("Can not find enemy on screen")
        time.sleep(0.3)
    return ret


def attack_and_collect(time_set):
    ret = True
    cur_time = time.time()
    while ret:
        x, y = enemy_available()
        if str(x) != 'None' and int(time.time() - cur_time) < time_set:
            distance = range_ret(CUR_X, CUR_Y, x, y)
            auto_skill(x, y)
            if distance < MAX_RANGE:
                auto_skill(x, y)
            else:
                collect_items_one_time(ring_list)
                collect_items_one_time(rune_list)
                teleport(int((CUR_X + x) / 2), int((CUR_Y + y) / 2))
        else:
            ret = False
            if int(time.time() - cur_time) > time_set:
                pyautogui.press("esc")
                print("You have Died")
            else:
                print("Can not find enemy on screen")
        time.sleep(0.3)
    return ret


def auto_attack_in_time(time_set):
    ret = True
    cur_time = time.time()
    while ret:
        x, y = enemy_available()
        if str(x) != 'None' and int(time.time() - cur_time) < time_set:
            distance = range_ret(CUR_X, CUR_Y, x, y)
            auto_skill(x, y)
            if distance < MAX_RANGE:
                auto_skill(x, y)
            else:
                teleport(int((CUR_X + x) / 2), int((CUR_Y + y) / 2))
        a, b = boss_available(boss_5)
        if int(time.time() - cur_time) > time_set or str(a) == 'None':
            ret = False
        time.sleep(1)
    return ret


def auto_self_attack():
    pyautogui.press("F2")
    pyautogui.click(button='right', x=560, y=393)
    time.sleep(0.3)
    pyautogui.click(button='right', x=560, y=393)
    time.sleep(0.3)
    pyautogui.click(button='right', x=560, y=393)
    time.sleep(1)
    pyautogui.click(button='right', x=560, y=393)
    time.sleep(0.3)
    pyautogui.click(button='right', x=560, y=393)
    time.sleep(0.3)
    pyautogui.click(button='right', x=560, y=393)
    time.sleep(1)


def auto_self_attack_act3():
    pyautogui.press("F2")
    time.sleep(1)
    pyautogui.click(button='right', x=930, y=482)
    time.sleep(0.3)
    pyautogui.click(button='right', x=930, y=482)
    time.sleep(0.3)
    pyautogui.click(button='right', x=930, y=482)
    time.sleep(2)
    pyautogui.click(button='right', x=930, y=482)
    time.sleep(0.3)
    pyautogui.click(button='right', x=930, y=482)
    time.sleep(0.3)
    pyautogui.click(button='right', x=930, y=482)



def run_to_boss_act3_ama():
    start_game()
    time.sleep(0.5)
    buffama()
    time.sleep(0.5)
    teleport_to_waypoint_act3_ama()
    auto_attack_ama(30)


def run_to_boss_act3():
    start_game()
    time.sleep(0.5)
    buff()
    time.sleep(0.5)
    teleport_to_waypoint_act3()
    # auto_attack(30)
    auto_self_attack_act3()


def run_act3():
    pre_run_condition()
    while True:
        run_to_boss_act3()
        time.sleep(0.5)
        i = 2
        while i:
            collect_items(rune_list)
            collect_ring()
            i = i - 1
        close_app()
        time.sleep(0.5)


def run_act3_ama():
    pre_run_condition()
    # run_to_boss_act3()
    while True:
        run_to_boss_act3_ama()
        time.sleep(0.5)
        i = 2
        while i:
            collect_ring()
            collect_items(rune_list)
            i = i - 1
        close_app()
        time.sleep(0.5)


def run_pit():
    pre_run_condition()
    while True:
        start_game()
        time.sleep(0.5)
        buff()
        time.sleep(0.5)
        teleport_to_waypoint_act1_11()
        tele_pit()
        attack_and_collect(150)
        pyautogui.press("v")
        time.sleep(5)
        attack_and_collect(150)
        close_app()
        time.sleep(0.5)


def run_act1_125():
    pre_run_condition()
    while True:
        start_game()
        time.sleep(0.5)
        buff()
        time.sleep(0.5)
        teleport_to_waypoint_act1_125()
        tele_key1()
        auto_self_attack()
        i = 2
        while i:
            collect_ring()
            collect_items(rune_list)
            collect_items(key_1_list)
            # collect_items(amulet_list)
            i = i - 1
        close_app()
        time.sleep(0.5)


def sor_run_act1_125_800_600():
    pre_run_condition()
    while True:
        start_game()
        time.sleep(0.5)
        buffsor()
        time.sleep(0.5)
        sor_teleport_to_waypoint_act1_125()
        tele_key1()
        auto_self_attack()
        i = 2
        while i:
            collect_ring()
            collect_items(rune_list)
            collect_items(key_1_list)
            # collect_items(amulet_list)
            i = i - 1
        close_app()
        time.sleep(0.5)


def run_act2_125():
    pre_run_condition()
    while True:
        start_game()
        time.sleep(0.5)
        buff()
        time.sleep(0.5)
        teleport_to_waypoint_act2()
        tele_key2()
        auto_self_attack()
        i = 2
        while i:
            collect_ring()
            collect_items(rune_list)
            collect_items(key_2_list)
            i = i - 1
        close_app()
        time.sleep(0.5)


def run_act5_125():
    pre_run_condition()
    while True:
        start_game()
        time.sleep(0.5)
        buff()
        time.sleep(0.5)
        teleport_to_waypoint_act5("sample/HallsofPain.png", "sample/HallofPainConfirm.png")
        tele_key3()
        auto_self_attack()
        i = 2
        while i:
            collect_ring()
            collect_items(rune_list)
            collect_items(key_3_list)
            i = i - 1
        close_app()
        time.sleep(0.5)


def run_act5_20():
    pre_run_condition()
    # while True:
    start_game()
    time.sleep(0.5)
    buff()
    time.sleep(0.5)
    teleport_to_waypoint_act5("sample/Worldstone.png", "sample/WorldStoneConfirm.png")
    tele_boss_act5()
    auto_attack(30)
    pyautogui.press("g")
    time.sleep(1)
    auto_attack(30)
    pyautogui.press("g")
    time.sleep(1)
    auto_attack_in_time(90)
    i = 1
    while i:
        collect_ring()
        collect_items(rune_list)
        i = i - 1
    pyautogui.press("g")
    time.sleep(2)
    tele_boss_cuoi()
    auto_attack(30)
    j = 2
    while j:
        collect_ring()
        collect_items(rune_list)
        collect_items(boss_5_list)
        j = j - 1
    # close_app()
    # time.sleep(0.5)


if __name__ == '__main__':
    # run()
    # time.sleep(10)
    # rm_popup()
    try:
        # pre_run_condition()
        # buffama()
        # sor_run_act1_125_800_600()
        # auto_attack(900)
        run_act1_125()
        # run_act3()
        # run_act2_125()
        # run_act5_125()
        # run_act5_20()
        # run_act3_ama()

    except KeyboardInterrupt:
        print('interrupted!')
