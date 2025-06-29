import pyautogui
import time
import telebot
import cv2
import json
from PIL import ImageGrab
import pyperclip
import io
import random

bot = telebot.TeleBot('5803321421:AAF-xxzpQ3KFLTzDPLLFJwhfSV_mqnM_UlI')
to_run_pods = True
to_run_questions = True
print('bot started! :)')

with open('logins.json', 'r') as file:
    logins = json.load(file)


@bot.message_handler()
def start(message):
    global to_run_pods
    global to_run_questions
    global i
    global b
    global quizzes_done
    global logins

    if message.text == 'test':
        time.sleep(3)
        print(pyautogui.position())

    if message.text == 'photo':
        screenshot = ImageGrab.grab()

        image_buffer = io.BytesIO()
        screenshot.save(image_buffer, format="PNG")
        image_data = image_buffer.getvalue()

        bot.send_photo(message.chat.id, photo=image_data)

    if message.text.split()[0] == 'watch':
        bot.send_message(message.chat.id, f"starting the task")
        if len(message.text.split()) == 2:
            aim = int(message.text.split()[1])
        else:
            aim = 999999
        i = 0
        b = 0

        pyautogui.FAILSAFE = True
        to_run_pods = True
        x_close_tab = 1214
        y_close_tab = 26
        x_open_tab = 958
        y_open_tab = 24
        right = (654, 80)
        left = (555, 80)

        pyautogui.click(x_close_tab, y_close_tab)
        time.sleep(1)
        pyautogui.click(x_open_tab, y_open_tab)

        pyautogui.doubleClick()
        time.sleep(0.1)
        pyautogui.write(f"https://members.gcsepod.com/shared/podcasts/title/{random.randint(10200, 15125)}")
        pyautogui.keyDown('enter')
        time.sleep(5)

        while to_run_pods and i < aim:

            #type new topic index
            pyautogui.moveTo(right)
            pyautogui.mouseDown()
            pyautogui.moveTo(left)
            pyautogui.write(f"{random.randint(10200, 15125)}")
            pyautogui.mouseUp()
            pyautogui.keyDown('enter')
            time.sleep(2)

            try:

                #copy pods counter
                pod_count = pyautogui.locateOnScreen("C:\\Users\\kulik\\Downloads\\pods.jpg", confidence=0.7,region=(883, 395, 1797, 610))
                left_x = pod_count.left
                center_y = pod_count.top + pod_count.height / 2
                pyautogui.moveTo(left_x, center_y)
                pyautogui.mouseDown()
                pyautogui.move(-20, 0)
                pyautogui.hotkey('ctrl', 'c')
                pyautogui.mouseUp()
                clipboard_data = pyperclip.paste()
                pods = int(clipboard_data.split()[-1])
                pyautogui.click()

            except:
                continue

            try:
                close_add = pyautogui.locateOnScreen("C:\\Users\\kulik\\Videos\\RimWorld\\arrow_down.jpg",confidence=0.8)
                center_x = close_add.left + close_add.width / 2
                center_y = close_add.top + close_add.height / 2
                pyautogui.click(center_x, center_y)
            except:
                pass

            pod_location = pyautogui.locateOnScreen("C:\\Users\\kulik\\Downloads\\star_cloud.jpg",confidence=0.8)
            center_x = pod_location.left
            center_y = pod_location.top + pod_location.height / 2
            choose_new_pod = (center_x - 100, center_y)

            for counter in range(pods):
                try:
                    if not to_run_questions:
                        break
                    if counter != 0:
                        pyautogui.scroll(-126)

                    pyautogui.click(choose_new_pod)

                    time.sleep(1)

                    pause_loc = pyautogui.locateOnScreen("C:\\Users\\kulik\\Downloads\\pause.jpg", confidence=0.8)
                    center_x = pause_loc.left + pause_loc.width + 66
                    center_y = pause_loc.top + pause_loc.height - 10
                    time_left = (center_x, center_y)

                    pyautogui.moveTo(time_left)
                    pyautogui.mouseDown()
                    pyautogui.move(60, 0)
                    pyautogui.hotkey('ctrl', 'c')
                    pyautogui.mouseUp()
                    pyautogui.click()
                    clipboard_data = pyperclip.paste()
                    lengths = clipboard_data.split()[-1].split(':')
                    bot.send_message(message.chat.id, str(lengths))
                    lengths = int(lengths[0]) * 60 + int(lengths[1]) - random.randint(5, 10)

                    time.sleep(lengths)
                    i += 1
                except:
                    bot.send_message(message.chat.id, "error")

                    i += 1


        bot.send_message(message.chat.id, f"{i} pods were wached")

    if message.text == 'help':
        bot.send_message(message.chat.id, "() : optional variable;\n\nfarmila (x): do quizzes x times;\n\nlogin username: loggin the user;\n\npods: see the pods progress;\n\nquizzes: see the quizzes progress;\n\nstop: stop grinding;\n\nstart x: click pods x times (counts as clicked, not as watched, quick);\n\nregister name username password: add new user for login function;\n\naccounts: see all account with detailes; \n\nwatch (x) actually watch x pods (counts as watched, not clicked, slow) \n\nphoto: sends a screenshot of an entire screen")

    if message.text == "accounts":
        out = ''
        for username, details in logins.items():
            email, password = details
            out += f"Username: {username}, Email: {email}, Password: {password}\n\n"
        bot.send_message(message.chat.id, out)

    if message.text == "data":
        bot.send_message(message.chat.id, f"starting the task")
        to_run_pods = False
        to_run_questions = False
        time.sleep(3)
        close_tab = (1214, 26)
        open_tab = (958, 24)
        region = (116, 113, 2000, 520)
        pyautogui.click(close_tab[0], close_tab[1])
        time.sleep(1)
        pyautogui.click(open_tab[0], open_tab[1])
        time.sleep(1)
        pyautogui.write("https://members.gcsepod.com/shared/users/me/activity?mode=pods")

        pyautogui.keyDown('enter')
        time.sleep(5)

        screenshot = ImageGrab.grab(bbox=region)

        image_buffer = io.BytesIO()
        screenshot.save(image_buffer, format="PNG")
        image_data = image_buffer.getvalue()

        bot.send_photo(message.chat.id, photo=image_data)

    if message.text.split()[0] == 'farmila':
        bot.send_message(message.chat.id, f"starting the task")

        if len(message.text.split()) == 2:
            aim = int(message.text.split()[1])
        else:
            aim = 1000000000000000
        to_run_questions = True
        quizzes_done = -1
        close_tab = (1214, 26)
        open_tab = (958, 24)


        pyautogui.click(close_tab[0], close_tab[1])
        time.sleep(1)
        pyautogui.click(open_tab[0], open_tab[1])
        time.sleep(1)
        pyautogui.write("https://members.gcsepod.com/shared/podcasts/title/15005/89052")

        pyautogui.keyDown('enter')
        time.sleep(5)
        while to_run_questions:
            try:
                quizzes_done += 1
                if quizzes_done >= aim:
                    bot.send_message(message.chat.id, f"aim of {aim} quizzes was achieved")
                    break
                try:
                    redo_the_test = pyautogui.locateOnScreen("C:\\Users\\kulik\\Videos\\RimWorld\\do_test.jpg", confidence=0.8)
                except:
                    redo_the_test = pyautogui.locateOnScreen("C:\\Users\\kulik\\Videos\\RimWorld\\continue_the_test.jpg", confidence=0.8)

                center_x = redo_the_test.left + redo_the_test.width / 2
                center_y = redo_the_test.top + redo_the_test.height / 2
                pyautogui.click(center_x, center_y)
                time.sleep(2)
                wrong = False
                question = 1
                while question < 15:
                    if not to_run_questions:
                        break
                    time.sleep(1)
                    pyautogui.keyDown('pagedown')
                    answer = pyautogui.locateOnScreen(f"C:\\Users\\kulik\\Downloads\\{question}.jpg", confidence=0.8)
                    pyautogui.click(answer.left + answer.width / 2, answer.top + answer.height / 2)
                    pyautogui.keyDown('pagedown')
                    time.sleep(0.3)

                    submit = pyautogui.locateOnScreen(f"C:\\Users\\kulik\\Downloads\\check.jpg", confidence=0.9)
                    pyautogui.click(submit.left + submit.width / 2, submit.top + submit.height / 2)
                    time.sleep(0.3)
                    try:
                        if not wrong:
                            pyautogui.locateOnScreen(f"C:\\Users\\kulik\\Downloads\\tick.jpg", confidence=0.8)
                        pyautogui.keyDown('pagedown')
                        time.sleep(0.3)

                        pyautogui.click(958, 881)
                        wrong = False
                    except:
                        try:
                            pyautogui.locateOnScreen(f"C:\\Users\\kulik\\Downloads\\cross.jpg", confidence=0.8)
                            pyautogui.keyDown('pagedown')
                            retry = pyautogui.locateOnScreen(f"C:\\Users\\kulik\\Downloads\\retry.jpg", confidence=0.8)
                            pyautogui.click(retry.left + retry.width / 2, retry.top + retry.height / 2)
                            wrong = True
                            question -= 1
                        except:
                            pyautogui.keyDown('pagedown')
                            time.sleep(0.3)

                            pyautogui.click(958, 881)
                            wrong = False
                    question += 1

                pyautogui.click(1848, 143)
                time.sleep(2)

            except:
                pyautogui.click(close_tab[0], close_tab[1])
                time.sleep(1)
                pyautogui.click(open_tab[0], open_tab[1])
                time.sleep(1)
                pyautogui.write("https://members.gcsepod.com/shared/podcasts/title/15005/89052")

                pyautogui.keyDown('enter')
                time.sleep(5)

    if message.text.split()[0] == 'register':
        bot.send_message(message.chat.id, f"new account have been added")
        if len(message.text.split()) != 4:
            bot.send_message(message.chat.id, "Error: Wrong queury, (register name username password)")
            return
        logins[message.text.split()[1].lower()] = [message.text.split()[2], message.text.split()[3]]
        with open('logins.json', 'w') as file:
            json.dump(logins, file)

    if message.text.split()[0] == 'login':
        bot.send_message(message.chat.id, f"starting the task")
        to_run_pods = False

        if len(message.text.split()) != 2:
            name = ''
        else:
            name = message.text.split()[1].lower()

        if name not in logins.keys():
            bot.send_message(message.chat.id,f"there is no user {name}, try one of this ones: {list(logins.keys())}")
            return

        x_close_tab = 1214
        y_close_tab = 26
        x_open_tab = 958
        y_open_tab = 24
        write_username = (1277, 455)
        write_password = (1289, 544)
        submit_login = (1407, 620)

        pyautogui.click(x_close_tab, y_close_tab)
        time.sleep(1)
        pyautogui.click(x_open_tab, y_open_tab)

        pyautogui.doubleClick()
        pyautogui.write("https://members.gcsepod.com/login")

        pyautogui.keyDown('enter')
        time.sleep(2)

        pyautogui.click(write_username[0], write_username[1], 3)
        pyautogui.write(logins[name][0])
        pyautogui.click(write_password[0], write_password[1], 3)
        pyautogui.write(logins[name][1])
        pyautogui.click(submit_login[0], submit_login[1])


    if message.text == 'pods':
        bot.send_message(message.chat.id, f"Pods watched in this session: {b * 500 + i}")

    if message.text == 'quiz':
        bot.send_message(message.chat.id, f"Quizzes watched in this session: {quizzes_done}")

    if message.text == 'stop':
        bot.send_message(message.chat.id, f"starting the task")
        to_run_pods = False
        to_run_questions = False
        return

    if message.text.split()[0] == 'start':
        bot.send_message(message.chat.id, f"starting the task")
        if len(message.text.split()) == 2:
            aim = int(message.text.split()[1])
        else:
            aim = 10000000000
        pyautogui.FAILSAFE = True
        to_run_pods = True

        # x_skip_video = 960 science
        # y_skip_video = 922 science
        x_skip_video = 829 #maths
        y_skip_video = 925 #maths
        x_restart_page = 117
        y_restart_page = 77
        # x_restart_video = 115 science
        # y_restart_video = 75 science
        x_restart_video = 953 #maths
        y_restart_video = 564 #maths
        x_close_tab = 1214
        y_close_tab = 26
        x_open_tab = 958
        y_open_tab = 24

        pyautogui.click(x_close_tab, y_close_tab)
        time.sleep(1)
        pyautogui.click(x_open_tab, y_open_tab)

        pyautogui.doubleClick()
        time.sleep(0.1)
        # pyautogui.write("https://members.gcsepod.com/shared/podcasts/title/15005/89052") science
        pyautogui.write("https://members.gcsepod.com/shared/podcasts/title/12432/76383") #maths

        pyautogui.keyDown('enter')
        time.sleep(5)

        try:
            close_add = pyautogui.locateOnScreen("C:\\Users\\kulik\\Videos\\RimWorld\\arrow_down.jpg", confidence=0.8)
        except:
            bot.send_message(message.chat.id, "oh uh, something went wrong")
            screenshot = ImageGrab.grab()

            image_buffer = io.BytesIO()
            screenshot.save(image_buffer, format="PNG")
            image_data = image_buffer.getvalue()

            bot.send_photo(message.chat.id, photo=image_data)

            return

        center_x = close_add.left + close_add.width / 2
        center_y = close_add.top + close_add.height / 2

        pyautogui.click(center_x, center_y)

        pyautogui.scroll(-240)
        pyautogui.click(x_restart_video, y_restart_video)
        time.sleep(1)
        i = 0
        b = 0

        while to_run_pods:
            if i + b*500 >= aim:
                to_run_pods = False
                bot.send_message(message.chat.id, f"aim of {aim} pods was achieved")
            if i > 200:
                i = 0
                b += 1

                pyautogui.moveTo(x_restart_page, y_restart_page)
                pyautogui.click(x_restart_page, y_restart_page)
                time.sleep(7)


                try:
                    close_add = pyautogui.locateOnScreen("C:\\Users\\kulik\\Videos\\RimWorld\\arrow_down.jpg",confidence=0.8)
                except:
                    bot.send_message(message.chat.id, "oh uh, something went wrong")
                    screenshot = ImageGrab.grab()

                    image_buffer = io.BytesIO()
                    screenshot.save(image_buffer, format="PNG")
                    image_data = image_buffer.getvalue()

                    bot.send_photo(message.chat.id, photo=image_data)

                    return

                center_x = close_add.left + close_add.width / 2
                center_y = close_add.top + close_add.height / 2

                pyautogui.click(center_x, center_y)

                pyautogui.scroll(-240)
                pyautogui.click(x_restart_video, y_restart_video)
                time.sleep(1)

            pyautogui.moveTo(x_skip_video, y_skip_video, duration=2)
            time.sleep(1)
            pyautogui.click(x_skip_video, y_skip_video)

            time.sleep(1)

            pyautogui.click(x_restart_video, y_restart_video)
            i += 1

            time.sleep(80)

        bot.send_message(message.chat.id, 'pods farming have finished')



bot.polling(none_stop=True)