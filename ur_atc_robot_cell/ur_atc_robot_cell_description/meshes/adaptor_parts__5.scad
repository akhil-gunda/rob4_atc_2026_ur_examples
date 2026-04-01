% scale(1000) import("adaptor_parts__5.stl");

// Append pure shapes (cube, cylinder and sphere), e.g:
// cube([10, 10, 10], center=true);
// cylinder(r=10, h=10, center=true);
// sphere(10);

translate([-5,0,0])
rotate([0,0,0])
cube([5,8,23], center=false);

translate([-2.5,-5,2.5])
rotate([90,0,0])
cylinder(r=2.2, h=10, center=true);

translate([-2.5,13,2.5])
rotate([90,0,0])
cylinder(r=2.2, h=10, center=true);