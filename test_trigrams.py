# -*- coding: utf-8 -*-

import pytest

TEST_OPENFILE = {
    ('test.txt', 'six words repeat six words repeat')
}

@pytest.mark.parametrize("fn, result", TEST_OPENFILE)
def test_get_fileFun(fn, result):
    from trigrams import get_fileFun
    assert get_fileFun(fn) == result



