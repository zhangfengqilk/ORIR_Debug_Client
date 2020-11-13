import grpc
from . import AvicRobotInterface_pb2
from . import AvicRobotInterface_pb2_grpc


class AvicRobotClient:
    def __init__(self):
        self.channel = None
        self.stub = None
        pass

    def connect(self, target='192.168.1.120:10000'):
        # 连接 rpc 服务器
        self.channel = grpc.insecure_channel(target)
        # 调用 rpc 服务
        self.stub = AvicRobotInterface_pb2_grpc.AvicRobotInterfaceStub(self.channel)
        pass

    def ptz_get_version(self) -> str:
        """

        :rtype:
        """
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            return self.stub.ptz_get_version(void).value
        except Exception as e:
            print(e)


    def ptz_left_arm_down(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            return self.stub.ptz_left_arm_up(void)
        except Exception as e:
            print(e)

    def ptz_turn_left(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            return self.stub.ptz_turn_left(void)
        except Exception as e:
            print(e)

    def ptz_turn_right(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            return self.stub.ptz_turn_right(void)
        except Exception as e:
            print(e)

    def ptz_turn_up(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            return self.stub.ptz_turn_up(void)
        except Exception as e:
            print(e)

    def ptz_turn_down(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            return self.stub.ptz_turn_down(void)
        except Exception as e:
            print(e)

    def ptz_set_bearing_value(self, p):
        try:
            param = AvicRobotInterface_pb2.integer_rpc()
            param.value = p
            return self.stub.ptz_set_bearing_value(param)
        except Exception as e:
            print(e)

    def ptz_set_pitching_value(self, p):
        try:
            param = AvicRobotInterface_pb2.integer_rpc()
            param.value = p
            return self.stub.ptz_set_pitching_value(param)
        except Exception as e:
            print(e)

    def ptz_get_bearing_val(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.ptz_get_bearing_val(void)
            return ret.value
        except Exception as e:
            print(e)

    def ptz_get_pitching_val(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.ptz_get_pitching_val(void)
            return ret.value
        except Exception as e:
            print(e)

    def ptz_get_pitching_val(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.ptz_get_pitching_val(void)
            return ret.value
        except Exception as e:
            print(e)

    def ptz_left_arm_up(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.ptz_left_arm_up(void)
            return ret
        except Exception as e:
            print(e)

    def ptz_left_arm_down(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.ptz_left_arm_down(void)
            return ret
        except Exception as e:
            print(e)

    def ptz_right_arm_up(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.ptz_right_arm_up(void)
            return ret
        except Exception as e:
            print(e)

    def ptz_right_arm_down(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.ptz_right_arm_down(void)
            return ret
        except Exception as e:
            print(e)

    def ptz_set_left_arm_pitch(self, p):
        try:
            param = AvicRobotInterface_pb2.integer_rpc()
            param.value = p
            ret = self.stub.ptz_set_left_arm_pitch(param)
            return ret
        except Exception as e:
            print(e)

    def ptz_set_right_arm_pitch(self, p):
        try:
            param = AvicRobotInterface_pb2.integer_rpc()
            param.value = p
            ret = self.stub.ptz_set_right_arm_pitch(param)
            return ret
        except Exception as e:
            print(e)

    def ptz_get_left_arm_pitch(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.ptz_get_left_arm_pitch(void)
            return ret
        except Exception as e:
            print(e)

    def ptz_get_right_arm_pitch(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.ptz_get_right_arm_pitch(void)
            return ret
        except Exception as e:
            print(e)

    def ptz_is_inplace(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.ptz_is_inplace(void)
            return ret
        except Exception as e:
            print(e)

    def ptz_stop(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.ptz_stop(void)
            return ret
        except Exception as e:
            print(e)

    def ptz_set_positioning_speed(self, p):
        try:
            param = AvicRobotInterface_pb2.integer_rpc()
            param.value = p
            ret = self.stub.ptz_set_positioning_speed(param)
            return ret
        except Exception as e:
            print(e)

    def ptz_get_speed(self):
        try:
            ret = self.stub.ptz_get_speed()
            return ret.value
        except Exception as e:
            print(e)

    def ptz_set_positioning_speed(self):
        try:
            ret = self.stub.ptz_get_speed()
            return ret.value
        except Exception as e:
            print(e)

    def ptz_power_on(self):
        try:
            ret = self.stub.ptz_power_on
            return ret
        except Exception as e:
            print(e)

    def ptz_power_off(self):
        try:
            ret = self.stub.ptz_power_off
            return ret
        except Exception as e:
            print(e)

    def ptz_set_headlamp_on(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.ptz_set_headlamp_on(void)
            return ret
        except Exception as e:
            print(e)

    def ptz_set_headlamp_off(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.ptz_set_headlamp_off(void)
            return ret
        except Exception as e:
            print(e)

    def ptz_self_test(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.ptz_self_test(void)
            return ret
        except Exception as e:
            print(e)

    def pd_is_inplace(self):
        try:
            p = AvicRobotInterface_pb2.void_rpc
            ret = self.stub.pd_is_inplace(p)
            return ret
        except Exception as e:
            print(e)

    def pd_power_off(self):
        try:
            p = AvicRobotInterface_pb2.void_rpc
            ret = self.stub.pd_power_off(p)
            return ret
        except Exception as e:
            print(e)

    def pd_power_on(self):
        try:
            p = AvicRobotInterface_pb2.void_rpc
            ret = self.stub.pd_power_on(p)
            return ret
        except Exception as e:
            print(e)

    def pd_set_position(self):
        try:
            p = AvicRobotInterface_pb2.integer_rpc
            p.value = 100
            ret = self.stub.pd_set_position(p)
            return ret
        except Exception as e:
            print(e)

    def pd_get_position(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.pd_get_position(void)
            return ret
        except Exception as e:
            print(e)

    def pd_ultrasonic_basic_get(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.pd_ultrasonic_basic_get(void)
            return ret
        except Exception as e:
            print(e)

    def pd_ultrasonic_prpd_get(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.pd_ultrasonic_prpd_get(void)
            return ret
        except Exception as e:
            print(e)

    def pd_ultrasonic_prps_get(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.pd_ultrasonic_prps_get(void)
            return ret
        except Exception as e:
            print(e)

    def pd_tev_basic_get(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.pd_tev_basic_get(void)
            return ret
        except Exception as e:
            print(e)

    def pd_tev_prpd_get(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.pd_tev_prpd_get(void)
            return ret
        except Exception as e:
            print(e)

    def pd_tev_prps_get(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.pd_tev_prps_get(void)
            return ret
        except Exception as e:
            print(e)

    def pd_stretch_out(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.pd_stretch_out(void)
            return ret
        except Exception as e:
            print(e)

    def pd_take_back(self):
        try:
            void = AvicRobotInterface_pb2.void_rpc()
            ret = self.stub.pd_take_back(void)
            return ret
        except Exception as e:
            print(e)


    pass
