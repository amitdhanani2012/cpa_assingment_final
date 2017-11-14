#!/usr/bin/env bash

echo "Shell script is starting"
apt-get update >/dev/null 
apt-get install -y apache2  
apt-get install -y build-essential libssl-dev libffi-dev python-dev memcached curl
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python get-pip.py
pip install pyopenssl --index-url=https://pypi.python.org/simple/
pip install flask --index-url=https://pypi.python.org/simple/
pip install python-memcached --index-url=https://pypi.python.org/simple/


#rm -rf /var/www
#ln -fs /vagrant /var/www
#mkdir /var/www/app
#echo "testing from app">/var/www/app/index.html
echo "<VirtualHost *:80>" > /etc/apache2/sites-available/default
echo "ServerAdmin webmaster@localhost">> /etc/apache2/sites-available/default
echo "DocumentRoot /var/www/">>/etc/apache2/sites-available/default
echo "RewriteEngine On">> /etc/apache2/sites-available/default
echo "RewriteCond %{HTTPS} off">>/etc/apache2/sites-available/default
echo "RewriteRule ^ https://localhost:8443%{REQUEST_URI}">>/etc/apache2/sites-available/default
echo "ErrorLog ${APACHE_LOG_DIR}/error.log">>/etc/apache2/sites-available/default
echo "CustomLog ${APACHE_LOG_DIR}/access.log combined">>/etc/apache2/sites-available/default
echo "</VirtualHost>" >> /etc/apache2/sites-available/default
a2ensite default
#a2ensite default-ssl
#a2enmod ssl
a2dismod ssl
a2enmod rewrite
service apache2 restart
service memcached start
cp /vagrant/flask_memcached_test_final.py /var/www/.
cp /vagrant/memcached_getter_setter_cron.py /root/.
cp /vagrant/memcached_getter_setter.py /root/.
cp /vagrant/memcached_getter_setter_check.py /root/.
 
chmod 550 /var/www/flask_memcaced_test_final.py
chmod 550 /root/memcached_getter_setter_cron.py
chmod 550 /root/memcached_getter_setter.py
chmod 550 /root/memcached_getter_setter_check.py

/usr/bin/python /root/memcached_getter_setter.py
echo "*/1 * * * * /usr/bin/python /root/memcached_getter_setter_cron.py" |tee -a /var/spool/cron/crontabs/root
chmod 600 /var/spool/cron/crontabs/root
service cron restart
/usr/bin/python /var/www/flask_memcached_test_final.py &
sed -i '/exit 0/d' /etc/rc.local
echo "service memcached start" >> /etc/rc.local
echo "service apache2 start">>/etc/rc.local
echo "/usr/bin/python /root/memcached_getter_setter.py" >> /etc/rc.local
echo "/usr/bin/python /var/www/flask_memcached_test_final.py &" >> /etc/rc.local
echo "exit 0">>/etc/rc.local
chmod u+x /etc/rc.local
update-rc.d  rc.local enable 2345

