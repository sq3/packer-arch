Packer Arch
===========

Packer Arch is a bare bones [Packer](https://www.packer.io/) template and
installation script that can be used to generate a [Vagrant](https://www.vagrantup.com/)
base box for [Arch Linux](https://www.archlinux.org/).

Overview
--------

* 64-bit
* 12 GB disk
* 512 MB memory
* Only a single /root partition (ext4)
* No swap
* Includes the `base` and `base-devel` package groups
* OpenSSH is also installed and enabled on boot

The installation script follows the
[official installation guide](https://wiki.archlinux.org/index.php/Installation_Guide)
pretty closely, with a few tweaks to ensure functionality within a VM. Beyond
that, the only customizations to the machine are related to the vagrant user
and the steps recommended for any base box.

Usage
-----

### VirtualBox Provider

Assuming that you already have [Packer](https://www.packer.io/),
[VirtualBox](https://www.virtualbox.org/), and
[Vagrant](https://www.vagrantup.com) installed, you
should be good to clone this repo and go:

    $ git clone https://github.com/sq3/packer-arch.git
    $ cd packer-arch/
    $ packer build template.json

Then you can import the generated box into Vagrant:

    $ vagrant box add arch builds/_arch_virtualbox.box

You can run update-iso-url.py to get the URL of the latest ArchLinux
.iso verion to template.json. It automatically adds, commits and pushs
the changes for continuous integration e.g. via travis
License
-------

Packer Arch is provided under the terms of the
[ISC License](https://en.wikipedia.org/wiki/ISC_license).

Copyright &copy; 2013&#8211;2016, [Aaron Bull Schaefer](mailto:aaron@elasticdog.com).
