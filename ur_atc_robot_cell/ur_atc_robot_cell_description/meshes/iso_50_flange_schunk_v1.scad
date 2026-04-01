% scale(1000) import("iso_50_flange_schunk_v1.stl");

// Append pure shapes (cube, cylinder and sphere), e.g:
// cube([10, 10, 10], center=true);
// cylinder(r=10, h=10, center=true);
// sphere(10);

translate([0,-11,0])
rotate([90,0,0])
cylinder(r=35,h=22, center=true);