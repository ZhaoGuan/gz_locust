# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import requests
import time
import yaml
import json
import csv
import os
import shutil
import time


def config_reader(yaml_file):
    yf = open(yaml_file)
    yx = yaml.load(yf)
    yf.close()
    return yx


config = config_reader('./test_plan.yml')
master_host = config['master_host']
dir = str(config['dir'])
plan = config['plan']
duration = config['duration']
check_stat_time = 1
try:
    os.mkdir('./' + dir)
except:
    shutil.rmtree('./' + dir)
    os.mkdir('./' + dir)


class RunLocustTestPlant():
    def start(self, locust_count, hatch_rate):
        url = master_host + 'swarm'
        post_data = {'locust_count': locust_count, 'hatch_rate': hatch_rate}
        response = requests.post(url, data=post_data)
        return response

    def stop(self):
        url = master_host + 'stop'
        response = requests.get(url)
        print(response.text)
        print('测试结束-。-')

    def get_csv_report(self, locust_count):
        request_csv_url = master_host + 'stats/requests/csv'
        distribution_csv_url = master_host + 'stats/distribution/csv'
        response_request_csv = requests.get(request_csv_url)
        with open('./' + dir + '/' + str(locust_count) + '_request_report.csv', 'w') as request_f:
            for row in response_request_csv.text:
                request_f.write(row)
        response_distribution_csv = requests.get(distribution_csv_url)
        with open('./' + dir + '/' + str(locust_count) + '_distribution_report.csv', 'w') as distribution_f:
            for row in response_distribution_csv.text:
                distribution_f.write(row)

    def get_state(self):
        url = master_host + 'stats/requests'
        state = json.loads(requests.get(url).text)
        fail_ratio = state['fail_ratio']
        total_rps = state['total_rps']
        user_count = state['user_count']
        fail_number = 0
        for i in state['stats']:
            if i['name'] == 'Total':
                fail_number = i['num_failures']
        return {'fail_ratio': fail_ratio, 'fail_number': fail_number, 'total_rps': total_rps, 'user_count': user_count}

    def get_all_reports(self):
        report_dir = './' + dir
        csvs = os.walk(report_dir)
        files = []
        files_temp = []
        for i in csvs:
            files_temp = i[2]
        for dir_f in files_temp:
            if ('.D' not in dir_f) or ('all' not in dir_f):
                files.append(dir_f)
        distribution_first_line = ['Name', '# requests', '50%', '66%', '75%', '80%', '90%', '95%', '98%', '99%', '100%']
        request_first_line = ['Method', 'Name', '# requests', '# failures', 'Median response time',
                              'Average response time',
                              'Min response time', 'Max response time', 'Average Content Size', 'Requests/s']
        distribution = []
        request = []
        if len(files) > 0:
            for i in files:
                with open('./' + dir + '/' + i) as f:
                    csv_data = csv.reader(f)
                    if 'distribution' in i:
                        usr_number = i.split('_')[0]
                        for h in csv_data:
                            last_line = h
                        distribution_temp = {}
                        for g in range(len(distribution_first_line)):
                            distribution_temp.update({distribution_first_line[g]: last_line[g]})
                        distribution_temp.update({'User Number': usr_number})
                        distribution_temp.pop('Name')
                        distribution.append(distribution_temp)
                    else:
                        usr_number = i.split('_')[0]
                        for z in csv_data:
                            last_line = z
                            request_temp = {}
                        for g in range(len(request_first_line)):
                            request_temp.update({request_first_line[g]: last_line[g]})
                        request_temp.update({'User Number': usr_number})
                        request_temp.pop('Method')
                        request_temp.pop('Name')
                        request.append(request_temp)
        else:
            assert 1 + 1 > 2, '未发现csv报告'
        distribution_report_first_line = ['User Number', '# requests', '50%', '66%', '75%', '80%', '90%', '95%',
                                          '98%', '99%', '100%']
        request_report_first_line = ['User Number', '# requests', '# failures',
                                     'Median response time',
                                     'Average response time',
                                     'Min response time', 'Max response time', 'Average Content Size', 'Requests/s']
        with open('./' + dir + '/' + 'distribution_all_report.csv', 'w') as distribution_report:
            dw = csv.DictWriter(distribution_report, distribution_report_first_line)
            dw.writeheader()
            for row in distribution:
                dw.writerow(row)
        with open('./' + dir + '/' + 'request_all_report.csv', 'w') as request_report:
            dw = csv.DictWriter(request_report, request_report_first_line)
            dw.writeheader()
            for row in request:
                dw.writerow(row)

    def get_false(self, locust_count):
        now_user_number = self.get_state()['user_count']
        now_fail_number = self.get_state()['fail_number']
        if int(now_fail_number) > 0:
            print('出现错误！！！！')
            time.sleep(duration)
            fail_report_name = str(locust_count) + 'fail'
            self.get_csv_report(fail_report_name)
            return False
        else:
            return now_user_number

    def run_test(self, locust_count, hatch_rate, duration):
        start = self.start(locust_count, hatch_rate)
        if json.loads(start.text)['success']:
            while True:
                now_user_number = self.get_false(locust_count)
                if str(now_user_number) == 'False':
                    return False
                else:
                    if now_user_number >= locust_count:
                        time.sleep(duration)
                        self.get_csv_report(locust_count)
                        return True
                    else:
                        time.sleep(check_stat_time)
        else:
            print(str(locust_count) + '启动失败！')

    def run_plan(self):
        for i in plan:
            plan_locust_count = i['locust_count']
            plan_hatch_rate = i['hatch_rate']
            print('执行用户数为' + str(plan_locust_count) + '的测试')
            test = self.run_test(plan_locust_count, plan_hatch_rate, duration)
            if test is False:
                print(test)
                print('在用户数为' + str(plan_locust_count) + '时出现错误')
                break
        self.stop()
        self.get_all_reports()


if __name__ == "__main__":
    RunLocustTestPlant().run_plan()
