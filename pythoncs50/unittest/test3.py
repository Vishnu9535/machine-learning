from test2 import hello

def test_hello():
    assert hello("vishnu") == "hello vishnu"
    assert hello() == "hello world"

test_hello()