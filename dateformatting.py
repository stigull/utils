#! /usr/bin/env python
# -*- coding: utf8 -*-

WEEKDAYS = (u'mánu%s', u'þriðju%s', u'miðviku%s', u'fimmtu%s', u'föstu%s', u'laugar%s', u'sunnu%s')
NEFNIFALL, THOLFALL, THAGUFALL, EIGNARFALL = u'nf',u'þf',u'þgf',u'ef'
WEEKDAYS_SUFFIXES = {   NEFNIFALL : u'dagur',
                        THOLFALL: u'dag',
                        THAGUFALL: u'degi',
                        EIGNARFALL: u'dags'}
MONTHS = {  1: u'janúar', 
            2: u'febrúar', 
            3: u'mars', 
            4: u'apríl',
            5: u'maí', 
            6 : u'júní',
		    7: u'júlí', 
		    8 : u'ágúst', 
		    9 : u'september', 
		    10 : u'október', 
		    11 : u'nóvember', 
		    12 : u'desember'}

def get_day_of_week_in_icelandic(weekday, tense='nf'):
    """
    Usage:  day = get_day_of_week_in_icelandic(weekday, [beyging='nf'])
    Pre:  weekday is and integer in the interval [0,6]
            tense is one of NEFNIFALL, THOLFALL, THAGUFALL, EIGNARFALL
    Post:  day is the icelandic name of the weekday in the preferred tense
    """
    return WEEKDAYS[weekday] % WEEKDAYS_SUFFIXES[tense]
