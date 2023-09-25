# -*- coding: utf-8 -*-
import sys
import time

from typing import List

from alibabacloud_dingtalk.robot_1_0.client import Client as dingtalkrobot_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.robot_1_0 import models as dingtalkrobot__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_dingtalk.oauth2_1_0.client import Client as dingtalkoauth2_1_0Client
from alibabacloud_dingtalk.oauth2_1_0 import models as dingtalkoauth_2__1__0_models
from alibabacloud_tea_util.client import Client as UtilClient



from authorization import dingding_id,dingding_secret,dingding_userid

class DingRobot:

    @staticmethod
    def create_client1() -> dingtalkoauth2_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkoauth2_1_0Client(config)

    @staticmethod
    def create_client2() -> dingtalkrobot_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkrobot_1_0Client(config)


def get_access_from_Ding(time_stamp):

        client1 = DingRobot.create_client1()
        get_access_token_request = dingtalkoauth_2__1__0_models.GetAccessTokenRequest(
            app_key=dingding_id,
            app_secret=dingding_secret
        )
        try:
            rtn = client1.get_access_token(get_access_token_request)
            print(rtn.body)
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                print(err)
                pass
        str_to_write = rtn.body.access_token + ' ' + str(time_stamp)
        filename='access_token_cache'
        with open(filename,"w") as f:
            f.write(str_to_write)
        return rtn.body.access_token

def get_access():
        time_stamp = time.time()
        print("Current time:",time_stamp)
        filename='access_token_cache'
        try:
            f = open(filename,"r")
        except IOError:
            print("File not exitsts,get from Ding and create it")
            return(get_access_from_Ding(time_stamp))
        else:
            str_to_read = f.read()
            old_token=str_to_read.split(' ',1)[0]
            old_time=float(str_to_read.split(' ',1)[1])
            print("old token and time:",str_to_read)
            f.close()
            if (time_stamp-old_time)<7200:
                return(old_token)
            else:
                return(get_access_from_Ding(time_stamp))

def ding_send(text1,title1):

        client2 = DingRobot.create_client2()
        batch_send_otoheaders = dingtalkrobot__1__0_models.BatchSendOTOHeaders()
        batch_send_otoheaders.x_acs_dingtalk_access_token = get_access()
        batch_send_otorequest = dingtalkrobot__1__0_models.BatchSendOTORequest(
            robot_code=dingding_id,
            user_ids=[dingding_userid],
            msg_key='sampleMarkdown',
            msg_param='{"text": "'+text1+'","title": "'+title1+'"}'
        )
        try:
            rtn2=client2.batch_send_otowith_options(batch_send_otorequest, batch_send_otoheaders, util_models.RuntimeOptions())
            print(rtn2)
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                print(err)
        return

i=0
while i<2:
      ding_send('time is: '+ time.ctime(),'test time '+ str(i)) 
      i+=1
      time.sleep(60)
ding_send('测试结束','挺好') 
