#半径租房（杭州地铁版）
import re
from urllib.request import urlopen

#origin = input("请输入原点");#建业路
#radius = input("请输入可接受通勤时间");#30min

#遍历线路获取各站点
subway = [1];#地铁线路 ,2,4,5,6,7,8,9,16
s = r'<li><a target="_blank" href="http://quote.eastmoney.com/\S\S(.*?).html">'
s = r'<li class="ser_3_listli">九和路站</li><li class="ser_3_listli2">';
matching = re.compile(s);
for id in subway:
    subwayUrl = "http://www.hzmetro.com/build_SiteInfo.aspx?Id={}#midc".format(id);
    subwayUrlContent = urlopen(subwayUrl).read().decode('utf-8');
    station = matching.findall(subwayUrlContent);
