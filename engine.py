"""空间检索引擎（模拟实现）。

提供根据目标位置查找附近司机的能力。
当前版本使用内存中的模拟数据，不依赖数据库或任何第三方库。
"""

import math

from models import Driver


class SpatialEngine:
    """基于司机位置提供空间检索能力的引擎。"""

    def __init__(self) -> None:
        # 模拟的司机数据源；实际项目中可替换为数据库或空间索引查询
        self._drivers = [
            Driver(driver_id=1, x=116.30, y=39.90, is_idle=True),
            Driver(driver_id=2, x=116.42, y=39.95, is_idle=False),
            Driver(driver_id=3, x=116.38, y=39.92, is_idle=True),
        ]

    def mock_get_nearest(self, target_x: float, target_y: float) -> Driver:
        """返回距离目标位置最近的空闲司机（模拟实现）。

        通过平面欧氏距离在内置数据中做简单比较，
        仅用于演示，并非真实的地理距离计算。

        Args:
            target_x: 目标位置的 X 坐标。
            target_y: 目标位置的 Y 坐标。

        Returns:
            Driver: 距离目标位置最近的空闲司机。

        Raises:
            RuntimeError: 数据源中不存在空闲司机时抛出。
        """
        # 只考虑可接单的空闲司机
        idle_drivers = [driver for driver in self._drivers if driver.is_idle]
        if not idle_drivers:
            raise RuntimeError("当前没有可接单的空闲司机")

        def distance(driver: Driver) -> float:
            # 平面欧氏距离；真实场景应使用地理距离公式（如 Haversine）
            return math.hypot(driver.x - target_x, driver.y - target_y)

        return min(idle_drivers, key=distance)
