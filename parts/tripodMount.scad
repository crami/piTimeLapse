
$fn=64;

module hex(w,h) {
  b=w/2;
  a=tan(30)*b;
  for (x = [ 0 : 5] ) {
    rotate([0,0,x*60]) translate([a*-1,0,0]) cube([2*a,b,h]);
  }
}



difference() {
  union(){
    hull() {
      cylinder(12,16,10);
      translate([15,0,0]) cylinder(12,10,10);
      translate([-15,0,0]) cylinder(12,10,10);
    }
  }
  
  translate([0,0,1]) hex((25.4*7/16)+0.5,12);
  translate([0,0,-1]) cylinder(h=3,r=(25.4/8)+0.5);
  translate([15,0,-1]) cylinder(14,2.7,2.7);
  translate([-15,0,-1]) cylinder(14,2.7,2.7);

  translate([15,0,10]) cylinder(0.6,4.4,2.7);
  translate([-15,0,10]) cylinder(0.6,4.4,2.7);

  translate([15,0,-1]) cylinder(11.001,4.4,4.4);
  translate([-15,0,-1]) cylinder(11.001,4.4,4.4);

}
