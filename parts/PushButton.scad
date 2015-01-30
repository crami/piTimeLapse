$fn=32;

difference() {
  translate([-3,-3,0]) cube([6,6,2]);
  translate([0,0,-0.5]) cylinder(1,1.6,1.6);
}

translate([0,0,1.9]) cylinder(3.1,2.25,2.25);