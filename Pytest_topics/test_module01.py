from utils.myconfigparser import getPetAPIURL

BASE_URL_PETSTORE = getPetAPIURL()

def test_a1():
    print("just testing the function")


def test_a2():
    assert 4 == 4, "in case failed"  # assert LHS==RHS (pass if true;else false with mssg)


def test_a3():
    assert 5 * 4 == 25, "failing the test intentionally"
## run in verbose mode; pytest -r <name of directory containing test_<>.py files

def test_a4():
    url=BASE_URL_PETSTORE+'123'
    print(url)
    assert 'petstore' in url