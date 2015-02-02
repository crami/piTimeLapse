
module button() {
  $fn=32;
  union() {
    translate([0,0,0]) cylinder(0.8,3.2,3.2);
    translate([0,0,0.7]) cylinder(4.5,2.5,2.5);
  }
}

for (x = [0 : 3]) {
  for( y = [0 : 3]) {
  translate([x*10, y*10, 0]) button();
  }
}