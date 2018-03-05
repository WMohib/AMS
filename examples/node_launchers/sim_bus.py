#!/usr/bin/env python
# coding: utf-8

from time import time
import random
from argparse import ArgumentParser
from uuid import uuid1 as uuid

from ams import Waypoint, Arrow, Route, Intersection, Schedule, Target
from ams.nodes import SimBus

from pprint import PrettyPrinter
pp = PrettyPrinter(indent=2).pprint


parser = ArgumentParser()
parser.add_argument("-H", "--host", type=str, default="localhost", help="host")
parser.add_argument("-P", "--port", type=int, default=1883, help="port")
parser.add_argument("-ID", "--id", type=str, default=None, help="node id")
parser.add_argument("-N", "--name", type=str, default="sim_bus 1", help="name")
parser.add_argument("-W", "--path_waypoint_json", type=str,
                    default="../../res/waypoint.json", help="waypoint.json path")
parser.add_argument("-A", "--path_arrow_json", type=str,
                    default="../../res/arrow.json", help="arrow.json path")
parser.add_argument("-I", "--path_intersection_json", type=str,
                    default="../../res/intersection.json", help="intersection.json path")
parser.add_argument("-WID", "--start_waypoint_id", type=str,
                    default=None, help="start waypoint id")
parser.add_argument("-RID", "--circular_route_id", type=str,
                    default=None, help="circular route id")
args = parser.parse_args()


if __name__ == '__main__':

    waypoint = Waypoint()
    waypoint.load(args.path_waypoint_json)

    arrow = Arrow(waypoint)
    arrow.load(args.path_arrow_json)

    route = Route()
    route.set_waypoint(waypoint)
    route.set_arrow(arrow)

    intersection = Intersection()
    intersection.load(args.path_intersection_json)

    stop_waypoint_ids = [
        "8910", "8911", "8912", "8913", "8914", "8915", "8916", "8917", "8918", "8919", "8920", "8921", "8922", "8923",
        "8924", "8925", "8926",
        "9362", "9363", "9364", "9365", "9366", "9367", "9368", "9369", "9370", "9371", "9372", "9373", "9374", "9375",
        "9376", "9377",
        "8883", "8884", "8885", "8886", "8887", "8888", "8889", "8890", "8891", "8892", "8893", "8894", "8895", "8896",
        "8897",
        "9392", "9393", "9394", "9395", "9396", "9397", "9398", "9399", "9400", "9401", "9402", "9403", "9404",
        "10350", "10351", "10352", "10353", "10354", "10355", "10356", "10357", "10358", "10359", "10360", "10361",
        "10362", "10363", "10364", "10365", "10366", "10367", "10368", "10369", "10370", "10371", "10372", "10373",
        "10374",
        "9697", "9698", "9699", "9700", "9701", "9702", "9703", "9704", "9705", "9706", "9707", "9708",
        "8936", "8937", "8938", "8939", "8940", "8941", "8942", "8943", "8944", "8945", "8946", "8947", "8948", "8949",
        "8950", "8951", "8952", "8953", "8954", "8955", "8956", "8957", "8958", "8959", "8960", "8961", "8962", "8963",
        "8964", "8965", "8966", "8967", "8968",
    ]
    start_waypoint_id = args.start_waypoint_id
    if start_waypoint_id is None:
        start_waypoint_id = random.choice(stop_waypoint_ids)
    start_arrow_code = arrow.get_arrow_codes_from_waypoint_id(start_waypoint_id)[0]
    current_time = time()

    sim_bus = SimBus(
        _id=args.id if args.id is not None else str(uuid()),
        name=args.name,
        waypoint=waypoint,
        arrow=arrow,
        route=route,
        intersection=intersection,
        dt=0.5
    )
    sim_bus.set_waypoint_id_and_arrow_code(start_waypoint_id, start_arrow_code)
    sim_bus.set_velocity(3.0)
    sim_bus.set_schedules([Schedule.new_schedule(
        [Target.new_node_target(sim_bus)],
        SimBus.CONST.SCHEDULE.STAND_BY, current_time, current_time + 86400,
        Route.new_point_route(start_waypoint_id, start_arrow_code)
    )])
    sim_bus.start(host=args.host, port=args.port)
