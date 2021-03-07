# WeatherStation

This is my setup for pulling data from the Acurite 5-in-1 weather station.

The C code to interface with the weather station is copied from https://github.com/draythomp/Desert-Home-RPi and has no modifications (at this point).

The rest of the code has been implemented to suit my needs. 

## Prerequisites

* Add `10-local.rules` to `/etc/udev/rules.d/` and reboot
* Ensure you have `libudev-dev` and `bzip2` installed
  ``` sh
  sudo apt install libudev-dev bzip2 -y
  ```
* Download libusb-1.0.19 from [here](http://downloads.sourceforge.net/libusb/libusb-1.0.19.tar.bz2), build and install it
  ``` sh
  tar jxf libusb-1.0.19.tar.bz2
  cd libusb-1.0.19
  ./configure
  make
  sudo make install
  ```
* Create MySQL or MariaDB database and database user to store the data (can be local or remote database)
* Run the SQL statements in `create_tables.sql` on that database

## Installation

* make
* cp env.sample .env
* Modify .env for your database environment
* pip install dotenv-python mysql-connector

## Run

* ./weatherstation 2>weatherstation.log | python writetodb.py
