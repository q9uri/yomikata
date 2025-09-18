import pytest
from yomikata.dictionary import Dictionary
from yomikata.dbert import dBert

def test_yomikata_reader_furigana_test():
    text = 'そして、畳の表は、すでに幾年前に換えられたのか分らなかった。'
    reader = dBert()
    output = reader.furigana(text)
    assert output == "そして、畳の{表/おもて}は、すでに幾年前に換えられたのか分らなかった。"
    print(output)

def test_yomikata_dictreader_furigana_test():
    text = 'そして、畳の表は、すでに幾年前に換えられたのか分らなかった。'
    dictreader = Dictionary()
    output = dictreader.furigana(text)
    assert output == "そして、{畳/たたみ}の{表/ひょう}は、すでに{幾/いく}{年/ねん}{前/まえ}に{換/か}えられたのか{分/わか}らなかった。"
    print(output)
