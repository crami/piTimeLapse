$fn=64;

difference() {
  union() {
    roundedcube(31,75,10,3);
    translate([15.5,37.5,0]) cylinder(7,19.5,15.5);
  }

  translate([15.5,37.5,4]) cylinder(7,10.5,10.5);
  translate([15.5,37.5,-0.5]) cylinder(11,5,5);

  translate([15.5,22.5,-0.5]) cylinder(11,2,2);

  translate([15.5,37.5+30,0]) screwhole();
  translate([15.5,37.5-30,0]) screwhole();
}

module roundedcube(x, y, z, cr) {
  hull() {
    translate([cr,cr,0]) cylinder(z,cr,cr);
    translate([x-cr,cr,0]) cylinder(z,cr,cr);
    translate([cr,y-cr,0]) cylinder(z,cr,cr);
    translate([x-cr,y-cr,0]) cylinder(z,cr,cr);
  }
}

module screwhole() {
  union() {
    translate([0,0,-0.5]) cylinder(11,2.6,2.6);
   // translate([0,0,-0.5]) cylinder(5,4.6,4.6);
   // translate([0,0,4.495]) cylinder(1,4.6,2.6);
  }
}