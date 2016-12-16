#!/bin/bash
systemctl disable podm-scheduler podm-concrete podm-versioner podm-alarm podm-alarmagent podm-api
systemctl stop podm-scheduler podm-concrete podm-versioner podm-alarm podm-alarmagent podm-api
