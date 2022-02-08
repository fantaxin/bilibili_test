# encoding: utf-8
from mytime import sleep

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import mytime
from logger import logger


class BasePage:
    #  初始化,传入一个driver
    def __init__(self, driver: WebDriver):
        self.driver = driver

    #  二次封装元素等待,如果错误,记录日志,并截图保存
    def wait(self, loc):
        """
        元素等待
        :param loc: 等待的元素
        :return:
        这里使用的是隐式等待，同时将隐式等待和元素是否可见的判断进行了结合，这样更加稳定!
        """
        logger.info('正待等待元素{}'.format(loc))
        try:
            WebDriverWait(self.driver, timeout=30).until(EC.visibility_of_element_located(loc))
            # 首先是隐式等待表达式（driver对象，等待时长)
            # 同时每0.5秒会查看一次,查看元素是否出现,如果超过30s未出现,则报错timeout
            # until()是等待元素可见,这里加入了元素是否可见的判断
        except Exception as e:
            logger.exception('元素等待错误发生:{}元素为{}'.format(e, loc))
            raise

    def screenshots(self, name):
        """
        保存截图
        :param name:根据被调用传入的名字,生成png的图片
        :return:
        """

        try:
            file_path = 'screenshots\\'
            times = mytime.time_now()
            filename = file_path + times + '{}.png'.format('1')

            self.driver.get_screenshot_as_file(filename)
            logger.info("正在保存图片:{}".format(filename))

        except Exception as e:
            logger.error('图片报存错误:{}'.format(e))
            raise

    def get_ele(self, loc):
        """
        查找元素
        :param loc:
        :return:
        """
        logger.info('正在查找元素:{}'.format(loc))
        try:
            #  这里使用的是find_element查找单个元素,这里需要传入的是一个表达式,需要告诉driver对象使用的是什么定位方法,以及元素定位!
            # By是继承了selenium里面的8大定位方法,所以框架里操作元素的皆是By.XPATH或者By.id等等
            # 同时因为需要传入的是一个表达式,而By.XPATH是一个元组,这里做了解包处理
            ele = self.driver.find_element(*loc)
        except Exception as e:
            logger.exception('查找元素失败：')
            raise
        else:
            return ele

    def send_key(self, loc, name):
        """
        输入文本
        :param loc:元素
        :param name: 输入的名字
        :return:
        """
        logger.info('正在操作元素{},输入文本{}'.format(loc, name))
        self.wait(loc)
        try:
            self.get_ele(loc).clear()
            self.get_ele(loc).send_keys(name)
        except:
            logger.exception('元素错误 {}:')
            raise

    def click_key(self, loc):
        """
        元素点击
        :param loc:
        :return:
        """
        logger.info('正在操作元素{}'.format(loc))
        self.wait(loc)
        try:
            self.get_ele(loc).click()
        except Exception as e:
            logger.exception('点击元素错误:{}'.format(e))
            raise

    def get_ele_text(self, loc):
        """
        获取元素文本
        :param loc: 
        :return: 
        """""
        logger.info('{}正在获取文本{}'.format(loc))
        self.wait(loc)
        ele = self.get_ele(loc)
        try:
            text = ele.text
            logger.info('获取文本成功{}'.format(text))
            return text

        except:
            logger.exception('获取文本错误:')

    def get_ele_attribute(self, loc, attribute_name):
        """
        获取元素属性
        :param loc:
        :param attribute_name:
        :return:
        """
        sleep(2)
        logger.info('正在获取元素{}的属性'.format(loc))
        self.wait(loc)
        ele = self.get_ele(loc)
        try:
            value = ele.get_attribute(attribute_name)
            logger.info('获取属性成功{}'.format(value))
            return value
        except:
            logger.exception('获取属性失败')

    def wait_ele_click(self, loc):
        logger.info('正待等待可点击元素{}'.format(loc))
        try:
            WebDriverWait(self.driver, timeout=20).until(EC.element_to_be_clickable(loc))
            # logger.info('等待可点击元素{}'.format(loc))
        except:
            logger.exception('等待可点击元素错误:元素为{}'.format(loc))
            raise

    def switch_to_new(self):
        try:
            handles = self.driver.window_handles  # 获取当前浏览器的所有窗口句柄
            self.driver.switch_to.window(handles[-1])  # 切换到最新打开的窗口
            logger.info('正在进入最新的标签页:{}'.format(handles[-1].title()))
        except:
            handles = self.driver.window_handles  # 获取当前浏览器的所有窗口句柄
            logger.exception('进入最新的标签页失败{}'.format(handles[-1].title()))

    def switch_to_iframe(self, loc):
        try:
            WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it(loc))
            logger.info('正在进入嵌套页面:{}'.format(loc))
        except:
            logger.exception('进入嵌套页面失败{}'.format(loc))

    def click_wait_ele(self, loc):
        logger.info('正在等待{}元素出现'.format(loc))
        self.wait_ele_click(loc)
        try:
            self.get_ele(loc).click()
            logger.info('正在点击元素{}'.format(loc))
        except:
            logger.info('点击{}元素失败'.format(loc))

    def scroll_to(self, high):
        try:
            logger.info('正在下拉滚动条,距离为{}'.format(high))
            self.driver.execute_script("window.scrollTo(0,"+str(high)+")")
        except:
            logger.info('下拉滚动条失败'.format())

    def quit(self):
        self.driver.quit()