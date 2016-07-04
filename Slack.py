#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
import json
import urllib
import sys
sys.dont_write_bytecode = True

class Slack():
  def __init__(self):
    self._webhookUrl = ''
    self._text = ''
    self._channel = ''
    self._username = ''
    self._iconEmoji = ''
    self._attachments = []

  def setConfig(self, webhookUrl, channel, username, iconEmoji = ':monkey_face:'):
    self._webhookUrl = webhookUrl
    self._channel = channel
    self._username = username
    self._iconEmoji = iconEmoji

  def setText(self, text):
    self._text = text

  def send(self):
    payload = json.dumps(self._build())
    resp = requests.post(url = self._webhookUrl, data = payload)
    return resp

  def _build(self):
    payload = {}
    payload['channel'] = self._channel
    payload['username'] = self._username
    payload['icon_emoji'] = self._iconEmoji
    payload['text'] = self._text
    return payload

if __name__ == '__main__':
  slack = Slack()
  slack.setConfig(
    webhookUrl = 'https://hooks.slack.com/services/XXXXXX/YYYYYY/ZZZZZZ',
    channel = '#channel-name',
    username = 'SimpleBot'
  )
  slack.setText('Hi')
  resp = slack.send()
  print(resp)