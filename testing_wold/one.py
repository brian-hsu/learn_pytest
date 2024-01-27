from collections import namedtuple

# 定义一个命名元组
Dinner = namedtuple('Dinner', ['food', 'cook', 'ready', 'id'])

# 设置默认值
Dinner.__new__.__defaults__ = (None, None, False, None)

def test_defaults():
    t1 = Dinner()
    t2 = Dinner(None, None, False, None)
    assert t1 == t2  # 检查默认值

def test_not_defaults():
    t = Dinner('potatoes', 'Sam')
    assert t.food == 'potatoes'
    assert t.cook == 'Sam'
    assert t.ready == False
    assert t.id == None  # 检查属性赋值

def test_as_dict():
    t = Dinner('potatoes', 'Sam', False, 10)
    t_dict = t._asdict()
    expected = {'food': 'potatoes', 'cook': 'Sam', 'ready': False, 'id': 10}
    assert t_dict == expected  # 檢查轉換為字典後是否匹配

def test_replace():
    t_before = Dinner('meat', 'Sam', False, 34)
    t_after = t_before._replace(id=10, ready=True)
    expected = Dinner('meat', 'Sam', True, 10)
    assert t_after == expected  # 檢查更改後的值