
module slot(l) {
  polyhedron(
    points=[[0.3,0,0],[13.7,0,0],[13.7,l,0],[0.3,l,0], 
            [3.3,0,3.9],[10.7,0,3.9],[10.7,l,3.9],[3.3,l,3.9]],

    faces=[[0,1,2,3],[7,6,5,4],[3,7,4,0],
           [1,5,6,2],[4,5,1,0],[2,6,7,3],
    ]
  );
}


module tooth(length) {
  union() {
    for (y= [0:2:length]) {
      translate([0,y-0.01,-0.1]) cube([6,1.1,1.1]);
    }
  }
}


union() {
difference() {
  cube([20,35,4]);
  translate([7,0,0]) tooth(35);
  translate([3,17.5,-0.5]) cylinder(5,1.4,1.4, $fn=30);
  translate([17,17.5,-0.5]) cylinder(5,1.4,1.4, $fn=30);
}

translate([17,0,7.9]) rotate([0,180,0]) slot(35);
}


difference(){
  translate([0,0,4]) cube([20,4,15]);
  translate([10,-1,12]) rotate([-90,0,0]) cylinder(6,2,2, $fn=30);
}


translate([-30,0,0])
difference() {
  cube([20,35,5]);
  translate([3,17.5,-0.5]) cylinder(6,1.9,1.9, $fn=30);
  translate([17,17.5,-0.5]) cylinder(6,1.9,1.9, $fn=30);
  translate([7,-0.5,4.5]) cube([6,36,3]);

}
