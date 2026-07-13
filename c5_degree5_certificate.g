# Explicit certificate for the C5-symmetric degree-five candidate.

F:=FreeGroup("x","y","z");;
x:=F.1;; y:=F.2;; z:=F.3;;
Gam:=F/[x^5,y^5,z^5,x*y*z];;
gg:=GeneratorsOfGroup(Gam);;

H:=CyclicGroup(IsPermGroup,5);; r:=GeneratorsOfGroup(H)[1];;
base:=[r,r,r^3];;
psi:=GroupHomomorphismByImages(Gam,H,gg,base);;
K:=Kernel(psi);;
isoK:=IsomorphismFpGroup(K);; P:=Image(isoK);;
pg:=GeneratorsOfGroup(P);; fpg:=FreeGeneratorsOfFpGroup(P);;
rels:=RelatorsOfFpGroup(P);;
kus:=List(pg,u->PreImagesRepresentative(isoK,u));;

A5:=AlternatingGroup(5);;
a:=(1,2,3,4,5);;
b:=(1,2,4,5,3);;
c:=(a*b)^-1;;
rho:=GroupHomomorphismByImages(Gam,A5,gg,[a,b,c]);;
simgs:=List(kus,u->Image(rho,u));;

SLg:=SL(2,5);; cen:=Centre(SLg);;
minusI:=First(Elements(cen),u->u<>One(SLg));;
pmap:=NaturalHomomorphismByNormalSubgroup(SLg,cen);;
QQ:=Image(pmap);; iqa:=IsomorphismGroups(QQ,A5);;
cov:=CompositionMapping(iqa,pmap);;
lifts:=List(simgs,u->PreImagesRepresentative(cov,u));;
vals:=List(rels,R->MappedWord(R,fpg,lifts));;

Ext:=DirectProduct(A5,H);;
embA:=Embedding(Ext,1);; embH:=Embedding(Ext,2);;
orbimgs:=[Image(embA,a)*Image(embH,r),
          Image(embA,b)*Image(embH,r),
          Image(embA,c)*Image(embH,r^3)];;

Print("orbifold A5 tuple = ",[a,b,c],"\n");
Print("orders A5 tuple = ",List([a,b,c],Order)," product = ",a*b*c,
      " generated A5 order = ",Size(Group(a,b,c)),"\n");
Print("orbifold lift orders = ",List(orbimgs,Order),
      " product = ",Product(orbimgs),
      " generated extension order = ",Size(Group(orbimgs)),"\n");
Print("surface index = ",Index(Gam,K),
      " fp generators = ",Length(pg),
      " fp relators = ",Length(rels),"\n");
Print("surface fp generators = ",fpg,"\n");
Print("surface relator = ",rels,"\n");
Print("surface generators as orbifold words = ",kus,"\n");
Print("surface A5 images = ",simgs,"\n");
Print("surface image order = ",Size(Group(simgs)),"\n");
Print("chosen SL2(5) lifts = ",lifts,"\n");
Print("lifted relator values = ",vals,"\n");
Print("minusI = ",minusI,"\n");
Print("w2 = ",not ForAll(vals,v->v=One(SLg)),"\n");
QUIT;
