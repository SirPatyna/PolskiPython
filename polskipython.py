import random
import math


def drukuj(tekst: any, koniec=None, separator=None):
    """Odpowiednik funkcji print"""
    print(tekst, end=koniec, sep=separator)


def wprowadź(prompt):
    """Odpowiednik funkcji input"""
    return input(prompt)

def dodaj_do_listy(lista, dana):
    """Odpowiednik lista.append"""
    lista.append(dana)

def wstaw_do_listy(lista, miejsce, dana):
    """Odpowiednik lista.insert"""
    lista.insert(miejsce,dana)

def losuj_od_do(a, b):
    """Odpowiednik random.randint"""
    return random.randint(a, b)


def typ(dana: any):
    """Odpowiednik type"""
    return type(dana)


def bzw(bezwzględna):
    """Odpowiednik abs"""
    return abs(bezwzględna)


def pot(podstawa, wykładnik):
    """odpowiednik pow"""
    return pow(podstawa, wykładnik)


def kwd(kwadrat):
    """odpowiednik math.sqrt"""
    return math.sqrt(kwadrat)


def zaod(podłoga):
    """odpowiednik math.floor"""
    return math.floor(podłoga)


def zaog(sufit):
    """odpowiednik math.ceil"""
    return math.ceil(sufit)


# Definiowanie typów danych

def nat(naturalna):
    """Odpowienik int"""
    return int(naturalna)


def zp(zmienn_przecin):
    """Odpowiednik float"""
    return float(zmienn_przecin)


def walo(wartosc_logiczna):
    """Odpowiednik bool"""
    return bool(wartosc_logiczna)


def sznur(string):
    """Odpowiednik str"""
    return str(string)


def kompleks(kompleksowa):
    """Odpowiednik complex"""
    return complex(kompleksowa)


def zasięg(zas):
    """Odpowiednik range"""
    return range(zas)


def szykbitów(bitt):
    """Odpowiednik bytearray"""
    return bytearray(bitt)
