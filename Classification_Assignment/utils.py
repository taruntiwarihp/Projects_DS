from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import logging
import time
from pathlib import Path

def create_logger(cfg, phase = 'train'):
    root_output_dir = Path(cfg.logDir)
    # set up logger
    if not root_output_dir.exists():
        print('=> creating {}'.format(root_output_dir))
        root_output_dir.mkdir()

    time_str = time.strftime('%Y-%m-%d-%H-%M')
    
    log_file = '{}_{}_{}.log'.format(time_str, cfg.model_type, phase)
    final_log_file = root_output_dir / log_file

    head = '%(asctime)-15s %(message)s'
    logging.basicConfig(filename=str(final_log_file),
                        format=head)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    console = logging.StreamHandler()
    logging.getLogger('').addHandler(console)

    tensorboard_log_dir = Path(cfg.logDir) / ('tensorboard' + '_' + time_str + '_' + cfg.model_type)

    print('=> creating {}'.format(tensorboard_log_dir))
    tensorboard_log_dir.mkdir(parents=True, exist_ok=True)

    return logger, str(tensorboard_log_dir)