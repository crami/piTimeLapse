
$fn=64;

rotate([0,-45+180,0]) {
difference() {
  cube([16.8,60,4]);
  translate([5,30-25,-0.5]) roundedcube(4.2,5,10,2.1);
  translate([5,30-2.5,-0.5]) roundedcube(4.2,5,10,2.1);
  translate([5,30+20,-0.5]) roundedcube(4.2,5,10,2.1);
}

translate([14,0,1.2]) 
  rotate([0,45,0]) {
    cube([65,60,4]);
    translate([2,0,0]) rotate([270,0,0]) cylinder(60,3,3);
  }

}

module roundedcube(x, y, z, cr) {
  hull() {
    translate([cr,cr,0]) cylinder(z,cr,cr);
    translate([x-cr,cr,0]) cylinder(z,cr,cr);
    translate([cr,y-cr,0]) cylinder(z,cr,cr);
    translate([x-cr,y-cr,0]) cylinder(z,cr,cr);
  }
}
