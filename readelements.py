import os
import yaml


class Element(object):
    """获取元素"""

    def __init__(self, name):
        self.file_name = 'elements.yaml'
        self.element_path = 'elements.yaml'
        if not os.path.exists(self.element_path):
            raise FileNotFoundError("%s 文件不存在！" % self.element_path)
        with open(self.element_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        """获取属性"""
        data = self.data.get(item)
        if data:
            name, value = data.split('==')
            return name, value
        raise ArithmeticError("{}中不存在关键字：{}".format(self.file_name, item))


if __name__ == '__main__':
    search = Element('elements')
    print(search['video'][1]+'['+str(1)+']/a')
