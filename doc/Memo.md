# メモ
- `src/files/nfs/exports`で`no_root_squash`を指定する必要がある
    - nfsマウント後にクライアントにansible playbookを実行すると、gathering factsで落ちる