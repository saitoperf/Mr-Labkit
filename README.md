# Mr-Labkit
- 2022年9月10日／技育展／インフラ・セキュリティテーマ／発表作品
    - [優秀賞受賞ページ](https://talent.supporterz.jp/geekten/2022/exhibition.html#theme3)
    - [Youtube](https://www.youtube.com/watch?v=LOkjSkE-tF0&feature=youtu.be)
    - [前作品(技育キャンプ)](https://github.com/saitoperf/mini-lab)

## Quick Start
```sh
git clone https://github.com/saitoperf/Mr-Labkit.git
cd Mr-Labkit/src
./install.sh
```
- 前提条件：
    - ターゲットノードにPython3がインストールされていること
    - 公開鍵接続が出来ること
- 変数をいじるファイルは以下(jinja2等を使ってそのうち自動化したい)
    - src/inv.ini
    - src/vars.yml
        - `serverip`をサーバのIPアドレスにご変更ください
    - src/files/nfs/exports
        - `192.168.122.0/255.255.255.0`を公開するセグメントにご変更ください
    - src/files/prometheus/server/prometheus.yml
        - `target`をご変更ください
    - src/files/gitlab/docker-compose.yml
    
- 各種サービスへのアクセス(ServerIPはそのうちドメインで指定できるようにしたい)
    - `ServerIP:8080`：LDAP管理画面
        - Login DN：cn=admin,dc=example,dc=com
        - Password：admin
    - `ServerIP:8929`：GitLab
        - 初期のユーザ名とパスワードは[こちら](https://docs.gitlab.com/ee/install/docker.html#install-gitlab-using-docker-engine)をご参照ください
        - Username or email：root
        - Password：`docker exec -it gitlab grep 'Password:' /etc/gitlab/initial_root_password`
    - `ServerIP:3000`：Grafana
        - Email or username：admin
        - Password：admin
    - `ServerIP:9090`：Prometheus

## 注意！
- nfsはまだコンテナ化されていません！(aptコマンドが使えるディストリビューションでのみ実行可能)

## 今後の予定
- nfsのコンテナ化 or playbook内でディストリビューションごとに分岐できるようにする
- GitLabコンテナを立ててLDAP認証出来るようにする
- jinja2を使って設定ファイル内のIPアドレスを変数化する
- Latexの自動ビルド機能の追加(CIパイプラインの作成)
- 

## お問い合わせ
- メール：d203326@gmail.com
