import sys

sys.path.append('api')
import dummy

## Test 2
def test():
	if 1!=dummy.one(): exit(1)

if __name__ == "__main__":
	test()
