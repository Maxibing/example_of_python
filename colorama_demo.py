#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :usage of colorama
@Date     :2021/04/29 17:07:14
@Author      :xbMa
'''

from colorama import Fore, Back, Style

'''
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''
# Fore
print(f"{Fore.BLACK} This is BLACK Fore {Fore.RESET}")
print(f"{Fore.RED} This is RED Fore {Fore.RESET}")
print(f"{Fore.GREEN} This is GREEN Fore {Fore.RESET}")
print(f"{Fore.YELLOW} This is YELLOW Fore {Fore.RESET}")
print(f"{Fore.BLUE} This is BLUE Fore {Fore.RESET}")
print(f"{Fore.MAGENTA} This is MAGENTA Fore {Fore.RESET}")
print(f"{Fore.CYAN} This is CYAN Fore {Fore.RESET}")
print(f"{Fore.WHITE} This is WHITE Fore {Fore.RESET}")

# Back
print(f"{Back.BLACK} This is BLACK Back {Back.RESET}")
print(f"{Back.RED} This is RED Back {Back.RESET}")
print(f"{Back.GREEN} This is GREEN Back {Back.RESET}")
print(f"{Back.YELLOW} This is YELLOW Back {Back.RESET}")
print(f"{Back.BLUE} This is BLUE Back {Back.RESET}")
print(f"{Back.MAGENTA} This is MAGENTA Back {Back.RESET}")
print(f"{Back.CYAN} This is CYAN Back {Back.RESET}")
print(f"{Back.WHITE} This is WHITE Back {Back.RESET}")

# Style
print(f"{Style.DIM} This is DIM Style {Style.RESET_ALL}")
print(f"{Style.NORMAL} This is NORMAL Style {Style.RESET_ALL}")
print(f"{Style.BRIGHT} This is BRIGHT Style {Style.RESET_ALL}")