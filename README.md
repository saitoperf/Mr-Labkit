# Mr-Labkit
- 2022年9月10日／技育展／インフラ・セキュリティテーマ／発表作品
    - [優秀賞受賞ページ](https://talent.supporterz.jp/geekten/2022/exhibition.html#theme3)
    - [Youtube](https://www.youtube.com/watch?v=LOkjSkE-tF0&feature=youtu.be)
    - [前作品(技育キャンプ)](https://github.com/saitoperf/mini-lab)

## Quick Start
```sh
git clone https://github.com/saitoperf/Mr-Labkit.git
cd Mr-Labkit/src
# vars.yml を編集した後に実行してください
```
```sh
# venvの設定
python3 -m venv venv
source venv/bin/activate
pip install ansible-core==2.12.3
```
```sh
./run.sh generate
# vagrantを使ってVMを準備します
./run.sh vagrant
# ベアメタルのサーバを構築します
./run.sh baremetal
# k8sクラスタを構築します
./run.sh k8s-create
```
- 事前準備：
    - `src/vars.yml`を編集してください

## アクセス
- ブラウザで、`src/vars.yml`に記述したリバースプロキシのIPアドレスを指定してください

## 各種サービスの初期ユーザ名とパスワード
<!-- - (ServerIPはそのうちドメインで指定できるようにしたい) -->
- 
- LDAP管理画面
    - Login DN：cn=admin,dc=example,dc=com
    - Password：admin
- GitLab
    - ルートユーザ名とパスワードは[こちら](https://docs.gitlab.com/ee/install/docker.html#install-gitlab-using-docker-engine)をご参照ください
        - Username：root
        - Password：`docker exec -it gitlab grep 'Password:' /etc/gitlab/initial_root_password`
    - テスト用のLDAPユーザを使う場合
        - Username：user01
        - Password：user01
- Grafana
    - Email or username：admin
    - Password：admin
- Prometheus

## 注意！
- nfsはまだコンテナ化されていません！(aptコマンドが使えるディストリビューションでのみ実行可能)
    - ubuntu20.04でのみ動作確認

## 今後の予定
- nfsのコンテナ化 or playbook内でディストリビューションごとに分岐できるようにする
- GitLabコンテナで、LDAP認証出来るようにする
- Latexの自動ビルド機能の追加(CIパイプラインの作成)
- VPN機能
- DNS機能

## お問い合わせ
- メール：d203326@gmail.com
- コメント大歓迎です！お気軽にどうぞ！
