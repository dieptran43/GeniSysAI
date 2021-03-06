# Asociacion De Investigacion En Inteligencia Artificial Para La Leucemia Peter Moss
## GeniSysAI
### UP2 NCS1 Foscam Security System

[![HIAS GeniSysAI](../../../../Media/Images/GeniSysAI.png)](https://github.com/LeukemiaAiResearch/GeniSysAI)

&nbsp;

# Table Of Contents

- [Introduction](#introduction)
- [Siamese Neural Networks](#siamese-neural-networks)
- [Triplet Loss](#triplet-loss)
- [Intel® Movidius™ Neural Compute Stick](#intel-movidius-neural-compute-stick)
- [Prerequisites](#prerequisites)
  - [HIAS Server](#hias-server)
- [System Requirements](#system-requirements)
- [Hardware Requirements](#hardware-requirements)
- [Setup](#setup)
  - [UFW Firewall](#ufw-firewall)
  - [Clone the repository](#clone-the-repository)
      - [Developer Forks](#developer-forks)
  - [Install Dependencies](#install-dependencies)
  - [Known & Test Datasets](#known--test-datasets)
  - [Configuration](#configuration)
    - [Foscam](#foscam)
    - [iotJumpWay](#iotJumpWay)
  - [Server Test](#server-test)
  - [HIAS Proxy](#hias-proxy)
  - [Service Setup](#service-setup)
- [HIAS UI](#hias-ui)
- [Contributing](#contributing)
    - [Contributors](#contributors)
- [Versioning](#versioning)
- [License](#license)
- [Bugs/Issues](#bugs-issues)

&nbsp;

# Introduction
The UP2 NCS1 Foscam Security System connects to a Foscam IP camera and uses a **Facenet** classifier to provide Facial Recognition. Facenet uses **Siamese Neural Networks** trained with **Triplet Loss**, and is used in this project due to it's ability to help overcome the **Open Set Recognition Issue** in **facial recogniton**.

The project runs on an **UP Squared** IoT development board and uses an **Intel® Movidius™ Neural Compute Stick 1**.

&nbsp;

# Siamese Neural Networks
![Siamese Neural Networks](Media/Images/siamese-neural-networks.jpg)

Siamese Neural Networks are made up of 2 **Convolutional Neural Networks** that are exactly identical, hence the name Siamese Neural Networks. Siamese Neural Networks can be used to differentiate between objects, or in this case, faces. Facenet uses Siamese Neural Networks that have been trained with Triplet Loss.

Given an unseen example and a known example / multiple known examples we can pass the unseen example through the first Siamese Neural Network, and then compare the output encodings with output encodings from the single or multiple examples by calculating the difference between them. Using this method we are able to determine if the example passed to the first network is the same as one of the known examples, verifying if the person is known or not.

&nbsp;

# Triplet Loss
Triplet Loss was used when training Facenet and reduces the difference between an anchor (an image) and a positive sample from the same class, and increases the difference between the ancher and a negative sample from an opposite class. Basically this means that 2 images with the same class (in this case, the same person) will have a smaller distance than two images from different classes (or 2 different people).

&nbsp;

# Intel® Movidius™ Neural Compute Stick
![Intel® Movidius™ Neural Compute Stick](Media/Images/Movidius-NCS1.jpg)
The Intel® Movidius™ Neural Compute Stick is a piece of hardware, specifically a USB device, used for enhancing the inference process of computer vision models on low-powered/edge devices. The Intel® Movidius™ product is a USB appliance that can be plugged into devices such as Raspberry Pi and UP Squared, and basically takes the processing power off the device and onto the Intel Movidius brand chip, making the classification process a lot faster.

&nbsp;

# Prerequisites
Before you can install this project there are some prerequisites.

## HIAS Server
If you are going to be using the full system you will need to install the [HIAS](https://github.com/LeukemiaAiResearch/HIAS) server. Follow the [HIAS Installation Guide](https://github.com/LeukemiaAiResearch/HIAS/blob/master/Documentation/Installation/Installation.md) to complete your HIAS server setup.

&nbsp;

# System Requirements
- Tested on Ubuntu 18.04 & 16.04
- [Python 3.6](https://www.python.org/ "Python 3.6")
- Requires PIP3
- [Intel® Movidius™ NCSDK](https://github.com/movidius/ncsdk "Intel® Movidius™ NCSDK")
- [Tensorflow 1.4.0](https://www.tensorflow.org/install "Tensorflow 1.4.0")

# Hardware Requirements
- 1 x [Intel® Movidius™ Neural Compute Stick](https://www.movidius.com/ "Intel® Movidius™ Neural Compute Stick")
- 1 x UP Squared

&nbsp;

# Setup
Now we will setup the UP2 NCS1 Foscam Security System. The following tutorial will take you through the setup steps.

## UFW Firewall
UFW firewall is used to protect the ports of your device. Use the following command to check the status of your firewall:

```
  sudo ufw status
```
You should see the output:
```
  Status: inactive
```

The ports are specified in **Required/config.json**. The default setting is set to **8080** for the streaming port.

**FOR YOUR SECURITY YOU SHOULD CHANGE THIS!**.

```
  "Server": {
      "IP": "",
      "Port": 8080
  }
```

To allow access to the ports use the following command for each of your ports:

```
  sudo ufw allow 22
  sudo ufw allow 8080
  audo ufw enable
  sudo ufw status
```

You should see the following output:

```
  Status: active

  To                         Action      From
  --                         ------      ----
  22                         ALLOW       Anywhere
  8080                       ALLOW       Anywhere
  22 (v6)                    ALLOW       Anywhere (v6)
  8080 (v6)                  ALLOW       Anywhere (v6)
```

## Clone the repository
Clone the [HIAS GeniSysAI](https://github.com/LeukemiaAiResearch/GeniSysAI "HIAS GeniSysAI") repository from the [Asociacion De Investigacion En Inteligencia Artificial Para La Leucemia Peter Moss](https://github.com/LeukemiaAiResearch "Asociacion De Investigacion En Inteligencia Artificial Para La Leucemia Peter Moss") Github Organization.

To clone the repository and install the UP2 NCS1 Foscam Security System, make sure you have Git installed. Now navigate to the home directory on your device using terminal/commandline, and then use the following command.

```
  git clone https://github.com/LeukemiaAiResearch/GeniSysAI.git
```

Once you have used the command above you will see a directory called **GeniSysAI** in your home directory.

```
  ls
```

Using the ls command in your home directory should show you the following.

```
  GeniSysAI
```

Navigate to **GeniSysAI/Vision/UP2/NCS1/Foscam** directory, this is your project root directory for this tutorial.

### Developer Forks
Developers from the Github community that would like to contribute to the development of this project should first create a fork, and clone that repository. For detailed information please view the [CONTRIBUTING](../../../../CONTRIBUTING.md "CONTRIBUTING") guide. You should pull the latest code from the development branch.

```
  git clone -b "0.2.0" https://github.com/LeukemiaAiResearch/GeniSysAI.git
```

The **-b "0.2.0"** parameter ensures you get the code from the latest master branch. Before using the below command please check our latest master branch in the button at the top of the project README.

## Install Dependencies
Now you will install the required dependencies. [Setup.sh](Setup.sh "Setup.sh")is an executable shell script that will do the following:

- Install the required Python packages
- Install full NCSDK
- Downloads the pretrained Facenet model (**davidsandberg/facenet**)
- Downloads the pretrained **Inception V3** model
- Converts the **Facenet** model to a **Intel® Movidius/NCSDK** compatible graph

To execute the script, make enter the following commands. This will take a long time!

```
  sed -i 's/\r//' Setup.sh
  sh Setup.sh
```

## Known & Test Datasets
Before you can use your facial identification server, you need to add 1 image of all people that you want your server to classify as known to the **Model/Data/Known** directory and as many different faces as you like to the **Model/Data/Test** directory.

## Configuration
You need to updated the following settings in [Required/config.json](Required/config.json "Required/config.json") to ensure that your server is accessible.

### Foscam
- The value **Foscam->RTSPuser** should be the RTSP user provided in your Foscam IP camera settings.
- The value **Foscam->RTSPpass** should be the RTSP password provided in your Foscam IP camera settings.
- The value **Foscam->RTSPip** should be the IP of your Foscam IP camera.
- The value **Foscam->RTSPport** should be the RTSP port provided in your Foscam IP camera settings, this is usually 554.
- The value **Foscam->RTSPendpoint** should be the RTSP endpoint provided in your Foscam IP camera settings, this is usually videoMain.
- The value **Foscam->IP** should be the IP of your server machine.
- The value **Foscam->Port** should be the port that the server is listening on.

```
  "Foscam": {
      "RTSPuser": "",
      "RTSPpass": "",
      "RTSPip": "",
      "RTSPport": "554",
      "RTSPendpoint": "videoMain",
      "IP": "",
      "Port": 8080
  }
```
You should also update the socket configuration settings.

```
  "Socket": {
      "host": "localhost",
      "port": 8181
  }
```

Remember if you change the port settings, you need to allow these through the UFW firewall.

### iotJumpWay
![iotJumpWay](Media/Images/HIAS-IoT-Create-Device.png)

You need to setup your iotJumpWay GeniSysAI security device that will be used to communicate with the HIAS iotJumpWay broker. In the HIAS UI, navigate to **Security->GeniSysAI->Create**.

- For **Name** add a custom name for your device
- For **Type** select **Foscam Camera**
- For **Location** and **Zone** select the iotJumpWay location and zone, if you have not set these up yet you can do this in the **IoT** section.
- For **IP** add the IP address of your UP2 device.
- For **Mac** add the MAC address of your UP2 device.
- For **Stream Port**, add whatever port you used above in your configuration settings.
- For **Stream Directory**, this can be anything you like, your HIAS proxy will use this name to direct traffic to the correct device.
- For **Stream File**, this can be anything you like but it must end with **.mjpg**.
- For **Socket Port** add what ever port you used in the configuration.

Once you have created your device you will be taken to the new device page. Add your server name and the information provided on that page to your  configuration.

```
  "iotJumpWay": {
    "host": "",
    "port": 8883,
    "ip": "localhost",
    "lid": 0,
    "zid": 0,
    "did": 0,
    "dn": "",
    "un": "",
    "pw": ""
  }
```

## HIAS Proxy
Now you need to the entry to your HIAS proxy that will allow encrypted connection protected by a password. Use the following command to open up your HIAS server configuration:

```
sudo nano /etc/nginx/sites-available/default
```
Now add the following block underneath your existing GeniSysAI server camera proxy rules. You should replace **StreamDirectory** with the value you entered into the HIAS UI for **Stream Directory** and replace **###.###.#.##** with the IP address of your UP2. If you changed the default port number you should also replace **8080** with that port.

```
location ~* ^/Security/GeniSysAI/StreamDirectory/(.*)$ {
  auth_basic "Restricted";
  auth_basic_user_file /etc/nginx/security/htpasswd;
  proxy_pass http://###.###.#.##:8080/$1;
}
```

## Server Test
To make sure that your server is responding correctly, you need to open two terminals.

In your first terminal, use the following command:

```
 python3 FoscamRead.py
```

You should see the following output:

```
2020-08-24 20:32:31,361 - FoscamRead - INFO - Helpers class initialization complete.
2020-08-24 20:32:31,363 - Sockets - INFO - Helpers class initialization complete.
2020-08-24 20:32:31,363 - Sockets - INFO - Sockets Class initialized.
2020-08-24 20:32:31,364 - Sockets - INFO - Connected to strem socket: tcp://localhost:8181
2020-08-24 20:32:31,366 - iotJumpWay - INFO - Helpers class initialization complete.
2020-08-24 20:32:31,366 - iotJumpWay - INFO - Initiating Local iotJumpWay Device.
2020-08-24 20:32:31,367 - iotJumpWay - INFO - JumpWayMQTT Device Initiated.
2020-08-24 20:32:31,367 - iotJumpWay - INFO - Initiating Local iotJumpWay Device Connection.
2020-08-24 20:32:31,621 - iotJumpWay - INFO - Local iotJumpWay Device Connection Initiated.
2020-08-24 20:32:31,623 - iotJumpWay - INFO - -- Subscribed to Device Commands Channel
2020-08-24 20:32:31,674 - iotJumpWay - INFO - Local iotJumpWay Device Connection Successful.
2020-08-24 20:32:31,674 - iotJumpWay - INFO - rc: 0
2020-08-24 20:32:31,675 - iotJumpWay - INFO - Published to Device Status 1/Devices/1/19/Status
2020-08-24 20:32:31,676 - iotJumpWay - INFO - JumpWayMQTT Subscription: 1
2020-08-24 20:32:31,677 - iotJumpWay - INFO - -- Published to Device channel
2020-08-24 20:32:36,698 - FoscamRead - INFO - Connected To Camera
2020-08-24 20:32:36,700 - NCS1 - INFO - Helpers class initialization complete.
2020-08-24 20:32:40,399 - NCS1 - INFO - Connected to Neural Compute Stick 1
2020-08-24 20:32:40,436 - NCS1 - INFO - Loaded NCS1 graph
2020-08-24 20:32:41,060 - NCS1 - INFO - Known data preprocessed!
2020-08-24 20:32:41,060 - NCS1 - INFO - NCS1 class initialized.
2020-08-24 20:32:41,061 - FoscamRead - INFO - NCS configured.
2020-08-24 20:32:41,062 - FoscamRead - INFO - FoscamRead class initialized.
```

Next open a new terminal and execute the following command:

```
 python3 FoscamStream.py
```

You should see the following output:

```
2020-08-24 20:40:13,559 - FoscamStream - INFO - Helpers class initialization complete.
2020-08-24 20:40:13,560 - Sockets - INFO - Helpers class initialization complete.
2020-08-24 20:40:13,561 - Sockets - INFO - Sockets Class initialized.
2020-08-24 20:40:13,562 - Sockets - INFO - Connected to received socket: tcp://localhost:8181
2020-08-24 20:40:13,563 - FoscamStream - INFO - FoscamStream class initialized.
2020-08-24 20:40:13,576 - FoscamStream - INFO - Foscam server started on ###.###.#.##:8080
```

Now visit URL replacing the values as expected: **http://YourUp2Ip:YourPort/YourStreamFile**.

If everything has been done correctly you will now see the live stream from your Foscam camera in your browser.

![GeniSysAI Foscam Local Stream](Media/Images/foscam-local-stream.jpg)

## Service Setup
To ensure that the system will start each time your UP2 boots up, we will create a service. Use the following command to create and open a new service file for reading and processing the streams from the Foscam camera.

```
  sudo nano /lib/systemd/system/Foscam.service
```

Next add the following code to the file, replacing **YourUser** with the username you use to login to your UP2 with.

```
[Unit]
Description=GeniSysAI Foscam IP Camera Security System
After=multi-user.target

[Service]
User=YourUser
Type=simple
ExecStart=/usr/bin/python3 /home/YourUser/GeniSysAI/Vision/UP2/NCS1/Foscam/Foscam.py

[Install]
WantedBy=multi-user.target
```

Save and close the file. Now use the following command to restart the services daemon:

```
  sudo systemctl daemon-reload
```

Now enable, start and check your Foscam reading service:

```
sudo systemctl enable Foscam.service
sudo systemctl start Foscam.service
sudo systemctl status Foscam.service
```

You should see the following output.

```
● api.service - GeniSysAI Foscam IP Camera Security System
   Loaded: loaded (/lib/systemd/system/Foscam.service; enabled; vendor preset: enabled)
   Active: active (running) since Mon 2020-08-24 19:45:31 CEST; 4s ago
 Main PID: 3481 (python3)
    Tasks: 4
   Memory: 46.3M
      CPU: 2.878s
   CGroup: /system.slice/Foscam.service
           └─3481 /usr/bin/python3 /home/YourUser/GeniSysAI/Vision/UP2/NCS1/Foscam/Foscam.py
```

Your system will now start every time you boot up your UP2. You can use the following commands to manage your service in the future.

```
sudo systemctl restart Foscam.service
sudo systemctl start Foscam.service
sudo systemctl stop Foscam.service
sudo systemctl status Foscam.service
```

# HIAS UI
![GeniSysAI Foscam HIAS Stream](Media/Images/foscam-hias-stream.jpg)

If you visit the device page in the HIAS UI by navigating to **Security->GeniSysAI->List**, you will be able to locate your device. On your device page you will be able to see your stream. This stream is encrypted and is password protected. If you have not authenticated yourself for the HIAS streams a pop up will ask you to provide your HIAS UI user credentials.

![GeniSysAI Foscam HIAS Data](Media/Images/hias-device-life-data.png)

Your UP2 will publish device vitals to the iotJumpWay broker regularly, these can be viewed in the data section by visiting **IoT->Data**. You will also be able to see classifications from the facial recognition classifier as shown below.

![GeniSysAI Foscam HIAS Data](Media/Images/hias-device-foscam-data.png)

&nbsp;

# Contributing
Asociacion De Investigacion En Inteligencia Artificial Para La Leucemia Peter Moss encourages and welcomes code contributions, bug fixes and enhancements from the Github community.

Please read the [CONTRIBUTING](../../../../CONTRIBUTING.md "CONTRIBUTING") document for a full guide to forking our repositories and submitting your pull requests. You will also find information about our code of conduct on this page.

## Contributors

- [Adam Milton-Barker](https://www.leukemiaresearchassociation.ai/team/adam-milton-barker "Adam Milton-Barker") - [Asociacion De Investigation En Inteligencia Artificial Para La Leucemia Peter Moss](https://www.leukemiaresearchassociation.ai "Asociacion De Investigation En Inteligencia Artificial Para La Leucemia Peter Moss") President & Lead Developer, Sabadell, Spain

&nbsp;

# Versioning

We use SemVer for versioning. For the versions available, see [Releases](../../../../releases "Releases").

&nbsp;

# License

This project is licensed under the **MIT License** - see the [LICENSE](../../../../LICENSE "LICENSE") file for details.

&nbsp;

# Bugs/Issues

We use the [repo issues](../../../../issues "repo issues") to track bugs and general requests related to using this project.