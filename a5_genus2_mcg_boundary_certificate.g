# Exact finite-group certificate for the nontrivial genus-two A5 orbit.
#
# Surface convention:
#   pi_1(Sigma_2)=<a1,b1,a2,b2 | [a1,b1][a2,b2]=1>.
# The tuple below has cyclic image C5 on the first handle and Klein-four
# image V4 on the second handle.  Its spin lifting invariant is nonzero.

A5 := AlternatingGroup(5);;

a1 := (1,2,3,4,5);;
b1 := a1;;
a2 := (1,2)(4,5);;
b2 := (1,4)(2,5);;

surfaceValue := Comm(a1,b1) * Comm(a2,b2);;
surfaceImage := Group(a1,b1,a2,b2);;

Print("surface tuple = ",[a1,b1,a2,b2],"\n");
Print("orders = ",List([a1,b1,a2,b2],Order),"\n");
Print("surface relator value = ",surfaceValue,"\n");
Print("surface image order = ",Size(surfaceImage),"\n");

H1 := Group(a1,b1);;
H2 := Group(a2,b2);;
orbits1 := Orbits(H1,[1..5]);;
orbits2 := Orbits(H2,[1..5]);;

# For the five-point permutation module, invariant dimension is the number
# of point-orbits.  Removing the trivial line gives augmentation invariants
# of dimension (#orbits - 1).
Print("first handle order = ",Size(H1),
      " point orbits = ",orbits1,
      " augmentation invariant dimension = ",Length(orbits1)-1,"\n");
Print("second handle order = ",Size(H2),
      " point orbits = ",orbits2,
      " augmentation invariant dimension = ",Length(orbits2)-1,"\n");

# Pull back the natural A5 -> SO(4) augmentation representation through
# Spin(4) -> SO(4).  This is the Schur double cover SL(2,5) -> A5.
SLg := SL(2,5);;
centreSL := Centre(SLg);;
minusI := First(Elements(centreSL),u -> u <> One(SLg));;
project := NaturalHomomorphismByNormalSubgroup(SLg,centreSL);;
PSLimage := Image(project);;
identify := IsomorphismGroups(PSLimage,A5);;
cover := CompositionMapping(identify,project);;

liftA1 := PreImagesRepresentative(cover,a1);;
liftB1 := PreImagesRepresentative(cover,b1);;
liftA2 := PreImagesRepresentative(cover,a2);;
liftB2 := PreImagesRepresentative(cover,b2);;

liftComm1 := Comm(liftA1,liftB1);;
liftComm2 := Comm(liftA2,liftB2);;
liftSurfaceValue := liftComm1 * liftComm2;;

Print("first lifted commutator = ",liftComm1,"\n");
Print("second lifted commutator = ",liftComm2,"\n");
Print("lifted surface relator = ",liftSurfaceValue,"\n");
Print("minus identity = ",minusI,"\n");
Print("w2 nonzero = ",liftSurfaceValue = minusI,"\n");

if surfaceValue <> One(A5) then
  Error("surface relation failed");
fi;
if Size(surfaceImage) <> 60 then
  Error("tuple does not generate A5");
fi;
if Length(orbits1)-1 <> 0 or Length(orbits2)-1 <> 1 then
  Error("unexpected augmentation invariant dimensions");
fi;
if liftSurfaceValue <> minusI then
  Error("expected the nontrivial spin lifting invariant");
fi;

QUIT;
