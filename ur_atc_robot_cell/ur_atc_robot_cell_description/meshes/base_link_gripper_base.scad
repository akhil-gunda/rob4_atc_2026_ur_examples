% scale(1000) import("base_link_gripper_base.stl");

// Append pure shapes (cube, cylinder and sphere), e.g:
// cube([10, 10, 10], center=true);
// cylinder(r=10, h=10, center=true);
// sphere(10);

translate([0,95/2,0])
rotate([0,0,0])
cube([65,95,35], center=true);

translate([0,105,14])
rotate([0,0,0])
cube([65,20,7], center=true);

translate([0,105,-14])
rotate([0,0,0])
cube([65,20,7], center=true);