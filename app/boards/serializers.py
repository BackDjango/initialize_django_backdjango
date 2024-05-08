"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Board Serializers
"""

# System
from django.db import IntegrityError
from rest_framework import serializers

# Project
from core.constants import SYSTEM_CODE
from core.exception import raise_exception
from app.boards.models import Board


class BoardCreateUpdateSerializer(serializers.ModelSerializer):
    """
    게시판 생성 및 수정 Serializer
    """

    class Meta:
        model = Board
        fields = ["title", "content"]

    def create(self, validated_data, user):
        """
        게시판 생성
        """

        try:
            validated_data["author"] = user
            reponse = Board.objects.create(**validated_data)
        except IntegrityError:
            raise_exception(code=SYSTEM_CODE.BOARD_CREATE_ERROR)

        return reponse

    def update(self, instance, validated_data):
        """
        게시판 수정
        """
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.save()
        return instance


class BoardSerializer(serializers.ModelSerializer):
    """
    게시판 Response Serializer
    """

    author = serializers.SerializerMethodField(read_only=True)

    def get_author(self, obj):
        return obj.author.email if obj.author else None

    class Meta:
        model = Board
        fields = "__all__"
