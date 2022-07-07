from os import system
from time import sleep
from .const import debug
from colorama import Fore
from builtins import input
from platform import system as platform
from aev import *

class Display(object):

    __is_color = None
    total_lines = None
    account_exists = None

    def __init__(self, username=None, passlist=None, is_color=None):
        self.delay = 1.3
        self.username = username
        self.passlist = passlist
        self.colors_disabled = True
        self.cls = 'cls' if platform() == 'Windows' else 'clear'

        if Display.__is_color == None:
            Display.__is_color = is_color

    def clear(self):
        if not debug or self.colors_disabled:
            system(self.cls)

            if self.colors_disabled and self.__is_color:
                self.colors_disabled = False
        else:
            print('\n\n')

    def stats(self, password, attempts, browsers, load=True):
        self.clear()
        complete = round((attempts/Display.total_lines) * 100, 4)
        account_exists = self.account_exists if self.account_exists != None else ''

        if self.__is_color:
            print('{0}[{1}-{0}] {1}Wordlist         : {2}{3}{4}'.format(
                Fore.YELLOW, Fore.WHITE, Fore.CYAN, self.passlist, Fore.RESET
            ))

            print('{0}[{1}-{0}] {1}Kullanıcı Adı    : {2}{3}{4}'.format(
                Fore.YELLOW, Fore.WHITE, Fore.CYAN, self.username.title(), Fore.RESET
            ))

            print('{0}[{1}-{0}] {1}Şifreler         : {2}{3}{4}'.format(
                Fore.YELLOW, Fore.WHITE, Fore.CYAN, password, Fore.RESET
            ))

            print('{0}[{1}-{0}] {1}Tamamlanma %     : {2}{3}%{4}'.format(
                Fore.YELLOW, Fore.WHITE, Fore.CYAN, complete, Fore.RESET
            ))

            print('{0}[{1}-{0}] {1}Denenilen Şifre  : {2}{3}{4}'.format(
                Fore.YELLOW, Fore.WHITE, Fore.CYAN, attempts, Fore.RESET
            ))

            print('{0}[{1}-{0}] {1}Denenilecek Şifre: {2}{3}{4}'.format(
                Fore.YELLOW, Fore.WHITE, Fore.CYAN, browsers, Fore.RESET
            ))

            print('{0}[{1}-{0}] {1}Durum            : {2}{3}{4}'.format(
                Fore.YELLOW, Fore.WHITE, Fore.CYAN, account_exists, Fore.RESET
            ))
            print()
            menu.ctrlc()
            menu.p3("1","Donuyorsa Proxy Aradığı İçin Bekleyin Düzelir.")
            menu.p3("2","Şifreler Kısmı Wordlisteki Şifreleri Gösteriyor ")
            menu.p3("3","Beklemenize Gerek Yok Çıkabilirsiniz")
            menu.p3("4","Çıkmadan Önce Telefonun Yukardan Aşşağı Çekin\nVe Termuxa Basın 'Acquire Wakelock'\nSeçeneğine Tıkladıktan Sonra Çıkabilirsiniz.\nBu Seçenek Termuxun Oto Kapanmamasını Sağlar.")
            menu.p3("5","Durumda True Yazıyor İse Başarılı")
            menu.p3("6","Ancak False Yazıyor İse Durum Başarısız\nKullanıcı Adını Yanlış Yazmış Olabilirsiniz.")
        else:
            print(
                f'[-] Wordlist: {self.passlist}\n[-] Username: {self.username}\n[-] Password: {password}')

            print(
                f'Complete: {complete}\n[-] Attempts: {attempts}\n[-] Browsers: {browsers}\n[-] Exists: {account_exists}')

        if load:
            sleep(self.delay)

    def stats_found(self, password, attempts, browsers):
        self.stats(password, attempts, browsers, load=False)

        if self.__is_color:
            print('\n{0}[{1}!{0}] {2}Şifre Bulundu{3}'.format(
                Fore.YELLOW, Fore.RED, Fore.WHITE, Fore.RESET
            ))

            print('{0}[{1}+{0}] {2}Kullanıcı Adı: {1}{3}{4}'.format(
                Fore.YELLOW, Fore.GREEN, Fore.WHITE, self.username.title(), Fore.RESET
            ))

            print('{0}[{1}+{0}] {2}Şifre: {1}{3}{4}'.format(
                Fore.YELLOW, Fore.GREEN, Fore.WHITE, password, Fore.RESET
            ))
        else:
            print('\n[!] Şifre Bulundu\n[+] Kullanıcı Adı: {}\n[+] Şifre: {}'.format(
                self.username.title(), password
            ))

        sleep(self.delay)

    def stats_not_found(self, password, attempts, browsers):
        self.stats(password, attempts, browsers, load=False)

        if self.__is_color:
            print('\n{0}[{1}!{0}] {2}Şifre Bulunamadı{3}'.format(
                Fore.YELLOW, Fore.RED, Fore.WHITE, Fore.RESET
            ))
        else:
            print('\n[!] Şifre Bulunamadı')

        sleep(self.delay)

    def shutdown(self, password, attempts, browsers):
        self.stats(password, attempts, browsers, load=False)

        if self.__is_color:
            print('\n{0}[{1}!{0}] {2}Kapatılıyor...{3}'.format(
                Fore.YELLOW, Fore.RED, Fore.WHITE, Fore.RESET
            ))
        else:
            print('\n[!] Kapatılıyor ...')

        sleep(self.delay)

    def info(self, msg):
        self.clear()

        if self.__is_color:
            print('{0}[{1}i{0}] {2}{3}{4}'.format(
                Fore.YELLOW, Fore.CYAN, Fore.WHITE, msg, Fore.RESET
            ))
        else:
            print('[i] {}'.format(msg))

        sleep(2.5)

    def warning(self, msg):
        self.clear()

        if self.__is_color:
            print('{0}[{1}!{0}] {1}{2}{3}'.format(
                Fore.YELLOW, Fore.RED, msg, Fore.RESET
            ))
        else:
            print('[!] {}'.format(msg))

        sleep(self.delay)

    def prompt(self, data):
        self.clear()

        if self.__is_color:
            return input('{0}[{1}?{0}] {2}{3}{4}'.format(
                Fore.YELLOW, Fore.CYAN, Fore.WHITE, data, Fore.RESET
            ))
        else:
            return input('[?] {}'.format(data))
