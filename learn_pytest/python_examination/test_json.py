# test_json.py
# coding: utf-8
import json

filename='/home/real/ads1/test6/producer_release/zhuluoji_json.cfg'
myfile = open(filename,'r')
# json_data ={"persons":[{"personId":"def151d4-4fd7-4c81-b16a-cec8f8222e3e","name":"chris","description":"female character"}],"host":"10.10.51.237","authorization":"person100","similarscore":0.8,"frame_interval":10,"seek_interval_items":1000}
json_data = json.load(myfile)
print json_data["persons"][0]["name"]
myfile.close()