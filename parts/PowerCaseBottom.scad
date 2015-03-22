x=51;
y=38;
w=2;
h=16;

$fn=32;

difference() {
  union() {
    cube([x+2*w,y+2*w,w]);
    cube([w,y+2*w,h+w]);
    cube([w*2,y+2*w,7]);
    
    cube([x+2*w,w,h+w]);
    cube([x+2*w,w*2,7]);

    translate([0,y+w,0]) cube([x+2*w,w,h+w]);
    translate([0,y,0]) cube([x+2*w,w*2,7]);
    
    translate([x+w,0,0]) cube([w,y+2*w,h+w]);
  }
  translate([4,-0.5,9]) cube([14,3,13]);
  translate([x+w-0.5,20+w,2]) cube([3,7,17]);

  translate([16,y/2+w,-0.5]) cylinder(3,1.6,1.6);
  translate([16,y/2+w,1]) cylinder(3,3,3);
}