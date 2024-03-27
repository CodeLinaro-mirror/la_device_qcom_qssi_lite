# Copyright (c) 2024 Qualcomm Innovation Center, Inc. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause-Clear

FAILED_FILEPATHS_WHITELIST = {
}

SHELL_WHITELIST = {
    "device/qcom/sepolicy/SEPolicy.mk",
}

RM_WHITELIST = {
    "vendor/qcom/proprietary/common/scripts/Android.mk",
}

LOCAL_COPY_HEADERS_WHITELIST = {}

DATETIME_WHITELIST = {}

TARGET_PRODUCT_WHITELIST = {
    "vendor/qcom/opensource/core-utils/build/AndroidBoardCommon.mk",
    "vendor/qcom/opensource/core-utils/build/build.sh",
    "vendor/qcom/opensource/core-utils/build/build_image_standalone.py",
}

RECURSIVE_WHITELIST = {}

KERNEL_WHITELIST = {}

FOREACH_WHITELIST = {
    "vendor/qcom/opensource/core-utils/build/utils.mk",
    "vendor/qcom/proprietary/common/config/device-vendor-qssi.mk",
    "vendor/qcom/proprietary/common/config/device-vendor-SDM845-pureAOSP.mk",
    "vendor/qcom/proprietary/common-noship/build/generate_extra_images_prop.mk",
}

MACRO_WHITELIST = {
    "device/qcom/sepolicy/SEPolicy.mk",
    "vendor/qcom/opensource/commonsys/display/config/display-product-commonsys.mk",
    "vendor/qcom/proprietary/common-noship/etc/device-vendor-noship-SDM845-pureAOSP.mk",
    "vendor/qcom/proprietary/common-noship/etc/device-vendor-noship.mk",
    "vendor/qcom/proprietary/common-noship/etc/device-vendor-qssi-noship.mk",
    "vendor/qcom/proprietary/common/config/device-vendor-SDM845-pureAOSP.mk",
    "vendor/qcom/proprietary/common/config/device-vendor-qssi.mk",
    "vendor/qcom/proprietary/commonsys-intf/data/dpm_system_product_noship.mk",
    "vendor/qcom/proprietary/commonsys/telephony-build/build/telephony_system_product.mk",
}

OVERRIDE_WHITELIST = {
    "device/qcom/qssi_lite/qssi_lite.mk",
    "device/qcom/qssi_lite/qssi_whitelist.mk",
}

SOONG_WHITELIST = {
    "device/qcom/qssi_lite/base.mk",
    "vendor/qcom/opensource/commonsys/display/config/display-product-commonsys.mk",
    "vendor/qcom/proprietary/commonsys-intf/bluetooth/bt-system-proprietary-product.mk",
}
