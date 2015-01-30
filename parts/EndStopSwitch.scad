
$fn=32;

difference(){
  union() {
    cube([12.8+15,28,1.5]);
    translate([0,7.5,0.5]) cube([12.8+15,1.5,4]);
  }

  translate([6.2-3.25+15,5,-0.5]) cylinder(3,1.4,1.4);
  translate([6.2+3.25+15,5,-0.5]) cylinder(3,1.4,1.4);
  translate([6.2,22,-0.5]) cylinder(3,2.2,2.2);
  translate([12.8+15,28,-0.5]) cylinder(3,16,16);
}

translate([-35,0,0])
difference(){
  union() {
    cube([12.8+15,28,1.5]);
    translate([0,7.5,0.5]) cube([12.8+15,1.5,4]);
  }

  translate([6.2-3.25,5,-0.5]) cylinder(3,1.4,1.4);
  translate([6.2+3.25,5,-0.5]) cylinder(3,1.4,1.4);
  translate([6.2+15,22,-0.5]) cylinder(3,2.2,2.2);
  translate([0,28,-0.5]) cylinder(3,16,16);
}