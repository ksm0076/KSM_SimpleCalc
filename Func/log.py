import logging

def get_logger():
    # 로그 인스턴스
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # 로그 형식
    formatter = logging.Formatter(u'%(asctime)s [%(levelname)s] %(message)s')

    # 로그 기록 handler
    file_handler_info = logging.FileHandler('log.log')
    file_handler_warn = logging.FileHandler('warning.log')

    # level 설정
    file_handler_info.setLevel(logging.INFO)
    file_handler_warn.setLevel(logging.WARNING)

    # format 설정
    file_handler_info.setFormatter(formatter)
    file_handler_warn.setFormatter(formatter)

    # logger에 handler 추가
    logger.addHandler(file_handler_info)
    logger.addHandler(file_handler_warn)

    return logger
