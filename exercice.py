#!/usr/bin/env python
# -*- coding: utf-8 -*-
def capitaliser_pays(nom):
    # TODO completer la fonction
    return nom('(?<=^)[a-z]|(?<=\s)[a-z]', '{}', s).format(*map(str.upper, re.findall('(?<=^)[a-z]|(?<=\s)[a-z]', s)))


if __name__ == '__main__':
    pays = [
        'AfghanIstan',
        'albania',
        'algeria',
        'AndorRa',
        'angolA',
        'antigua ANd barbuda',
        'argEntina',
        'Armenia',
        'austrAlia',
        'ausTria',
        'azerBaijaN'
    ]
    for i in range(len(pays)):
        pays[i] = capitaliser_pays(pays[i]).capitalize()

    print(pays)
