
height=23;

$fn=32;

module post(){
  difference() {
    cylinder(6,3,2.5);
    translate([0,0,1]) cylinder(6,1.4,1.4);
  }
}

difference(){
  union(){
    cube([71,65,2]);
    cube([71,2,height]);
    cube([2,65,height]);
    translate([0,65-2,0]) cube([71,2,height]);
    translate([71-2,0,0]) cube([2,65,height]);
    translate([0,23,22]) cube([2,16,3]); // Micro SD
  }

  translate([68,19.5,17]) cube([4,16,10]); // USB
  translate([8,65-3,20]) cube([12,8,5.5]); // Power
  translate([11,12,-1]) cube([55,40,4]); // LCD

  translate([17,56,-1]) cylinder(4,3,3);
  translate([17+13,56,-1]) cylinder(4,3,3);
  translate([17+2*13,56,-1]) cylinder(4,3,3);
  translate([17+3*13,56,-1]) cylinder(4,3,3);


}

translate([6.5,6.5,0]) post();
translate([6.5,65-6.5-3,0]) post();
translate([71-6.5,6.5,0]) post();
translate([71-6.5,65-6.5-3,0]) post();

