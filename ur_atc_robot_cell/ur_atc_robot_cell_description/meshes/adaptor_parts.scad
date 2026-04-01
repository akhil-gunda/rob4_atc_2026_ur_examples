% scale(1000) import("adaptor_parts.stl");

// Append pure shapes (cube, cylinder and sphere), e.g:
// cube([10, 10, 10], center=true);
// cylinder(r=10, h=10, center=true);
// sphere(10);

difference(){
translate([0,0,5])
rotate([0,0,0])
cylinder(r=32, h=10, center=true);
    
translate([0,0,5])
rotate([0,0,0])
cylinder(r=23, h=12, center=true);
    
translate([0,23,5])
rotate([0,0,0])
cube([46,50,12], center=true);
}

translate([0,0,-4/2])
rotate([0,0,0])
cylinder(r=32, h=4, center=true);