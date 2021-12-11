class just_some_exceptions:

    def __init__(self, x):
        self.x = x

    def __enter__(self):
        x = self.x
        print("Enter")
        return x + 5 * 2

    def __exit__(self, exc_key, exc_index, traceback):
        print("Exit")
        if exc_key != None:
            print("Error Report")
            print(exc_index)
            print(exc_key)

with just_some_exceptions(4) as x:
    print(x)


#
# import contextlib
#
# @contextlib.contextmanager
# def just_some_exceptions(text):
#     print("Enter")
#     yield text
#     print("Exit")
#
# with just_some_exceptions('test') as t:
#     print(t)

