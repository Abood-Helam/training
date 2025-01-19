from test_name import hello
def main():
    test_default()
    test_argument()
   

def test_default():
    assert hello =="hello, world"

def test_argument():
    for name in ["harry","ron","draco"]:
        assert hello(name) == f"hello, {name}"

if __name__=="__main__":
    main()
