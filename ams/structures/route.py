#!/usr/bin/env python
# coding: utf-8

from ams.structures import get_base_class

template = {
    "start_waypoint_id": "0",
    "goal_waypoint_id": "1",
    "arrow_codes": ["0_1"]
}

'''
route_code = "[start_waypoint_id]:[joined_arrow_codes]:[goal_waypoint_id]"
routes = {
    route_code: route,
}
'''

schema = {
    "start_waypoint_id": {
        "type": "string",
        "required": True,
        "nullable": False,
    },
    "goal_waypoint_id": {
        "type": "string",
        "required": True,
        "nullable": False,
    },
    "arrow_codes": {
        "type": "list",
        "required": True,
        "nullable": False,
        "minlength": 1
    }
}


class Route(get_base_class(template, schema)):
    pass
