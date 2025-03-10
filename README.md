# telegram_client_for_write_comments

#### P.S. Данный репозиторий создан для помощи всем беспомощным.

**Описание:**

У этого репозитория есть две папки ``check tg group`` и ``podpiska otpiska group``, которые по отдельности являются разными проектами, но вместе могут стать помошником в рекламе вашей тг группы. 

``podpiska otpiska group:`` принимает список групп телеграмм каналов, для которых проверяет возможность ``оставлять комментарии`` под постами. Если такая возможность есть, то скрипт подписывается на телеграмм канал, если комментарии закрыты телеграмм канал уходил в ``blacklist``. Затем с помощью ``grep`` фильтруем каналы и создаем эталонный список телеграмм групп.

``check tg group:`` принимает эталонный список групп телеграмм, на которые уже подписан телеграмм аккаунт. Мониторит каналы в реальном времени и оставляет комментарии по вашему списку-желаний. Может подключить AI для составлений комментаий, чтобы они были уникальны, но в данном проекте мне это не интересно.

Детально описание работ представлено в соответствующих директориях.

*Python 3.12*
*requirements.txt:*
```txt
asyncio
random
time
os
pysqlite3-binary 0.5.4
Telethon         1.38.1
```

#### For questions or helping (The Open Network min 10 ton):
UQBBBT6BBGuxxDFK96Yj80nfg7QjIJ-mu3cCGn0wl1sTnlti
