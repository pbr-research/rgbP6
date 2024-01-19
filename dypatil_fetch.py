##################################################################################################
#                               Data Fetching From Server                                        #
#                                                                                                #
# Description: This is standardised module for specifically designed for fetching data of D.Y.   #
#              PATIL S.S.K LTD (15MH289) Sugar Industries and Padmashree Dr.D.Y.patil.S.S.K.Ltd  #                                                                                  
#              (Distilley Unit) from which we are fetching PM,MASS_FLOW,PM,COD,BOD,TSS,PH and
#              FLOW respectively.                                                                # 
#                                                                                                #
# Note: i)This module may require to perform several changes if and only if several changes are  #
#       made on server side.                                                                     #
#       ii)The CPCB data is the average of fetch data whose output will change if we change      #
#       dividing factor of total data.                                                           #
#                                                                                                #
# Result: di = {"pm_forbs":"","mass_flow":"","server_datatime_forbs":"","pm_cpcb":"","cod":"",   #
#               "bod":"","tss":"","ph":"","flow":"","server_datatime_cpcb":"","fetching_time":"" #
#              }                                                                                 #
#                                                                                                #
#                                                                                                #
#                                                                                                #
#                           Version: 1.0                                                         #
#                           Author: Kanhaiya Lasurkar, PBR Research.                             #
#                                                                                                #
##################################################################################################

import requests
import json
from datetime import datetime
import time
import warnings

#Declearing Required Variables
param = ["pm_forbs","mass_flow","server_datatime_forbs","pm_cpcb","cod","bod","tss","ph","flow","server_datatime_cpcb","fetching_time","counter"]
ls = []
di = {}
json_data={}

#Standard Data Used to Fetch Information from Server
cookies = {
    'key': 'value',
    'slide-user': '1965',
    'SameSite': 'strict',
}

headers = {
    key :{"User-Agent":User_Agent,"Accept":Accept,"Accept-Language":Accept_Language,"Content-Type":Content_Type,"token":token,"Origin":Origin,"Connection":Connection,"Referer":Referer,"Sec-Fetch-Dest":Sec_Fetch_Dest,"Sec-Fetch-Mode":Sec_Fetch_Mode,"Sec-Fetch-Site":Sec_Fetch_Site}
    for key, User_Agent, Accept,Accept_Language, Content_Type, token, Origin, Connection, Referer, Sec_Fetch_Dest, Sec_Fetch_Mode, Sec_Fetch_Site in [
        (0,"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0","application/json, text/plain, */*","en-US,en;q=0.7,mr;q=0.3","text/plain","abhishek","https://rtdms.cpcb.gov.in","keep-alive","https://rtdms.cpcb.gov.in/","empty","cors","same-origin"),
        (1,"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0","application/json, text/plain, */*","en-US,en;q=0.7,mr;q=0.3","application/json;charset=utf-8","abhishek","https://rtdms.cpcb.gov.in","keep-alive","https://rtdms.cpcb.gov.in/industry-status?id=576&st=live","empty","cors","same-origin")
         ]
    }

headers_2 = {
    head :{"User-Agent":user_agent,"Accept":accept,"Accept-Language":accept_language,"Content-Type":content_type,"X-Requested-With":x_requested_with,"Origin":origin,"Connection":connection,"Referer":referer,"Upgrade-Insecure-Requests":upgrade_insecure_requests}
    for head, user_agent, accept, accept_language, content_type, x_requested_with, origin, connection, referer, upgrade_insecure_requests in [
        (0,"Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0","text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8","en-US,en;q=0.7,mr;q=0.3","application/x-www-form-urlencoded","","http://cpdms.forbesmarshall.in:8080","keep-alive","http://cpdms.forbesmarshall.in:8080/enviroconnect/","1"),
        (1,"Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0","text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8","en-US,en;q=0.7,mr;q=0.3","","","","keep-alive","http://cpdms.forbesmarshall.in:8080/enviroconnect/servlet/com.aipl.pls.web.admin.AdminServlet?FunctionKey=412&GroupID=676&PlantId=657&PlantName=Pad.Dr.D.Y.Patil%20Sahakari%20Sakhar%20Karkhana%20Ltd%20old(Orient%20Green%20Power%20Company%20Ltd&dhxr1703590556569","1"),
        (2,"Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0","text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8","en-US,en;q=0.7,mr;q=0.3","application/x-www-form-urlencoded","XMLHttpRequest","","keep-alive","http://cpdms.forbesmarshall.in:8080/enviroconnect/plantlink?FunctionKey=751&WidgetClassName=com.aipl.pls.web.widgets.onlinedata.OnlineData&WidgetId=5&JspName=OnlineData.jsp&plantId=657&deviceId=1641&page=portlet&groupId=676&dashboardType=3","")
         ]
    }

data_log2 = {
    'loginname': 'PDYSSKL',
    'password': 'Pdysskl@123',
    'email': '',
    'purpose': '',
    'language': 'en',
    'Submit': 'Login',
}

params = {
    head :{"FunctionKey":function_key,"ajaxCall":ajax_call,"WidgetClassName":widget_class_name,"WidgetId":widget_id,"_":dash,"groupId":group_id,"plantId":plant_id}
    for head, function_key, ajax_call, widget_class_name, widget_id, dash, group_id, plant_id in [
        (0,"301","","","","","1395","1237"),
        (1,"752","val","com.aipl.pls.web.widgets.onlinedata.OnlineData","5","1703583555207","1395","1237")
        ]
    }

json_data = {
    name : {"param":param,"avg":avg,"startDate":startDate}
    for name, param, avg, startDate in [
        ("json_pm","pm","minute_5","4h-ago"),
        ("json_cod","cod","minute_5","4h-ago"),
        ("json_bod","bod","minute_5","4h-ago"),
        ("json_tss","tss","minute_5","4h-ago"),
        ("json_ph","ph","minute_5","4h-ago"),
        ("json_flow","flow.rate","minute_5","4h-ago"),
        ]
    }

post_url = ["https://rtdms.cpcb.gov.in/api/stations/10627/devices/15264/data","https://rtdms.cpcb.gov.in/api/stations/1853/devices/2257/data","https://rtdms.cpcb.gov.in/api/stations/1853/devices/2258/data","https://rtdms.cpcb.gov.in/api/stations/1853/devices/2259/data","https://rtdms.cpcb.gov.in/api/stations/1853/devices/2260/data","https://rtdms.cpcb.gov.in/api/stations/1853/devices/2261/data","http://cpdms.forbesmarshall.in:8080/enviroconnect/servlet/com.aipl.pls.web.admin.AdminServlet"]

get_url = ["http://cpdms.forbesmarshall.in:8080/enviroconnect","http://cpdms.forbesmarshall.in:8080/enviroconnect/AQMS","http://cpdms.forbesmarshall.in:8080/enviroconnect/plantlink"] 

data = {
    'eyJlbWFpbCI6ImR5cGF0aWxzc2tsdGRAZ21haWwuY29tIiwicGFzc3dvcmQiOiIyNmQ2NTZiOGRmOGM1YjZiZTgzMDI1YzMwNWE1MDI4MmY3NTY4OWQwIn0': '',
}

# Function which Fetch Data from 2 Websites with Different Sessions as rs and rs1 respectively.
def getData_cpcb():
    #Session to Fetch Data from CPCB Board
    global di
    with requests.session() as rs:
        response_data = []
        warnings.simplefilter("ignore")
        #print("cpcb response")
        
        try:
            response = rs.post('https://rtdms.cpcb.gov.in/api/enclogin', cookies=cookies, headers=headers[0], data=data,verify=False, timeout=10)
        except:
            print("Error: Cannot Establish Connection!!")
            return
        
        cook = response.cookies.get_dict()
        
        #print("cpcb response executed")
        count = 0
        
        for attribute in json_data:
            try:
                response_data.append(rs.post(post_url[count],cookies=cook,headers=headers[1],json=json_data[attribute],verify=False, timeout=10))
                count+=1
            except:
                print("CPCB Data is Not Available!!")
                return
        
        #print(response_data[1].text)
        #exit(0)
        temp = 0
        for attribute in json_data:
            try:
                ls.append((response_data[temp].json())[attribute.split('_')[1]][len((response_data[temp].json())[attribute.split('_')[1]])-1]["value"])
            except:
                ls.append("NULL")
                continue
            temp+=1
        try:
            ls.append((response_data[len(response_data)-1].json())[attribute.split('_')[1]][len(response_data[len(response_data)-1].json()["flow"])-1]["time"])
        except:
            ls.append("NULL")
        
        ls.append(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    
    counter = 0
    for value in ls:
        if value != "NULL":
            continue
        else:
            counter += 1
            continue
    
    ls.append(counter)
    di = dict(zip(param,ls))
    #print("di = ",di)
    #return di
    
#Session to Fetch Data From Forbesmarshall
def getData_forbs():
    ls.clear()
    with requests.session() as rs1:
        response_data1 = []
        warnings.simplefilter("ignore")
        try:
            rs1.get(get_url[0],timeout = 10)
        except:
            print("Failed to Establish Connection!!")
            return
        
        cook = rs1.cookies.get_dict()
        try:
            response = rs1.post(
                post_url[len(post_url)-1],
                cookies=cook,
                headers=headers_2[0],
                data=data_log2,
                timeout = 10,
                )
        except:
            print("No Response to Requests!!")
            return
                
        for url_count in range(len(params)):
            try:
                response_data1.append(rs1.get(
                    get_url[url_count+1],
                    cookies=cook,
                    headers = headers_2[url_count+1],
                    params=params[url_count],
                    timeout = 10,
                    ))
            except:
                print("No Response Data from Server!!")
                return
        
        for count in range(len((response_data1[1].json())["list"])):
            try:
                ls.append(str((response_data1[1].json())["list"][count]["onlineValue"]))
            except:
                ls.append("NULL")
                continue
        try:
            ls.append(response_data1[1].json()["list"][len(response_data1[1].json()["list"])-1]["updateOnlineTime"])
        except:
            ls.append("NULL")
        #print(ls)
        getData_cpcb()
        return di

#Iteration to Fetch Data by calling getData() function.
if __name__ == "__main__":
    print("testing D.Y. PATIL S.S.K LTD")
    for get in range(100):
        #print("forbs fetch")
        #getData_forbs()
        print("forbs fetch")
        print(getData_forbs())
        time.sleep(10)
