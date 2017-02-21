#!/usr/bin/env python

from __future__ import print_function
from sqlalchemy import create_engine, Column, Integer, Float, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import json
import subprocess
import re
import time
# Set constants
DIRECTORY = os.path.dirname(os.path.realpath(__file__))

DOWNLOAD_RE = re.compile(r"Download: ([\d.]+) .bit")
UPLOAD_RE = re.compile(r"Upload: ([\d.]+) .bit")
PING_RE = re.compile(r"([\d.]+) ms")


Base = declarative_base()
# Load config file
with open(os.path.join(DIRECTORY, "config.json"), "r") as configfile:
    config = json.load(configfile)

#Create da engine
engine = create_engine('mysql+cymysql://%s:%s@%s/%s' % (config["username"], config["password"], config["host"], config["database"]), echo=True)
#Speedtest class
class Speedtest(Base):
    __tablename__ = 'speedtest'
    id = Column(Integer, primary_key=True)
    download = Column(Float)
    upload = Column(Float)
    ping = Column(Float)
    created_at = Column(TIMESTAMP)

#S'more sqlalchemy stuff
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
#Insert the results in the database
def mysql_stuff(ping, download, upload):
    speedtest = Speedtest(download=download, upload=upload, ping=ping)
    s = session()
    s.add(speedtest)
    s.commit()
    return

# Main function to run speedtest
def main():
    # Check for proper credentials

    # Run speedtest and store output
    print("Starting speed test ... ")
    speedtest_result = subprocess.check_output(["speedtest-cli"], stderr=subprocess.STDOUT)
    print("Starting speed finished!")

    # Find download bandwidth
    download = DOWNLOAD_RE.search(str(speedtest_result)).group(1)
    # Find upload bandwidth
    upload = UPLOAD_RE.search(str(speedtest_result)).group(1)
    # Find ping latency
    ping = PING_RE.search(str(speedtest_result)).group(1)

    # Write to spreadsheet
    mysql_stuff(ping, download, upload)

if __name__ == "__main__":
    main()
