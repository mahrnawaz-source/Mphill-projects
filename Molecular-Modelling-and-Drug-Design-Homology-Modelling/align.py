from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='6vrh', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='6vrh', atom_files='6vrh.pdb')
aln.append(file='unknown.ali', align_codes='unknown')
aln.align2d(max_gap_length=50)
aln.write(file='6vrh-unknown.ali', alignment_format='PIR')
aln.write(file='6vrh-unknown.pap', alignment_format='PAP')