#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: /do-construct-rs.py
# Created Date: Thursday, October 22nd 2020, 4:26:28 pm
# Author: Christian Perwass
# <LICENSE id="Apache-2.0">
#
#   Image-Render Standard Actions module
#   Copyright 2022 Robert Bosch GmbH and its subsidiaries
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# </LICENSE>
###

from catharsys.config.cls_config_list import CConfigList
from catharsys.plugins.std.action_class.manifest.cls_cfg_manifest_job import (
    CConfigManifestJob,
)


################################################################################
# Return action definition
def GetDefinition():
    return {
        "sDTI": "/catharsys/action-class/python/manifest-based:2.0",
        "sActionDTI": "/catharsys/action/std/blender/post-render/proc-label:1.0",
        "sExecuteDTI": "exec/python/*:*",
        "sProjectClassDTI": "/catharsys/project-class/std/blender/render:1.0",
        "sJobDistType": "frames;configs",
        "mArgs": {
            "iFrameFirst": {"sType": "int", "xDefault": 0},
            "iFrameLast": {"sType": "int", "xDefault": 0},
            "iRenderQuality": {"sType": "int", "xDefault": 4, "bOptional": True},
            "iConfigGroups": {"sType": "int", "xDefault": 1, "bOptional": True},
            "iFrameGroups": {"sType": "int", "xDefault": 1, "bOptional": True},
            "bDoProcess": {"sType": "bool", "xDefault": True, "bOptional": True},
        },
    }


# enddef


################################################################################
def ResultData(xJobCfg: CConfigManifestJob):
    from .lib.cls_label_result_data import CLabelResultData

    return CLabelResultData(xJobCfg=xJobCfg)


# enddef


################################################################################
# Call actual action from separate file, to avoid importing all modules
# when catharsys obtains the action definition.
def Run(_xCfg: CConfigList) -> None:
    from .lib.cls_construct_label import CConstructLabel
    from anybase import assertion

    assertion.FuncArgTypes()

    xConstruct = CConstructLabel()

    def Process(_xConstruct: CConstructLabel):
        def Lambda(_xPrjCfg, _dicCfg, **kwargs):
            _xConstruct.Process(_xPrjCfg, _dicCfg, kwargs=kwargs)

        # enddef
        return Lambda

    # enddef

    _xCfg.ForEachConfig(Process(xConstruct))


# enddef
