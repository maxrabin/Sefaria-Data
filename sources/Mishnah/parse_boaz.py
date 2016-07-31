# -*- coding: utf-8 -*-
from data_utilities import util
import sys
import codecs
import re
from sefaria.model import *

"""
Parsing strategy: Use @00 and @22 for structure in the auto-parser.

Two places have a repeated numbered comment (i.e. a and a*). I think dropping to depth 3 is silly, I'll add a line
break instead. I've marked these cases with the @23 tag.

I've skipped the text labeled as פירוש הקצר in בועז שבת, as I'm not sure this is actually a part of Boaz. This is
tagged with @10.

There is section called פתח האוהל in בועז אוהלות. This is styled as a run-on segment. These get an @23 tag which add a
line break.
"""


def get_file_names():

    he = [Ref(book).he_book() for book in library.get_indexes_in_category('Mishnah')[:-5]]
    boaz_file_names = [u'{}.txt'.format(name.replace(u'משנה', u'בועז')) for name in he]
    return boaz_file_names


def files_with_tag(tag):
    files = []
    for filename in get_file_names():
        with codecs.open(filename, 'r', 'utf-8') as boaz_file:
            for line in boaz_file:
                if re.search(tag, line):
                    files.append(filename)
                    break
    print 'found {} files with tag {}'.format(len(files), tag)
    for thing in files:
        print thing


def find_strange_stuff():
    weird_chars = []
    for filename in get_file_names():
        with codecs.open(filename, 'r', 'utf-8') as boaz_file:
            for line in boaz_file:
                weird_chars.append(re.findall(u'[^\u05d0-\u05ea \.0-9\(\):@\[\"]', line))
    weird_chars = [thing for char_list in weird_chars for thing in char_list]
    return set(weird_chars)


def unclear_lines(expected_tags):

    problems = 0
    for book in get_file_names():
        with codecs.open(book, 'r', 'utf-8') as data:
            for linenum, line in enumerate(data):
                if not any(re.match(pattern, line) for pattern in expected_tags):
                    print u'{}: {}'.format(book, linenum)
                    print line
                    problems += 1
    print '{} issues found'.format(problems)

# for book in get_file_names():
#     util.restructure_file(book, lambda x: x.replace(u'\ufeff', u''))

unclear_lines([u'@00פרק', u'@22', u'@23', u'@44', u'\n', u'@99'])




