# -*- coding: utf-8 -*-
'''
info = {
    "name": "módulo rgbcores",
    "autor": "James R. Torres",
    "versão": (1, 0),
    "python": (3, 0, 0),
    "descrição": "cores RGB Normal/Bold",
    "doc_url": " https://drive.google.com/drive/folders/1hmn0ImDw8OCX5bgsiax1v9DL6EzxdaEZ?usp=sharing ",
}
'''
def black(texto):
    a = '\033[30m'
    b = texto
    c = '\033[m'
    return a + b + c
def red(texto):
    a = '\033[31m'
    b = texto
    c = '\033[m'    
    return a + b + c
def blue(texto):
    a = '\033[94m'
    b = texto
    c = '\033[m'    
    return a + b + c
def green(texto):
    a = '\033[;32m'
    b = texto
    c = '\033[0;0m'    
    return a + b + c
def bred(texto):
    a = '\033[31;1m'
    b = texto
    c = '\033[0;0m'
    return a + b + c 
def bgreen(texto):
    a = '\033[32;1m'
    b = texto
    c = '\033[0;0m'    
    return a + b + c
def bblue(texto):
    a = '\033[34;1m'
    b = texto
    c = '\033[0;0m'    
    return a + b + c
