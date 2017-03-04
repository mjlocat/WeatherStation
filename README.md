# WeatherStation

This is my setup for pulling data from the Acurite 5-in-1 weather station.

The C code to interface with the weather station is copied from https://github.com/draythomp/Desert-Home-RPi and has no modifications (at this point).

The rest of the code has been implemented to suit my needs. 

## Installation

* TODO: Add build dependencies
* TODO: Add instructions for USB library
* make
* cp env.sample .env
* Modify .env for your environment
* pip install dotenv-python mysql-connector

## Run

* ./weatherstation 2>weatherstation.log | writetodb.py
