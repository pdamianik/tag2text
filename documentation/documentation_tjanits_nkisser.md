# CANopen Communication to a robot
The goal was to accomplish a microcontroller-operated robot communicating over CANopen. A connection to the robot had to be established and a python script had to be written, controlling the movement of the robot depending on incoming strings (text).

## The robot
The robot was a [EXCM Model](https://www.festo.com/at/de/p/flaechenportal-id_EXCM_FP) produced by [FESTO](https://www.festo.com/at). The information on how to communicate with the robot-interface was optained in its controllunits documentation.
Software and [control interface documentation](https://www.festo.com.cn/net/de_corp/SupportPortal/Files/737010/EXCM-10_30-_-E_2016-12b_8068048d1.pdf) were found on the [support portal](https://www.festo.com.cn/net/de_corp/SupportPortal/).

## CANopen
### Configuring the robot
Before we could begin trying to establish the connection between controlling software and the robots interface we had to set up its software, [the Festo Configuration Tool (FCT)](https://www.festo.com.cn/net/de_corp/SupportPortal/Details/245285/Document.aspx) according to chapter [5.3](https://www.festo.com.cn/net/de_corp/SupportPortal/Files/737010/EXCM-10_30-_-E_2016-12b_8068048d1.pdf) in the control-units handbook. After establishing a connection to the robot through ethernet connection we used the software to set up CANopen as the robots communication bussystem.

### Set up for [SocketCAN](https://doc.kusakata.com/networking/can.html?highlight=can)
If the kernel modules have already been setup (e.g. if you used SocketCAN before) jump to [kernel modules already existing](#kernel-modules-already-existing). Otherwise continue with the part below.
Load the kernel modules required for CAN:
```shell
    sudo modprobe can
    sudo modprobe can-raw
    sudo modprobe slcan
```
Continue in "kernel modules already existing".
#### kernel modules already existing
Check for already existing CAN interfaces:
```shell
    ifconfig
```
If not, configure an SocketCAN interface:
```shell
    ip link set your_can_socket type can bitrate your_bitrate
    // example
    ip link set can0 type can bitrate 1000000
```
Clone and make the CAN utils git repo:
```shell
    // clone into your working directory
    git clone https://github.com/linux-can/can-utils.github
    // enter the cloned directory
    cd can-utils
    // make 
    make
```
Attach the interface to your USB connection device:
```shell
    sudo ./slcan_attach -f -b your_baudrate -o /dev/your_usb_device
    // example
    sudo ./slcan_attach -f -b 1000000 -o /dev/ttyACM0
    // should return 
    attached tty /dev/ttyACM0 to netdevice slcan0
    // continue as followed
    sudo ./slcan ttyACM0 slcan0
    sudo ifconfig slcan up
```
Check if the interface is up and running/available:
```shell
    ifconfig
```

### Establishing a connection in python
After these steps it should have been possible to establish a connection in python using its [CANopen library](https://canopen.readthedocs.io/en/latest/) to communicate using [PDOs](https://canopen.readthedocs.io/en/latest/pdo.html) as the documentation described (chapter 4.2).
Although we tried multiple times and researched a lot, resulting in us getting stuck in half-chinese written websites, and some [GitHub Repositories](https://github.com/christiansandberg/canopen), we were not able to get a find a running solution for our communication-problem. 

## Conclusio
After all we learned a lot about CANopen, how shit the python documentation can be and how to set up a CAN-Socket on your local machine (for testing purposes), ultimately resulting in a failed project.
