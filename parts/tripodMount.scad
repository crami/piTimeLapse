
$fn=32;

/* [Screw Specifications] */
// specifies whether the screw is millimeters or inches; value of 1 for millimeters, value of 25.4 for inches
conversion = 25.4; // [1,25.4]
// the major diameter of the screw
diameter_major = 0.25;
// the pitch of the screw attachment
pitch = 0.05;
// integer multiplies the smoothness of the screw; suggested smoothness no greater than 5
Smoothness = 4;

/* [Hidden] */
Diameter_major = diameter_major*conversion;
Pitch = pitch*conversion;
Height = 8;
pi = 3.14159265359;
Circumference_major = Diameter_major*pi;
d27 = Pitch/8;
d28 = Pitch-d27;
d29 = 1.1*(Pitch-d27)/2;
number_of_bits = 8*Smoothness;
bit_thickness = 2.65/Smoothness;

A = [d28*cos(30),d28/2];
B = [d28*cos(30),d29];
C = [d28,d29];
D = [d28,-d29];
E = [d28*cos(30),-d29];
F = [d28*cos(30),-d28/2];
G = [d27*cos(30),-d27/2];
H = [d27*cos(30),d27/2];

module bit(Diameter_major,Pitch,Height,bit_thickness){
	translate([Diameter_major/2-d28*cos(30),bit_thickness/2,-d28/2+(d28+d27)*0]){
		rotate([90,0,0]){
			linear_extrude(height = bit_thickness)polygon(
				points = [A,B,C,D,E,F,G,H],
				paths = [[0,1,4,5,6,7]]
			);
		}
	}
}

module external_screw(Diameter_major,Pitch,Height,Smoothness){
	difference(){
		cylinder(r=Diameter_major/2-0.01,h=Height);
		for(j=[0:abs(Height)+1]){
			translate([0,0,Pitch*j]){
				rotate([0,0,j]){
					for(i=[0:(number_of_bits-1)]){
						translate([0,0,(1/number_of_bits)*Pitch*i]){
							rotate([0,0,(360/number_of_bits)*i]){
								bit(Diameter_major,Pitch,Height,bit_thickness);
							}
						}
					}
				}
			}
		}
	}
}

difference() {
  cube([40,20,3]);
  translate([30,7.5,-1]) cube([12,5,5]);
  translate([-2,7.5,-1]) cube([12,5,5]);
}

difference() {
  translate([20,10,2.5]) { cylinder(8.5,9,9);}
  translate([20,10,3.01]) external_screw(Diameter_major,Pitch,Height+0.2,Smoothness);
}