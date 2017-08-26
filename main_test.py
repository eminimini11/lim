from sub_test import bar


def boo():
    print('Iam main_test')
    print(__name__)
    print('boo')
    bar()


if __name__ == '__main__':
    boo()
