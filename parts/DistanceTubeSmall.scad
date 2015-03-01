$fn=32;

module post(d,h) {
  difference(){
    cylinder(h,d/2+0.8,d/2+0.8);
    translate([0,0,-0.2]) cylinder(h+0.4,d/2,d/2);
  }
}

for (x = [0 : 3]) {
  for( y = [0 : 3]) {
  translate([x*10, y*10, 0]) post(2.8,11.2);
  }
}