"""数据模型定义。

本模块仅包含项目中使用的基础数据结构，
不依赖任何第三方库。
"""

from dataclasses import dataclass


@dataclass
class Driver:
    """司机数据类，表示一名司机及其当前位置与接单状态。"""

    driver_id: int   # 司机唯一标识
    x: float         # 当前位置的 X 坐标（可理解为经度方向）
    y: float         # 当前位置的 Y 坐标（可理解为纬度方向）
    is_idle: bool    # 是否处于空闲（可接单）状态
