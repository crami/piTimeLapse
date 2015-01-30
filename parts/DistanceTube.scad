
$fn=32;

difference() {
  union() {
    cylinder(15,5,5);
    translate([0,0,14.95]) cylinder(2.55,5,4);
  }
  translate([0,0,-0.1]) cylinder(17.7,2.75,2.75);
}