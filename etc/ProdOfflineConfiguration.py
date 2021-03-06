#!/usr/bin/env python
"""
_OfflineConfiguration_

Processing configuration for the Tier0 - Replay version
"""

from T0.RunConfig.Tier0Config import addDataset
from T0.RunConfig.Tier0Config import createTier0Config
from T0.RunConfig.Tier0Config import setAcquisitionEra
from T0.RunConfig.Tier0Config import setConfigVersion
from T0.RunConfig.Tier0Config import ignoreStream
from T0.RunConfig.Tier0Config import addRepackConfig
from T0.RunConfig.Tier0Config import addExpressConfig
from T0.RunConfig.Tier0Config import addRegistrationConfig
from T0.RunConfig.Tier0Config import addConversionConfig
from T0.RunConfig.Tier0Config import addTier1Skim
from T0.RunConfig.Tier0Config import setLFNPrefix
from T0.RunConfig.Tier0Config import setBulkDataType
from T0.RunConfig.Tier0Config import setBulkDataLocation
from T0.RunConfig.Tier0Config import setPromptCalibrationConfig
from T0.RunConfig.Tier0Config import setDQMUploadUrl

# Create the Tier0 configuration object
tier0Config = createTier0Config()

# Set the verstion configuration
setConfigVersion(tier0Config, "replace with real version")

# Set global parameters:
#  Acquisition era
#  LFN prefix
#  Data type
#  PhEDEx location for Bulk data
setAcquisitionEra(tier0Config, "Run2013A")
setLFNPrefix(tier0Config, "/store")
setBulkDataType(tier0Config, "data")
setBulkDataLocation(tier0Config, "T0_CH_CERN_Export")

# Define the two default timeouts for reco release
# First timeout is used directly for reco release
# Second timeout is used for the data service PromptReco start check
# (to basically say we started PromptReco even though we haven't)
defaultRecoTimeout =  172800
defaultRecoLockTimeout = 1800


# Setup some useful defaults: processing version, reco framework version,
# global tag.
######################################################################

defaultRecoVersion = "CMSSW_5_3_8_patch3"
defaultAlcaVersion = defaultRecoVersion
defaultDQMVersion  = defaultRecoVersion

defaultProcVersion = 1
expressProcVersion = 1
recoProcVersion    = 1
alcaProcVersion    = 1
alcarawAlcaProcVer = 1

promptrecoGlobalTag = "GR_P_V43D::All"
expressGlobalTag    = "GR_E_V33A::All"
hltmonGlobalTag     = "GR_E_V29::All"
alcap0GlobalTag     = "GR_P_V43D::All"

#DQM Server
setDQMUploadUrl(tier0Config, "https://cmsweb.cern.ch/dqm/offline")

# Setup splittings

defaultRecoSplitting = 1728 
alcaRecoSplitting    = 100000
hiRecoSplitting      = 6000

# Setup repack and express mappings

repackVersionOverride = {
    "CMSSW_5_0_0" : "CMSSW_5_1_2_patch1",
    "CMSSW_5_0_1" : "CMSSW_5_1_2_patch1",
    "CMSSW_5_1_1" : "CMSSW_5_1_2_patch1",
    "CMSSW_5_1_2" : "CMSSW_5_1_2_patch1",
    "CMSSW_5_2_3" : "CMSSW_5_2_4",
    }

expressVersionOverride = {
    "CMSSW_5_0_0" : "CMSSW_5_1_2_patch1",
    "CMSSW_5_0_1" : "CMSSW_5_1_2_patch1",
    "CMSSW_5_1_1" : "CMSSW_5_1_2_patch1",
    "CMSSW_5_1_2" : "CMSSW_5_1_2_patch1",
    "CMSSW_5_2_2" : "CMSSW_5_3_8_patch3",
    "CMSSW_5_2_3" : "CMSSW_5_3_8_patch3",
    "CMSSW_5_2_4" : "CMSSW_5_3_8_patch3",
    "CMSSW_5_2_5" : "CMSSW_5_3_8_patch3",
    "CMSSW_5_2_6" : "CMSSW_5_3_8_patch3",
    "CMSSW_5_2_7" : "CMSSW_5_3_8_patch3",
    "CMSSW_5_2_8" : "CMSSW_5_3_8_patch3",
    "CMSSW_5_2_9" : "CMSSW_5_3_8_patch3",
    }

hltmonVersionOverride = {
    "CMSSW_5_0_0" : "CMSSW_5_1_2_patch1",
    "CMSSW_5_0_1" : "CMSSW_5_1_2_patch1",
    "CMSSW_5_1_1" : "CMSSW_5_1_2_patch1",
    "CMSSW_5_1_2" : "CMSSW_5_1_2_patch1",
    "CMSSW_5_2_2" : "CMSSW_5_2_7",
    "CMSSW_5_2_3" : "CMSSW_5_2_7",
    "CMSSW_5_2_4" : "CMSSW_5_2_4_hltpatch4",
    "CMSSW_5_2_5" : "CMSSW_5_2_7_hltpatch1",
    "CMSSW_5_2_6" : "CMSSW_5_2_7_hltpatch1",
    "CMSSW_5_2_7" : "CMSSW_5_2_7_hltpatch1",
    "CMSSW_5_2_8" : "CMSSW_5_2_7_hltpatch1",
    "CMSSW_5_2_9" : "CMSSW_5_2_7_hltpatch1",
    }

#set default repack settings for bulk streams
addRepackConfig(tier0Config, "Default",
                proc_ver = defaultProcVersion,
                versionOverride = repackVersionOverride,
                maxSizeSingleLumi = 10 * 1024 * 1024 * 1024,
                maxSizeMultiLumi = 6 * 1024 * 1024 * 1024,
                minInputSize = 1.6 * 1024 * 1024 * 1024,
                maxInputSize = 3 * 1024 * 1024 * 1024,
                maxEdmSize = 10 * 1024 * 1024 * 1024,
                maxOverSize = 6 * 1024 * 1024 * 1024,
                maxInputEvents = 10 * 1000 * 1000,
                maxInputFiles = 1000)

addDataset(tier0Config, "Default",
           scenario = "pp",
           reco_delay = defaultRecoTimeout,
           reco_delay_offset = defaultRecoLockTimeout,
           reco_version = defaultRecoVersion,
           default_proc_ver = defaultProcVersion,
           do_reco = False,
           global_tag = promptrecoGlobalTag,
           archival_node = "T0_CH_CERN")

#############################################
#############################################
### Used configuration during the Run2012 ###
#############################################
#############################################


# Physics PDs - extra ones from 7e33
addDataset(tier0Config, "BJetPlusX",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           dqm_sequences = [ "@common" ],
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "BTag",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           dqm_sequences = [ "@common" ],
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_IT_CNAF",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "JetHT",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           dqm_sequences = [ "@common", "@jetmet" ],
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "JetMon",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           #dqm_sequences = [ "@common", "@jetmet" ],
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "MET",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           dqm_sequences = [ "@common", "@jetmet", "@hcal" ],
           write_aod = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "MultiJet",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           dqm_sequences = [ "@common" ],
           write_aod = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "SingleMu",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           alca_producers = [ "MuAlCalIsolatedMu", "MuAlOverlaps", "TkAlMuonIsolated", "DtCalib" ],
           dqm_sequences = [ "@common", "@muon", "@jetmet" ],
           do_alca = True, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_IT_CNAF",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "DoubleMu",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           alca_producers = [ "MuAlCalIsolatedMu", "MuAlOverlaps", "DtCalib", "TkAlZMuMu" ],
           dqm_sequences = [ "@common", "@muon", "@egamma" ],
           do_alca = True, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_IT_CNAF",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "MuOnia",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           alca_producers = [ "TkAlJpsiMuMu", "TkAlUpsilonMuMu" ],
           dqm_sequences = [ "@common" ],
           reco_version = defaultRecoVersion,
           do_alca = True, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "MuEG",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           dqm_sequences = [ "@common" ],
           write_aod = True,
           #custodial_node = "T1_ES_PIC",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "MuHad",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           dqm_sequences = [ "@common" ],
           write_aod = True,
           #custodial_node = "T1_ES_PIC",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "SinglePhoton",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           dqm_sequences = [ "@common", "@ecal", "@egamma" ],
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_DE_KIT",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "SingleElectron",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           alca_producers = [ "EcalCalElectron" ],
           dqm_sequences = [ "@common", "@ecal" ],
           do_alca = True, alca_version= defaultAlcaVersion,
           write_aod = True,
           alca_proc_ver = alcaProcVersion,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "DataScouting",
           default_proc_ver = defaultProcVersion, scenario = "DataScouting",
           do_reco = True, global_tag = promptrecoGlobalTag, 
           reco_split = 3*defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           dqm_sequences = [ "@common" ],
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = False,
           write_dqm = True, 
           write_reco = False, 
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "DoubleElectron",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           alca_producers = [ "EcalCalElectron" ],
           dqm_sequences = [ "@common" ],
           do_alca = True, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "DoublePhoton",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           dqm_sequences = [ "@common", "@ecal", "@egamma" ],
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_FR_CCIN2P3",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "DoublePhotonHighPt",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           dqm_sequences = [ "@common", "@ecal", "@egamma" ],
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_FR_CCIN2P3",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "ElectronHad",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           dqm_sequences = [ "@common" ],
           write_aod = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "PhotonHad",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           dqm_sequences = [ "@common" ],
           write_aod = True,
           #custodial_node = "T1_TW_ASGC",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "HTMHT",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           dqm_sequences = [ "@common" ],
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_FR_CCIN2P3",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "Tau",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           dqm_sequences = [ "@common" ],
           write_aod = True,
           #custodial_node = "T1_UK_RAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "TauPlusX",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
          do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           dqm_sequences = [ "@common" ],
           write_aod = True,
           #custodial_node = "T1_UK_RAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "Commissioning",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           alca_producers = [ "HcalCalIsoTrk" ],
           reco_version = defaultRecoVersion,
           do_alca = True, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "Cosmics",
           default_proc_ver = defaultProcVersion, scenario = "cosmics",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = 10800,
           alca_producers = [ "TkAlCosmics0T","MuAlGlobalCosmics","HcalCalHOCosmics","DtCalibCosmics" ],
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = True, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "MinimumBias",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           alca_producers = [ "TkAlMinBias","SiStripCalMinBias" ],
           #dqm_sequences = [ "@commonSiStripZeroBias", "@ecal", "@hcal", "@muon" ],
           reco_version = defaultRecoVersion,
           do_alca = True, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "MinimumBias1",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = False, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           #alca_producers = [ "TkAlMinBias","SiStripCalMinBias" ],
           dqm_sequences = [ "@commonSiStripZeroBias", "@ecal", "@hcal", "@muon" ],
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           #write_aod = True,
           #custodial_node = "T1_IT_CNAF",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "MinimumBias2",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = False, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           #alca_producers = [ "TkAlMinBias","SiStripCalMinBias" ],
           dqm_sequences = [ "@commonSiStripZeroBias", "@ecal", "@hcal", "@muon" ],
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           #write_aod = True,
           #custodial_node = "T1_IT_CNAF",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "NoBPTX",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           dqm_sequences = [ "@common" ],
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_DE_KIT",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "ParkingMonitor",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           dqm_sequences = [ "@common", "@muon", "@hcal", "@jetmet", "@ecal", "@egamma" ],
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"AlCaP0",
           default_proc_ver = defaultProcVersion, scenario = "AlCaP0",
           do_reco = False, global_tag = alcap0GlobalTag,
           reco_split = alcaRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcarawAlcaProcVer,
           write_reco = False,
           custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"AlCaPhiSym",
           default_proc_ver = defaultProcVersion, scenario = "AlCaPhiSymEcal",
           do_reco = False, global_tag = promptrecoGlobalTag,
           reco_split = alcaRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcarawAlcaProcVer,
           write_reco = False,
           custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "HcalNZS",
           default_proc_ver = defaultProcVersion, scenario = "hcalnzs",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           alca_producers = [ "HcalCalMinBias" ],
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = True, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"AlCaLumiPixels",
           default_proc_ver = defaultProcVersion, scenario = "AlCaLumiPixels",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = alcaRecoSplitting,
           alca_producers = [ "LumiPixels" ],
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = True, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcarawAlcaProcVer,
           write_reco = False,
           custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"TestEnablesEcalHcalDT",
           default_proc_ver = defaultProcVersion, scenario = "AlCaTestEnable",
           do_reco = False, global_tag = promptrecoGlobalTag,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_reco = False,
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"TestEnablesTracker",
           default_proc_ver = defaultProcVersion, scenario = "AlCaTestEnable",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_version = defaultRecoVersion,
           alca_producers = [ "TkAlLAS" ],
           do_alca = True, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_reco = False,
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"ZeroBiasVdM",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           archival_node = "T0_CH_CERN"
           )


# Parking PDs from 7e33
addDataset(tier0Config,"DoubleMuParked",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = False, global_tag = promptrecoGlobalTag,
           #custodial_node = "T1_IT_CNAF",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "HTMHTParked",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = False, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = False,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "MuOniaParked",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = False, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = False,
           #custodial_node = "T1_TW_ASGC",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "MultiJet1Parked",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = False, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = False,
           #custodial_node = "T1_DE_KIT",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "TauParked",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = False, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = False,
           #custodial_node = "T1_UK_RAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "VBF1Parked",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = False, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = False,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
# Parked PDs that appeared on Run2012D
addDataset(tier0Config, "SinglePhotonParked",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = False, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = False,
           #custodial_node = "T1_DE_KIT",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "METParked",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = False, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = False,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "HLTPhysicsParked",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = False, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = False,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config, "ZeroBiasParked",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = False, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = False,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")


addDataset(tier0Config,"HcalHPDNoise",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = False, global_tag = promptrecoGlobalTag,
           custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"LogMonitor",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = False, global_tag = promptrecoGlobalTag,
	   custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"RPCMonitor",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = False, global_tag = promptrecoGlobalTag,
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"FEDMonitor",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = False, global_tag = promptrecoGlobalTag,
           archival_node = "T0_CH_CERN")


# Low-Pileup fill PDs / TOTEM Run
addDataset(tier0Config,"LP_L1Jets",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"LP_ExclEGMU",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"LP_Jets1",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"LP_Jets2",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"LP_MinBias1",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"LP_MinBias2",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"LP_MinBias3",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"LP_RomanPots",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"LP_ZeroBias",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"LP_Central",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"LP_Forward",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_aod = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
# HI PLead  tests

addDataset(tier0Config,"PAPhysics",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_reco = True,
           #write_aod = True,
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"PAZeroBias1",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_reco = True,
           #write_aod = True,
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"PAZeroBias2",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_reco = True,
           #write_aod = True,
           archival_node = "T0_CH_CERN")


### Heavy Ion 2013 datasets

addDataset(tier0Config,"PAMinBiasUPC",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = hiRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           alca_producers = [ "SiStripCalMinBias", "TkAlMinBias" ],
           do_alca = True, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN"
           )
addDataset(tier0Config,"PAMuon",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = hiRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           alca_producers = [ "TkAlMuonIsolated", "DtCalib" ],
           do_alca = True, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN"
           )
addDataset(tier0Config,"PAHighPt",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = hiRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN"
           )
addDataset(tier0Config,"PAMinBias1",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = hiRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN"
           )
addDataset(tier0Config,"PAMinBias2",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = hiRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN"
           )

### Run2013A datasets

addDataset(tier0Config,"PPFSQ",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = hiRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN"
           )
addDataset(tier0Config,"PPJet",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = hiRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN"
           )
addDataset(tier0Config,"PPMinBias",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = hiRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           alca_producers = [ "SiStripCalMinBias", "TkAlMinBias" ],
           do_alca = True, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN"
           )
addDataset(tier0Config,"PPMuon",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = hiRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = True, alca_version= defaultAlcaVersion,
           alca_producers = [ "TkAlMuonIsolated", "DtCalib" ],
           alca_proc_ver = alcaProcVersion,
           custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN"
           )
addDataset(tier0Config,"PPPhoton",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = hiRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN"
           )

# ZeroBias PDs - usually used for high rate tests
addDataset(tier0Config,"ZeroBias",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_reco = True,
           #write_aod = True,
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"ZeroBias1",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           alca_producers = [ "TkAlMinBias", "TkAlMuonIsolated"],
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_reco = True,
           #write_aod = True,
           custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"ZeroBias2",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           alca_producers = [ "TkAlMinBias", "TkAlMuonIsolated"],
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_reco = True,
           custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"ZeroBias3",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           alca_producers = [ "TkAlMinBias", "TkAlMuonIsolated"],
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_reco = True,
           custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"ZeroBias4",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           alca_producers = [ "TkAlMinBias", "TkAlMuonIsolated"],
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_reco = True,
           custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"ZeroBias5",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           alca_producers = [ "TkAlMinBias", "TkAlMuonIsolated"],
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_reco = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"ZeroBias6",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           alca_producers = [ "TkAlMinBias", "TkAlMuonIsolated"],
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_reco = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"ZeroBias7",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           alca_producers = [ "TkAlMinBias", "TkAlMuonIsolated"],
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_reco = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"ZeroBias8",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           alca_producers = [ "TkAlMinBias", "TkAlMuonIsolated"],
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_reco = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")

# HLTPhysics PDs for HPU run at the end of november
addDataset(tier0Config,"HLTPhysics1",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           alca_producers = [ "TkAlMinBias", "TkAlMuonIsolated"],
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_reco = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")
addDataset(tier0Config,"HLTPhysics2",
           default_proc_ver = defaultProcVersion, scenario = "pp",
           do_reco = True, global_tag = promptrecoGlobalTag,
           reco_split = defaultRecoSplitting,
           reco_proc_ver = recoProcVersion,
           reco_version = defaultRecoVersion,
           alca_producers = [ "TkAlMinBias", "TkAlMuonIsolated"],
           do_alca = False, alca_version= defaultAlcaVersion,
           alca_proc_ver = alcaProcVersion,
           write_reco = True,
           #custodial_node = "T1_US_FNAL",
           archival_node = "T0_CH_CERN")

##############################################
##############################################
### Express configuration for the Run2011A ###
##############################################
##############################################

addExpressConfig(tier0Config, "Express",
                 scenario = "pp",
                 data_tiers = [ "FEVT", "ALCARECO", "DQM" ],
                 alca_producers = [ "SiStripCalZeroBias", "TkAlMinBias", "MuAlCalIsolatedMu", "DtCalib", "PromptCalibProd" ],
                 global_tag = expressGlobalTag,
                 splitInProcessing = True,
                 proc_ver = expressProcVersion,
                 maxInputEvents = 200,
                 maxInputSize = 2 * 1024 * 1024 * 1024,
                 maxInputFiles = 500,
                 maxLatency = 15 * 23,
                 versionOverride = expressVersionOverride)

addExpressConfig(tier0Config, "ExpressCosmics",
                 scenario = "cosmics",
                 data_tiers = [ "FEVT", "ALCARECO", "DQM" ],
                 alca_producers = [ "SiStripCalZeroBias", "TkAlCosmics0T" ],
                 global_tag = expressGlobalTag,
                 splitInProcessing = True,
                 proc_ver = expressProcVersion,
                 maxInputEvents = 200,
                 maxInputSize = 2 * 1024 * 1024 * 1024,
                 maxInputFiles = 500,
                 maxLatency = 15 * 23,
                 versionOverride = expressVersionOverride)

addExpressConfig(tier0Config, "HLTMON",
                 scenario = "pp",
                 data_tiers = [ "FEVTHLTALL", "DQM" ],
                 global_tag = hltmonGlobalTag,
                 splitInProcessing = True,
                 proc_ver = expressProcVersion,
                 maxInputEvents = 200,
                 maxInputSize = 2 * 1024 * 1024 * 1024,
                 maxInputFiles = 500,
                 maxLatency = 15 * 23,
                 versionOverride = hltmonVersionOverride)


setPromptCalibrationConfig(tier0Config,
                           alcaHarvestTimeout = 12*3600,
                           alcaHarvestDir = "/afs/cern.ch/user/c/cmsprod/scratch0/wmagent_alcaharvest/",
                           conditionUploadTimeout = 18*3600,
                           dropboxHost = "webcondvm.cern.ch",
                           validationMode = False)


if __name__ == '__main__':
    print tier0Config
