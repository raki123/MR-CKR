import context

from rdflib import URIRef
from rdflib.namespace import RDF, RDFS, OWL, Namespace

class MRCKR(object):
    ckr = Namespace("http://dkm.fbk.eu/ckr/meta#")
    base = Namespace("http://www.semanticweb.org/rkiesel/ontologies/2023/0/untitled-ontology-10#")
    module_concept = ckr.term("Module")
    context_concept = ckr.term("Context")
    hasModule_relation = ckr.term("hasModule")
    name_to_relation = { "similarity" : ckr.term("prec-t"), "coverage" : ckr.term("prec-c") }
    name_to_axiomtype = { "similarity" : ckr.term("defeasibleTime"), "coverage" : ckr.term("defeasibleCovers") }
    hasAxiomType_relation = ckr.term("hasAxiomType")

    def __init__(self, base_ontology):
        # self.base_ontology = base_ontology
        self.global_context = context.Context("global", base_ontology.namespace_manager)
        self.global_context.axioms.namespace_manager.bind('ckr', self.ckr, override=False)
        self.global_context.axioms.bind('base', self.base, override=False)
        self.global_context.add_axiom((URIRef("http://www.semanticweb.org/rkiesel/ontologies/2023/0/untitled-ontology-10#"), RDF.type, OWL.Ontology))
        self.global_context.add_axiom((URIRef("http://www.semanticweb.org/rkiesel/ontologies/2023/0/untitled-ontology-10#"), OWL.imports, URIRef("http://dkm.fbk.eu/ckr/meta#")))
        for relation in self.name_to_relation.values():
            self.global_context.add_axiom((relation, RDF.type, OWL.ObjectProperty))
        self.contexts = { "global" : self.global_context }

    def get_context(self, name):
        return self.contexts[name]

    def add_context(self, context):
        self.global_context.add_axiom((self.base.term("m_" + context.name), RDF.type, self.module_concept))
        self.global_context.add_axiom((self.base.term(context.name), RDF.type, self.context_concept))
        self.global_context.add_axiom((self.base.term(context.name), self.hasModule_relation, self.base.term("m_" + context.name)))
        self.contexts[context.name] = context
    
    def add_relation(self, relation_type, context_from, context_to):
        self.global_context.add_axiom((self.base.term(context_from.name), self.name_to_relation[relation_type], self.base.term(context_to.name)))

    def to_file(self, path):
        for context in self.contexts.values():
            context.to_file(path)
        