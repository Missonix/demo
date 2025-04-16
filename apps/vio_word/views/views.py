from robyn import Request, Response
from core.response import ApiResponse
from apps.vio_word.core import vio_word_check
from core.middleware import error_handler, request_logger, auth_required, admin_required, rate_limit, auth_userinfo
from core.logger import setup_logger
import json

# 设置日志记录器
logger = setup_logger('vio_word_views')

@error_handler
@request_logger
@rate_limit(max_requests=5, time_window=60)  # 每分钟最多5次请求
async def vio_check(request: Request) -> Response:
    """传入话术，返回违规词检测结果"""
    request = request.json()
    input = request.get("input")
    result = await vio_word_check(input)  # 正确等待异步函数的结果
    
    # 创建API响应
    return ApiResponse.success(data={
        "result": result
    })








