"""
Create the Graph Script
"""

import os
import graphviz
from graphviz import dot
import pydot


def main():
    os.system("python -m pymodel.pmg TimberMusicPlayerFSM")

if __name__ == '__main__':
    main()
