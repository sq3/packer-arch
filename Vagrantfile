# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "arch-virtualbox.box"
  config.vm.provider "virtualbox" do |v|
    v.name = "arch"
    v.linked_clone = true
    v.memory = "512"
    v.cpus = 2
  end
end

