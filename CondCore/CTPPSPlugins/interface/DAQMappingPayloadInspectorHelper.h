#ifndef CONDCORE_CTPPSPLUGINS_PPSDAQMAPPINGPAYLOADINSPECTORHELPER_H
#define CONDCORE_CTPPSPLUGINS_PPSDAQMAPPINGPAYLOADINSPECTORHELPER_H

// User includes
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "CondCore/Utilities/interface/PayloadInspectorModule.h"
#include "CondCore/Utilities/interface/PayloadInspector.h"
#include "CondCore/CondDB/interface/Time.h"
#include "CondFormats/PPSObjects/interface/TotemDAQMapping.h"

// system includes
#include <memory>
#include <sstream>

// ROOT includes
#include "TCanvas.h"
#include "TStyle.h"
#include "TH2F.h"
#include "TLatex.h"
#include "TGraph.h"



template <class PayloadType>
class DAQMappingPayloadInfo : public cond::payloadInspector::PlotImage<PayloadType, cond::payloadInspector::SINGLE_IOV> {
public:
  DAQMappingPayloadInfo()
      : cond::payloadInspector::PlotImage<PayloadType, cond::payloadInspector::SINGLE_IOV>(
            "DAQMappingPayloadInfo text") {}

  bool fill() override {
    auto tag = cond::payloadInspector::PlotBase::getTag<0>();
    auto tagname = tag.name;
    auto iov = tag.iovs.back();
    auto m_payload = this->fetchPayload(std::get<1>(iov));

    if (m_payload != nullptr) {
      
      return true;
    } else {
      return false;
    }
  }
};

#endif
