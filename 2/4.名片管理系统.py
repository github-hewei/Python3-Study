# coding=utf-8

class card_manager:
    card_list = []
    last_id = 0

    def __init__(self):
        '''构造方法'''
        self.show_menu()
        while True:
            print('-'*40)
            opt = input('请输入选项(1添加 2展示 3删除 0退出)：')
            if opt not in ['1','2','3','0']:
                print('选项有误!!!')
                continue
            if opt == '1':
                self.add_card()
            elif opt == '2':
                self.show_card()
            elif opt == '3':
                self.del_card()
            else:
                break
        return None

    def show_menu(self):
        '''展示菜单'''
        print('-'*40,end='\n\n')
        print('{0:^40}'.format('名片管理系统 v1.0'),end='\n\n')
        print('{0:^40}'.format('1. 添加名片'))
        print('{0:^40}'.format('2. 展示名片'))
        print('{0:^40}'.format('3. 删除名片'),end='\n\n')
        print('{0:^40}'.format('0. 退出系统'),end='\n\n')
        return None

    def add_card(self):
        '''添加名片'''
        name = input('姓名：')
        sex = input('性别：')
        age = input('年龄：')
        tel = input('电话：')
        # 验证参数
        f , msg = True, []
        if len(name) < 1:
            f = False
            msg.append('姓名不能为空')
        if sex not in ['男', '女']:
            f = False
            msg.append('性别有误')
        if not age.isdigit() \
            or int(age) < 0 \
            or int(age) > 120:
            f = False
            msg.append('年龄有误')
        if len(tel) < 1:
            f = False
            msg.append('电话不能为空')
        if not f:
            for m in msg:
                print('* ' + m)
            return None
        self.last_id += 1
        card_dict = {}
        card_dict['id'] = self.last_id
        card_dict['name'] = name
        card_dict['sex'] = sex
        card_dict['age'] = age
        card_dict['tel'] = tel
        self.card_list.append(card_dict)
        print('保存成功!!!')
        return None

    def show_card(self):
        '''展示所有名片'''
        if len(self.card_list) < 1:
            print('列表为空!!!')
            return None
        print('编号\t\t', end='')
        print('姓名\t\t', end='')
        print('性别\t\t', end='')
        print('年龄\t\t', end='')
        print('电话\t\t', end='\n\n')
        for card in self.card_list:
            print('%s\t\t'%card['id'], end='')
            print('%s\t\t'%card['name'], end='')
            print('%s\t\t'%card['sex'], end='')
            print('%s\t\t'%card['age'], end='')
            print('%s\t\t'%card['tel'], end='\n')
        return None

    def del_card(self):
        '''删除名片'''
        _id = input('输入要删除的编号：')
        if not _id.isdigit():
            print('输入有误!!!')
            return None
        for k, card in enumerate(self.card_list):
            if int(_id) == card['id']:
                del self.card_list[k]
                print('删除成功!!!')
                return None
        else:
            print('删除失败!!!')
        return None

if __name__ == '__main__':
    card_manager()