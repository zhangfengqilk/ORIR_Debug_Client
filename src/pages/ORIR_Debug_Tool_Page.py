from src.uibasewindow.Ui_ORIR_Debug_Tool import Ui_ORIR_Debug_Tool
from PySide2.QtWidgets import QWidget,QFileDialog
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

class ORIR_Tool(QWidget, Ui_ORIR_Debug_Tool):
    """
    1. 加载点云数据，读取坐标数据到DataFrame类型的变量中
    2. 求点云图的四条边界（均值+平移）
    3. 求点云图的宽和高
    4. 求点云图的基准点（左上角的点）
    5. 点云图坐标平移
    6. 点云图缩放
    7. 输出数据（缩放系数，基准点，图片）
    """
    def __init__(self):
        super(ORIR_Tool, self).__init__()
        self.setupUi(self)
        self.load_pointcloud_data_btn.clicked.connect(self.load_pointcloud_data)
        self.set_edge_nums_btn.clicked.connect(self.get_basepoint)
        self.translation_pic_btn.clicked.connect(self.translation_pic)
        self.scale_pic_btn.clicked.connect(self.scale_to_pic)
        self.save_pic_btn.clicked.connect(self.save_figure)

        self._pointcloud_file = None        # 点云文件路径

        self.origin_datas = None            # 原始点云数据
        # 基准点（点云坐标系）
        self.base_x = 0
        self.base_y = 0

        # x坐标和y坐标分别的最小点和最大点
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0

        # 点云图中数据点数量
        self.data_total_nums = 0

        # 点云图的宽和高（点云图坐标系）
        self.data_width = 0
        self.data_height = 0

        # 缩放比例
        self.scale_factor = 0
        # 临时变量
        self.x_datas = []
        self.y_datas = []
        self.last_base_line_x = None
        self.last_base_line_y = None
        self.last_text = None

        self.figs = []


    def load_pointcloud_data(self):
        self._pointcloud_file = QFileDialog.getOpenFileName(self, '选择一个点云文件', './', 'map(*.map);;ALL(*.*)',
                                         '点云文件(*.map)')
        with open(self._pointcloud_file[0], 'r') as pc_fd:
            all_lines = pc_fd.readlines()
            print(type(all_lines))
            self._pointcloud_type = all_lines[0]

            for line in all_lines[22:]:
                line = line.strip()  # 去除每行的换行符
                data = line.split(' ')
                self.x_datas.append(int(data[0]))
                self.y_datas.append(int(data[1]))

            labels = ['x', 'y']
            datas = [(x, y) for x, y in zip(self.x_datas, self.y_datas)]
            self.origin_datas = pd.DataFrame.from_records(datas, columns = labels)

        self.figs.append(plt.figure(1))
        self.plot_figure(self.origin_datas['x'], self.origin_datas['y'])


    def save_figure(self):
        """
        点云图处理完成后，保存图片
        :param x:
        :param y:
        :return:
        """

        x = self.origin_datas['x']
        y = self.origin_datas['y']
        self.figs.append(plt.figure(4))

        plt.scatter(x, y, s=0.5)
        fig = matplotlib.pyplot.gcf()
        fig.set_size_inches(26.667, 15) # 设置图片尺寸
        plt.axis('off')  # 不显示坐标轴
        ax = plt.gca()
        ax.invert_yaxis()  # 绘图：y轴反向

        plt.savefig('pointcloud_pic.jpg', dpi=72, bbox_inches='tight')

        output_str = "基准点：（" + str(self.base_x) + ", " + str(self.base_y) + ")\n" + "缩放比例：" + str(float(self.scale_factor)) + "\n图片输出位置：.\pointcloud_pic.jpg"
        self.output_te.setText(output_str)


        plt.show()

    def plot_figure(self, x, y):
        plt.scatter(x, y, s=0.5)
        fig = matplotlib.pyplot.gcf()
        fig.set_size_inches(25.6, 14.4)
        plt.show()

    def get_basepoint(self):
        """
        获取基准点,获取图片左上角的点坐标，作为基准点。
        :return:
        """
        df_x = self.origin_datas.sort_values('x').reset_index(drop=True)  # x轴升序排序
        df_y = self.origin_datas.sort_values('y').reset_index(drop=True)  # y 轴升序排序
        # 各取x、y轴两端100个数据点，拟合出一条直线，这样求出四条边界的交点，左上角交点为基准点。
        self.data_total_nums = len(df_x)
        self.data_height = df_y.loc[self.data_total_nums-1, 'y'] - df_y.loc[0, 'y']
        self.data_width = df_x.loc[self.data_total_nums - 1, 'x'] - df_x.loc[0, 'x']
        self.min_x = df_x.loc[0, 'x']
        self.max_x = df_x.loc[self.data_total_nums-1, 'x']
        self.min_y = df_y.loc[0, 'y']
        self.max_y = df_y.loc[self.data_total_nums-1, 'y']
        up_nums = int(self.up_nums_le.text())
        bottom_nums = int(self.bottom_nums_le.text())
        left_nums = int(self.left_nums_le.text())
        right_nums = int(self.right_nums_le.text())

        self.base_x = df_x.loc[0:left_nums, 'x'].mean() - 1000
        self.base_y = df_y.loc[self.data_total_nums - up_nums:, 'y'].mean() + 1000

        self.plot_edges()


    def plot_edges(self):
        """
        绘制边界线，并画出来
        :return:
        """
        if self.last_base_line_x:
            self.last_base_line_x.remove()
            self.last_base_line_y.remove()
            self.last_text.remove()

        left_y = range(self.min_y-5000, self.max_y+5000, 100)
        up_x = range(self.min_x-5000, self.max_x+5000, 100)

        self.last_base_line_x, = plt.plot([self.base_x]*len(left_y), left_y, 'y', lw=2, markersize=6)
        self.last_base_line_y, = plt.plot(up_x, [self.base_y]*len(up_x), 'y', lw=2, markersize=6)
        self.last_text = plt.text(self.base_x + 1000, self.base_y+1500, "("+str(int(self.base_x)) + ", " + str(int(self.base_y)) + ")")
        plt.draw()
        plt.show()

    def translation_pic(self):
        """
        对点云图数据进行平移
        左上角的点为图片像素坐标的（0，0）点，点云图的（0，0）点一般为充电房所在的位置，需要做平移转换。
        (x_pixel, y_pixel) = (x_pointcloud + base_x, y_pointcloud - base_y)
        完成平移
        :return:
        """
        # 执行平移
        self.origin_datas['x'] = self.origin_datas['x'].map(lambda a: a - self.base_x)
        self.origin_datas['y'] = self.origin_datas['y'].map(lambda a: -1 * a + self.base_y)

        self.figs.append(plt.figure(2))
        plt.scatter(self.origin_datas['x'], self.origin_datas['y'], s=0.5)
        fig = matplotlib.pyplot.gcf()
        fig.set_size_inches(26.667, 15)

        ax = plt.gca()
        ax.invert_yaxis()  # 绘图：y轴反向
        plt.show()

    def scale_to_pic(self):
        """
        根据所给图片的宽和高（分辨率），对点云图数据进行映射。
        不进行拉伸，分别求出宽和高的缩放比例，选取大的那个比例作为统一缩放比例。
        :return:
        """
        pic_width = int(self.pic_width_le.text())
        pic_height = int(self.pic_height_le.text())

        factor_width = pic_width / abs(self.max_x - self.min_x)
        factor_height = pic_height / abs(self.max_y - self.min_y)
        self.scale_factor = factor_width
        if self.scale_factor < factor_height:
            self.scale_factor = factor_height


        self.origin_datas['x'] = self.origin_datas['x'].map(lambda a: a * self.scale_factor)
        self.origin_datas['y'] = self.origin_datas['y'].map(lambda a: a * self.scale_factor)
        self.figs.append(plt.figure(3))

        plt.scatter(self.origin_datas['x'], self.origin_datas['y'], s=0.5)
        fig = matplotlib.pyplot.gcf()
        fig.set_size_inches(13, 6)

        ax = plt.gca()
        ax.invert_yaxis()  # 绘图：y轴反向
        plt.show()



    def __del__(self):
        # message为窗口标题
        # Are you sure to quit?窗口显示内容
        # QtGui.QMessageBox.Yes | QtGui.QMessageBox.No窗口按钮部件
        # QtGui.QMessageBox.No默认焦点停留在NO上
        print("close")
        plt.close(1)
        # reply = QMessageBox.question(self, 'Message', "确定退出？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # # 判断返回结果处理相应事项
        # if reply == QMessageBox.Yes:
        #     self._debug_page.close_all()
        #     event.accept()
        # else:
        #     event.ignore()




