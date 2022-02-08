# -*- coding: utf-8 -*-
import pytest
import allure

from mytime import time_now
from operate import init, search, intovideo, like, collect, zhuifan, guanzhu, comment


class Test_bilibili:

    @pytest.mark.parametrize("content,num", [
        ('软件测试', 2),
        ('中国地质大学', 1),
        ('周杰伦', 5),
        ('软件测试', 6),
        ('高等数学', 1),
        ('老番茄', 1),
        ('嘉然今天吃什么', 1),
        ('华农兄弟', 1),
        ('Warma', 1),
        ('小镇姑娘', 1)
    ])
    def test_like(self, content, num):
        bp = init()
        search(bp, content)  # 搜索视频
        intovideo(bp, num)  # 进入第num个视频的详细页
        a = like(bp)  # 执行点赞操作
        bp.quit()  # 退出
        assert a[0] != a[1]  # 点赞前后的点赞图标会发生变化

    @pytest.mark.parametrize("content,num", [
        ('软件测试', 2),
        ('中国地质大学', 1),
        ('周杰伦', 5),
        ('软件测试', 6),
        ('高等数学', 1),
        ('老番茄', 1),
        ('嘉然今天吃什么', 1),
        ('华农兄弟', 1),
        ('Warma', 1),
        ('小镇姑娘', 1)
    ])
    def test_collect(self, content, num):
        bp = init()  # 初始化浏览器，包括获取cookie等操作
        search(bp, content)  # 搜索视频
        intovideo(bp, num)  # 进入第num个视频的详细页
        a = collect(bp)  # 执行收藏操作
        bp.quit()  # 退出
        assert a[0] != a[1]  # 收藏图标发生变化

    @pytest.mark.parametrize("content,num,c", [
        ('软件测试', 2, '老师讲得不错！'),
        ('中国地质大学', 1, '地大加油'),
        ('周杰伦', 5, '好听'),
        ('软件测试', 6, '通俗易懂'),
        ('高等数学', 1, '听了还是不会。。。'),
        ('老番茄', 1, 'nb'),
        ('嘉然今天吃什么', 1, '好看'),
        ('华农兄弟', 1, '嘿嘿'),
        ('Warma', 1, '沃玛'),
        ('小镇姑娘', 1, '好听')
    ])
    def test_comment(self, content, num, c):
        bp = init()  # 初始化浏览器，包括获取cookie等操作
        search(bp, content)  # 搜索视频
        intovideo(bp, num)  # 进入第num个视频的详细页
        a = comment(bp, c)  # 执行收藏操作
        bp.quit()  # 退出
        assert a[0] == a[1]  # 评论顶部增加一条自己的评论

    @pytest.mark.parametrize("num", [
        1, 2, 3, 4, 5
    ])
    def test_zhuifan(self, num):
        bp = init()  # 初始化浏览器，包括获取cookie等操作
        a = zhuifan(bp, num)  # 执行追番操作
        bp.quit()  # 退出
        assert a[0] != a[1]  # 追番变成已追番

    @pytest.mark.parametrize("up", [
        "中国地质大学武汉", "罗翔说刑法", "华农兄弟", "老番茄", "Warma", "嘉然今天吃什么"
    ])
    def test_guanzhu(self, up):
        bp = init()  # 初始化浏览器，包括获取cookie等操作
        search(bp, up)  # 搜索up主
        a = guanzhu(bp)  # 执行关注操作
        bp.quit()  # 退出
        if a[0] == '已关注':  # 追番变成已追番
            assert a[1] == '+ 关注'
        else:
            assert a[1] == '已关注'
