#  IRESS
# Toy Robot Code Challenge

## Description and requirements:

The application is a simulation of a toy robot moving on a square table top, of dimensions 5 units x 5 units. There are no other obstructions on the table surface. The robot is free to roam around the surface of the table, but must be prevented from falling to destruction. Any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed.

# already installed on server
just run 
ssh root@167.71.114.198
password:iress@8726

> python /home/iress/robot/start.py

> PLACE 0,0,NORTH

> MOVE

>LEFT

>RIGHT

>REPORT


for test
>  python /home/iress/robot/TestRobotMove.py 

# How to install 
### system requirement
**you have to be ROOT user **
- 1- git app
> apt install git -y  

- 2- System user
>    useradd -m -s $(which bash) -G sudo iress  

>echo -e "iress@8726\niress@8726" | passwd iress  

>echo 'iress ALL=NOPASSWD: ALL' >> /etc/sudoers  
> su - iress

- 3- clone project code
I've used publicuser666666 user with password just to make it easy to clone project but usually I use private key and add public key to git
>   git clone https://publicuser666666:Publicuser_666666@github.com/taylorsuccessor/iress.git /home/iress/robot
- 4- python 
      > apt install python -y
- 5- run app

> python /home/iress/robot/start.py

- 6- run test
>  python /home/iress/robot/TestRobotMove.py 



## config application
you can change config.py file and set default values
- the
>DIRECTION_LIST = ['NORTH','EAST','SOUTH','WEST']

should be clockwise 

- the
> DIRECTION_RELATED_COORDINATION = {
    'NORTH':['Y',1],
    'EAST':['X',1],
    'SOUTH':['Y',-1],
    'WEST':['X',-1]
}


robot movement will affect any coordination X,-X,Y,-Y according to face(direction of robot)



## add test case 
in test_case_list.py file you can add to lest new case
> {  
    'command_list': [  
        'PLACE 1,2,EAST',  
  'MOVE',  
  'MOVE',  
  'LEFT',  
  'MOVE'  
  ],  
  'output': '3,3,NORTH'  
},
 
 