# coding:utf-8
from django.test import TestCase
from report_show.models import EC


class StateViewTest(TestCase):

    def create_ec(self, ec_dict):
        return EC.objects.create(number=ec_dict['number'], product=ec_dict['product'],
                                 state=ec_dict['state'], theme=ec_dict['theme'], excel_month=ec_dict['excel_month'])

    def test_state_view_with_no_ec(self):
        ec_object_list = ['wait_confirm_refuse', 'wait_review', 'implementing', 'confirmed_refuse',
                          'wait_research', 'closed', 'reported', 'invalid']
        response = self.client.get('/state/')
        self.assertEqual(response.status_code, 200)
        for temp in ec_object_list:
            self.assertQuerysetEqual(response.context['state_dict'][temp], [])
            self.assertEqual(response.context['state_dict'][temp+'_nums'], 0)

    def test_state_view_with_one_EClist(self):
        ec_dict = {'number': '614004808394', 'product': 'ZXOPENCOS', 'state': u'待确认拒绝', 'theme': u'主题1',
                   'excel_month': u'201508'}
        self.create_ec(ec_dict)
        response = self.client.get('/state/')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['state_dict']['wait_confirm_refuse'],
                                 ['<EC: 614004808394>'])
        self.assertEqual(response.context['state_dict']['wait_confirm_refuse_nums'], 1)
        self.assertEqual(response.context['state_dict']['wait_confirm_refuse_percent'], 100.0)

    def test_state_view_with_two_ec(self):
        ec_dict1 = {'number': '6140048083', 'product': 'ZXOPENCOS', 'state': u'待确认拒绝', 'theme': u'主题1',
                    'excel_month': u'201508'}
        ec_dict2 = {'number': '6140048084', 'product': 'ZXTECS', 'state': u'待审核', 'theme': u'主题2',
                    'excel_month': u'201508'}
        self.create_ec(ec_dict1)
        self.create_ec(ec_dict2)
        response = self.client.get('/state/')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['state_dict']['wait_confirm_refuse'],
                                 ['<EC: 6140048083>'])
        self.assertQuerysetEqual(response.context['state_dict']['wait_review'],
                                 ['<EC: 6140048084>'])
        self.assertEqual(response.context['state_dict']['wait_confirm_refuse_nums'], 1)
        self.assertEqual(response.context['state_dict']['wait_review_nums'], 1)
        self.assertEqual(response.context['state_dict']['wait_confirm_refuse_percent'], 50.0)
        self.assertEqual(response.context['state_dict']['wait_review_percent'], 50.0)


class TeamViewTest(TestCase):
    def create_ec(self, ec_dict):
        return EC.objects.create(number=ec_dict['number'], product=ec_dict['product'],
                                 state=ec_dict['state'], theme=ec_dict['theme'], team=ec_dict['team'],
                                 excel_month=ec_dict['excel_month'])

    def test_team_view_with_no_EClist(self):
        response = self.client.get('/team/')
        self.assertEqual(response.status_code, 200)
        for team in response.context['state_dict']:
            self.assertEqual(team['wait_confirm_refuse_count'], 0)
            self.assertEqual(team['wait_review_count'], 0)
            self.assertEqual(team['wait_review_percent'], 0)

    def test_team_view_with_one_EClist(self):
        ec_dict = {'number': '614004808394', 'product': 'ZXOPENCOS', 'state': u'待确认拒绝', 'theme': u'主题1',
                   'team': u'CG', 'excel_month': u'201508'}
        self.create_ec(ec_dict)
        response = self.client.get('/team/')
        self.assertEqual(response.status_code, 200)
        for team in response.context['state_dict']:
            if team['team_name'] == u'CG':
                self.assertQuerysetEqual(team['wait_confirm_refuse'], ['<EC: 614004808394>'])
                self.assertEqual(team['wait_confirm_refuse_count'], 1)
                self.assertEqual(team['wait_confirm_refuse_percent'], 100.0)
            else:
                self.assertEqual(team['wait_confirm_refuse_count'], 0)
                self.assertEqual(team['wait_review_count'], 0)
                self.assertEqual(team['wait_review_percent'], 0)

    def test_team_view_with_two_EClist(self):
        ec_dict1 = {'number': '6140048083', 'product': 'ZXOPENCOS',
                    'state': u'待确认拒绝', 'theme': u'主题1', 'team': u'CG', 'excel_month': u'201508'}
        ec_dict2 = {'number': '6140048084', 'product': 'ZXOPENCOS',
                    'state': u'待审核', 'theme': u'主题2', 'team': u'CG', 'excel_month': u'201508'}
        ec_dict3 = {'number': '6140048085', 'product': 'ZXTECS',
                    'state': u'待审核', 'theme': u'主题3', 'team': u'CT、MIDWARE', 'excel_month': u'201508'}
        self.create_ec(ec_dict1)
        self.create_ec(ec_dict2)
        self.create_ec(ec_dict3)
        response = self.client.get('/team/')
        self.assertEqual(response.status_code, 200)

        for team in response.context['state_dict']:
            if team['team_name'] == u'CG':
                self.assertQuerysetEqual(team['wait_confirm_refuse'], ['<EC: 6140048083>'])
                self.assertQuerysetEqual(team['wait_review'], ['<EC: 6140048084>'])
                self.assertEqual(team['wait_confirm_refuse_count'], 1)
                self.assertEqual(team['wait_confirm_refuse_percent'], 50.0)
            elif team['team_name'] == u'CT、MIDWARE':
                self.assertQuerysetEqual(team['wait_review'], ['<EC: 6140048085>'])
                self.assertEqual(team['wait_review_count'], 1)
                self.assertEqual(team['wait_review_percent'], 100.0)
            else:
                self.assertEqual(team['wait_confirm_refuse_count'], 0)
                self.assertEqual(team['wait_review_count'], 0)
                self.assertEqual(team['wait_review_percent'], 0)


class IndexTest(TestCase):

    ec_dict1 = {'number': '6140048083', 'product': 'ZXOPENCOS', 'change_big_type': u'缺陷/故障',
                'change_small_type': u'A-致命', 'state': u'待确认拒绝', 'theme': u'主题1', 'team': u'CG',
                'submit_date': u'2015-08-31 18:47:14', 'found_department': u'平台软件一部/中心研究院/战略及平台',
                'excel_month': u'201508'}
    ec_dict2 = {'number': '6140048084', 'product': 'ZXOPENCOS', 'change_big_type': u'缺陷/故障',
                'change_small_type': u'C-一般', 'state': u'待审核', 'theme': u'主题2', 'team': u'CG',
                'submit_date': u'2015-08-31 18:47:14', 'found_department': u'平台软件一部/中心研究院/战略及平台',
                'excel_month': u'201508'}

    def create_ec(self, ec_dict):
        return EC.objects.create(number=ec_dict['number'],
                                 product=ec_dict['product'],
                                 change_big_type=ec_dict['change_big_type'],
                                 change_small_type=ec_dict['change_small_type'],
                                 submit_date=['submit_date'],
                                 state=ec_dict['state'],
                                 theme=ec_dict['theme'],
                                 team=ec_dict['team'],
                                 found_department=ec_dict['found_department'],
                                 excel_month=ec_dict['excel_month'],
                                 )

    def test_index_view_with_no_EClist(self):

        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)

        self.assertEqual(response.context['summary']['total_number'], 0)
        self.assertEqual(response.context['summary']['repetition_number'], 0)
        self.assertEqual(response.context['summary']['leak_rate'], 0)
        self.assertEqual(response.context['summary']['carry_out_number'], 0)
        self.assertEqual(response.context['summary']['total_valid_number'], 0)
        self.assertEqual(response.context['summary']['internal_leak_number'], 0)
        self.assertEqual(response.context['summary']['optimization_number'], 0)
        self.assertEqual(response.context['summary']['self_commit_number'], 0)
        self.assertEqual(response.context['summary']['requirement_number'], 0)

    def test_index_view_with_one_EClist(self):

        self.create_ec(self.ec_dict1)
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)

        self.assertEqual(response.context['summary']['total_number'], 1)
        self.assertEqual(response.context['summary']['repetition_number'], 0)
        self.assertEqual(response.context['summary']['leak_rate'], 0)
        self.assertEqual(response.context['summary']['carry_out_number'], 0)
        self.assertEqual(response.context['summary']['total_valid_number'], 1)
        self.assertEqual(response.context['summary']['internal_leak_number'], 0)
        self.assertEqual(response.context['summary']['optimization_number'], 0)
        self.assertEqual(response.context['summary']['self_commit_number'], 1)
        self.assertEqual(response.context['summary']['requirement_number'], 0)

    def test_index_view_with_two_EClist(self):

        self.create_ec(self.ec_dict1)
        self.create_ec(self.ec_dict2)
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)

        self.assertEqual(response.context['summary']['total_number'], 2)
        self.assertEqual(response.context['summary']['repetition_number'], 0.0)
        self.assertEqual(response.context['summary']['leak_rate'], 0)
        self.assertEqual(response.context['summary']['carry_out_number'], 0)
        self.assertEqual(response.context['summary']['total_valid_number'], 2)
        self.assertEqual(response.context['summary']['internal_leak_number'], 0)
        self.assertEqual(response.context['summary']['optimization_number'], 0)
        self.assertEqual(response.context['summary']['self_commit_number'], 2)
        self.assertEqual(response.context['summary']['requirement_number'], 0)


class StyleTest(TestCase):

    ec_dict1 = {'number': '6140048083', 'product': 'ZXOPENCOS', 'change_big_type': u'缺陷/故障',
                'change_small_type': u'A-致命', 'state': u'待确认拒绝', 'theme': u'主题1', 'team': u'CG',
                'submit_date': u'2015-08-31 18:47:14', 'found_department': u'平台软件一部/中心研究院/战略及平台',
                'excel_month': u'201508'}
    ec_dict2 = {'number': '6140048084', 'product': 'ZXOPENCOS', 'change_big_type': u'缺陷/故障',
                'change_small_type': u'C-一般', 'state': u'待审核', 'theme': u'主题2', 'team': u'CG',
                'submit_date': u'2015-08-31 18:47:14', 'found_department': u'平台软件一部/中心研究院/战略及平台',
                'excel_month': u'201508'}

    def create_ec(self, ec_dict):
        return EC.objects.create(number=ec_dict['number'],
                                 product=ec_dict['product'],
                                 change_big_type=ec_dict['change_big_type'],
                                 change_small_type=ec_dict['change_small_type'],
                                 submit_date=['submit_date'],
                                 state=ec_dict['state'],
                                 theme=ec_dict['theme'],
                                 team=ec_dict['team'],
                                 found_department=ec_dict['found_department'],
                                 excel_month=ec_dict['excel_month'],
                                 )

    def style_assert(self, response, numbers):
        self.assertEqual(response.context['style_dict']['a_deadly_count'], numbers[0])
        self.assertEqual(response.context['style_dict']['a_deadly_percent'], numbers[1])
        self.assertEqual(response.context['style_dict']['b_serious_count'], numbers[2])
        self.assertEqual(response.context['style_dict']['b_serious_percent'], numbers[3])
        self.assertEqual(response.context['style_dict']['c_general_count'], numbers[4])
        self.assertEqual(response.context['style_dict']['c_general_percent'], numbers[5])
        self.assertEqual(response.context['style_dict']['d_slight_count'], numbers[6])
        self.assertEqual(response.context['style_dict']['d_slight_percent'], numbers[7])
        self.assertEqual(response.context['style_dict']['add_count'], numbers[8])
        self.assertEqual(response.context['style_dict']['add_percent'], numbers[9])
        self.assertEqual(response.context['style_dict']['change_count'], numbers[10])
        self.assertEqual(response.context['style_dict']['change_percent'], numbers[11])
        self.assertEqual(response.context['style_dict']['delete_count'], numbers[12])
        self.assertEqual(response.context['style_dict']['delete_percent'], numbers[13])
        self.assertEqual(response.context['style_dict']['optimize_count'], numbers[14])
        self.assertEqual(response.context['style_dict']['optimize_percent'], numbers[15])

    def test_style_view_with_no_EClist(self):

        response = self.client.get('/style/')
        self.failUnlessEqual(response.status_code, 200)

        self.style_assert(response, [0, 0, 0, 0,
                                     0, 0, 0, 0,
                                     0, 0, 0, 0,
                                     0, 0, 0, 0])

    def test_style_view_with_one_EClist(self):

        self.create_ec(self.ec_dict1)
        response = self.client.get('/style/')
        self.failUnlessEqual(response.status_code, 200)

        self.style_assert(response, [1, 100.0, 0, 0,
                                     0, 0, 0, 0,
                                     0, 0, 0, 0,
                                     0, 0, 0, 0])

        for items in response.context['style_dict']['a_deadly']:
            self.assertEqual(items.number, self.ec_dict1['number'])
            self.assertEqual(items.product, self.ec_dict1['product'])
            self.assertEqual(items.change_big_type, self.ec_dict1['change_big_type'])
            self.assertEqual(items.change_small_type, self.ec_dict1['change_small_type'])
            self.assertEqual(items.state, self.ec_dict1['state'])
            self.assertEqual(items.theme, self.ec_dict1['theme'])
            self.assertEqual(items.team, self.ec_dict1['team'])
            self.assertEqual(items.found_department, self.ec_dict1['found_department'])

    def test_style_view_with_two_EClist(self):

        self.create_ec(self.ec_dict1)
        self.create_ec(self.ec_dict2)
        response = self.client.get('/style/')
        self.failUnlessEqual(response.status_code, 200)

        self.style_assert(response, [1, 50.0, 0, 0,
                                     1, 50.0, 0, 0,
                                     0, 0, 0, 0,
                                     0, 0, 0, 0])

        for items in response.context['style_dict']['a_deadly']:
            self.assertEqual(items.number, self.ec_dict1['number'])
            self.assertEqual(items.product, self.ec_dict1['product'])
            self.assertEqual(items.change_big_type, self.ec_dict1['change_big_type'])
            self.assertEqual(items.change_small_type, self.ec_dict1['change_small_type'])
            self.assertEqual(items.state, self.ec_dict1['state'])
            self.assertEqual(items.theme, self.ec_dict1['theme'])
            self.assertEqual(items.team, self.ec_dict1['team'])
            self.assertEqual(items.found_department, self.ec_dict1['found_department'])

        for items in response.context['style_dict']['c_general']:
            self.assertEqual(items.number, self.ec_dict2['number'])
            self.assertEqual(items.product, self.ec_dict2['product'])
            self.assertEqual(items.change_big_type, self.ec_dict2['change_big_type'])
            self.assertEqual(items.change_small_type, self.ec_dict2['change_small_type'])
            self.assertEqual(items.state, self.ec_dict2['state'])
            self.assertEqual(items.theme, self.ec_dict2['theme'])
            self.assertEqual(items.team, self.ec_dict2['team'])
            self.assertEqual(items.found_department, self.ec_dict2['found_department'])
