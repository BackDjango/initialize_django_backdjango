"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Board Views
"""

# System
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_spectacular.utils import extend_schema

# Project
from core.constants import SYSTEM_CODE
from core.exception import raise_exception
from core.response import create_response
from core.pagination import CustomPagination
from core.swagger import common_response_schema
from app.boards.serializers import (
    BoardCreateUpdateSerializer,
    BoardSerializer,
)
from app.boards.models import Board


@extend_schema(
    tags=["[Board]"],
)
class BoardViewSet(ViewSet):
    """
    게시판에 관련된 ViewSet 게시글 생성, 조회, 수정, 삭제를 처리함.
    """

    permission_classes = [IsAuthenticatedOrReadOnly]

    @extend_schema(
        summary="게시글 생성",
        request=BoardCreateUpdateSerializer,
    )
    @common_response_schema(
        status_code=201,
        description="게시글 생성 성공",
        serializer=BoardSerializer,
    )
    def create_board(self, request):
        """
        게시글을 생성합니다.
        """
        serializer = BoardCreateUpdateSerializer(data=request.data)

        # Validation Check
        if not serializer.is_valid():
            raise_exception(code=SYSTEM_CODE.INVALID_FORMAT)

        response = serializer.create(serializer.validated_data, request.user)

        serializer = BoardSerializer(response)

        return create_response(data=serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        summary="게시글 목록 조회",
    )
    @common_response_schema(
        status_code=200,
        description="게시글 목록 조회 성공",
        serializer=BoardSerializer,
    )
    def list_board(self, request):
        """
        게시글 목록을 조회합니다.
        """
        pagination = CustomPagination()

        boards = Board.objects.all().order_by("-created_at")

        page = pagination.paginate_queryset(boards, request)

        serializer = BoardSerializer(page, many=True)

        response = pagination.get_paginated_response(data=serializer.data, status=status.HTTP_200_OK)
        return response

    @extend_schema(
        summary="게시글 상세 조회",
        parameters=[{"name": "board_id", "required": True, "in": "path"}],
    )
    @common_response_schema(
        status_code=200,
        description="게시글 상세 조회 성공",
        serializer=BoardSerializer,
    )
    def detail_board(self, request, board_id: int = None):
        """
        게시글을 상세 조회합니다.
        """

        board = Board.objects.filter(id=board_id).first()

        if not board:
            raise_exception(code=SYSTEM_CODE.BOARD_NOT_FOUND)

        serializer = BoardSerializer(board)

        return create_response(data=serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="게시글 수정",
        parameters=[{"name": "board_id", "required": True, "in": "path"}],
        request=BoardCreateUpdateSerializer,
    )
    @common_response_schema(
        status_code=200,
        description="게시글 수정 성공",
        serializer=BoardSerializer,
    )
    def update_board(self, request, board_id: int = None):
        """
        게시글을 수정합니다.
        """

        board = Board.objects.filter(id=board_id, author=request.user).first()

        # 유저가 작성한 게시글이 아닌 경우
        if not board:
            raise_exception(code=SYSTEM_CODE.BOARD_PERMISSION_ERROR)

        serializer = BoardCreateUpdateSerializer(data=request.data)

        # Validation Check
        if not serializer.is_valid():
            raise_exception(code=SYSTEM_CODE.INVALID_FORMAT)

        response = serializer.update(board, serializer.validated_data)

        serializer = BoardSerializer(response)

        return create_response(data=serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="게시글 삭제",
        parameters=[{"name": "board_id", "required": True, "in": "path"}],
    )
    @common_response_schema(
        status_code=200,
        description="게시글 삭제 성공",
    )
    def delete_board(self, request, board_id: int = None):
        """
        게시글을 삭제합니다.
        """

        board = Board.objects.filter(id=board_id, author=request.user).first()

        if not board:
            raise_exception(code=SYSTEM_CODE.BOARD_PERMISSION_ERROR)

        board.delete()

        return create_response(data={}, status=status.HTTP_200_OK)
