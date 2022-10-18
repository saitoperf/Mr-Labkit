#!/bin/bash
/usr/sbin/service smbd start
/usr/sbin/service nmbd start

while true ; do
    /bin/bash    # 最後のプロセスはフォアグラウンドで起動
done
