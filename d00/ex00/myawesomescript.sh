#!/bin/bash
curl -s $1 | grep http | cut -d '"' -f2
