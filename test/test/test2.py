import sys

sys.path.append('lib')
import dummy

def test():
	if 1!=dummy.one(): exit(1)

if __name__ == "__main__":
	test()
