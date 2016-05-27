#!/usr/bin/env python

import sys

class Tentity:
    def __init__(self, this_line=None):
        self.type = None
        self.word_list = []
        self.id_list = set()
        if this_line is not None:
            self.load_from_line(this_line)
        
    def load_from_line(self, this_line):
        fields = this_line.split('\t')
        self.type = fields[0]
        self.word_list = fields[1].split(' ')
        self.id_list = set(fields[2].split(' '))
        
    def is_there_overlap(self, entity2):
        overlapping_ids = self.id_list & entity2.id_list
        return (len(overlapping_ids) != 0)

    def show(self):
        print '[[%s]]  Words: %s'  % (self.type,str(self.word_list))
        print '   Tokens: %s' % str(self.id_list)
        print
        
    def __str__(self):
        s = '[[%s]] ==> %s\n'  % (self.type,str(self.word_list))
        s += '   Tokens: %s\n' % str(self.id_list)
        return s
                
        
def load_relations(this_filename):
    fd = open(this_filename)
    all_lines = fd.readlines()
    idx = 0 
    relations = []
    while True:
        line1 = all_lines[idx].strip()
        idx += 1
        line2 = all_lines[idx].strip()
        idx += 1
        empty_line = all_lines[idx]
        idx += 1
        e1 = Tentity(line1)
        e2 = Tentity(line2)
        relations.append((e1,e2))

        if idx == len(all_lines):
            break        
    fd.close()
    return relations


def run_evaluation(system_relations, gold_relations):
    ok = wr = 0
    for (system_e1, system_e2) in system_relations:
        is_correct = False
        what_one_is_the_correct = None
        for (gold_e1, gold_e2) in gold_relations:
            if gold_e1.is_there_overlap(system_e1) and gold_e2.is_there_overlap(system_e2):
                is_correct = True
                what_one_is_the_correct = gold_e1, gold_e2
                break
        print '#'*50
        print 'System relation'
        print system_e1
        print system_e2
        print 'CORRECT:', is_correct
        if is_correct:
            print 'Matched with the GOLD relation'
            print what_one_is_the_correct[0]
            print what_one_is_the_correct[1]
        print '#'*50
        print
        
        if is_correct:
            ok +=1
        else:
            wr += 1
            
    if (ok+wr)==0:
        P = 0
    else:
        P = ok* 100.0 /(ok+wr)
    
    if len(gold_relations) == 0:
        R = 0
    else:
        R = ok* 100.0 / len(gold_relations)
        
    if (P+R) == 0:
        F=0
    else:
        F = 2*P*R/ (P+R)
    return P, R, F, ok, wr, len(gold_relations)
    
            
    
if __name__ == '__main__':
    system_filename = sys.argv[1]
    gold_filename = sys.argv[2]
    
    system_relations = load_relations(system_filename)
    print 'Len sys relations', len(system_relations)
    gold_relations = load_relations(gold_filename)
    print 'Len gold relations', len(gold_relations)
    #print 'GOLD'
    #for g in gold_relations:
    #    
    #    print str(g[0])
    #    print str(g[1])
    #    print

    P,R,F, ok, wrong, total = run_evaluation(system_relations, gold_relations)
    print '###'*20
    print 'PREC: %.2f' % P
    print 'REC: %.2f' % R
    print 'F: %.2f' % F
    print '###'*20
    print  '%%%<DATA>%%% ok wrong total'
    print ok, wrong, total
    print  '%%%</DATA>%%% ok wrong total'
     
        
        
        
