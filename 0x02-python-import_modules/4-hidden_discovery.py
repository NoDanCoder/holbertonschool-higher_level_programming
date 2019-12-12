#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    objs = sorted(dir(hidden_4))
    for item in objs:
        if not item.startswith("__"):
            print("{}".format(item))
