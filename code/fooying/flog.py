#!/usr/bin/env python
# coding=utf-8
# By Fooying 2013/12/16

import logging
import sys
import traceback
import StringIO 

class FLOG():
    def __init__(self, fpath, level=logging.DEBUG):
        logger = logging.getLogger("flog")
        formatter = logging.Formatter('%(name)-12s %(asctime)s %(levelname)-8s %(message)s', '%a, %d %b %Y %H:%M:%S',)
        file_handler = logging.FileHandler(fpath)  
        file_handler.setFormatter(formatter)  
        stream_handler = logging.StreamHandler(sys.stderr)  
        logger.addHandler(file_handler)  
        logger.addHandler(stream_handler)  
        logger.setLevel(level)  
        self.logger = logger

    def debug(self, msg):
        self.logger.debug(msg)

    def error(self, msg):
        fp = StringIO.StringIO()
        traceback.print_exc(file=fp)
        error_msg = fp.getvalue()
        if error_msg.strip():
            msg += '\n'+error_msg.strip()
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.debug(msg)

    def warning(self, msg):
        self.logger.debug(msg)
