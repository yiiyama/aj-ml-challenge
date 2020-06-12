#ifndef AJMLChallenge_DoubleLeptonSelector_H
#define AJMLChallenge_DoubleLeptonSelector_H

#include <AnaAlgorithm/AnaAlgorithm.h>

class DoubleLeptonSelector : public EL::AnaAlgorithm
{
public:
  // this is a standard algorithm constructor
  DoubleLeptonSelector(std::string const& name, ISvcLocator* pSvcLocator);

  // these are the functions inherited from Algorithm
  StatusCode initialize() override;
  StatusCode execute() override;
  StatusCode finalize() override;

private:
};

#endif
