# -*- mode: ruby -*-
# vi: set ft=ruby :

BASE_BOX = "bento/ubuntu-24.04"
Vagrant.configure("2") do |config|
  config.vm.box = BASE_BOX

  config.vm.provision "bootstrap", type: "shell", path: "provision/shell/bootstrap.sh"
  config.vm.provision "python-bootstrap", type: "shell", path: "provision/shell/python-bootstrap.sh"
  config.vm.provision "file", source: "~/.vimrc", destination: "/home/vagrant/.vimrc"
  config.vm.synced_folder "~/.vim", "/home/vagrant/.vim"
  config.vm.synced_folder "src/", "/opt/", type: "nfs", nfs_version: 4, nfs_udp: false
end
