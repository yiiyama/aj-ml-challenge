#ifndef AJMLChallenge_SingleLeptonSelector_H
#define AJMLChallenge_SingleLeptonSelector_H

#include <AnaAlgorithm/AnaAlgorithm.h>

class SingleLeptonSelector : public EL::AnaAlgorithm
{
public:
  // this is a standard algorithm constructor
  SingleLeptonSelector(std::string const& name, ISvcLocator* pSvcLocator);

  // these are the functions inherited from Algorithm
  StatusCode initialize() override;
  StatusCode execute() override;
  StatusCode finalize() override;

private:
};

#endif
