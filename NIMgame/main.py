import random
import time
from colorama import init
from colorama import Fore, Back, Style

init()

#global vars
maximo = 0
user_choose_n = 0
user_choose_m = 0
compt_choose_n = 0
compt_choose_m = 0
dev_lock = 0
last_play = []
turn = 0
running = True
n = 0

def check_turn():
    global compt_choose_m
    global user_choose_m
    global turn
    global n

    n = random.choice(range(0, 100))

    print("\nO "+Fore.BLUE+"número de peças"+Fore.RESET+" no tabuleiro é: {} \n".format(n))

    if turn % 2 == 0:
        compt_choose_m = random.choice(range(0, n))
        print(Fore.BLUE+"O Computador"+Fore.RESET+" escolheu o número máximo de peças por turno: "+Fore.BLUE+str(compt_choose_m)+Fore.RESET)
        int(compt_choose_m)
        user_choose_m = compt_choose_m
    else:
        user_choose_m = int(input("Escolha o número máximo de peças por turno: "))
        if user_choose_m > n:
            print(Fore.RED+"o número escolhido excede o número de peças no tabuleiro! [except: user_choose_n > n]")
        print(Fore.BLUE+"O Jogador"+Fore.RESET+" escolheu o número máximo de peças por turno: "+Fore.BLUE+str(user_choose_m)+Fore.RESET)
        int(user_choose_m)
        compt_choose_m = user_choose_m

def run():
    def single():
        global compt_choose_m
        global user_choose_m
        global compt_choose_n
        global user_choose_n
        global turn
        global n
        global last_play

        turn = random.choice(range(0, 2))
        check_turn()

        while n > 0:
            turn += 1
            print("Faltam "+Fore.BLUE+str(n)+Fore.RESET+" peças!")
            int(n)

            if dev_lock == 1:
                print(Fore.GREEN+"\ndev_msg"+Fore.RESET+" => turn: ", turn)
                print(Fore.GREEN+"dev_msg"+Fore.RESET+" => last_play: ", str(last_play))
                this_time = time.localtime()
                time_init = time.strftime("tempo de início: %m/%d/%Y, %H:%M:%S", this_time)
                print(Fore.GREEN+time_init+Fore.RESET)
                print("\n")
            else:
                pass

            if turn % 2 == 0:
                compt_range = (n-(compt_choose_m + 1))
                for i in range(1, compt_choose_m):
                    func = n - i
                    
                    if func % compt_range == 0:
                        compt_choose_n = i
                    else:
                        pass

                if dev_lock == 1:
                    print("op = ({} - ({} + 1))".format(str(n), str(compt_choose_m)))
                    print("op = {}".format(str(compt_range)))
                    print("func = {} - {}".format(str(n), str(i)))
                    print("right_num = {} / {} = 0".format(str(compt_choose_n), str(i)))
                else:
                    pass

                int(compt_choose_n)

                print(Fore.BLUE+"O computador"+Fore.RESET+" escolheu retirar "+Fore.BLUE+str(compt_choose_n)+Fore.RESET+" peças")
                int(compt_choose_n)
                if compt_choose_n > n:
                    print(Fore.RED+"\no computador retirou um número acima do permitido [except: deus ex machina]\n"+Fore.RESET)
                else:
                    if n > 0:
                        last_play.clear()
                        last_play.append("compt")
                        n -= compt_choose_n
                    else:
                        print("O Computador ganhou!")
                        break
            else:
                user_choose_n = int(input("Escolha quantas peças tirar: "))
                print(Fore.BLUE+"O Jogador"+Fore.RESET+" escolheu retirar "+Fore.BLUE+str(user_choose_n)+Fore.RESET+" peças")
                if user_choose_n > n:
                    print(Fore.RED+"\nnão é possível tirar essa quantidade de peças! [except: user_choose_n > n]\n"+Fore.RESET)
                else:
                    if n > 0:
                        last_play.clear()
                        last_play.append("user")
                        n -= user_choose_n
                    else:
                        print("O Jogador ganhou!")
                        break
        
        if dev_lock == 1:
            print(Fore.GREEN+"\ndev_msg"+Fore.RESET+" => turn: ", turn)
            print(Fore.GREEN+"dev_msg"+Fore.RESET+" => last_play: ", str(last_play))
            this_time2 = time.localtime()
            time_conc = time.strftime("tempo de conclusão: %m/%d/%Y, %H:%M:%S", this_time2)
            print(Fore.GREEN+time_conc+Fore.RESET)
            print("\n")
        else:
            pass

        if last_play[0] == "user":
            print(Fore.BLUE+"\nO Jogador ganhou!\n"+Fore.RESET)
        elif last_play[0] == "compt":
            print(Fore.BLUE+"\nO Computador ganhou!\n"+Fore.RESET)

    def champion():
        pass

    print(Fore.BLUE+"modo [1] = Uma partida")
    print("modo [2] = Campeonato\n"+Fore.RESET)
    choose_mode = input("Escolha o modo de jogo: ")

    if choose_mode == "1":
        single()
    elif choose_mode == "2":
        champion()
    else:
        print(Fore.RED+"\nmodo de jogo não reconhecido!\n"+Fore.RESET)

def partida(lock):
    if lock == 0:
        global turn

        print(Fore.BLUE+"Jogo iniciado!"+Fore.RESET)
        while running:
            run()
    else:
        mode = input("mode: ")
        if mode == "auto":
            print("mode_set = auto\n")
        elif mode == "semi-normal":
            print("mode_set = semi-normal\n")
        elif mode == "normal":
            print(Fore.BLUE+"Jogo iniciado!\n"+Fore.RESET)
            print(Fore.GREEN+"dev_msg"+Fore.RESET+" => turn: ", turn)
            print(Fore.GREEN+"dev_msg"+Fore.RESET+" => state_running: ", running)
            print(Fore.GREEN+"dev_msg"+Fore.RESET+" => START_ROTATION\n")
            print(Fore.GREEN+"mode_set = normal\n"+Fore.RESET)
            while running:
                print("debug => sec_1 = "+Fore.GREEN+"normal"+Fore.RESET)
                run()
        else:
            print("\no modo inserido não existe!\n")
        print("Jogo iniciado!\n")
        print("dev_msg => turn: ", turn)
        print("dev_msg => state_running: ", running)
        print("dev_msg => START_ROTATION\n")

        while running:
            run()

locker = input("lock: ")
dev_lock = int(locker)
partida(int(locker))