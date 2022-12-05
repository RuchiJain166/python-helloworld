#!/usr/bin/env python

"""Top-level script to invoke helloworld implementation."""

import sys
import helloworld.main
import os
os.system('pip install pygame')

if __name__ == '__main__':
    sys.exit(helloworld.main.main())
