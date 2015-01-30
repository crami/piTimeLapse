// Parametric thumb screw by Matt Hova
// More info at matthova.com
// Inspired in part by thingiverse.com/thing:11797/ by JRidley

/* CONSTANTS */
precision = 100; // Number of facets to generate for circles
pi = 3.1416; // Yum
slice = 0.1;
nudge = 0.00001;

/* VARIABLES */
bolt_head_diameter = 7;
bolt_head_height = 4;
bolt_diameter = 4;
knob_inner_diameter = bolt_head_diameter * 2; // The top cylinder diameter
knob_outer_diameter = bolt_head_diameter * 3; // The bottom cylinder diameter
knob_height = 8.1;
n_knob_nubs = 9;
knob_cutout_rad = knob_outer_diameter * pi / 24; // Sorta have to eyeball it on this one

/* DRAW! */
thumb_screw();

/* FUNCTIONS */
module thumb_screw(){
	difference(){
	
		union(){
			cylinder(r = knob_inner_diameter / 2, h = knob_height, $fn = precision); // top circle
			cylinder(r = knob_outer_diameter / 2, h = bolt_head_height, $fn = precision); // bottom circle
		}
	
		// Great Idea by JRidley to add a thin bridging layer instead of printing supports
		translate([0, 0, bolt_head_height + slice]) 
		cylinder(r = bolt_diameter / 2, h = knob_height, $fn = precision); // bolt hole
	
		// Here comes some TRIG!!! 
		// I'm using $fn = 6 to make a circle with 6 faces, (a.k.a. a hexagon)
		// A hexagon is made up of twelve 30º, 60º, 90º triangles
		//
		// In order to compensate for the bolt diameter
		// we will reach the desired hexagon size by dividing bolt_head_diameter by sin(60) aka sqrt(3) / 2
		cylinder(r = (bolt_head_diameter * 2 / sqrt(3)) / 2, h = bolt_head_height, $fn = 6); // bolt head hole. 
	
		knob_nubs(); // The 8 weird little nubs on the edge of the knob. Is there a better term for this?
	}
}

module knob_nubs(){
	//Creates n_knob_nubs cylinders, dispersed evenly around the edge of the outer knob
	for(i = [0:n_knob_nubs]){
		rotate([0, 0, i * 360 / n_knob_nubs])
		translate([0, knob_outer_diameter / 2 + knob_cutout_rad / 3, 0])
		cylinder(r = knob_cutout_rad, h = knob_height - bolt_head_height, $fn = precision/3);
	}
}