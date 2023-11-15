color Map[][]= new color [400][400];
int player1X=3;
int player1Y=3;
color player1Color=#ff0000;
int player1Dir=1;
int player2X=398;
int player2Y=398;
color player2Color=#0300FF;
int player2Dir=3;
void setup() {
  size(400, 400);
  noStroke();
  for (int y=0; y<=399; y=y+1) {
    for (int x=0; x<=399; x=x+1) {
      Map[y][x]=#000000;
    }
  }
}

void draw() {
  for (int y=0; y<=399; y=y+1) {
    for (int x=0; x<=399; x=x+1) {
      fill(Map[y][x]);
      rect(x, y, 1, 1);

    }
  }
  try{
      Player1();
      Player2();
  }catch(Exception e){
    exit();
  }
}
void Player1() {
  if (Map[player1Y][player1X]!=#000000) {
    exit();
  }
  if (player1X<0||player1X>399||player1Y<0||player1Y>399) {
    exit();
  }
  Map[player1Y][player1X]=player1Color;
  if (player1Dir==0) {
    player1X+=1;
  }
  if (player1Dir==1) {
    player1Y+=1;
  }
  if (player1Dir==2) {
    player1X-=1;
  }
  if (player1Dir==3) {
    player1Y-=1;
  }
}
void Player2() {
if (Map[player2Y][player2X]!=#000000) {
    exit();
  }
  if (player2X<0||player2X>399||player2Y<0||player2Y>399) {
    exit();
  }
  Map[player2Y][player2X]=player2Color;
  if (player2Dir==0) {
    player2X+=1;
  }
  if (player2Dir==1) {
    player2Y+=1;
  }
  if (player2Dir==2) {
    player2X-=1;
  }
  if (player2Dir==3) {
    player2Y-=1;
  }
}
void keyReleased(){
 if(key=='a')player1Dir-=1;
 if(key=='s')player1Dir+=1;
 if(player1Dir==4)player1Dir=0;
 if(player1Dir==-1)player1Dir=3;
 if(key=='k')player2Dir-=1;
 if(key=='l')player2Dir+=1;
 if(player2Dir==4)player2Dir=0;
 if(player2Dir==-1)player2Dir=3;
}
