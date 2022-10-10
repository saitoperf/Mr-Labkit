#!/bin/bash

sudo virsh snapshot-revert --domain node103 --snapshotname geekten
sudo virsh snapshot-revert --domain node104 --snapshotname geekten
sudo virsh snapshot-revert --domain node100 --snapshotname geekten

sudo virsh start node103
sudo virsh start node104
sudo virsh start node100
