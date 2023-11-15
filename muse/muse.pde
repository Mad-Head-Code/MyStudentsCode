import ddf.minim.*;
import ddf.minim.analysis.*;
import ddf.minim.effects.*;
import ddf.minim.signals.*;
import ddf.minim.spi.*;
import ddf.minim.ugens.*;
class Player {
  int x, y, s;
  AudioPlayer p;
  color c;
  Player(int x, int y, AudioPlayer p, color c) {
    this.x=x;
    this.y=y;
    this.p=p;
    s=height/15;
    this.c=c;
  }
  void play() {
    if (!p.isPlaying()) {
      p.rewind();
      p.play();
    }
  }
  void draw() {
    fill(c);
    rect(x, y, s, s);
  }
}
ArrayList music=new ArrayList<Player>();
int P=0;
void setup() {
  fullScreen();
}
void draw() {
  background(#05FFA5);
  for (int i=0; i<15; i++) {
    line(0, height/15*i, width, height/15*i);
  }
  line(P, 0, P, height);
  P+=5;
  P%=width;
  for (Object o : music) {
    ((Player)o).draw();
    if (P>((Player)o).x&& P<((Player)o).x+height/15)
    {
      ((Player)o).play();
    }
  }
}
void mouseReleased() {
  if (mouseButton==LEFT)music.add(new Player(mouseX, (mouseY/(height/15))*(height/15), new Minim(this).loadFile(((mouseY/(height/15))+".mp3")), color (mouseY, mouseY/2, mouseY*2)));
  else music.clear();
}
