
$fn=32;

difference(){
  union() {
    cube([12.8,28,1.5]);
    translate([0,7.5,0.5]) cube([12.8,1.5,4]);
  }

  translate([6.2-3.25,5,-0.5]) cylinder(3,1.3,1.3);
  translate([6.2+3.25,5,-0.5]) cylinder(3,1.3,1.3);
  translate([6.2,22,-0.5]) cylinder(3,2.2,2.2);
}