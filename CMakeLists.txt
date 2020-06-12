# The name of the package:
atlas_subdir(AJMLChallenge)

# Add the shared library:
atlas_add_library(AJMLChallengeLib
  AJMLChallenge/*.h Root/*.cxx
  PUBLIC_HEADERS AJMLChallenge
  LINK_LIBRARIES AnaAlgorithmLib xAODEventInfo)

if(XAOD_STANDALONE)
 # Add the dictionary(for AnalysisBase only):
 atlas_add_dictionary(AJMLChallengeDict
  AJMLChallenge/AJMLChallengeDict.h
  AJMLChallenge/selection.xml
  LINK_LIBRARIES AJMLChallengeLib)
endif()

if(NOT XAOD_STANDALONE)
  # Add a component library for AthAnalysis only:
  atlas_add_component(AJMLChallenge
    src/components/*.cxx
    LINK_LIBRARIES AJMLChallengeLib)
endif()

# Install files from the package:
atlas_install_joboptions(share/*_jobOptions.py)
atlas_install_scripts(share/*_eljob.py)
