# Lab for Learn Python the Hard Way

## Introduction
This repository contains (but not limited to) the exercises for the amazing book "Learn Python the Hard Way" by Zed A. Shaw. The exercises are organized in folders, one for each exercise. The folders contain the files with the code for the exercises.

### Disclaimer
The code in this repository isn't the original code from the book. It's my own code,
which I wrote while following the book. The code may contain errors, and it may not be the best way to solve the exercises.

You may also find some additional files in the folders that are not part of the book.
These files are there to help me understand the exercises better or even try different things for my own learning 
experience; so expect to find inconsistencies or even errors in the code.

## How to use this repository
1. Clone the repository:`git clone https://github.com/OscHer/lpthw.git`
2. Change to the directory: `cd lpthw`
3. Get the environment up: `vagrant up`

Under the hood, the Vagrantfile defines a virtual machine with with the necessary dependencies to run the code
in this repository.
To solve the dependencies and get the environment provisioned and configured I decided to go with provisioning scripts
in a Dockerfile-like way. The provisioning scripts are in the `provision` directory and are applied layer by layer 
to the base image defined in the Vagrantfile in this order:
1. [bootstrap](provision/shell/bootstrap.sh): My own bootstrap script to install my favorite tools and dependencies.
2. [python-bootstrap](provision/shell/bootstrap-python.sh): Install Python dependencies. 
3. [vimrc]: My own vim configuration file. #TODO: Add the vimrc file and other dodfiles.
4. [src](src): The source code for the exercises and other projects.

   Since this project was originaly intended for [Libvirt/KVM](https://libvirt.org/) I decided to go with the nfs 4 syncing strategy since it fitted my needs better than the default syncing strategy.




### Dependencies
- [Vagrant](https://www.vagrantup.com/)
- [Libvirt](https://libvirt.org/) is my choice but you can also use:
- [VirtualBox](https://www.virtualbox.org/) or other virtualization software supported by Vagrant
- [Vagrant libvirt plugin](https://vagrant-libvirt.github.io/vagrant-libvirt/installation.html) if you go with Libvirt
- [Git](https://git-scm.com/)

## Appendix
### TO-DO
- [] Add Dotfiles
- [] Add How-to get the full lab up and running

### About the author
Óscar Heredia
[GitHub](https://github.com/oscher)
### Bibliography and references
* [Learn Python the Hard Way](https://learnpythonthehardway.org/book/)
* [Learn Python the Hard Way GitHub repository](https://github.com/zedshaw/learn-python3-thw-code)
* [Zed A. Shaw](https://zedshaw.com/)
* [Learn more Python the hard way GitHub repository](https://github.com/zedshaw/learn-more-python-the-hard-way-solutions)
* [Other Learn X the Hard Way](https://learncodethehardway.org/)
* [Other Zed Shaw's books](https://www.informit.com/imprint/series_detail.aspx?ser=3511331)
