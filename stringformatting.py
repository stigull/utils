#! /usr/bin/env python
# -*- coding: utf8 -*-
import re

SPLITCAPS_REGEX = re.compile('[A-Z][^A-Z]+') #Finds the first upper cased letter of a CamelStyle word

def split_camel(string, separator = '-'):
  """
  Splits a word written in camel style to a lower case version where every word
  is separated by 'separator'.

  Usage:  non_camel = split_camel(string ,[separator = '-'])  
  Pre:    string is a single word, i.e. does not contain a space
  Post:   If string was a word written in camel style non_camel is a lower case version of string
          where separator separates every word
  """
  words = SPLITCAPS_REGEX.findall(string)
  if words:
    return separator.join([ word for word in words if word ]).lower()
  else:
    return string

def slugify(string):
  """
  Creates a url-friendly lower-case slug from a string

  Usage:  slug = slugify(string)
  After:  slug is a ascii slug of string
  """
  friendly_mappings = {u'á' : u'a',
                        u'ð' : u'd',
                        u'é' : u'e',
                        u'í' : u'i',
                        u'ó' : u'o',
                        u'ú' : u'u',
                        u'ý' : u'y',
                        u'þ' : u'th',
                        u'æ' : u'ae',
                        u'ö' : u'o',
                        u' ' : u'-',
                        u';' : u'-',
                        u'.' : u'-',
                        u',' : u'-',
                        u'#' : u'-',
                        u'+' : u'',
                        u'(' : u'',
                        u')' : u'',
                        u'/' : u'',
                        u'\\' : u'',
                        u'[' : u'',
                        u']' : u'',
                        u':' : u'',
                        u'?' : u'',
                        u'!' : u'', }
  string = string.strip().lower()
  for unsafe_symbol, safe_symbol in friendly_mappings.iteritems():
      string = string.replace(unsafe_symbol, safe_symbol)
  return string