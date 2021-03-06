
import math

def quat_plus(q1, q2):
    return [
        q1[0] + q2[0],
        q1[1] + q2[1],
        q1[2] + q2[2],
        q1[3] + q2[3],
    ]

def quat_minus(q1, q2):
    return [
        q1[0] - q2[0],
        q1[1] - q2[1],
        q1[2] - q2[2],
        q1[3] - q2[3],
    ]

def quat_multi(q1, q2):
    return [
        (q1[0] * q2[0]) - (q1[1] * q2[1]) - (q1[2] * q2[2]) - (q1[3] * q2[3]),
        (q1[0] * q2[1]) + (q1[1] * q2[0]) + (q1[2] * q2[3]) - (q1[3] * q2[2]),
        (q1[0] * q2[2]) + (q1[2] * q2[0]) + (q1[3] * q2[1]) - (q1[1] * q2[3]),
        (q1[0] * q2[3]) + (q1[3] * q2[0]) + (q1[1] * q2[2]) - (q1[2] * q2[1]),
    ]

def quat_identity(q1):
    s =math.sqrt((q1[0] * q1[0]) + (q1[1] * q1[1]) + (q1[2] * q1[2]) + (q1[3] * q1[3]))
    return [
        q1[0] / s, q1[1] / s, q1[2] / s, q1[3] / s,
    ]

def quat_to_matrix(q):
    return [
        [ q[0], -q[3], q[2], -q[1], ],
        [ q[3], q[0], -q[1], -q[2], ],
        [ -q[2], q[1], q[0], -q[3], ],
        [ q[1], q[2], q[3], q[0], ],
    ]

