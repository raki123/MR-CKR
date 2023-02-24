from context import *
from mr_ckr import *

from rdflib import Graph, BNode
from rdflib.namespace import RDF, RDFS, OWL, Namespace, NamespaceManager

from pprint import pprint


onto = Graph()
onto = onto.parse("with_scene.owl")
namespace_manager = NamespaceManager(onto)
dsc = Namespace('http://semantic.bosch.com/drivingscene/v02/')
namespace_manager.bind('dsc', dsc, override=False)

abox= []
tbox = []

owl_prefix = str(OWL)
ns1 = list(namespace_manager.namespaces())[-2]
ns1_prefix = str(ns1)
dsc_prefix = str(dsc)


# first get all the tbox axioms

for triple in onto.triples((None, RDF.type, None)):
    if not str(triple[2]).startswith(dsc):
        tbox.append(triple)


for triple in onto.triples((None, RDFS.subClassOf, None)):
    tbox.append(triple)


base = Graph()
for triple in tbox:
    base.add(triple)

mrckr = MRCKR(base)


non_scene_individuals = []

for indiv, _, concept in onto.triples((None, RDF.type, None)):
    if str(concept).startswith(dsc):
        non_scene_individuals.append(indiv)

for indiv in non_scene_individuals:
    for triple in onto.triples((indiv, None, None)):
        abox.append(triple)

concepts = []

for concept, _, _ in onto.triples((None, RDF.type, OWL.Class)):
    if type(concept) != BNode and str(concept).startswith(dsc):
        concepts.append(concept)

exch = Namespace('http://example.org/exchange/')
namespace_manager.bind('exch', exch, override=False)

named_individuals = exch.term("Named")

# create change context
change_context = Context("change_context", namespace_manager)
mrckr.add_context(change_context)

# add extra concepts
original_concepts = []
for concept in concepts:
    change_context.add_axiom((exch.term("EX" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.type, OWL.Class))
    original_concepts.append(exch.term("EX" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):]))

add_concepts = []
for concept in concepts:
    change_context.add_axiom((exch.term("ADD" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.type, OWL.Class))
    add_concepts.append(exch.term("ADD" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):]))

del_concepts = []
for concept in concepts:
    change_context.add_axiom((exch.term("DEL" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.type, OWL.Class))
    del_concepts.append(exch.term("DEL" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):]))


# add change defaults
change_context.add_axiom((named_individuals, RDF.type, OWL.Class))
for i in range(len(concepts)):
    change_context.add_defeasible("similarity", (named_individuals, RDFS.subClassOf, add_concepts[i]))
    change_context.add_defeasible("similarity", (named_individuals, RDFS.subClassOf, del_concepts[i]))



dontdel_concepts = []
for concept in concepts:
    change_context.add_axiom((exch.term("DONTDEL" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.type, OWL.Class))
    dontdel_concepts.append(exch.term("DONTDEL" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):]))

dontadd_concepts = []
for concept in concepts:
    change_context.add_axiom((exch.term("DONTADD" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.type, OWL.Class))
    dontadd_concepts.append(exch.term("DONTADD" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):]))


# add dontchange defaults
for i in range(len(concepts)):
    change_context.add_defeasible("similarity", (named_individuals, RDFS.subClassOf, dontadd_concepts[i]))
    change_context.add_defeasible("similarity", (named_individuals, RDFS.subClassOf, dontdel_concepts[i]))

basic_context = Context("basic_context", namespace_manager)
# build inclusion axioms
inter_concepts = []
eq_inter_concepts = []
for concept in concepts:
    # basic_context.add_axiom((BNode("INTER" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.type, OWL.Class))
    inter_concepts.append(BNode("INTER" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):]))
    # basic_context.add_axiom((BNode("EQINTER" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.type, OWL.Class))
    # eq_inter_concepts.append(BNode("EQINTER" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):]))
    # basic_context.add_axiom((BNode("EQINTER" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):]), OWL.equivalentClass, BNode("INTER" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):])))

for i in range(len(concepts)):
    basic_context.add_axiom((inter_concepts[i], OWL.intersectionOf, BNode("INTER1" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):])))
    basic_context.add_axiom((BNode("INTER1" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.first, original_concepts[i]))
    basic_context.add_axiom((BNode("INTER1" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.rest, BNode("INTER2" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):])))
    basic_context.add_axiom((BNode("INTER2" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.first, dontdel_concepts[i]))
    basic_context.add_axiom((BNode("INTER2" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.rest, RDF.nil))

# union_concepts = []
# eq_union_concepts = []
# for concept in concepts:
#     # basic_context.add_axiom((BNode("UNION" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.type, OWL.Class))
#     union_concepts.append(BNode("UNION" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):]))
#     # basic_context.add_axiom((BNode("EQUNION" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.type, OWL.Class))
#     # eq_union_concepts.append(BNode("EQUNION" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):]))
#     # basic_context.add_axiom((BNode("EQUNION" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):]), OWL.equivalentClass, BNode("UNION" + str(concept)[len('http://semantic.bosch.com/drivingscene/v02/'):])))

# for i in range(len(concepts)):
#     basic_context.add_axiom((union_concepts[i], OWL.unionOf, BNode("UNION1" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):])))
#     basic_context.add_axiom((BNode("UNION1" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.first, inter_concepts[i]))
#     basic_context.add_axiom((BNode("UNION1" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.rest, BNode("UNION2" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):])))
#     basic_context.add_axiom((BNode("UNION2" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.first, add_concepts[i]))
#     basic_context.add_axiom((BNode("UNION2" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.rest, RDF.nil))

for i in range(len(concepts)):
    basic_context.add_axiom((original_concepts[i], RDF.type, OWL.Class))
    basic_context.add_axiom((concepts[i], RDF.type, OWL.Class))
    basic_context.add_axiom((add_concepts[i], RDF.type, OWL.Class))
    basic_context.add_axiom((dontadd_concepts[i], RDF.type, OWL.Class))
    basic_context.add_axiom((del_concepts[i], RDF.type, OWL.Class))
    basic_context.add_axiom((dontdel_concepts[i], RDF.type, OWL.Class))
    basic_context.add_axiom((add_concepts[i], RDFS.subClassOf, concepts[i]))
    basic_context.add_axiom((inter_concepts[i], RDFS.subClassOf, concepts[i]))

# make sure change and dontchange are disjoint
for i in range(len(concepts)):
    basic_context.add_axiom((BNode("NBOTHADD" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):]), OWL.intersectionOf, BNode("NBOTHADD1" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):])))
    basic_context.add_axiom((BNode("NBOTHADD1" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.first, add_concepts[i]))
    basic_context.add_axiom((BNode("NBOTHADD1" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.rest, BNode("NBOTHADD2" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):])))
    basic_context.add_axiom((BNode("NBOTHADD2" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.first, dontadd_concepts[i]))
    basic_context.add_axiom((BNode("NBOTHADD2" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.rest, RDF.nil))
    basic_context.add_axiom((BNode("NBOTHADD" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDFS.subClassOf, OWL.Nothing))

    basic_context.add_axiom((BNode("NBOTHDEL" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):]), OWL.intersectionOf, BNode("NBOTHDEL1" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):])))
    basic_context.add_axiom((BNode("NBOTHDEL1" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.first, del_concepts[i]))
    basic_context.add_axiom((BNode("NBOTHDEL1" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.rest, BNode("NBOTHDEL2" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):])))
    basic_context.add_axiom((BNode("NBOTHDEL2" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.first, dontdel_concepts[i]))
    basic_context.add_axiom((BNode("NBOTHDEL2" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDF.rest, RDF.nil))
    basic_context.add_axiom((BNode("NBOTHDEL" + str(concepts[i])[len('http://semantic.bosch.com/drivingscene/v02/'):]), RDFS.subClassOf, OWL.Nothing))


basic_context.add_axiom((named_individuals, RDF.type, OWL.Class))
for indiv in non_scene_individuals[:1]:
    basic_context.add_axiom((indiv, RDF.type, named_individuals))

mrckr.add_context(basic_context)
mrckr.add_relation("similarity", basic_context, change_context)

mrckr.to_file("./MR_CKR")