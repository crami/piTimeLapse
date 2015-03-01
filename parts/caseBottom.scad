
height=9;

$fn=32;

module post(){
  difference() {
    translate([0,0,2]) cylinder(3,3,3);
    translate([0,0,-0.5]) cylinder(6,1.4,1.4);
  }
}

module cone() {
  union(){
    translate([0,0,-0.599]) cylinder(1,2.2,2.2);
    translate([0,0,0.4]) cylinder(2,2.2,0);
    translate([0,0,0]) cylinder(3,1.4,1.4);
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
  translate([71-8,23-0.2,-0.5]) cube([10,16.4,10]); // Micro SD
  translate([-1,19.5,6]) cube([4,16,10]); // USB
  translate([71-8-12,65-3,4]) cube([12,8,5.5]); // Power
  translate([68,12,7]) cube([4,6,4]); // Camera Jack
  translate([-1,7,7.5]) cube([4,10,2]); // Ribbon Cable

  translate([6.5,6.5,0]) cone();
  translate([6.5,65-6.5-3,0]) cone();
  translate([71-6.5,6.5,0]) cone();
  translate([71-6.5,65-6.5-3,0]) cone();


}

translate([6.5,6.5,0]) post();
translate([6.5,65-6.5-3,0]) post();
translate([71-6.5,6.5,0]) post();
translate([71-6.5,65-6.5-3,0]) post();

