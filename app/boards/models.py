"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Board Model
"""

# System
from django.db import models

# Project
from core.models import BaseModel


class Board(BaseModel):
    """
    게시판 모델입니다.
    """

    title = models.CharField(max_length=100, verbose_name="게시판 제목")
    content = models.TextField(verbose_name="게시판 내용")

    author = models.ForeignKey(
        "users.User",
        on_delete=models.DO_NOTHING,
        related_name="boards_user",
        blank=True,
        null=True,
        verbose_name="게시판 작성자",
    )

    class Meta:
        app_label = "boards"
        db_table = "boards"

    def __str__(self) -> str:
        return self.title
