import turtle;

#setup board
#define: each tile is 100*100 px
turtle.screensize(1024, 768);
turtle.speed(0);
turtle.hideturtle();
turtle.fillcolor("light grey");

#left zone
turtle.up();
turtle.goto(-400,150);
turtle.down();
turtle.begin_fill();
turtle.setx(0);
turtle.sety(-150);
turtle.setx(-400);
turtle.sety(150);
turtle.end_fill();

#center zone
turtle.up();
turtle.goto(0,50);
turtle.down();
turtle.begin_fill();
turtle.setx(200);
turtle.sety(-50);
turtle.setx(0);
turtle.sety(50);
turtle.end_fill();

#right zone
turtle.up();
turtle.goto(200,150);
turtle.down();
turtle.begin_fill();
turtle.setx(400);
turtle.sety(-150);
turtle.setx(200);
turtle.sety(150);
turtle.end_fill();

#lines
for i in range(9):
    if i != 5:
        turtle.up();
        turtle.goto(-400+i*100,150);
        turtle.down();
        turtle.sety(-150);
turtle.up();
turtle.goto(100,50);
turtle.down();
turtle.sety(-50);

turtle.up();
turtle.goto(-400,50);
turtle.down();
turtle.setx(400);
turtle.sety(-50);
turtle.setx(-400);

turtle.up();
turtle.goto(200,150);
turtle.down;
turtle.setx(400);
turtle.sety(-150);
turtle.setx(200);
turtle.up();


#walls right
turtle.up();
turtle.goto(200,55);
turtle.down();
turtle.setx(300);
turtle.sety(-55);
turtle.setx(200);

#walls left
turtle.up();
turtle.setx(0);
turtle.down();
turtle.setx(-300);
turtle.sety(55);
turtle.setx(0);


#flower tiles
#left down
turtle.up();
turtle.goto(-390,-100);
turtle.down();
turtle.setx(-310);
turtle.up();
turtle.sety(-60);
turtle.down();
turtle.goto(-390,-140);
turtle.up();
turtle.sety(-60);
turtle.down();
turtle.goto(-310,-140);
turtle.up();
turtle.goto(-350,-60);
turtle.down();
turtle.sety(-140);
#left up
turtle.up();
turtle.goto(-390,100);
turtle.down();
turtle.setx(-310);
turtle.up();
turtle.sety(60);
turtle.down();
turtle.goto(-390,140);
turtle.up();
turtle.sety(60);
turtle.down();
turtle.goto(-310,140);
turtle.up();
turtle.goto(-350,60);
turtle.down();
turtle.sety(140);
#right down
turtle.up();
turtle.goto(290,-100);
turtle.down();
turtle.setx(210);
turtle.up();
turtle.sety(-60);
turtle.down();
turtle.goto(290,-140);
turtle.up();
turtle.sety(-60);
turtle.down();
turtle.goto(210,-140);
turtle.up();
turtle.goto(250,-60);
turtle.down();
turtle.sety(-140);
#right up
turtle.up();
turtle.goto(290,100);
turtle.down();
turtle.setx(210);
turtle.up();
turtle.sety(60);
turtle.down();
turtle.goto(290,140);
turtle.up();
turtle.sety(60);
turtle.down();
turtle.goto(210,140);
turtle.up();
turtle.goto(250,60);
turtle.down();
turtle.sety(140);
#center
turtle.up();
turtle.goto(-90,0);
turtle.down();
turtle.setx(-10);
turtle.up();
turtle.sety(40);
turtle.down();
turtle.goto(-90,-40);
turtle.up();
turtle.sety(40);
turtle.down();
turtle.goto(-10,-40);
turtle.up();
turtle.goto(-50,40);
turtle.down();
turtle.sety(-40);


#initialize piece turtles
blackPieces = [];
whitePieces = [];

for i in range(7):
    t = turtle.Turtle();
    t.resizemode("user");
    t.turtlesize(3,3,1);
    t.up();
    t.shape("circle");
    t.fillcolor("white");
    t.goto(0,200);
    whitePieces.append(t);

for i in range(7):
    t = turtle.Turtle();
    t.resizemode("user");
    t.turtlesize(3,3,1);
    t.up();
    t.shape("circle");
    t.fillcolor("black");
    t.goto(0,-200);
    blackPieces.append(t);



whitePath = [ [0,200], [-50,100], [-150,100], [-250,100], [-350,100], [-350,0], [-250,0], [-150,0], [-50,0], [50,0], [150,0], [250,0], [350,0], [350,100], [250,100], [200,200] ]
blackPath = [ [0,-200], [-50,-100], [-150,-100], [-250,-100], [-350,-100], [-350,0], [-250,0], [-150,0], [-50,0], [50,0], [150,0], [250,0], [350,0], [350,-100], [250,-100], [200,-200] ]


for i in range(16):
    whitePieces[6].goto(whitePath[i][0],whitePath[i][1]);
    blackPieces[6].goto(blackPath[i][0],blackPath[i][1]);

turtle.done();

