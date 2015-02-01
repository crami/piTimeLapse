
height=9;

$fn=32;

module post(){
  difference() {
    cylinder(5,3,3);
    translate([0,0,-0.5]) cylinder(6,1.4,1.4);
  }
}


difference(){
  union(){
    cube([71,65,2]);
    cube([71,2,height]);
    cube([2,65,height]);
    translate([0,65-2,0]) cube([71,2,height]);
    translate([71-2,0,0]) cube([2,65,height]);
  }
  translate([71-5,24,-0.5]) cube([10,16,10]); // Micro SD
  translate([-1,17,6]) cube([4,15,10]); // USB
  translate([71-5-12,65-3,4]) cube([12,8,5.5]); // Power
}

translate([6.5,6.5,0]) post();
translate([6.5,65-6.5-3,0]) post();
translate([71-6.5,6.5,0]) post();
translate([71-6.5,65-6.5-3,0]) post();