#!usr/bin/env python
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt # MQTT のライブラリをインポート
import csv
import re

# ブローカーに接続できたときの処理
def on_connect(client, userdata, flag, rc):
    print("Connected with result code " + str(rc)) # 接続できた旨表⽰
    client.subscribe("RFID INFO") # sub するトピックを設定

# ブローカーが切断したときの処理
def on_disconnect(client, userdata, flag, rc):
    if rc != 0:
    	print("Unexpected disconnection.")
	
# メッセージが届いたときの処理
def on_message(client, userdata, msg):
    # msg.topic にトピック名が，msg.payload に届いたデータ本体が⼊っている
    msg_payload = msg.payload.decode("utf8")
    msg_qos = msg.qos
    print("Received message '" + msg_payload + "' on topic '" + str(msg.topic) + "' with QoS " + str(msg_qos))
    csv_write(msg_payload)

def csv_write(d):
    d = list(d.split(",")) 
    with open("data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(d)

# MQTT の接続設定
client = mqtt.Client() # クラスのインスタンス(実体)の作成
client.on_connect = on_connect # 接続時のコールバック関数を登録
client.on_disconnect = on_disconnect # 切断時のコールバックを登録
client.on_message = on_message # メッセージ到着時のコールバック
client.connect("localhost", 1883, 60) # 接続先は⾃分⾃⾝
client.loop_forever() # 永久ループして待ち続ける
