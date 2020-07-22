
def byte2hex_str(byte_data):
    """
    将btyes数据转为十六进制数据，然后将十六进制数据转为字符串
    将十六进制数据转为hex字符串，每个字节中间加入空格
    :param byte_data:
    :return:
    """
    try:
        hex_str = str(byte_data.hex())
        hex_str = hex_str.upper()
    except:
        return None
    hex_str_list = []
    for i in range(0, len(hex_str) - 1, 2):
        hex_str_list.append(hex_str[i:i + 2])
        hex_str_list.append(' ')

    return ''.join(hex_str_list)

def int2hex_str(byte_len, data):
    """
    将某个整数转换为指定字节长度的十六进制字符串
    如：整数12，转为 2个字节长度的十六进制字符串，为000c
    先将整型数据转为十六进制，然后将十六进制数据转为字符串
    :param byte_len:
    :param data:
    :return: 返回十六进制形式的字符串
    """
    try:
        hex_str = hex(data)
        hex_str = hex_str[2:]
    except:
        return None

    if len(hex_str) % 2:
        hex_str = '0' + hex_str

    if len(hex_str) < byte_len * 2:
        hex_str = '00' * int(byte_len - len(hex_str)/2) + hex_str
    return hex_str

# bytes 类型的各种数据转换
def b2uint(bytes):
    """
    bytes 转无符号整型
    :param bytes:
    :return:
    """
    return int.from_bytes(bytes, byteorder='big', signed=False)

def b2int(bytes):
    """
    bytes 转有符号整型
    :param bytes:
    :return:
    """
    return int.from_bytes(bytes, byteorder='big', signed=True)

def hex2b(hex):
    """
    十进制转bytes
    :param hex:
    :return:
    """
    return bytes.fromhex(hex)

def b2hex(bytes):
    """
    btyes转十六进制
    :param bytes:
    :return:
    """
    return bytes.hex()
# -----------------------------------------------------------------------------
# import serial
# def hex2b(hex):
#     return bytes.fromhex(hex)
# def b2hex(bytes):
#     return bytes.hex()
# def b2uint(bytes):
#     return int.from_bytes(bytes, byteorder='big', signed=False)
# def uint2b(num):
#     return num.to_bytes(2, byteorder='big', signed=False)
# def check_sum(data):
#     sum = 0
#     for i in data:
#         sum = sum + i
#     sum = bytes([uint2b(sum)[1]])
#     return sum
# def get_file_info(file_id):
#     header = b'\xEB\x10'
#     data = b'\x00\x01'+ uint2b(file_id)+b'\x00'*8
#     sum = check_sum(data)
#     return header + data + sum + b'\x90'
# def parser_file_info(data):
#     frame_sum = bytes([data[7],data[8]])
#     file_size = bytes([data[9],data[10]])
#     return b2uint(frame_sum), b2uint(file_size)
# def get_file_frame(file_id, frame_id, file_size):
#     header = b'\xEB\x81'
#     data = b'\x00\x01' + uint2b(file_id) + uint2b(frame_id) + uint2b(file_size) + bytes([0])*4
#     sum = check_sum(data)
#     return header + data + sum + b'\x90'
# def parser_file_frame(data):
#     return data[8:254]
# buff = bytes()
# ser = serial.Serial("com4", 115200, timeout=0.5)
# if ser:
#     print('open com4')
#     # 获取第一张图像
#     file_id = 1
#     ser.write(get_file_info(file_id))
#     r = ser.read(16)
#     frame_sum, file_size = parser_file_info(r)
#     for i in range(frame_sum):
#         ser.write(get_file_frame(file_id, i+1, file_size))
#         r = ser.read(256)
#         if len(r)==256:
#             r = parser_file_frame(r)
#             print('get frame %d success'%(i+1))
#             buff = buff + r
#         else:
#             print('get frame %d failure'%(i+1))
#     with open('test.jpg', 'wb') as f:
#         f.write(buff)
#     ser.close()
# -----------------------------------------------------------------------------
