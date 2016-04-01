#   Copyright (c) 2016, Xilinx, Inc.
#   All rights reserved.
# 
#   Redistribution and use in source and binary forms, with or without 
#   modification, are permitted provided that the following conditions are met:
#
#   1.  Redistributions of source code must retain the above copyright notice, 
#       this list of conditions and the following disclaimer.
#
#   2.  Redistributions in binary form must reproduce the above copyright 
#       notice, this list of conditions and the following disclaimer in the 
#       documentation and/or other materials provided with the distribution.
#
#   3.  Neither the name of the copyright holder nor the names of its 
#       contributors may be used to endorse or promote products derived from 
#       this software without specific prior written permission.
#
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, 
#   THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR 
#   PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR 
#   CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
#   EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
#   PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
#   OR BUSINESS INTERRUPTION). HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
#   WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
#   OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF 
#   ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

__author__      = "Giuseppe Natale"
__copyright__   = "Copyright 2016, Xilinx"
__email__       = "xpp_support@xilinx.com"


from setuptools import setup, Extension, find_packages

#: Audio and video source files
_audio_src = ['pynq/_pynq/_audio/_audio.c', 'pynq/_pynq/src/audio.c', 
              'pynq/_pynq/src/gpio.c', 'pynq/_pynq/src/i2cps.c', 
              'pynq/_pynq/src/utils.c']

_video_src = ['pynq/_pynq/_video/_video.c', 'pynq/_pynq/_video/_capture.c', 
              'pynq/_pynq/_video/_display.c', 'pynq/_pynq/_video/_frame.c', 
              'pynq/_pynq/src/gpio.c', 'pynq/_pynq/src/py_xaxivdma.c', 
              'pynq/_pynq/src/py_xgpio.c', 'pynq/_pynq/src/utils_xlnk.c', 
              'pynq/_pynq/src/py_xvtc.c', 'pynq/_pynq/src/utils.c',  
              'pynq/_pynq/src/video_capture.c', 
              'pynq/_pynq/src/video_display.c']

#: BSP source files
bsp_axivdma = \
  ['pynq/_pynq/bsp/ps7_cortexa9_0/libsrc/axivdma_v6_0/src/xaxivdma.c',
   'pynq/_pynq/bsp/ps7_cortexa9_0/libsrc/axivdma_v6_0/src/xaxivdma_channel.c', 
   'pynq/_pynq/bsp/ps7_cortexa9_0/libsrc/axivdma_v6_0/src/xaxivdma_intr.c', 
   'pynq/_pynq/bsp/ps7_cortexa9_0/libsrc/axivdma_v6_0/src/xaxivdma_selftest.c']

bsp_gpio = \
  ['pynq/_pynq/bsp/ps7_cortexa9_0/libsrc/gpio_v4_0/src/xgpio.c', 
   'pynq/_pynq/bsp/ps7_cortexa9_0/libsrc/gpio_v4_0/src/xgpio_extra.c',
   'pynq/_pynq/bsp/ps7_cortexa9_0/libsrc/gpio_v4_0/src/xgpio_intr.c',
   'pynq/_pynq/bsp/ps7_cortexa9_0/libsrc/gpio_v4_0/src/xgpio_selftest.c']

bsp_vtc = \
  ['pynq/_pynq/bsp/ps7_cortexa9_0/libsrc/vtc_v7_0/src/xvtc.c', 
   'pynq/_pynq/bsp/ps7_cortexa9_0/libsrc/vtc_v7_0/src/xvtc_intr.c', 
   'pynq/_pynq/bsp/ps7_cortexa9_0/libsrc/vtc_v7_0/src/xvtc_selftest.c']

bsp_standalone = \
  ['pynq/_pynq/bsp/ps7_cortexa9_0/libsrc/standalone_v5_2/src/xplatform_info.c',
   'pynq/_pynq/bsp/ps7_cortexa9_0/libsrc/standalone_v5_2/src/xil_assert.c',
   'pynq/_pynq/bsp/ps7_cortexa9_0/libsrc/standalone_v5_2/src/xil_io.c',
   'pynq/_pynq/bsp/ps7_cortexa9_0/libsrc/standalone_v5_2/src/xil_exception.c']


#: Merge BSP src to _audio src
audio = []
audio.extend(bsp_standalone)
audio.extend(_audio_src)

#: Merge BSP src to _video src
video = []
video.extend(bsp_standalone)
video.extend(bsp_axivdma)
video.extend(bsp_gpio)
video.extend(bsp_vtc)
video.extend(_video_src)

setup(  name='pynq',
        version='0.1',
        description='Python for Xilinx package',
        author='XilinxPythonProject',
        author_email='xpp_support@xilinx.com',
        url='https://github.com/Xilinx/Pyxi',
        packages = find_packages(),
        download_url = 'https://github.com/Xilinx/Pyxi',
        package_data = {
          '': ['test/*', 'tests/*', '*.bin'],
        },
        ext_modules = [
            Extension('pynq.audio._audio', audio, 
                      include_dirs = ['pynq/_pynq/inc', 
                                      'pynq/_pynq/bsp/ps7_cortexa9_0/include'],
                     ),
            Extension('pynq.video._video', video, 
                      include_dirs = ['pynq/_pynq/inc', 
                                      'pynq/_pynq/bsp/ps7_cortexa9_0/include'],
                     ),
        ]
    )
