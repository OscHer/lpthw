# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "generic/ubuntu2204" # Base box for our lab

  # Synced folder. Needed for ansible_local
  config.vm.synced_folder ".", "/vagrant"

  # Deploy host user public key to guest. 
  config.vm.provision "pubkey", type: "file", source: "~/.ssh/id_rsa.pub", destination: "/tmp/host-id_rsa.pub"

  # We don't want vagrant to install ansible a-la-vagrant
  # Intalling it the canonical way (pun intended)
  config.vm.provision "pre-shell", type: "shell", path: "provision/shell/pre-shell.sh"

  # Vagrant ssh options to have the environment closer to plug and play
  # May be later I'll ansibilize this.
  # config.ssh.forward_x11 = true # We need this to play mission python game

  # Ansible provision config
  # Ansible will be run from the guest, as in inception.
  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "provision/ansible/playbook.yml"
    ansible.verbose = "v"
  end
end
