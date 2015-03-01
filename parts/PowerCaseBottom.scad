x=51;
y=38;
w=2;
h=16;

difference() {
  union() {
    cube([x+2*w,y+2*w,w]);
    cube([w,y+2*w,h+w]);
    cube([w*2,y+2*w,6]);
    
    cube([x+2*w,w,h+w]);
    cube([x+2*w,w*2,6]);

    translate([0,y+w,0]) cube([x+2*w,w,h+w]);
    translate([0,y,0]) cube([x+2*w,w*2,6]);
    
    translate([x+w,0,0]) cube([w,y+2*w,h+w]);
  }
  translate([3,-0.5,8]) cube([15,3,13]);
  translate([x+w-0.5,20+w,2]) cube([3,7,17]);
}