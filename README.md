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
- 変数をいじるファイルは以下
    - inv.ini
    - vars.yml
    - files/nfs/exports
    - files/prometheus/server/prometheus.yml


## メモ
- prometheusのデプロイはまだです！
- nfsはまだコンテナ化されていません！(aptコマンドが使えるディストリビューションでのみ実行可能)