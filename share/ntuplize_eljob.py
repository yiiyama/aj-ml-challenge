#!/usr/bin/env python

import os
import sys

import argparse

parser = argparse.ArgumentParser(description='Ntuplizer for AJ ML Challenge')
parser.add_argument('sample', metavar='SAMPLE', help='Sample')
parser.add_argument('selection', metavar='SELECTION', help='Selection')

options = parser.parse_args()
sys.argv = []

import ROOT
ROOT.xAOD.Init().ignore()

sh = ROOT.SH.SampleHandler()
sh.setMetaString('nc_tree', 'CollectionTree')

input_path = '/data/maxi215/atljphys/tnobe/AJPhysicsChallenge/Signal/mc16_13TeV.999999.PowhegPythia8EvtGen_CT10_AZNLOCTEQ6L1_ggH411W2_inclUniBR.DAOD_SUSY1.p3990'
ROOT.SH.ScanDir().filePattern('DAOD_SUSY1.test.pool.root').scan(sh, input_path)
sh.printContent()

job = ROOT.EL.Job()
job.sampleHandler(sh)
job.options().setDouble(ROOT.EL.Job.optMaxEvents, 500)
job.options().setString(ROOT.EL.Job.optSubmitDirMode, 'unique-link')

from AnaAlgorithm.DualUseConfig import createAlgorithm
if options.selection == 'singlelepton':
    alg = createAlgorithm('SingleLeptonSelector', 'Selector')

job.algsAdd(alg)

driver = ROOT.EL.DirectDriver()
driver.submit(job, 'ntuplize_job')
