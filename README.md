# simple-slack-sender

```
#!/usr/bin/env python
#-*- coding: utf-8 -*-

import Slack

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
```
