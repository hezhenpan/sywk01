#!/usr/bin/env python3

import sys
import csv


class Args(object):
    
    def __init__(self):
        self.args = sys.argv[1:]
        
    def getdir(typp):
        if typp == 'cfg':
            index = args.index('-c')
            configfile = args[index+1]
            return configfile
        elif typp == 'soucsv':
            index = args.index('-d')
            configfile = args[index+1]
            return configfile
        elif typp == 'outcsv':
            index = args.index('-o')
            configfile = args[index+1]
            return configfile


class Config(object):
    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):
        config = {}
        cfgdir = Args().getdir('cfg')
        file = open(cfgdir)
        









