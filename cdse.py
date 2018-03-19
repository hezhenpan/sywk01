# *_*coding:utf-8 *_*
'''
./calculator.py -c /home/shiyanlou/test.cfg
-d /home/shiyanlou/user.csv -o /tmp/gongzi.csv


'''
import sys, csv


class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]

    def getdir(self):
        if {'-c', '-d', '-o'}.issubset(self.args):
            tmplist = []
            for i in ['-c','-d','-o']:
                index = self.args.index(i)
                tmplist.append(self.args[index + 1])

            return tmplist
        else:
            raise TypeError


class Config(object):
    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):
        config = {}
        with open(Args().getdir()[0]) as cfgfile:
            while True:
                oneline = cfgfile.readline()
                if oneline == '':
                    break
                tmplist = oneline.strip().split('=')
                try:
                    config[tmplist[0]] = tmplist[1]
                except Exception:
                    raise ValueError
        return config

    def get_config(self,key):
        return self.config[key]



class UserData(object):
    def __init__(self):
        self.userdata = self._read_users_data()

    def _read_users_data(self):
        userdata = []
        with open(Args().getdir()[1]) as usrfile:
            for i in range(8):
                opaline = usrfile.readline()
                titlist = opaline.strip().split(',')
                try:
                    userdata.append((titlist[0],titlist[1]))
                except Exception:
                    raise ValueError
        return userdata

    def get_userdata(self):
        return self.userdata



class IncomeTaxCalculator(object):

    def calc_for_all_userdata(self):

        realist = []
        tmplist = []


        for userid,wages in UserData().get_userdata():
            realist.append(userid)
            realist.append(wages)
            realist.append(format(self.shebao(int(wages)),'.2f'))
            realist.append(format(self.geshui(int(wages)),'.2f'))
            realist.append(float(wages) - float(format(self.shebao(int(wages)),'.2f')) - float(format(self.geshui(int(wages)),'.2f')))
            tmplist.append(realist)

        return tmplist

    def shebao(self,wages):
        alleen = float(Config().get_config('YangLao')) + float(Config().get_config('YiLiao')) \
                 + float(Config().get_config('ShiYe')) + float(Config().get_config('GongShang')) \
                 + float(Config().get_config('ShengYu')) + float(Config().get_config('GongJiJin'))

        if wages <= float(Config().get_config('JiShuL')):
            return float(Config().get_config('JiShuL'))*alleen
        elif float(Config().get_config('JiShuL')) < wages <= float(Config().get_config('JiShuH')):
            return wages*alleen
        elif wages >= float(Config().get_config('JiShuH')):
            return float(Config().get_config('JiShuH')) * alleen


    def geshui(self,wages):
        leftwages = wages - self.shebao(wages) - 3500

        if leftwages <= 0:
            return 0
        elif 0 < leftwages <= 1500:
            return format(leftwages * 0.03, '.2f')
        elif 1500 < leftwages <= 4500:
            return (format(leftwages * 0.1 - 105, '.2f'))
        elif 4500 < leftwages <= 9000:
            return (format(leftwages * 0.2 - 555, '.2f'))
        elif 9000 < leftwages <= 35000:
            return (format(leftwages * 0.25 - 1005, '.2f'))
        elif 35000 < leftwages <= 55000:
            return (format(leftwages * 0.30 - 2755, '.2f'))
        elif 55000 < leftwages <= 80000:
            return (format(leftwages * 0.35 - 5505, '.2f'))
        elif 80000 < leftwages:
            return (format(leftwages * 0.45 - 13505, '.2f'))


    def export(self, default='csv'):
        result = self.calc_for_all_userdata()
        with open(Args().getdir()[2],'w') as f:
            writer = csv.writer(f)
            writer.writerows(result)


if __name__ == '__main__':
    IncomeTaxCalculator().export()