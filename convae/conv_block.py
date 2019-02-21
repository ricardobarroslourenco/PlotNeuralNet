import sys

sys.path.append('../')
from core.tikzeng import *
from core.blocks import *

arch = [
    to_head('..'),
    to_cor(),
    to_begin(),

    # input image
    to_input('./coast_of_chile_high_res.png'),

    # Define a convolution block
    to_Conv('conv01',),

    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()