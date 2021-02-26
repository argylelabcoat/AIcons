#!/usr/bin/env python3

# This script creates a directory "png_out" with PNG versions of all the icons
# Requirements: ImageMagick and optipng installed on the system and on $PATH

import os
import subprocess

for root, dirs, files in os.walk(".", topdown=False):
    # Let's reject .git and output dirs:
    if not root.startswith("./.git") and \
            not root.startswith("./png_out"):
        # Not in .git or output:
        destdir = os.path.join("png_out", root)
        if not os.path.exists( destdir ):
            os.makedirs( destdir )
        for filename in files:
            inpath = os.path.join(root,filename)
            name,ext = os.path.splitext(filename)
            outpath = os.path.join(destdir,name+".png")
            print (inpath, outpath)
            output = subprocess.run(["convert", inpath, outpath], capture_output=True)
            output = subprocess.run(["optipng", "-o7", outpath], capture_output=True)

