#############################
#                           #
#     Console Original      #
#                           #
#############################
"""By Gleb"""
"""made in 2017"""
from re import *
import os
import sys
import math
import zipfile
import json as js
import subprocess as subr
import chardet
from random import randint, randrange

settings = {
    "limits": {
        "length_jokes": 4
    },
    "type_jokes": 3,
    "game": True,
    "start_preview": [True, True],
    "first_dir": "C:\\",
    "input_str": ">>>",
    "base_wars": {
        "list": ["hi", "from", "co"]
    }
}
os.chdir(settings['first_dir'])
__author__ = "Gleb"
__version__ = "0.0.2"
i = ""
if settings['start_preview'][0]:
    print("""Console Original 
          ╔═ ╔╗
          ╚═ ╚╝""")
    print("by", __author__ + ", version -", __version__)
xc = 0
######################
# 1 - Анекдот;
# 2 - Рассказы;
# 3 - Стишки;
# 4 - Афоризмы;
# 5 - Цитаты;
# 6 - Тосты;
# 8 - Статусы;
# 11 - Анекдот (+18);
# 12 - Рассказы (+18);
# 13 - Стишки (+18);
# 14 - Афоризмы (+18);
# 15 - Цитаты (+18);
# 16 - Тосты (+18);
# 18 - Статусы (+18);
######################
error = {
    "s_error": "SyntaxError: invalid syntax.",
    "n_error": "NameError: name of war is not defined.",
    "d_error": "DirectoryNotFoundError: could not find the specified directory.",
    "f_error": "FileExistsError: File exists.",
    "e_error": "FileExistsError: Dir exists.",
    "z_error": "NotZipFileError: It isn`t zipfile"
}
list_command_help = {
    "echo!out": "echo!out пример или echo!out %OS% OS это базавая переменная",
    "echo!in": "создает переменные echo!in %название переменной% < пример ",
    "writefile": r"Вписывает в файл информацию \n -- делает пробел пример : writefile file.txt < Привет\nмир",
}
list_command_logic = {
    "echo!out": r"echo!out\s*(?P<out>.*)",
    "echo!in": r"echo!in\s*(?P<in>%([\w\s]*)%)\s*<\s*(?P<data>.*)",
    "e!out": r"e!out\s*(?P<out>.*)",
    "e!in": r"e!in\s*(?P<in>%([\w\s]*)%)\s*<\s*(?P<data>.*)",
    "cd": r"cd\s+(?P<out>.*)",
    "close": r"close",
    "list": r"list (?P<out>\w*)",
    "write": r"write\s*m=(?P<coding>[aw])\s*(?P<in>.*) < (?P<data>.*)",
    "create": r"create (?P<data>file|dir) (?P<file>.+)",
    "start": r"start (?P<data>o_game|file|c_game) (?P<in>.+)",
    "cmd": r"cmd!(?P<data>.*)",
    "wars": r"wars",
    "zip!in": r"zip!in (?P<file>.+) < (?P<data>.+)",
    "zip!out": r"zip!out (?P<files>.+) > (?P<data>.+)",
    "index": r"index!(?P<tag>.+)!(?P<ind>\d)\s*<\s*(?P<ni>.+)",  # index!%op%!3 < new index
    "http!json!get": r"http!json!get\s+<(?P<tag>.*)>:(?P<ind>.*):" # http!json!get <google.com>:contents:
}
if settings['start_preview'][1]:
    print("Commands ")
    print(list(list_command_logic.keys()))


def mult_list(f):
    v = split(r"[\s,]", f)
    clist = []
    clist.append(v[0][2:])
    for i in v[1:len(v) - 1]:
        clist.append(i)
    clist.append(v[len(v) - 1][:-2])
    return clist


def game_calc():
    er = 0
    while True:
        po = input("Выбирете мод умножения(*) деления(/)")
        if po == "*":
            print("*Вы выбрали умножения*")
            while True:
                wer = input("Кол-во примеров ")
                try:
                    wer = int(wer)
                except ValueError:
                    print("Вы ввели не верные данные")
                    wer = 0
                if wer == 0:
                    print("У вас 4 примера")
                    wer = 4
                skol = input("Множетель ")
                try:
                    skol = int(skol)
                except ValueError:
                    print("Вы ввели не верные данные")
                    skol = 0
                if skol == 0:
                    print("Множетель = 4")
                    skol = 4
                sh = 0
                for i in range(wer):
                    s = randint(1, 9)
                    while True:
                        d = input(str(skol) + "*" + str(s) + "=")
                        try:
                            d = int(d)
                            break
                        except ValueError:
                            print("Вы ввели не верные данные")
                    if d == skol * s:
                        print("правильно ")
                        sh = sh + 1
                    if d != skol * s:
                        print("не правильно ")
                print("ваш счет -", sh)
                if sh > er:
                    aw = sh - er
                    er = aw + er
                print("ваш рекорд -", er)
                r = input("играеш еще да/нет ")
                if r == "нет":
                    break
        if po == "/":
            print("/Вы выбрали деление/")
            while True:
                wer = input("Кол-во примеров ")  # start o_game calc_game
                try:
                    wer = int(wer)
                except ValueError:
                    print("Вы ввели не верные данные")
                    wer = 0
                if wer == 0:
                    print("У вас 4 примера")
                    wer = 4
                skol = input("Делитель ")
                try:
                    skol = int(skol)
                except ValueError:
                    print("Вы ввели не верные данные")
                    skol = 0
                if skol == 0:
                    print("Делитель = 6")
                    skol = 6
                sh = 0
                for i in range(wer):
                    s = randrange(skol, skol * 9, skol)
                    while True:
                        d = input(str(s) + "/" + str(skol) + "=")
                        try:
                            d = int(d)
                            break
                        except ValueError:
                            print("Вы ввели не верные данные")
                    if d == s / skol:
                        print("правильно ")
                        sh = sh + 1
                    if d != s / skol:
                        print("не правильно ")
                print("ваш счет -", sh)
                if sh > er:
                    aw = sh - er
                    er = aw + er
                print("ваш рекорд -", er)
                r = input("играеш еще да/нет ")
                if r == "нет":
                    break
        m = input("Выйти из игры да\нет ")
        if m == "да":
            break


def game_ghosts():
    global xc
    while True:
        print("Ghost Game by Gleb")
        feeling_brave = True
        score = 0
        while feeling_brave:
            ghost_door = randint(1, 3)
            print("Three doors ahead...")
            print("A ghost behind one.")
            print("Which door do u open?")
            door = input("1, 2, or 3? ")
            door_num = int(door)
            if door_num == ghost_door:
                print("GHOST!")
                feeling_brave = False
            else:
                print("No ghost!")
                print("U enter the next room.")
                score = score + 1
        print("Run away!")
        print("Game over! U scored", score)
        print("Your record", xc)
        if score >= xc:
            sk = score - xc
            xc = sk + score
        ans = input("Do u want to play again? (y/n)")
        if ans == "n":
            break


wars = {
    "OS": sys.platform,
    "list": ["hi", "from", "co"]
}


def is_list(string):
    if match(r"_\(.*\)_", string):
        return True
    else:
        return False


def ward(j, out=False):
    if out:
        e = match(r"%(?P<in>([\w\s]*))%", j)
        if e:
            return [True, e.group("in")]
        else:
            return False
    else:
        if match(r"%(?P<in>([\w\s]*))%", j):
            return True
        else:
            return False


def is_war(dcount, war=None):
    if war == None:
        war_name = "out"
    else:
        war_name = war
    falip = dcount.group(war_name)
    li2 = findall(r"%[\w\s]*%", dcount.group(war_name))
    lis2 = findall(r"%[\w\s]*:[\w\s]*%", dcount.group(war_name))
    li = search(r"%(?P<in>[\w\s]*)%", dcount.group(war_name))
    lu = search(r"%(?P<in>[\w\s]*):(?P<ind>[\w\s]*)%", dcount.group(war_name))
    if lu:
        try:
            if os.path.isdir(str(wars[lu.group("in")])):
                for key in li2:  # .replace("\\", r"\\")
                    falip = sub(key, wars[match(r"%(?P<in>([\w\s]*))%", key).group("in")], falip)
                return falip
            else:
                for key in li2:  # match(r"%(?P<in>([\w\s]*))%", key).group("in")
                    falip = sub(key, str(wars[match(r"%(?P<in>([\w\s]*))%", key).group("in")]), falip)
                for key_list in lis2:  # match(r"%(?P<in>([\w\s]*))%", key).group("in")

                    lipa = match(r"%(?P<in>[\w\s]*):(?P<ind>[\w\s]*)%", key_list)
                    falip = sub(key_list, str(wars[lipa.group("in")][int(lipa.group('ind'))]), falip)
                return falip
        except KeyError:
            return error["n_error"]
    elif li:
        try:
            if os.path.isdir(str(wars[li.group("in")])):
                for key in li2:  # .replace("\\", r"\\")
                    falip = sub(key, wars[match(r"%(?P<in>([\w\s]*))%", key).group("in")], falip)
                return falip
            else:
                for key in li2:  # match(r"%(?P<in>([\w\s]*))%", key).group("in")
                    falip = sub(key, str(wars[match(r"%(?P<in>([\w\s]*))%", key).group("in")]), falip)
                return falip
        except KeyError:
            return error["n_error"]
    else:
        try:
            return dcount.group(war_name)
        except KeyError:
            return error["s_error"]


while True:
    i = input("{} ".format(os.getcwd()) + settings["input_str"])
    echout = match(list_command_logic["echo!out"], i)
    echoin = match(list_command_logic["echo!in"], i)
    cd = match(list_command_logic["cd"], i)
    close = match(list_command_logic["close"], i)
    list_dir = match(list_command_logic["list"], i)
    writefile = match(list_command_logic["write"], i)
    create = match(list_command_logic["create"], i)
    start = match(list_command_logic["start"], i)
    cmd_c = match(list_command_logic["cmd"], i)
    wr = match(list_command_logic["wars"], i)
    zipout = match(list_command_logic["zip!out"], i)
    zipin = match(list_command_logic["zip!in"], i)
    ein = match(list_command_logic["e!in"], i)
    eout = match(list_command_logic["e!out"], i)
    index = match(list_command_logic["index"], i)
    if echout:
        print(is_war(echout))
    elif index:  # index!(?P<tag>.+)!(?P<ind>\d)\s*<\s*(?P<ni>.+)
        inis_war, inis2_war = ward(index.group("tag"), True)
        if inis_war:
            if type(wars[inis2_war]) == list:
                kou = wars[inis2_war]
                kou[int(is_war(index, "ind"))] = is_war(index, "ni")
                wars[inis2_war] = kou
    elif eout:
        print(is_war(eout))
    elif zipin:  # zip!in H:\1111.zip < (C:\Users\Gleb\Desktop\сайты.txt,C:\Users\Gleb\Desktop\istock_000020116885large_-_copy-700x461.jpg)
        print(is_war(zipin, "data"))  # _(ghj,kop)_
        z = zipfile.ZipFile(is_war(zipin, "file"), 'w')
        for hlp in js.loads(is_war(zipin, "data")):
            z.write(hlp)
        z.close()
    elif wr:
        bnb = list(wars.items())
        line_war = bnb[0][0] + " = " + bnb[0][1]
        for list_wars in list(bnb)[1:]:
            line_war = str(line_war) + ", " + str(list_wars[0]) + " = " + str(list_wars[1])
        print(line_war)
    elif zipin:
        if zipfile.is_zipfile(is_war(zipout, "files")):
            if os.path.exists(is_war(zipout, "data")):
                z = zipfile.ZipFile(is_war(zipout, "file"), 'r')
                z.extractall(is_war(zipout, "data"))
                z.close()
                print("В", is_war(zipout, "data"), "все успешно извелечено")
            else:
                print(error["d_error"])
        else:
            print(error["z_error"])
    elif list_dir:
        if is_war(list_dir) == "file":
            for i in os.scandir(os.getcwd()):
                if i.is_file():
                    print(os.path.split(os.path.abspath(i))[1], "(размер:", os.path.getsize(i), "байт,",
                          "последний доступа к файлу :", str(math.ceil(os.path.getatime(i))) + "c)")
        elif is_war(list_dir) == "dir":
            for i in os.scandir(os.getcwd()):
                print(os.path.split(os.path.abspath(i))[1], "(занимает :", os.path.getsize(i), "байт,",
                      "последний доступа к файлу :", str(math.ceil(os.path.getatime(i))) + "c)")
        else:
            pass
    elif zipout:
        if zipfile.is_zipfile(is_war(zipout, "file")):
            if os.path.exists(is_war(zipout, "data")):
                z = zipfile.ZipFile(is_war(zipout, "file"), 'r')
                z.extractall(is_war(zipout, "data"))
                z.close()
                print("В", is_war(zipout, "data"), "все успешно извелечено")
            else:
                print(error["d_error"])
        else:
            print(error["z_error"])
    elif ein:
        vi = match(r"%(?P<in>([\w\s]*))%", ein.group("in"))
        if is_list(is_war(ein, "data")):
            if vi:
                wars[vi.group("in")] = mult_list(is_war(ein, "data"))
                print("переменная " + vi.group("in") + " успешно создана")
            else:
                print(error["s_error"])
        else:
            if vi:
                wars[vi.group("in")] = is_war(ein, "data")
                print("переменная " + vi.group("in") + " успешно создана")
            else:
                print(error["s_error"])
    elif echoin:
        vi = match(r"%(?P<in>([\w\s]*))%", echoin.group("in"))
        if is_list(is_war(echoin, "data")):
            if vi:
                wars[vi.group("in")] = mult_list(is_war(echoin, "data"))
                print("переменная " + vi.group("in") + " успешно создана")
            else:
                print(error["s_error"])
        else:
            if vi:
                wars[vi.group("in")] = is_war(echoin, "data")
                print("переменная " + vi.group("in") + " успешно создана")
            else:
                print(error["s_error"])
    elif cd:
        if cd.group("out") == "..":
            os.chdir(os.path.dirname(os.getcwd()))
        else:
            try:
                os.chdir(is_war(cd))
            except:
                print(error["d_error"])
    elif close:
        break
    elif writefile:
        file = open(is_war(writefile, "in"), is_war(writefile,
                                                    "coding") + "b")  # write m=w lolkek.txt < privet ot console cd C:\Users\Gleb\PycharmProjects\utilits_console
        file.write(is_war(writefile, "data").encode())
        file.close()
        print("в файл " + is_war(writefile, "in"), "все успешно",
              ("записано" if is_war(writefile, "coding") == "w" else "добавлено"))
    elif create:  # file|dir
        if is_war(create, "data") == "dir":
            try:
                os.mkdir(is_war(create, "file"))
            except FileExistsError:
                print(error["e_error"])
        elif is_war(create, "data") == "file":
            try:
                pier = open(is_war(create, "file"), "x")
                pier.close()
                print("файл создан успешно")
            except FileExistsError:
                print(error["f_error"])
    elif start:
        if is_war(start, "data") == "o_game":
            if is_war(start, "in") == "ghost_game":
                game_ghosts()
            elif is_war(start, "in") == "calc_game":
                game_calc()
        elif is_war(start, "data") == "file":
            cmd = 'start ' + is_war(start, "in")
            p = subr.Popen(cmd, shell=True)
            p.wait()
            print("+")
    elif cmd_c:
        print("Loading...")
        cmd_len = subr.Popen(is_war(cmd_c, "data"), shell=True, stdout=subr.PIPE).communicate()[0]
        try:
            print(cmd_len.decode(chardet.detect(cmd_len)['encoding']))
        except TypeError:
            print("Error or get zero")
print("CO has been closed")
sys.exit(0)
