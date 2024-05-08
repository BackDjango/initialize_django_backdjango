"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Board Admin
"""

# System
from django.contrib import admin

# Project
from app.boards.models import Board

admin.site.register(Board)
