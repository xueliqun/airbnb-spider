import requests
from bs4 import BeautifulSoup
import pymongo
import time
page_lists = ['https://www.airbnb.com/s/New-York--NY--United-States?page={}'.format(str(i)) for i in range(1,18)]
url_host = 'https://www.airbnb.com'
headers = {

}
def get_room_urls():
    for page in page_lists:
        web_data = requests.get(page)
        soup = BeautifulSoup(web_data.text,'lxml')
        links = soup.select('a.text-normal.link-reset')
        for link in links:
            room_url = url_host + link.get('href')
            print(room_url)
        time.sleep(0.5)

#get_room_urls()
room_urls = '''
https://www.airbnb.com/rooms/14586513
https://www.airbnb.com/rooms/15727768
https://www.airbnb.com/rooms/10726217
https://www.airbnb.com/rooms/13880972
https://www.airbnb.com/rooms/15728377
https://www.airbnb.com/rooms/14967908
https://www.airbnb.com/rooms/15148038
https://www.airbnb.com/rooms/13409293
https://www.airbnb.com/rooms/9476900
https://www.airbnb.com/rooms/11871690
https://www.airbnb.com/rooms/12902566
https://www.airbnb.com/rooms/698882
https://www.airbnb.com/rooms/14486991
https://www.airbnb.com/rooms/13413214
https://www.airbnb.com/rooms/13313377
https://www.airbnb.com/rooms/13389324
https://www.airbnb.com/rooms/13883249
https://www.airbnb.com/rooms/14211384
https://www.airbnb.com/rooms/15472338
https://www.airbnb.com/rooms/2719640
https://www.airbnb.com/rooms/15812883
https://www.airbnb.com/rooms/10855464
https://www.airbnb.com/rooms/11850717
https://www.airbnb.com/rooms/2631224
https://www.airbnb.com/rooms/13398837
https://www.airbnb.com/rooms/15066466
https://www.airbnb.com/rooms/15009466
https://www.airbnb.com/rooms/14809025
https://www.airbnb.com/rooms/14468845
https://www.airbnb.com/rooms/14767195
https://www.airbnb.com/rooms/14176286
https://www.airbnb.com/rooms/15065730
https://www.airbnb.com/rooms/15707075
https://www.airbnb.com/rooms/13004002
https://www.airbnb.com/rooms/11720909
https://www.airbnb.com/rooms/15360364
https://www.airbnb.com/rooms/14486991
https://www.airbnb.com/rooms/3694182
https://www.airbnb.com/rooms/13091737
https://www.airbnb.com/rooms/15592860
https://www.airbnb.com/rooms/13883249
https://www.airbnb.com/rooms/6738207
https://www.airbnb.com/rooms/15798996
https://www.airbnb.com/rooms/548609
https://www.airbnb.com/rooms/15452345
https://www.airbnb.com/rooms/11753645
https://www.airbnb.com/rooms/10647977
https://www.airbnb.com/rooms/15662948
https://www.airbnb.com/rooms/13961073
https://www.airbnb.com/rooms/14417576
https://www.airbnb.com/rooms/4946624
https://www.airbnb.com/rooms/15707075
https://www.airbnb.com/rooms/2193649
https://www.airbnb.com/rooms/15816210
https://www.airbnb.com/rooms/12586620
https://www.airbnb.com/rooms/14767195
https://www.airbnb.com/rooms/8955886
https://www.airbnb.com/rooms/10043733
https://www.airbnb.com/rooms/9653522
https://www.airbnb.com/rooms/15478933
https://www.airbnb.com/rooms/13216953
https://www.airbnb.com/rooms/9175459
https://www.airbnb.com/rooms/14881794
https://www.airbnb.com/rooms/698882
https://www.airbnb.com/rooms/15800923
https://www.airbnb.com/rooms/15596221
https://www.airbnb.com/rooms/1003290
https://www.airbnb.com/rooms/5178
https://www.airbnb.com/rooms/8943358
https://www.airbnb.com/rooms/15785681
https://www.airbnb.com/rooms/8796876
https://www.airbnb.com/rooms/4205815
https://www.airbnb.com/rooms/14211384
https://www.airbnb.com/rooms/8438801
https://www.airbnb.com/rooms/11999777
https://www.airbnb.com/rooms/11475963
https://www.airbnb.com/rooms/2719640
https://www.airbnb.com/rooms/7083273
https://www.airbnb.com/rooms/15478933
https://www.airbnb.com/rooms/548609
https://www.airbnb.com/rooms/9696653
https://www.airbnb.com/rooms/14967908
https://www.airbnb.com/rooms/698882
https://www.airbnb.com/rooms/15026594
https://www.airbnb.com/rooms/4531110
https://www.airbnb.com/rooms/13389324
https://www.airbnb.com/rooms/10043733
https://www.airbnb.com/rooms/10060921
https://www.airbnb.com/rooms/14742316
https://www.airbnb.com/rooms/13294856
https://www.airbnb.com/rooms/15790071
https://www.airbnb.com/rooms/13062489
https://www.airbnb.com/rooms/3859690
https://www.airbnb.com/rooms/15715946
https://www.airbnb.com/rooms/10060921
https://www.airbnb.com/rooms/15238184
https://www.airbnb.com/rooms/15790640
https://www.airbnb.com/rooms/13641995
https://www.airbnb.com/rooms/8800628
https://www.airbnb.com/rooms/14584733
https://www.airbnb.com/rooms/11475963
https://www.airbnb.com/rooms/15173309
https://www.airbnb.com/rooms/15545981
https://www.airbnb.com/rooms/6292893
https://www.airbnb.com/rooms/13126576
https://www.airbnb.com/rooms/11791968
https://www.airbnb.com/rooms/11851560
https://www.airbnb.com/rooms/8016946
https://www.airbnb.com/rooms/11791968
https://www.airbnb.com/rooms/11851560
https://www.airbnb.com/rooms/6292893
https://www.airbnb.com/rooms/8865645
https://www.airbnb.com/rooms/14992950
https://www.airbnb.com/rooms/1520813
https://www.airbnb.com/rooms/15629659
https://www.airbnb.com/rooms/12298684
https://www.airbnb.com/rooms/10847705
https://www.airbnb.com/rooms/13126576
https://www.airbnb.com/rooms/6480509
https://www.airbnb.com/rooms/6249050
https://www.airbnb.com/rooms/15644306
https://www.airbnb.com/rooms/11140302
https://www.airbnb.com/rooms/15827716
https://www.airbnb.com/rooms/15767894
https://www.airbnb.com/rooms/13192965
https://www.airbnb.com/rooms/11568637
https://www.airbnb.com/rooms/2193649
https://www.airbnb.com/rooms/10272841
https://www.airbnb.com/rooms/8386220
https://www.airbnb.com/rooms/14136862
https://www.airbnb.com/rooms/9653522
https://www.airbnb.com/rooms/10847705
https://www.airbnb.com/rooms/10726217
https://www.airbnb.com/rooms/14595378
https://www.airbnb.com/rooms/14804704
https://www.airbnb.com/rooms/15194855
https://www.airbnb.com/rooms/10503392
https://www.airbnb.com/rooms/14804934
https://www.airbnb.com/rooms/14966494
https://www.airbnb.com/rooms/13083276
https://www.airbnb.com/rooms/14547628
https://www.airbnb.com/rooms/10042625
https://www.airbnb.com/rooms/9748739
https://www.airbnb.com/rooms/15537940
https://www.airbnb.com/rooms/14804704
https://www.airbnb.com/rooms/12605864
https://www.airbnb.com/rooms/10512932
https://www.airbnb.com/rooms/14882397
https://www.airbnb.com/rooms/9021705
https://www.airbnb.com/rooms/14211384
https://www.airbnb.com/rooms/13639595
https://www.airbnb.com/rooms/12464635
https://www.airbnb.com/rooms/10855464
https://www.airbnb.com/rooms/15777126
https://www.airbnb.com/rooms/14547628
https://www.airbnb.com/rooms/11187353
https://www.airbnb.com/rooms/1056185
https://www.airbnb.com/rooms/10185960
https://www.airbnb.com/rooms/13782517
https://www.airbnb.com/rooms/9021829
https://www.airbnb.com/rooms/13259442
https://www.airbnb.com/rooms/12434953
https://www.airbnb.com/rooms/8386220
https://www.airbnb.com/rooms/8438801
https://www.airbnb.com/rooms/13944942
https://www.airbnb.com/rooms/11528086
https://www.airbnb.com/rooms/14340142
https://www.airbnb.com/rooms/14373594
https://www.airbnb.com/rooms/14756958
https://www.airbnb.com/rooms/15002948
https://www.airbnb.com/rooms/8688748
https://www.airbnb.com/rooms/14741560
https://www.airbnb.com/rooms/9839906
https://www.airbnb.com/rooms/15111898
https://www.airbnb.com/rooms/13728712
https://www.airbnb.com/rooms/15037103
https://www.airbnb.com/rooms/2719640
https://www.airbnb.com/rooms/4134035
https://www.airbnb.com/rooms/13783352
https://www.airbnb.com/rooms/12522952
https://www.airbnb.com/rooms/12298684
https://www.airbnb.com/rooms/14691107
https://www.airbnb.com/rooms/13259442
https://www.airbnb.com/rooms/14238574
https://www.airbnb.com/rooms/14122714
https://www.airbnb.com/rooms/14266442
https://www.airbnb.com/rooms/11476122
https://www.airbnb.com/rooms/10241021
https://www.airbnb.com/rooms/14068062
https://www.airbnb.com/rooms/13103786
https://www.airbnb.com/rooms/14742316
https://www.airbnb.com/rooms/14881091
https://www.airbnb.com/rooms/7727798
https://www.airbnb.com/rooms/15721465
https://www.airbnb.com/rooms/15227011
https://www.airbnb.com/rooms/14874823
https://www.airbnb.com/rooms/15507292
https://www.airbnb.com/rooms/8353634
https://www.airbnb.com/rooms/11669359
https://www.airbnb.com/rooms/15644899
https://www.airbnb.com/rooms/2582812
https://www.airbnb.com/rooms/15165794
https://www.airbnb.com/rooms/8984085
https://www.airbnb.com/rooms/13264899
https://www.airbnb.com/rooms/15337044
https://www.airbnb.com/rooms/14928089
https://www.airbnb.com/rooms/15006441
https://www.airbnb.com/rooms/14347194
https://www.airbnb.com/rooms/13480134
https://www.airbnb.com/rooms/1370405
https://www.airbnb.com/rooms/10232588
https://www.airbnb.com/rooms/7053496
https://www.airbnb.com/rooms/13374115
https://www.airbnb.com/rooms/15604323
https://www.airbnb.com/rooms/9885501
https://www.airbnb.com/rooms/13376594
https://www.airbnb.com/rooms/12774885
https://www.airbnb.com/rooms/15508468
https://www.airbnb.com/rooms/15725698
https://www.airbnb.com/rooms/15630359
https://www.airbnb.com/rooms/10272841
https://www.airbnb.com/rooms/13084465
https://www.airbnb.com/rooms/12071153
https://www.airbnb.com/rooms/15468538
https://www.airbnb.com/rooms/15593184
https://www.airbnb.com/rooms/15565466
https://www.airbnb.com/rooms/13892662
https://www.airbnb.com/rooms/10042625
https://www.airbnb.com/rooms/13157173
https://www.airbnb.com/rooms/12674883
https://www.airbnb.com/rooms/257568
https://www.airbnb.com/rooms/15782857
https://www.airbnb.com/rooms/14699186
https://www.airbnb.com/rooms/14340328
https://www.airbnb.com/rooms/15701695
https://www.airbnb.com/rooms/489965
https://www.airbnb.com/rooms/15725698
https://www.airbnb.com/rooms/15552862
https://www.airbnb.com/rooms/9648721
https://www.airbnb.com/rooms/12952364
https://www.airbnb.com/rooms/13264899
https://www.airbnb.com/rooms/14885186
https://www.airbnb.com/rooms/15800461
https://www.airbnb.com/rooms/648047
https://www.airbnb.com/rooms/13396536
https://www.airbnb.com/rooms/12158713
https://www.airbnb.com/rooms/11418938
https://www.airbnb.com/rooms/15589663
https://www.airbnb.com/rooms/15087383
https://www.airbnb.com/rooms/10245959
https://www.airbnb.com/rooms/9958610
https://www.airbnb.com/rooms/15537940
https://www.airbnb.com/rooms/13591923
https://www.airbnb.com/rooms/8972815
https://www.airbnb.com/rooms/14748150
https://www.airbnb.com/rooms/8720655
https://www.airbnb.com/rooms/11254989
https://www.airbnb.com/rooms/11543124
https://www.airbnb.com/rooms/15507292
https://www.airbnb.com/rooms/7515787
https://www.airbnb.com/rooms/3363890
https://www.airbnb.com/rooms/15782857
https://www.airbnb.com/rooms/15110299
https://www.airbnb.com/rooms/4988526
https://www.airbnb.com/rooms/15066466
https://www.airbnb.com/rooms/8686167
https://www.airbnb.com/rooms/14885186
https://www.airbnb.com/rooms/14238574
https://www.airbnb.com/rooms/12336668
https://www.airbnb.com/rooms/14263034
https://www.airbnb.com/rooms/15187898
https://www.airbnb.com/rooms/8843995
https://www.airbnb.com/rooms/8353634
https://www.airbnb.com/rooms/15227011
https://www.airbnb.com/rooms/14627817
https://www.airbnb.com/rooms/13334161
https://www.airbnb.com/rooms/7875162
https://www.airbnb.com/rooms/9532510
https://www.airbnb.com/rooms/11254989
https://www.airbnb.com/rooms/6603534
https://www.airbnb.com/rooms/5663222
https://www.airbnb.com/rooms/13039122
https://www.airbnb.com/rooms/11547967
https://www.airbnb.com/rooms/6576336
https://www.airbnb.com/rooms/14960623
https://www.airbnb.com/rooms/15338155
https://www.airbnb.com/rooms/8386220
https://www.airbnb.com/rooms/11476122
https://www.airbnb.com/rooms/14882397
https://www.airbnb.com/rooms/14366054
https://www.airbnb.com/rooms/13374115
https://www.airbnb.com/rooms/9667009
https://www.airbnb.com/rooms/4746336
https://www.airbnb.com/rooms/14572907
https://www.airbnb.com/rooms/12649685
https://www.airbnb.com/rooms/13142326
https://www.airbnb.com/rooms/14741560
https://www.airbnb.com/rooms/14913356
https://www.airbnb.com/rooms/13175146
https://www.airbnb.com/rooms/11711862
https://www.airbnb.com/rooms/13370088
https://www.airbnb.com/rooms/6603534
https://www.airbnb.com/rooms/8969269
https://www.airbnb.com/rooms/15205100
https://www.airbnb.com/rooms/3563271
https://www.airbnb.com/rooms/13912003
'''
#print(len(set(room_urls.split())))