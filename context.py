from mr_ckr import MRCKR

from rdflib.namespace import RDF, OWL
from rdflib import Graph

class Context(object):
    def __init__(self, name, namespace_manager):
        self.def_axiom_ctr = 0
        self.name = name
        self.axioms = Graph()
        self.axioms.namespace_manager = namespace_manager
        self.axioms.add((MRCKR.hasAxiomType_relation, RDF.type, OWL.AnnotationProperty))

    def add_axiom(self, axiom):
        self.axioms.add(axiom)

    def add_defeasible(self, relation_type, axiom):
        def_axiom = MRCKR.base.term(f"{self.name}_axiom_{self.def_axiom_ctr}")
        self.def_axiom_ctr += 1
        self.axioms.add((def_axiom, RDF.type, OWL.Axiom))
        self.axioms.add((def_axiom, MRCKR.hasAxiomType_relation, MRCKR.name_to_axiomtype[relation_type]))
        self.axioms.add((def_axiom, OWL.annotatedSource, axiom[0]))
        self.axioms.add((def_axiom, OWL.annotatedProperty, axiom[1]))
        self.axioms.add((def_axiom, OWL.annotatedTarget, axiom[2]))

    def to_file(self, path):
        self.axioms.serialize(f"{path}/m_{self.name}.n3", format="n3")
    