
module base() {
  difference() {
    translate([-10.05,-10.05,0]) cube([20.1,20.1,4.05]);
    translate([0,0,-0.5]) cylinder(5,2.1,2.1,$fn=60);
  }
}

module slotplug() {
slottop=10;
  translate([-10,-10,0])
  union(){
    //translate([1.9,10-slottop/2,4]) cube([1.50, slottop, 10]);
    translate([-0.05,10-5.68/2,4]) cube([5.4, 5.68, 10]);
  }
}

module slider() {
  union() {
    translate([-10,-13.00006,0]) cube([20,3,20]);

    translate([-10,-13,0]) rotate([0,0,270])
    polyhedron(
      points=[[0,0,0],[0,2.5,0],[4,5.5,0],[4,0,0], 
             [0,0,20],[0,2.5,20],[4,5.5,20],[4,0,20]],

      faces=[[3,2,1,0],[4,5,6,7],[7,6,2,3],
             [4,7,3,0],[1,2,6,5],[0,1,5,4]]
    );

    translate([10,-13,20]) rotate([0,180,90])
    polyhedron(
      points=[[0,0,0],[0,2.5,0],[4,5.5,0],[4,0,0], 
             [0,0,20],[0,2.5,20],[4,5.5,20],[4,0,20]],

      faces=[[3,2,1,0],[4,5,6,7],[7,6,2,3],
             [4,7,3,0],[1,2,6,5],[0,1,5,4]]
    );
  }
}


module endstop() {
  translate([10,-8,0]) cube([4,16,24]);

  union() {
    difference() {
      translate([14,0,0]) cylinder(20,2,8,$fn=60);
      translate([4.5,-8.5,-0.5]) cube([9,17,21]);
    }
  
    difference() {
      translate([14,0,19.9]) cylinder(4.1,8,8,$fn=60);
      translate([4.5,-8.5,19.5]) cube([9,17,5]);
    }
  }
}


union() {
  base();
  slotplug();
  rotate([0,0,90]) slotplug();
  rotate([0,0,180]) slotplug();
  rotate([0,0,270]) slotplug();

  endstop();

  slider();
  rotate([0,0,180]) slider();
}
