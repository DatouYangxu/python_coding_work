import matplotlib.pyplot as plt
import numpy as np

# 生成波长数据
wavelengths = np.linspace(380, 750, 100)
reference_wavelength = 550
reference_intensity = 1.0
scattering_intensity = reference_intensity * (reference_wavelength / wavelengths)**4

# 创建图形
fig, ax = plt.subplots(figsize=(12, 7), dpi=100)

# 绘制散射强度曲线
ax.plot(wavelengths, scattering_intensity, linewidth=3, color='royalblue',
        label='Rayleigh Scattering Intensity (∝1/λ⁴)', zorder=5)

# 标记关键颜色区域（使用英文）
colors = {
    'Violet': (380, 450),
    'Blue': (450, 495),
    'Green': (495, 570),
    'Yellow': (570, 590),
    'Orange': (590, 620),
    'Red': (620, 750)
}

color_map = {
    'Violet': 'purple',
    'Blue': 'blue',
    'Green': 'green',
    'Yellow': 'yellow',
    'Orange': 'orange',
    'Red': 'darkred'
}

y_max = 3.5
for color_name, (w_start, w_end) in colors.items():
    ax.axvspan(w_start, w_end, alpha=0.2, color=color_map[color_name], zorder=1)
    center = (w_start + w_end) / 2
    ax.text(center, y_max * 0.95, color_name, 
            ha='center', va='top', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8, edgecolor='gray'))

# 标记关键波长点（英文）
key_wavelengths = {
    450: 'Blue Light (450nm)',
    550: 'Green Light (550nm)\nReference Point',
    650: 'Red Light (650nm)'
}

for wl, label in key_wavelengths.items():
    intensity = reference_intensity * (reference_wavelength / wl)**4
    ax.plot(wl, intensity, 'o', markersize=8, color='red', zorder=6)
    ax.annotate(f'{label}\nIntensity: {intensity:.2f}', 
                xy=(wl, intensity),
                xytext=(wl + 5, intensity + 0.3),
                fontsize=9,
                arrowprops=dict(arrowstyle="->", color='gray', alpha=0.7),
                bbox=dict(boxstyle="round,pad=0.2", facecolor='yellow', alpha=0.7))

# 添加公式和标题
formula_text = r'$I(\lambda) \propto \frac{1}{\lambda^4}$'
ax.text(0.02, 0.98, formula_text,
        transform=ax.transAxes,
        fontsize=16,
        verticalalignment='top',
        bbox=dict(boxstyle="round,pad=0.5", facecolor='white', edgecolor='blue'))

ax.text(400, 2.8, 'Blue light scattered ~4.4× more than red light', 
        fontsize=11, fontweight='bold', color='darkblue',
        bbox=dict(boxstyle="round,pad=0.3", facecolor='lightcyan', edgecolor='blue'))

# 设置坐标轴和标题（英文）
ax.set_xlabel('Wavelength (nm)', fontsize=13, fontweight='bold')
ax.set_ylabel('Relative Scattering Intensity', fontsize=13, fontweight='bold')
ax.set_title('Rayleigh Scattering Intensity vs Wavelength', fontsize=16, fontweight='bold', pad=20)

ax.set_xlim(380, 750)
ax.set_ylim(0, y_max)
ax.grid(True, alpha=0.3, linestyle='--')
ax.legend(loc='upper right', fontsize=11, framealpha=0.9)

# 添加脚注
footnote = "Data source: Rayleigh scattering formula I ∝ 1/λ⁴, normalized at 550nm"
plt.figtext(0.5, 0.01, footnote, ha='center', fontsize=9, style='italic', color='gray')

plt.tight_layout()
output_path = 'rayleigh_scattering_intensity_en.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Image saved to: {output_path}")
plt.show()