from django.shortcuts import render
import requests
from datetime import datetime
# Create your views here.

def display(request):
    response = requests.get('https://api.covid19india.org/raw_data.json')
    data = response.json()
    listData=data["raw_data"]
    dataDic={}
    totCase={'Ahmadabad':0,'Amreli':0,'Anand':0,'Aravalli':0,'Banaskantha':0,'Bharuch':0,'Bhavnagar':0,'Botad':0,'Chota Udaipur':0,'Dahod':0,'Dang':0,'Devbhoomi Dwarka':0,'Gandhinagar':0,'Gir Somnath':0,'Jamnagar':0,'Junagadh':0,'Kachchh':0,'Kheda':0,'Mahisagar':0,'Mahesana':0,'Morbi':0,'Narmada':0,'Navsari':0,'Panch Mahals':0,'Patan':0,'Porbandar':0,'Rajkot':0,'Sabarkantha':0,'Surat':0,'Surendranagar':0,'Tapi':0,'Vadodara':0,'Valsad':0}
    recoveredCase={'Ahmadabad':0,'Amreli':0,'Anand':0,'Aravalli':0,'Banaskantha':0,'Bharuch':0,'Bhavnagar':0,'Botad':0,'Chota Udaipur':0,'Dahod':0,'Dang':0,'Devbhoomi Dwarka':0,'Gandhinagar':0,'Gir Somnath':0,'Jamnagar':0,'Junagadh':0,'Kachchh':0,'Kheda':0,'Mahisagar':0,'Mahesana':0,'Morbi':0,'Narmada':0,'Navsari':0,'Panch Mahals':0,'Patan':0,'Porbandar':0,'Rajkot':0,'Sabarkantha':0,'Surat':0,'Surendranagar':0,'Tapi':0,'Vadodara':0,'Valsad':0}
    hospitalizedCase={'Ahmadabad':0,'Amreli':0,'Anand':0,'Aravalli':0,'Banaskantha':0,'Bharuch':0,'Bhavnagar':0,'Botad':0,'Chota Udaipur':0,'Dahod':0,'Dang':0,'Devbhoomi Dwarka':0,'Gandhinagar':0,'Gir Somnath':0,'Jamnagar':0,'Junagadh':0,'Kachchh':0,'Kheda':0,'Mahisagar':0,'Mahesana':0,'Morbi':0,'Narmada':0,'Navsari':0,'Panch Mahals':0,'Patan':0,'Porbandar':0,'Rajkot':0,'Sabarkantha':0,'Surat':0,'Surendranagar':0,'Tapi':0,'Vadodara':0,'Valsad':0}
    deceasedCase={'Ahmadabad':0,'Amreli':0,'Anand':0,'Aravalli':0,'Banaskantha':0,'Bharuch':0,'Bhavnagar':0,'Botad':0,'Chota Udaipur':0,'Dahod':0,'Dang':0,'Devbhoomi Dwarka':0,'Gandhinagar':0,'Gir Somnath':0,'Jamnagar':0,'Junagadh':0,'Kachchh':0,'Kheda':0,'Mahisagar':0,'Mahesana':0,'Morbi':0,'Narmada':0,'Navsari':0,'Panch Mahals':0,'Patan':0,'Porbandar':0,'Rajkot':0,'Sabarkantha':0,'Surat':0,'Surendranagar':0,'Tapi':0,'Vadodara':0,'Valsad':0}

    totCount=0
    recoverCount=0
    deathCount=0
    totInceseCount=0
    increseDict={}
    gujRecord=list( [d["detectedcity"],d["detecteddistrict"],d["detectedstate"],d["currentstatus"],d['dateannounced'],d['statuschangedate']] for d in listData if 'Gujarat' in d["detectedstate"])
    for cd in gujRecord:
        if datetime.now().strftime('%d/%m/%Y')==cd[4]:
            totInceseCount=totInceseCount+1
            if cd[1] in increseDict.keys():
                value=increseDict[cd[1]]
                increseDict[cd[1]]=value+1
            else:
                increseDict[cd[1]]=1
        if cd[1] in totCase.keys():
            totCount+=1
            value=totCase[cd[1]]
            totCase[cd[1]]=value+1
            if cd[3]=="Recovered":
                recoverCount+=1
                value=recoveredCase[cd[1]]
                recoveredCase[cd[1]]=value+1
            elif cd[3]=="Hospitalized":
                value=hospitalizedCase[cd[1]]
                hospitalizedCase[cd[1]]=value+1
            elif cd[3]=="Deceased":
                deathCount+=1
                value=deceasedCase[cd[1]]
                deceasedCase[cd[1]]=value+1
    tmpList=[]
    datalist=[]
    mapData={}
    for key,value in totCase.items():
        tmpList=[key,totCase[key],hospitalizedCase[key], recoveredCase[key],deceasedCase[key]]
        datalist.append(tmpList)
        if value>0:
            if key=="Panch Mahals":
                mapData["panchmahal"]=value
            elif key=="Gir Somnath":
                mapData["somnath"]=value
            elif key=="Chota Udaipur":
                mapData["chotaudaipur"]=value
            elif key=="Devbhoomi Dwarka":
                mapData["dwarka"]=value    
            else:
                mapData[key]=value
   
    #return render(request,'tmp.html',{'data':gujRecord})

    return render(request,'display.html',{'data':datalist,"totCount":totCount,"recoverCount":recoverCount,"deathCount":deathCount,"mapData":mapData,"increseDict":increseDict,"totInceseCount":totInceseCount})
