# https://docs.pytest.org/en/7.4.x/

# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5 # 테스트에 실패하도록 짰음
