import cartopy.crs as ccrs # 地理投影
import cartopy.feature as cfeature # 地理特征
import matplotlib.pyplot as plt
import xarray as xr # 读取气象数据

# 1. 读取气象数据（例如NetCDF格式的再分析资料）
# 数据通常包含经度、纬度、时间、等压面高度等多个维度
data = xr.open_dataset('era5_slp.nc')
slp = data['msl'] # 提取海平面气压变量

# 2. 创建带有地理投影的画布
# 使用PlateCarree（经纬度）投影，这是最常用的
fig = plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

# 3. 添加地理背景
# 自动添加海岸线、国界等，使图表立即专业起来
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')

# 4. 绘制气象要素
# 在正确的投影上绘制等值线和填色图
contour = ax.contour(slp.longitude, slp.latitude, slp[0, :, :],
                     levels=20, colors='black', transform=ccrs.PlateCarree())
ax.clabel(contour, inline=True, fontsize=8) # 为等值线标注数值

# 5. 添加标题并显示
ax.set_title('Sea Level Pressure (hPa) - Example from ERA5')
plt.show()