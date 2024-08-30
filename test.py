
import win32api

# 获取缩放比例
scaling_factor = win32api.GetScaleFactorForDevice(0)  # 0 表示主显示器
print(f"缩放比例: {scaling_factor}")