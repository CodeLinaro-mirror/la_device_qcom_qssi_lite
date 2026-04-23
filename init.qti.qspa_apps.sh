#! /system/bin/sh
#
# Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
# SPDX-License-Identifier: BSD-3-Clause-Clear
#

soc_id=`cat /sys/devices/soc0/soc_id` 2> /dev/null

if [ "$soc_id" -eq 554 ] || [ "$soc_id" -eq 739 ]; then
    setprop ro.vendor.config.qspa.apps true
elif [ "$soc_id" -eq 579 ] || [ "$soc_id" -eq 740 ]; then
    setprop ro.vendor.config.qspa.apps false
fi
