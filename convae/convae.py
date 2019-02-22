import sys

sys.path.append('../')
from core.tikzeng import *
from core.blocks import *


###### Param list ######################################################################################################

# Block 01 -------------------------------------------------------------------------------------------------------------
## Conv 01
conv_b01_l01_side = 128
scaling_factor_b1 = 40/conv_b01_l01_side
conv_b01_l01_params = 16

## Leaky ReLU
relu_b01_l01_side = 128
relu_b01_l01_params = 16

## Conv02
conv_b01_l02_side = 64
conv_b01_l02_params = 16

## Leaky ReLU
relu_b01_l02_side = 64
relu_b01_l02_params = 16

## Conv03
conv_b01_l03_side = 64
conv_b01_l03_params = 16

# Block 02 -------------------------------------------------------------------------------------------------------------
## Conv 01
conv_b02_l01_side = 128
scaling_factor_b2 = 40/conv_b02_l01_side
conv_b02_l01_params = 16

## Leaky ReLU
relu_b02_l01_side = 128
relu_b02_l01_params = 16

## Conv02
conv_b02_l02_side = 64
conv_b02_l02_params = 16

## Leaky ReLU
relu_b02_l02_side = 64
relu_b02_l02_params = 16

## Conv03
conv_b02_l03_side = 64
conv_b02_l03_params = 16


# Block 03 -------------------------------------------------------------------------------------------------------------
## Conv 01
conv_b03_l01_side = 128
scaling_factor_b3 = 40/conv_b03_l01_side
conv_b03_l01_params = 16

## Leaky ReLU
relu_b03_l01_side = 128
relu_b03_l01_params = 16

## Conv02
conv_b03_l02_side = 64
conv_b03_l02_params = 16

## Leaky ReLU
relu_b03_l02_side = 64
relu_b03_l02_params = 16

## Conv03
conv_b03_l03_side = 64
conv_b03_l03_params = 16


# Block 04 -------------------------------------------------------------------------------------------------------------
## Conv 01
conv_b04_l01_side = 128
scaling_factor_b4 = 40/conv_b04_l01_side
conv_b04_l01_params = 16

## Leaky ReLU
relu_b04_l01_side = 128
relu_b04_l01_params = 16

## Conv02
conv_b04_l02_side = 64
conv_b04_l02_params = 16

## Leaky ReLU
relu_b04_l02_side = 64
relu_b04_l02_params = 16

## Conv03
conv_b04_l03_side = 64
conv_b04_l03_params = 16

#=======================================================================================================================
## Latent Space


#=======================================================================================================================
# Block 05 -------------------------------------------------------------------------------------------------------------
## DeConv 01
deconv_b05_l01_side = 128
scaling_factor_b5 = 40/deconv_b05_l01_side
deconv_b05_l01_params = 16

## Leaky ReLU
relu_b05_l01_side = 128
relu_b05_l01_params = 16

## DeConv02
deconv_b05_l02_side = 64
deconv_b05_l02_params = 16

## Leaky ReLU
relu_b05_l02_side = 64
relu_b05_l02_params = 16

## DeConv03
deconv_b05_l03_side = 64
deconv_b05_l03_params = 16

# Block 06 -------------------------------------------------------------------------------------------------------------
## DeConv 01
deconv_b06_l01_side = 128
scaling_factor_b6 = 40/deconv_b06_l01_side
deconv_b06_l01_params = 16

## Leaky ReLU
relu_b06_l01_side = 128
relu_b06_l01_params = 16

## DeConv02
deconv_b06_l02_side = 64
deconv_b06_l02_params = 16

## Leaky ReLU
relu_b06_l02_side = 64
relu_b06_l02_params = 16

## DeConv03
deconv_b06_l03_side = 64
deconv_b06_l03_params = 16


# Block 07 -------------------------------------------------------------------------------------------------------------
## DeConv 01
deconv_b07_l01_side = 128
scaling_factor_b7 = 40/deconv_b07_l01_side
deconv_b07_l01_params = 16

## Leaky ReLU
relu_b07_l01_side = 128
relu_b07_l01_params = 16

## DeConv02
deconv_b07_l02_side = 64
deconv_b07_l02_params = 16

## Leaky ReLU
relu_b07_l02_side = 64
relu_b07_l02_params = 16

## DeConv03
deconv_b07_l03_side = 64
deconv_b07_l03_params = 16


# Block 08 -------------------------------------------------------------------------------------------------------------
## DeConv 01
deconv_b08_l01_side = 128
scaling_factor_b8 = 40/deconv_b08_l01_side
deconv_b08_l01_params = 16

## Leaky ReLU
relu_b08_l01_side = 128
relu_b08_l01_params = 16

## DeConv02
deconv_b08_l02_side = 64
deconv_b08_l02_params = 16

## Leaky ReLU
relu_b08_l02_side = 64
relu_b08_l02_params = 16

## DeConv03
deconv_b08_l03_side = 64
deconv_b08_l03_params = 16

########################################################################################################################




###### Architecture with param list
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),

    # input image
    to_input('./coast_of_chile_high_res.png'),

    # Define a convolution block b01 ##################################################################################
    # Conv01
    to_Conv('conv_b01_l01', s_filer=conv_b01_l01_side, n_filer=conv_b01_l01_params,
            width=(conv_b01_l01_params*scaling_factor_b1), height=(conv_b01_l01_side*scaling_factor_b1),
            depth=(conv_b01_l01_side*scaling_factor_b1), offset="(0,0,0)", to="(0,0,0)"),
    # Relu01
    to_Relu('relu_b01_l01', s_filer=relu_b01_l01_side, n_filer=relu_b01_l01_params,
            width=(relu_b01_l01_params*scaling_factor_b1), height=(relu_b01_l01_side*scaling_factor_b1),
            depth=(relu_b01_l01_side*scaling_factor_b1), offset="(1,0,0)", to="(conv_b01_l01-east)"),
    # Conv02
    to_Conv('conv_b01_l02', s_filer=conv_b01_l02_side, n_filer=conv_b01_l02_params,
            width=(conv_b01_l02_params*scaling_factor_b1), height=(conv_b01_l02_side*scaling_factor_b1),
            depth=(conv_b01_l02_side*scaling_factor_b1), offset="(1,0,0)", to="(relu_b01_l01-east)"),
    # Relu02
    to_Relu('relu_b01_l02', s_filer=relu_b01_l02_side, n_filer=relu_b01_l02_params,
            width=(relu_b01_l02_params*scaling_factor_b1), height=(relu_b01_l02_side*scaling_factor_b1),
            depth=(relu_b01_l02_side*scaling_factor_b1), offset="(1,0,0)", to="(conv_b01_l02-east)"),
    # Conv03
    to_Conv('conv_b01_l03', s_filer=conv_b01_l03_side, n_filer=conv_b01_l03_params,
            width=(conv_b01_l03_params*scaling_factor_b1), height=(conv_b01_l03_side*scaling_factor_b1),
            depth=(conv_b01_l03_side*scaling_factor_b1), offset="(1,0,0)", to="(relu_b01_l02-east)"),
    to_skip( of='conv_b01_l01', to='conv_b01_l03', pos=1.25),
    to_connection('conv_b01_l03','conv_b02_l01'),

    # Define a convolution block b02 ##################################################################################
    # Conv01
    to_Conv('conv_b02_l01', s_filer=conv_b02_l01_side, n_filer=conv_b02_l01_params,
            width=(conv_b02_l01_params * scaling_factor_b2), height=(conv_b02_l01_side * scaling_factor_b2),
            depth=(conv_b02_l01_side * scaling_factor_b2), offset="(0,0,0)", to="(0,0,0)"),
    # Relu01
    to_Relu('relu_b02_l01', s_filer=relu_b02_l01_side, n_filer=relu_b02_l01_params,
            width=(relu_b02_l01_params * scaling_factor_b2), height=(relu_b02_l01_side * scaling_factor_b2),
            depth=(relu_b02_l01_side * scaling_factor_b2), offset="(1,0,0)", to="(conv_b02_l01-east)"),
    # Conv02
    to_Conv('conv_b02_l02', s_filer=conv_b02_l02_side, n_filer=conv_b02_l02_params,
            width=(conv_b02_l02_params * scaling_factor_b2), height=(conv_b02_l02_side * scaling_factor_b2),
            depth=(conv_b02_l02_side * scaling_factor_b2), offset="(1,0,0)", to="(relu_b02_l01-east)"),
    # Relu02
    to_Relu('relu_b02_l02', s_filer=relu_b02_l02_side, n_filer=relu_b02_l02_params,
            width=(relu_b02_l02_params * scaling_factor_b2), height=(relu_b02_l02_side * scaling_factor_b2),
            depth=(relu_b02_l02_side * scaling_factor_b2), offset="(1,0,0)", to="(conv_b02_l02-east)"),
    # Conv03
    to_Conv('conv_b02_l03', s_filer=conv_b02_l03_side, n_filer=conv_b02_l03_params,
            width=(conv_b02_l03_params * scaling_factor_b2), height=(conv_b02_l03_side * scaling_factor_b2),
            depth=(conv_b02_l03_side * scaling_factor_b2), offset="(1,0,0)", to="(relu_b02_l02-east)"),
    to_skip(of='conv_b02_l01', to='conv_b02_l03', pos=1.25),

    # # Define a convolution block b03 ##################################################################################
    # # Conv01
    # to_Conv('conv_b01_l01', s_filer=conv_b01_l01_side, n_filer=conv_b01_l01_params,
    #         width=(conv_b01_l01_params * scaling_factor), height=(conv_b01_l01_side * scaling_factor),
    #         depth=(conv_b01_l01_side * scaling_factor), offset="(0,0,0)", to="(0,0,0)"),
    # # Relu01
    # to_Relu('relu_b01_l01', s_filer=relu_b01_l01_side, n_filer=relu_b01_l01_params,
    #         width=(relu_b01_l01_params * scaling_factor), height=(relu_b01_l01_side * scaling_factor),
    #         depth=(relu_b01_l01_side * scaling_factor), offset="(1,0,0)", to="(conv_b01_l01-east)"),
    # # Conv02
    # to_Conv('conv_b01_l02', s_filer=conv_b01_l02_side, n_filer=conv_b01_l02_params,
    #         width=(conv_b01_l02_params * scaling_factor), height=(conv_b01_l02_side * scaling_factor),
    #         depth=(conv_b01_l02_side * scaling_factor), offset="(1,0,0)", to="(relu_b01_l01-east)"),
    # # Relu02
    # to_Relu('relu_b01_l02', s_filer=relu_b01_l02_side, n_filer=relu_b01_l02_params,
    #         width=(relu_b01_l02_params * scaling_factor), height=(relu_b01_l02_side * scaling_factor),
    #         depth=(relu_b01_l02_side * scaling_factor), offset="(1,0,0)", to="(conv_b01_l02-east)"),
    # # Conv03
    # to_Conv('conv_b01_l03', s_filer=conv_b01_l03_side, n_filer=conv_b01_l03_params,
    #         width=(conv_b01_l03_params * scaling_factor), height=(conv_b01_l03_side * scaling_factor),
    #         depth=(conv_b01_l03_side * scaling_factor), offset="(1,0,0)", to="(relu_b01_l02-east)"),
    # to_skip(of='conv_b01_l01', to='conv_b01_l03', pos=1.25),
    #
    # # Define a convolution block b04 ##################################################################################
    # # Conv01
    # to_Conv('conv_b01_l01', s_filer=conv_b01_l01_side, n_filer=conv_b01_l01_params,
    #         width=(conv_b01_l01_params * scaling_factor), height=(conv_b01_l01_side * scaling_factor),
    #         depth=(conv_b01_l01_side * scaling_factor), offset="(0,0,0)", to="(0,0,0)"),
    # # Relu01
    # to_Relu('relu_b01_l01', s_filer=relu_b01_l01_side, n_filer=relu_b01_l01_params,
    #         width=(relu_b01_l01_params * scaling_factor), height=(relu_b01_l01_side * scaling_factor),
    #         depth=(relu_b01_l01_side * scaling_factor), offset="(1,0,0)", to="(conv_b01_l01-east)"),
    # # Conv02
    # to_Conv('conv_b01_l02', s_filer=conv_b01_l02_side, n_filer=conv_b01_l02_params,
    #         width=(conv_b01_l02_params * scaling_factor), height=(conv_b01_l02_side * scaling_factor),
    #         depth=(conv_b01_l02_side * scaling_factor), offset="(1,0,0)", to="(relu_b01_l01-east)"),
    # # Relu02
    # to_Relu('relu_b01_l02', s_filer=relu_b01_l02_side, n_filer=relu_b01_l02_params,
    #         width=(relu_b01_l02_params * scaling_factor), height=(relu_b01_l02_side * scaling_factor),
    #         depth=(relu_b01_l02_side * scaling_factor), offset="(1,0,0)", to="(conv_b01_l02-east)"),
    # # Conv03
    # to_Conv('conv_b01_l03', s_filer=conv_b01_l03_side, n_filer=conv_b01_l03_params,
    #         width=(conv_b01_l03_params * scaling_factor), height=(conv_b01_l03_side * scaling_factor),
    #         depth=(conv_b01_l03_side * scaling_factor), offset="(1,0,0)", to="(relu_b01_l02-east)"),
    # to_skip(of='conv_b01_l01', to='conv_b01_l03', pos=1.25),


    to_end()




]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()