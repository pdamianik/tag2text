import canopen

network = canopen.Network()
network.connect(bustype='socketcan', channel='slcan0', bitrate=1000000)

node = canopen.RemoteNode(1, )  # Change 'robot' to the actual node name
network.add_node(node)

network.check()
node.nmt.state = 'OPERATIONAL'

node.tpdo.read()
node.rpdo.write()

# Example: Sending a PDO message to control the robot
node.rpdo[1].raw = b'\x00'  # Example data

node.rpdo.write()


network.disconnect()
