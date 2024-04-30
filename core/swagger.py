"""
    Copyright ⓒ 2024 Dcho, Inc. All Rights Reserved.
    Author : Dcho (tmdgns743@gmail.com)
    Description : Common Response Swaggers
"""

# System
from drf_spectacular.utils import extend_schema, OpenApiResponse, inline_serializer
from rest_framework import serializers

# Project


def common_response_schema(status_code=200, description="성공", serializer=None):
    """
    공통 응답 스키마를 추가하는 데코레이터
    """

    if serializer is None:
        serializer = serializers.DictField(default={})

    def decorator(view_func):
        response_schema = inline_serializer(
            name="CommonResponse",
            fields={
                "data": serializer,
                "status_code": serializers.IntegerField(default=status_code),
                "msg": serializers.CharField(default="SUCCESS"),
                "code": serializers.IntegerField(default=0),
            },
        )

        return extend_schema(
            responses={
                status_code: OpenApiResponse(
                    description=description,
                    response=response_schema,
                )
            }
        )(view_func)

    return decorator
