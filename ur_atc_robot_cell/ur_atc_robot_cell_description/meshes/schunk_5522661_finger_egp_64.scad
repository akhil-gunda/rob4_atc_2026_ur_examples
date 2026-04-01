% scale(1000) import("schunk_5522661_finger_egp_64.stl");

// Append pure shapes (cube, cylinder and sphere), e.g:
// cube([10, 10, 10], center=true);
// cylinder(r=10, h=10, center=true);
// sphere(10);

translate([-5,-8,0])
rotate([0,0,0])
cube([10,16,20], center=true);

translate([-54/2,-26,5])
rotate([0,0,0])
cube([54,20,10], center=true);