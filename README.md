# Mr-Labkit
- 2022年9月10日 技育展 インフラセ/キュリティ 発表作品
- [プレゼン資料](https://docs.google.com/presentation/d/1S5N9mMJPrSEZmwhkFLieLZNFTAQOk1g5)
- [ver1](https://github.com/saitoperf/mini-lab)

## Quick Start
```sh
git clone https://github.com/saitoperf/Mr-Labkit.git
cd Mr-Labkit
./install.sh
```
- ターゲットノードは，Python3がインストールされていることと，公開鍵接続出来ることが前提
- 変数をいじるファイルは以下(そのうち自動化したい)
    - inv.ini
    - vars.yml
        - `serverip`をサーバのIPアドレスにご変更ください
    - files/nfs/exports
        - `192.168.122.0/255.255.255.0`を公開するセグメントにご変更ください
    - files/prometheus/server/prometheus.yml
        - `target`をご変更ください

- `ServerIP:8080`でLDAPの管理画面にアクセス出来ます
    - Login DN：cn=admin,dc=example,dc=com
    - Password：admin

## 注意！
- nfsはまだコンテナ化されていません！(aptコマンドが使えるディストリビューションでのみ実行可能)

## 今後の予定
- nfsのコンテナ化 or playbook内でディストリビューションごとに分岐できるようにする
- GitLabコンテナを立ててLDAP認証出来るようにする
- terraformを用いたAWSへのデプロイ

## お問い合わせ
- メール：d203326@gmail.com
