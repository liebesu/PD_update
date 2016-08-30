#!/usr/bin python
# -*- coding: UTF-8 -*-

import os
import sys
import logging
from xmlrpclib import ServerProxy


def call_to_process_pkgs(pkg_names_str_zip):
    """调用远程方法处理新生成的升级包
    """
    try:
        server = ServerProxy("http://192.168.25.21:8089")
        result = server.deal_with_upgpkgs(pkg_names_str_zip)

        if not result:
            return False
    except:
        return False

    return True


if __name__ == '__main__':

    current_dir = os.path.abspath(os.path.dirname(__file__))
    log_file = os.path.join(current_dir, 'call_server.log')
    logging.basicConfig(filename = log_file, level = logging.DEBUG,
                        format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s')

    logger = logging.getLogger('call_server')

    if len(sys.argv) == 2:
        pkg_names_str_zip = sys.argv[1]
        result = call_to_process_pkgs(pkg_names_str_zip)
        if result:
            logger.info('Status: success; Content: {0}.'.format(pkg_names_str_zip))
            sys.exit(0)
        else:
            logger.error('Status: failed; Content: {0}.'.format(pkg_names_str_zip))
            sys.exit(1)
    else:
        print 'Usage: {0} pkg_names_split_with_commas.'.format(sys.argv[0])
        logger.error('Status: error; Usage: {0} pkg_names_split_with_commas.'.format(sys.argv[0]))
        sys.exit(2)
