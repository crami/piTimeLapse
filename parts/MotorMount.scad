
$fn=32;

difference() {
  translate([-35,-21,0])
  difference() {
    union() {
      translate([0,-0.5,0]) cube([56,43,4]);
      translate([0,0-9,0]) cube([14,60,9]);
    }


    union() {
      translate([35,21,-0.5]) cylinder(5,3.5,3.5);
      translate([35,21,1.5]) cylinder(3,11.5,11.5);
    }
  }

  translate([15.75,15.75,-0.5]) cylinder(5,1.7,1.7);
  translate([-15.75,15.75,-0.5]) cylinder(5,1.7,1.7);
  translate([15.75,-15.75,-0.5]) cylinder(5,1.7,1.7);
  translate([-15.75,-15.75,-0.5]) cylinder(5,1.7,1.7);

  translate([-30.1,-25,-0.5]) cube([4.2,10,10]);
  translate([-30.1,-5,-0.5]) cube([4.2,10,10]);
  translate([-30.1,15,-0.5]) cube([4.2,10,10]);

}

translate([-25,-25.45,0]) cube([46,4,9]);
translate([-25,+21.45,0]) cube([46,4,9]);