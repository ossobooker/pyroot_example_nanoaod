import ROOT
ROOT.gROOT.SetBatch(True) 
# setup some ROOT stuff
ROOT.PyConfig.DisableRootLogon = True
ROOT.PyConfig.IgnoreCommandLineOptions = False
ROOT.gROOT.SetBatch(True)

# Instructions for CMS plot styles:
# https://twiki.cern.ch/twiki/bin/view/CMS/Internal/PubGuidelines
# https://twiki.cern.ch/twiki/bin/view/CMS/Internal/FigGuidelines

# clean old stuff
import os
os.system("rm -rf outputs_files/*.png")
os.system("rm -rf outputs_files/*.pdf")

# Open a ROOT file 
output_file = ROOT.TFile('output_file.root')

# save the histogram
h_muon_pt_1 = output_file.Get("h_muon_pt_1")
h_muon_phi_1 = output_file.Get("h_muon_phi_1")
h_MET_phi_1 = output_file.Get("h_MET_phi_1")
h_MET_pt_1 = output_file.Get("h_MET_pt_1")
h_nmuon_1 = output_file.Get("h_nmuon_1")
h_muon_pt_2 = output_file.Get("h_muon_pt_2")
h_muon_phi_2 = output_file.Get("h_muon_phi_2")
h_MET_phi_2 = output_file.Get("h_MET_phi_2")
h_MET_pt_2 = output_file.Get("h_MET_pt_2")
h_nmuon_2 = output_file.Get("h_nmuon_2")
h_MmM1 = output_file.Get("h_MmM1")
h_MmM2 = output_file.Get("h_MmM2")

# setting the title
h_muon_pt_1.SetTitle("Data")
h_muon_phi_1.SetTitle("Data")
h_MET_phi_1.SetTitle("Data")
h_MET_pt_1.SetTitle("Data")
h_nmuon_1.SetTitle("Data")
h_MmM1.SetTitle("Data")

h_muon_pt_2.SetTitle("Signal MC")
h_muon_phi_2.SetTitle("Signal MC")
h_MET_phi_2.SetTitle("Signal MC")
h_MET_pt_2.SetTitle("Signal MC")
h_nmuon_2.SetTitle("Signal MC")
h_MmM2.SetTitle("Signal MC")

h_muon_pt_1.SetMarkerStyle(ROOT.kFullCircle)
h_muon_pt_2.SetLineWidth(2)
h_muon_pt_2.SetFillColorAlpha(ROOT.kOrange-2, 0.35)

h_muon_phi_1.SetMarkerStyle(ROOT.kFullCircle)
h_muon_phi_2.SetLineWidth(2)
h_muon_phi_2.SetFillColorAlpha(ROOT.kOrange-2, 0.35)

h_MmM1.SetMarkerStyle(ROOT.kFullCircle)
h_MmM2.SetLineWidth(2)
h_MmM2.SetFillColorAlpha(ROOT.kOrange-2, 0.75)

h_MET_pt_1.SetMarkerStyle(ROOT.kFullCircle)
h_MET_pt_2.SetLineWidth(2)
h_MET_pt_2.SetFillColorAlpha(ROOT.kOrange-2, 0.35)

h_MET_phi_1.SetMarkerStyle(ROOT.kFullCircle)
h_MET_phi_2.SetLineWidth(2)
h_MET_phi_2.SetFillColorAlpha(ROOT.kOrange-2, 0.35)

h_nmuon_1.SetMarkerStyle(ROOT.kFullCircle)
h_nmuon_2.SetLineWidth(2)
h_nmuon_2.SetFillColorAlpha(ROOT.kOrange-2, 0.35)


c1 = ROOT.TCanvas("c1","c1",1200,800)


h_hs_M = ROOT.THStack("h_hs_M","; m_{T} (GeV);Events")
h_hs_muon_pt = ROOT.THStack("h_hs_muon_pt","; Lepton p_{T} (GeV);Events")
h_hs_muon_phi = ROOT.THStack("h_hs_muon_phi","; Lepton #phi;Events")
h_hs_MET_pt = ROOT.THStack("h_hs_MET_pt","; Missing E_{T} (GeV);Events")
h_hs_MET_phi = ROOT.THStack("h_hs_MET_phi","; Missing E_{T} #phi;Events")
h_hs_nmuon = ROOT.THStack("h_hs_nmuon","; Number of muons;Events")

h_hs_M.Add(h_MmM1, "E1")
h_hs_M.Add(h_MmM2, "hist")
h_hs_muon_pt.Add(h_muon_pt_1, "E1")
h_hs_muon_pt.Add(h_muon_pt_2, "hist")
h_hs_muon_phi.Add(h_muon_phi_1, "E1")
h_hs_muon_phi.Add(h_muon_phi_2, "hist")
h_hs_MET_pt.Add(h_MET_pt_1, "E1")
h_hs_MET_pt.Add(h_MET_pt_2, "hist")
h_hs_MET_phi.Add(h_MET_phi_1, "E1")
h_hs_MET_phi.Add(h_MET_phi_2, "hist")
h_hs_nmuon.Add(h_nmuon_1, "E1")
h_hs_nmuon.Add(h_nmuon_2, "hist")


#Drawing Histograms
h_hs_M.Draw("nostack")
c1.Modified()
ROOT.gPad.BuildLegend(0.75,0.75,0.95,0.95,"")
c1.SaveAs("outputs_files/h_hs_M.png")
c1.SaveAs("h_hs_M.pdf")

h_hs_muon_pt.Draw("nostack")
c1.Modified()
ROOT.gPad.BuildLegend(0.75,0.75,0.95,0.95,"")
c1.SaveAs("outputs_files/h_hs_muon_pt.png")
c1.SaveAs("outputs_files/h_hs_muon_pt.pdf")

h_hs_muon_phi.Draw("nostack")
c1.Modified()
ROOT.gPad.BuildLegend(0.75,0.75,0.95,0.95,"")
c1.SaveAs("outputs_files/h_hs_muon_phi.png")
c1.SaveAs("outputs_files/h_hs_muon_phi.pdf")

h_hs_MET_pt.Draw("nostack")
c1.Modified()
ROOT.gPad.BuildLegend(0.75,0.75,0.95,0.95,"")
c1.SaveAs("outputs_files/h_hs_MET_pt.png")
c1.SaveAs("outputs_files/h_hs_MET_pt.pdf")

h_hs_MET_phi.Draw("nostack")
c1.Modified()
ROOT.gPad.BuildLegend(0.75,0.75,0.95,0.95,"")
c1.SaveAs("outputs_files/h_hs_MET_phi.png")
c1.SaveAs("outputs_files/h_hs_MET_phi.pdf")

h_hs_nmuon.Draw("nostack")
c1.Modified()
ROOT.gPad.BuildLegend(0.75,0.75,0.95,0.95,"")
c1.SaveAs("outputs_files/h_hs_nmuon.png")
c1.SaveAs("outputs_files/h_hs_nmuon.pdf")

'''c1.SaveAs("h_hs_M.png")
c1.SaveAs("h_hs_M.pdf")
c1.SaveAs("h_hs_muon_pt.png")
c1.SaveAs("h_hs_muon_pt.pdf")
c1.SaveAs("h_hs_muon_phi.png")
c1.SaveAs("h_hs_muon_phi.pdf")
c1.SaveAs("h_hs_MET_pt.png")
c1.SaveAs("h_hs_MET_pt.pdf")
c1.SaveAs("h_hs_MET_phi.png")
c1.SaveAs("h_hs_MET_phi.pdf")
c1.SaveAs("h_hs_nmuon.png")
c1.SaveAs("h_hs_nmuon.pdf")'''


output_file.Close()

'''# open a file that contains stacked histogras
stacked_file = ROOT.TFile('stacked_file.root', 'RECREATE')

h_hs_M.Write()
h_hs_muon_pt.Write()
h_hs_muon_phi.Write()
h_hs_MET_pt.Write()
h_hs_MET_phi.Write()
h_hs_nmuon.Write()

#close file...
stacked_file.Close()'''

