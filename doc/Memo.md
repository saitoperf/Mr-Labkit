# メモ
- `src/files/nfs/exports`で`no_root_squash`を指定する必要がある
    - nfsマウント後にクライアントにansible playbookを実行すると、gathering factsで落ちる
    - ホームディレクトリを作る場合は、サーバPCで最初にログインする必要があったが、これを記述するとクライアントでのログインでもOK
