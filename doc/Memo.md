# メモ
- `src/files/nfs/exports`で`no_root_squash`を指定する必要がある
    - nfsマウント後にクライアントにansible playbookを実行すると、gathering factsで落ちる
    - ホームディレクトリを作る場合は、サーバPCで最初にログインする必要があったが、これを記述するとクライアントでのログインでもOK

- [dns関係](https://qiita.com/shora_kujira16/items/31d09b373809a5a44ae5)

## 変更履歴
- 1/23
  - kubeadm, kubelet, kubectlのバージョンを1.23.1に固定
  - これに伴いansibleのversionを2.12.3に更新