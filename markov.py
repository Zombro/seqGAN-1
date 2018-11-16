# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 20:56:44 2018
@author: kevzo
"""

import re
# import numpy as np
from numpy import random
from nltk.tokenize import wordpunct_tokenize
from scraper import kafka


def genmarkov(tokens):
    # beginner simplification : eliminate all punctuation and capitalization
    # the LAST WORD might need some special handling which is ignored for now
    f = [i.lower() for i in tokens if re.search('\\w', i)]
    markov = {}
    i = 0
    j = len(f)
    # flat = ' '.join(f)
    # norm = {i: len(re.findall(i, flat)) for i in g}
    for i in range(j-1):
        a = f[i]
        b = f[i+1]
        if a not in markov:
            markov[a] = {b: 1}
        else:
            if b in markov[a]:
                markov[a][b] += 1
            else:
                markov[a][b] = 1
    # convert word occurence count to local probability distribution
    # R(count) = (0,inf)  -->  R(pdist) = (0,1)
    for w in markov:
        n = markov[w]
        m = sum([n[i] for i in n])
        p = {k: (v / m) for k, v in n.items()}
        markov[w] = p

    return markov


def test1():
    tokens = wordpunct_tokenize(kafka())
    markov = genmarkov(tokens)
    q = [random.choice(list(markov.keys()))]
    for i in range(50):
        w = markov[q[-1]]
        n = []
        p = []
        for k, v in w.items():
            n.append(k)
            p.append(v)
        q.append(random.choice(n, p=p))
    return q


r = test1()
print(' '.join(r))
