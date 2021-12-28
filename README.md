# thcolors
Colours from characters of bullet hell game series Touhou Project.

This file contains main colours of original Touhou characters designed by ZUN. The colours are picked up from original ZUN's art, with minor modifications to make plots more clear. The code is constantly revised with more characters and modified colours.

To use these colours, just copy the .py file to your working directory and import, then call the colour name in a plotting function from matplotlib.

Example:

from thcolors import *
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10)
y1 = 2 * x
y2 = 3 * x

plt.plot(x, y1, c='hina1')
plt.plot(x, y1, c='hina2')

=========================Chinese version=====================================

本文件包括ZUN制作的弹幕射击游戏系列《东方Project》主要人物的主要配色。所有的颜色皆取自ZUN绘人物。为了使颜色更实用我进行了一些小的修改。

使用方法：把.py文件复制到你的代码所在文件夹，在你的代码开头import thcolors，然后就可以在matplotlib的绘图函数中使用这些颜色了。还会有更多人物加入其中，颜色也可能会有微调。

使用示例：

from thcolors import *
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10)
y1 = 2 * x
y2 = 3 * x

plt.plot(x, y1, c='hina1')
plt.plot(x, y1, c='hina2')

