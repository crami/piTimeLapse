
height=17;

$fn=32;

module post(){
  difference() {
    cylinder(7,3,2.5);
    translate([0,0,1]) cylinder(7,1.3,1.3);
  }
}

difference(){
  union(){
    cube([71,65,2]);
    cube([71,2,height]);
    cube([2,65,height]);
    translate([0,65-2,0]) cube([71,2,height]);
    translate([71-2,0,0]) cube([2,65,height]);
    translate([0,23.1,height-1]) cube([2,15.8,4.5]); // Micro SD
  }
  //translate([21,9,0.5]) rotate([180,0,0]) scale(0.013) import("piTimeLapse.stl");
 
  translate([68,19.5,height-6]) cube([4,16,10]); // USB
  translate([8,65-3,height-3]) cube([12,8,5.5]); // Power
  translate([12,14,-1]) cube([49,36,4]); // LCD
  translate([-0.5,12,height-3]) cube([4,6,4]); // Camera Jack

  translate([17,56,-1]) cylinder(4,3,3);
  translate([17+13,56,-1]) cylinder(4,3,3);
  translate([17+2*13,56,-1]) cylinder(4,3,3);
  translate([17+3*13,56,-1]) cylinder(4,3,3);

  translate([6.5,6.5,1]) cylinder(2,1.3,1.3);
  translate([6.5,65-6.5-3,1]) cylinder(2,1.3,1.3);
  translate([71-6.5,6.5,1]) cylinder(2,1.3,1.3);
  translate([71-6.5,65-6.5-3,1]) cylinder(2,1.3,1.3);

}

translate([6.5,6.5,0]) post();
translate([6.5,65-6.5-3,0]) post();
translate([71-6.5,6.5,0]) post();
translate([71-6.5,65-6.5-3,0]) post();

