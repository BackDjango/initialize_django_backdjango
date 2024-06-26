"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Project Constants
"""

# System
import os
from dotenv import load_dotenv


load_dotenv()


class SERVICE:
    """
    Service Config
    """

    DJANGO_SETTINGS_MODULE = os.getenv("DJANGO_SETTINGS_MODULE")
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = bool(os.getenv("DEBUG", False))
    ACCESS_TOKEN_EXP_MIN = int(os.getenv("ACCESS_TOKEN_EXP_MIN"))
    REFRESH_TOKEN_EXP_DAY = int(os.getenv("REFRESH_TOKEN_EXP_DAY"))


class SYSTEM_CODE:
    """
    각종 System Code (나중에 다국어 처리를 위해서)
    """

    # 0~1000 Base
    SUCCESS = (0, "SUCCESS")
    BAD_REQUEST = (1, "BAD_REQUEST")
    UNKNOWN_SERVER_ERROR = (2, "UNKNOWN_SERVER_ERROR")
    CLIENT_ERROR = (3, "CLIENT_ERROR")
    INVALID_FORMAT = (4, "INVALID_FORMAT")

    # 1001 ~ 2000 Auth
    EMAIL_ALREADY = (1001, "EMAIL_ALREADY")
    USER_NOT_FOUND = (1002, "USER_NOT_FOUND")
    USER_INVALID_PW = (1003, "USER_INVALID_PW")
    USER_NOT_ACTIVE = (1004, "USER_NOT_ACTIVE")
    USER_CREATE_ERROR = (1005, "USER_CREATE_ERROR")
    TOKEN_EXPIRED = (1006, "TOKEN_EXPIRED")
    TOKEN_INVALID = (1007, "TOKEN_INVALID")

    # 2001 ~ 3000 Board
    BOARD_NOT_FOUND = (2001, "BOARD_NOT_FOUND")
    BOARD_CREATE_ERROR = (2002, "BOARD_CREATE_ERROR")
    BOARD_UPDATE_ERROR = (2003, "BOARD_UPDATE_ERROR")
    BOARD_DELETE_ERROR = (2004, "BOARD_DELETE_ERROR")
    BOARD_PERMISSION_ERROR = (2005, "BOARD_PERMISSION_ERROR")
