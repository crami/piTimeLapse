$fn=32;

difference() {
  translate([-3,-3,0]) cube([6,6,2]);
  translate([0,0,-0.5]) cylinder(1.5,1.7,1.7);
}

translate([0,0,1.9]) cylinder(3.1,2.5,2.5);