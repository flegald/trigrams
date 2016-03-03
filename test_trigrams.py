# -*- coding: utf-8 -*-

import pytest

TEST_OPENFILE = {
    ('test.txt', 'six words repeat six words repeat')
}

@pytest.mark.parametrize("fn, result", TEST_OPENFILE)
def test_open_fileFun(fn, result):
    from trigrams import open_fileFun
    assert open_fileFun(fn) == result



