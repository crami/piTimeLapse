
$fn=32;


difference() {
  cube([40,20,4]);
  translate([30,7.5,-1]) roundedcube(12,5,6,2);
  translate([-2,7.5,-1]) roundedcube(12,5,6,2);
  translate([32.5,10,3]) cylinder(4,4.5,4.5);
  translate([7.5,10,3]) cylinder(4,4.5,4.5);
}
translate([0,0.5,0]) leg();
translate([40,19.5,0]) rotate([0,0,180]) leg();



module roundedcube(x, y, z, cr) {
  hull() {
    translate([cr,cr,0]) cylinder(z,cr,cr);
    translate([x-cr,cr,0]) cylinder(z,cr,cr);
    translate([cr,y-cr,0]) cylinder(z,cr,cr);
    translate([x-cr,y-cr,0]) cylinder(z,cr,cr);
  }
}

module leg() {
  hull() {
    translate([0,-2,0]) cube([2,2,4]);
    translate([38,-2,0]) cube([2,2,4]);
    translate([10,-45,0]) cylinder(4,2,2);
    translate([30,-45,0]) cylinder(4,2,2);
  }
  translate([10,-45,0]) cylinder(12,4,2);
  translate([30,-45,0]) cylinder(12,4,2);
}