# Whip and Nei Nei

import qi
import argparse
import sys
import math
import time

def main(session):
    """
    Task management - the second motion is not postponed
    """
    # Get the service ALMotion.

    motion_service = session.service("ALMotion")

    # Wake up robot
    motion_service.wakeUp()


# Say 'Watch Me Whip!'

    
    from naoqi import ALProxy
    tts = ALProxy("ALTextToSpeech", "172.18.5.223", 9559)
    tts.say("Watch me Whip!")
    time.sleep(1.)

# Whip Action
    names  = ["LElbowYaw", "LShoulderRoll", "LWristYaw", "LShoulderPitch", "LElbowRoll"]
    angles = [0., 0.3, 0., 1.6, -.01]
    times  = [.50, .2, 1., 1., 1.]
    isAbsolute = True
    motion_service.angleInterpolation(names, angles, times, isAbsolute)

    names  =  ["LElbowYaw", "LShoulderRoll", "LWristYaw", "LShoulderPitch", "LElbowRoll"]
    angles = [-2., .3, -1, .5, -1.]
    fractionMaxSpeed = .4
    motion_service.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(1.)


    names  =  ["LElbowYaw", "LShoulderRoll", "LWristYaw", "LShoulderPitch", "LElbowRoll"]
    angles = [0., .3, 0, -.35, -.01]
    fractionMaxSpeed = .5
    motion_service.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(1.5)



# Say 'Watch Me Nei NEi
    tts.say("Watch me Neigh Neigh!")

 
# Waving Hand
    
    names  =  ["LElbowYaw", "LShoulderRoll", "LWristYaw", "LShoulderPitch", "LElbowRoll"]
    angles = [-1.9, .3, 0.1, -.35, -.01]
    fractionMaxSpeed = .5
    motion_service.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(.75)

    names  =  ["LElbowYaw", "LShoulderRoll", "LWristYaw", "LShoulderPitch", "LElbowRoll"]
    angles = [-1.9, .3, 0.4, -.35, -1.2]
    fractionMaxSpeed = .5
    motion_service.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(.75)

    names  =  ["LElbowYaw", "LShoulderRoll", "LWristYaw", "LShoulderPitch", "LElbowRoll"]
    angles = [-1.0, .3, 0.4, -.35, -1.2]
    fractionMaxSpeed = .5
    motion_service.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(1.0)

    names  =  ["LElbowYaw", "LShoulderRoll", "LWristYaw", "LShoulderPitch", "LElbowRoll"]
    angles = [-1.7, .3, 0.4, -.35, -1.2]
    fractionMaxSpeed = .5
    motion_service.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(1.0)

    # Go to rest position
    motion_service.rest()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="172.18.5.223",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)