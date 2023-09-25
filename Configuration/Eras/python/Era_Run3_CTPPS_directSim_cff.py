import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3
from Configuration.Eras.Modifier_run3_directSim_cff import run3_directSim

Run3_CTPPS_directSim = cms.ModifierChain(Run3,run3_directSim)