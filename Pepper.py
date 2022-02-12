# Whip and Nei Nei

import qi
import argparse
import sys
import math
import time

def new_motion(motion_service, new_angles, max_speed, wait):
    motion_service.setAngles( ["LElbowYaw", "LShoulderRoll", "LWristYaw", "LShoulderPitch", "LElbowRoll"], new_angles, max_speed)
    time.sleep(wait)


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
    angles = [0.0, 0.3, 00., 1.6, -0.01]
    times  = [0.50, 0.2, 1.0, 1.0, 1.0]
    isAbsolute = True
    motion_service.angleInterpolation(names, angles, times, isAbsolute)

    new_angles = [[[-2.0, 0.3, -1.0, 0.5, -1.0], [0.0, 0.3, 0.0, -0.35, -0.01]],
                  [[-1.9, 0.3, 0.1, -0.35, -0.01], [-1.9, 0.3, 0.5, -0.35, -1.2], 
                  [-1.0, 0.3, 0.5, -0.35, -1.2], [-1.7, 0.3, 0.5, -0.35, -1.2]]]
    max_speed = 0.5
    wait = 1.0

    for i in range(0, len(new_angles[0])):
        new_motion(motion_service, new_angles[0][i], max_speed, wait)

    time.sleep(2.0)

    # Say 'Watch Me Nei NEi
    tts.say("Watch me Neigh Neigh!")

 
    # Waving Hand
    for i in range(0, len(new_angles[1])):
        new_motion(motion_service, new_angles[1][i], max_speed, wait)
    

    # Go to rest position
    motion_service.rest()
    sys.exit(0)
    
    


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