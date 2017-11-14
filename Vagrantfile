Vagrant.configure("2") do |config|
  config.vm.box = "precise64"
  config.vm.define "assignment_final" do |assignment_final|
      assignment_final.vm.box_url = "http://files.vagrantup.com/precise64.box"
      assignment_final.vm.provision "shell", path: "provision.sh"
      assignment_final.vm.network "forwarded_port", guest: 80, host: 8080
      assignment_final.vm.network "forwarded_port", guest: 443, host: 8443
  end
end
