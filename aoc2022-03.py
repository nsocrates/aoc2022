"""
--- Day 3: Rucksack Reorganization ---
One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.

Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).

The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

For example, suppose you have the following list of contents from six rucksacks:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
The fourth rucksack's compartments only share item type v.
The fifth rucksack's compartments only share item type t.
The sixth rucksack's compartments only share item type s.
To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

Your puzzle answer was 8039.

--- Part Two ---
As you finish identifying the misplaced items, the Elves come to you with another issue.

For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their group. For efficiency, within each group of three Elves, the badge is the only item type carried by all three Elves. That is, if a group's badge is item type B, then all three Elves will have item type B somewhere in their rucksack, and at most two of the Elves will be carrying any other item type.

The problem is that someone forgot to put this year's updated authenticity sticker on the badges. All of the badges need to be pulled out of the rucksacks so the new authenticity stickers can be attached.

Additionally, nobody wrote down which item type corresponds to each group's badges. The only way to tell which item type is the right one is by finding the one item type that is common between all three Elves in each group.

Every set of three lines in your list corresponds to a single group, but each group can have a different badge item type. So, in the above example, the first group's rucksacks are the first three lines:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
And the second group's rucksacks are the next three lines:

wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
In the first group, the only item type that appears in all three rucksacks is lowercase r; this must be their badges. In the second group, their badge item type must be Z.

Priorities for these items must still be found to organize the sticker attachment efforts: here, they are 18 (r) for the first group and 52 (Z) for the second group. The sum of these is 70.

Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?

Your puzzle answer was 2510.
"""

puzzle_input = """qFdBBvtHHfvRlfvsqldvqjPpQmnQmjnjjjTRTLGRNG
ZCWhhCsJCzSJzSbzgsmPTGNNPPNGjgLTLjgn
WJZsbJMwJcszJcScwhVltFwBFBlqddvFdHDfqq
crtTsGTtqFThGQGCrsjTwdNJwpRdnJJwffRClpSf
PWVBPVHLvHHVgvZWBzmPpnfRSJJRQnSRflRPSNSl
gmzBzDgzmZQWLDLLgVmDrqGhsscrqDMGhcqtqcFr
HsbcdVrsbVbcLfPqqQsqqtPj
mMBFzZRnmFMRBDnDFBGZDGdDqLjtdQtPtgfPfttgtqgq
BZvZZdJMBFdJhSvhbhchcHll
GNRSqRfcNTpfGCcqjfzBpDQPWBzgDpQsPWzW
rrSdnVHlbMdLdBDzgtBtBmQt
rbFwwnLFLFwlMLrFwFhMVLrGNSTfZTRhfTqjGJRRZTCNcf
QWTnQCnWNNWmTnSPQwmqDbcscbpcjPjVPbrjpq
vJhzZNlNNgdzgzJdlGzHHcHDpjsHqrvbVrbvrD
RzRdRlhLgtCwCWSLnN
SFTJFTTwTVVSJBnSTdvNNfWbZCZWNZCNNhBv
srLrcHDcsjtLcLLcrLctjlcvbDNhmWCvNhZWGZZhNvhZmb
rclgtMPrrSgVTgJCng
DbrhDzcDffbzNbZvZWSSqSTNSVWv
gCPltPmCPglFnPFwtGPhGPwTCTdZZWZVRvWqdRqVVdTdvR
hLBhlmlstcffBzrpfj
wFLLmhMfwZLDwmMNRhZwRLDvJgldbJHPdQvcQHHJQPgH
bjrVrTSSJdQHcVll
CGCSsCCBpspBrqbSttpbqWmWZRmfFRZhZMNNLFqFLm
zWGjjBHGjzzTWMjhtDDWtPPlJZPJpvqQrmZTqQQpmr
RFbVLcBVLRcRVcCsCCqvpCZqmplqQJmPrlvQ
FLNRRSSRgScSVLLLNdFdwjHjnftBtGMgMjzHgzjWjj
znVSqnqbqzSbzTHqDDZmlcFcnhDMnDmn
LtjsvdvLJdjfFwRRCCMlChwCpMcclCcZ
LgvjjfjFQVgNTgWq
SJRJRFFCMSsGRMMwtZJRCVTgqgTVgTBCVpjTjmmWlB
ccvnnpnDVqTcBVTV
vPHprdHdpnzHSMsSrMRZJGws
GddGrcGNHnGvnCHddvCSWqTSWsTwTWShbHlhhb
gDPzLRVZgQfpRRFQDDVFDfzhSzsTBqqqnqbhnWTSSlST
QVFfFgRQQgLtgffZRfpFPfntjrcrjCmtCdMMmjMdJJJNtm
jjmNcpGCNmDqqsBfnZnGGGRLsZ
lrmlVWlQQtWllgtbQVrWBnZsJgsRLfZLhZBBBffL
rWMVQtrFlbFlSSMHVSdHHNHdcdDcddzppzzm
bTpjpjcVTLmphbLppJwqzqwJLqqzzzgRLJ
sdHNbrvNHrqPvZZZPRww
bNQCrCNtNsSlhffhVhpVWFCW
lpNnpMMZZDbNbnBjcrbjvScFmbGj
wqhdqVqdscrjdLsv
HQftVqWCfhwqtCCjWwfqzzVPZRJQgMlggZMMMZTNMNTnNRTN
fvvGbFtVmtTwgtMT
WcCcClzPCCcczJJScPWWZzBDmwbhBBHSghgDDMTHMDBD
nWPljWzZWnbcbRsNFjFFdFdVjFsj
NQrcLNmQGRfGLHHLZgbbnpjZJJJndbgnlv
DWtThDWtzzhltWTwjbdpvjbgqjgg
VtSPFWtBPBFSFBWCStshWBmlRfHfMRcfQLQLLlmCrCcN
pbmwqJnqSJVwwDPCjZZzrZfD
QtssBTvNdNvNtQvQGpGhdjPjDjczZDfjhgPPDcgjgr
GltptQpMGNNpRWlWFVFHJFHLWH
ZLLsDGGVhZcQQLhrLshrVFwHnWqJnWMnJJJnqfWfGn
jMlPdTlPlgCgFpngFWFnJfpw
TlTNbdSSTSTmTjPMTCdBPjBMrLDczsZcNrDhRNDRQRLLRVVz
HDLpBqDVVTvwGDDNRT
PlVWjfhsPMMmWtlFNTrhrrvCCCTNNbvw
lsglfgVJmsfMjJfSqSzdZnLgqcnLnp
pfCDJWBpfDffpJLgQJzzVzNrgNgNgNhNzmVr
ZnnGZbGTPZnsnRFdTlbrwdrNzrrmmWwmwVwttH
GbPGRvTnZljWnpqSMMCjqJQSCf
ZgnFgwggznFrfrwfHhNMMr
pctLCLRhPHBLMLWfBL
JJcdJcQCCJmQJppmlgndnFslsVnsvghZ
WpMgTppWGSWWJmJDpJcJJhqm
zZzjZNHvNjPvNsbZLbRLzsPcqhVJSVttdwhwmdRhtdJRVd
sLbvvCZCPSSSbbPfNlQQTQGBllCTnMnWQn
fwbwswddwSbBfDBggMBPDPhHcPWDmhHhmWnWPC
FQFlzLCzQTlrTTzvltFqFrmhPHjnhhnnchcJWcRRmRRq
lpLzlFZzCltrTNlTztQLZfSMGBNdSBVwbBNVSMSbVs
FMmgbTFdgLSgFQdjrRPrQBPDdj
ZqqWRvsfGrrPvvPC
wZzwnqccRwRNNpRSMztSMMFbgzLTFS
qTwBPfTfqQDMDrssHdvtRHccHMjR
gWSZGWzGFhnFFgnhNsRHtRdsVjZcRjHs
jgplhpJJFgnDrrwfqprwDP
CWhMSRfWhVVnRSZnVVdsLQqQMzGqLBvGMQqczv
PHbpNwrjJplttvcclLlQzzDszc
NrJbJrFNNJNPrmwrtbjtNmCfSWfWhSZZfSWCsfShfFVR
VLhRPLGLRPRSStRRLwfGqfmDwbmqbqqDlD
rBSFvppnzTbwDwlDcFWm
MJrnJTMvMsrTsPtshRNPZdSLhL
BZBrRCrnCQBBnZfGqhGGMMRcthMhMG
TLjsCdDCPTvNssjdsPsDgsgqGcPHczchtHczWzPWzzlWhG
gsTpsdNbvNNjNSpsNDTsmCnSVQFmSFwZnQBnmnQQ
llbsNsWrmbrGbWCNtBjcCFBzQFZBCFjF
LdSpwgdqSgzwJdRdLMRHLjQQjHjFHctjHBDTZj
gSppgpSJMhpzwrhblfbhhlWlnW
DwhTvvsJZWsBnDzPpBLbFp
GHtNGRGNdzbMBBtmBt
NljlCSVSHdjGSQRGlCQSCswqfWzhZfTcfzcJvshJ
lmsGNFsDGqCbFQBbffjjwpzptw
hRQdvdrvrvSngWnvnHrTMfzfzRtftzwVTwwpzB
HnSSWrvLJvWJGFDsmFLPDFcQ
bwwpGphpLghpTvpWphvJlFLJqqltjSjVlSStSR
cmszZdDdBZzcNcDCDcNsmNMcqVjMJStFRJltVPVrlVPjVJll
HcdmcCzzzQcHNcsCdpnGnhwGgnRggHvbbR
CfMBbwBGbMbDCFrDvhFFDT
mjzRjjRdSmjPnzFZgnnrTT
cmSsVcHjLHTwMfLBpBpBwM
whqqfZzgHvhSzzVNVDbpDbmbVbNpJD
GcQFntGTCCcCTMCTGBlJsJsDDWpRbWBsJpNS
FnPcrGFFdddMnCnTqgqgqPHfLjLqgSzz
zMSzzjssFdGnszRtNftqqwFHbbZw
RRPLVrgrwHqBqgwt
rPWmLCTCQlCQQmmrWLrQShJshhzdhhJjcSjlzRds
lvgvCDfPqLHppqpCCDJncbntttbBtBBVHjwtrB
TdddszSQsWcngjzVbcVZ
hRWsTRTGQhNRGhRTFSWmlpgfqlvLmplPqvvGgv
LbWFLQdWWPwWSjSHPHRfppHHDRpggR
zmqqNNzlzmnzzNCmVCmtBzpfGsfpBgDgspprcfcfsrRB
qNNVNJtNmmmNzznVJzvCTDZWhvZZjZFbWQQhFhbZSw
DjdHqJVVhHVZjhDHPWtDtZLFBRBFmSRTFSbwmRRTffTTJf
NNznnGlgMQsnQzNclzpfSRSMRmfPMmFRwBwB
vzrcGcNcPPvHvHPt
wLCcmZwWTNtZNdMSMGSCnJGGMB
RFbHsPhVvFPRjlshhrnQnGjQGSdSqJfqnQBM
HhzVlFHhPwzScmSTgL
TNlBhDNvNBFpJgpPPpDQ
jjfCdCZZqsCZsbdqPgFGGMRzSFMqQMRS
jnWPtWssCtWcmZbbtstvnrrvhVBhTNNhBHlBlL
DZwNWPDzPVWbJngrQjrNnrQcMg
GRRfttLBhhvTvmLmFcFcgFFSnjWrnsrG
TLthBWtTRLHqhlLLfmhBqVPDJVdPwzJCPPZHwdDdVd
GGVhrVSMQwQqfVssVvnWFgvgWn
jtlcRBBtQRmpWsjzFCvzWnvF
QPcRbpppDmNDtPPblZMfhZdDwdMrqSSGrq
ZRrdtBdQvQsWnnfWFZsF
bJLcMzNDLbMgwfnGMWFv
lpvhmzNDmDmlNbzbmrVVPrHRCPHQBVCP
rZllQrsRWrlQswccMVbGbVbTdcQQ
NtJCntLSHCjznfLTcGGGqWMdWM
jCtzzSFthhSSSjPJrFDlvWrlDZRpwpRZ
mQmbLjbrLQjLmTtwwWBTTvWjtt
BHSqdHclHHNFlppNqWPwfwDvTfDPPtCw
ddSGMGHcdcMhMZnBbmbZmgGJJg
lvvBzvDnlzjfPnfjnQPlldRbVbRqbqqCgsqqVpQQgVqc
NNFtGNMtTNFmJNGNZtZMwVRTTcsCpVTbbgCbgRhscp
FGNGZMtNLWmmJWGFWJGLSNtPrPnBfDzzvjnDBzpnvDBLnv
fwvQRFQvQqwpwNJrwN
BstDnBjhjBhnshSptpJzWqNppbfr
CsDjCdZcBCDcjnfDHfhnfggZMGlgQVmgMTRmgVGMMl
MwlBVqVlsgnmzwJsvjhWZhGPvjvRRWzG
QNQpQpftHdHHCHGfSpCrQNdSrDRDhchhjvjcPrRRWrPvhZjv
LtLSCTSGfHGdGwswnqsggssTqV
qDDCHjzjznTvWshZQWfnZZ
PFFmmNMMtNMVFtczcFPJNrLhZwQZQsSvvSvWvGQQJQssss
tFzrrPPNNFlzVrpRTpblRDqjTpDC
DWDrrBdpmdpBrCgDthdtfcHsqJsCqscqwfsjzHcq
TNLNFNSTQNQTSnlMcczVJjVzsqLDDfJJ
TFPZQRvvlMSPPtRWDtmDRWrBGr
LWGVZdrvWdpLGWRsjPMsHmdHdHldlj
zJzznChzzzCSfTgMhCPDmlDCbmlsmjDDQj
nSTTJhJtnShNtzwhgNrGRRWZZRvMWMtVrqGp
PbPmtNmBbPlqBvqlDJBT
LpGVDzVpVZqqSTvq
pMnWGLRLRppnGpGndrGPtgDCjMPmbPgCQmPPNN
sqcZcbZZpcZspcCCRMmznWGWdLWhwDRGTTWggT
NjFSJgVHrvfVtrGzWdSznDwLSTLn
jFrBNVVjBFNvHrFHBlBFFpMslPgPcpMPmcQPPZCgpP
frddqsThtsTfTbPcvhsrbsRLpRBNRpmDpGmRGcRNLpGp
QWJHCJwWzlHZQZHQCJJRzRqnLDGRGpnGBRnNDN
CVwHCClJjQgWCZVZQgMwSdthjrqvrSPPhdbqtPhs
TvdphBBhhhCgdLNNJJJLWz
fVcsqRVrPcnJWgDnJN
JlqsRJtssZwqwVtPwltRPsHHbFTwTFbpjHhQjTQbvpTF
cQSnPDDQJGNzwnNpZb
RHDrssVRDHRgsRFHRlrVwzzpNGZlfZdppZdwGNZb
sHCHtDgtCjVVLFChqPMhBCMcSTqB
hdbQbqcCCQcqFbCbVdcWCQQlRMBtGlRHBtBMpHhpHThZMR
LLsSLLfgJPrgPnssnmlZtlZpHGHVGfZVtZpl
PvmvgmvvnzmrSsSLJDqDNzqFDQdDwzWWbV
HNNjnLbpLGHvWJDhdWWPpWDW
lVcSNgcSVclhRlPZPRCDCR
cqmSQrwwrrVSrtQFqVNmFwjQnvjHzBbLLGjfjzHTzvnH
QmvWVppPHQQvbbvmSHSpPzfzwnWMTZFFzwFMCzLnwT
jGBljlNNjgDtGDrNjjtjqqDRnMzRLnFzCFnMfRfMzCnttF
jqNrrGdJcdgLjqDqBrDQbbmhdQQmmpPbphmbVv
ZHQCggVHHRDWvbfjGptVtLvL
nnFwnwrDDMShnhFrFLLLpjvPlPGGtLGb
dcNSMhrrTDCBCsWgCTQW
HqDDLGtDdCnhfDnwnV
PmlJsJTPlbdBTzTnzhnnCCWWzV
lSPjMScggsScgjSMMbqHLFGrRLGHRZZtdrcG
ZVVtNNppdZSdLtCPqnHhqJJFtb
zgwwQBfwmGgSrDfgrrGBggzHCnbJbqbCJFnqhHBhnHHCqJ
rvrzfmlRrgDgmrzfggvwzvdjjcccLjMjVcVcsVLjVSZR
dppcLRHpphchhNhSddjzHzWQWQLtrMsrWQCWCsMZssCZ
JGfBfJJfBqvGVlVbDBwDBDBfZnrQsMQtssMttssDsQMWZncn
qPVwlgPBmjpPhcmS
zGPnzBgPzPnPlHZlDDHnZBNCvrtcjcjmMcFzNcNFmFdc
qQpfsLTTSspqTfJdmdCtMjdtjvJcmr
bfQqqSrswLLrfpLTqprfTnDVDVBBbgHPDHnhDPgDbV
JssTnsdFztZLdNJnNtTsLNZGqlbGFBqrGMHqHBcFBqMFMH
CCgSfgPSvSfhpShSRppCdfrlqGHGGcHmclmqbbqbqlPc
wvVSVjQSSQhRVvfQChvZZsdtJstjLNLZDJnLss
CmfNNNZNqDrnDjMhZM
gdczzGtdFcddtWQgGGMnVhnjJwnrJFDPTwMP
dlvcdzdHtzQSLRSfmhLSqv
ZpFFLcHFZZRRmJVZgD
PzhrtQntzcrjCRJtbtRgBsBRVR
zdzWfCzhQzlhWfWhlvpFNlpSqcMSHHMv
NrrMgMhNQhNjQrtqtPtwVtZpggPw
TfRLndnLFCRFTFbbRDHwpVqqBBwsHwZsfH
TJFRdLlRThrlcvZcvQ
scrwRVjbQvQBzsBC
gMfVqNnVmnCBQDTvdn
SMqhWqVlmWSmqMVRSJjjpcFrcLpJrR
HtSQHQntHsHMrtHnGfHQVVzLvSBSVvVVSFNJzzVN
cmPRmpqlpPmcgTlTpjJNjjVDvDRFNVVBFD
hlmCpmqmpgqpZTlcdQHFQfbHHZttwMQwtr
VpWgbgfwCjbftwVPPpGQFQhzTBQTBGPzqFTS
dbRbDcRrsnsRrLZmLRDZldDZqTNTGqqFFzGGhSTNTFTzNmNT
MlLdHlDDHrHclMMrCwgHCCwWwCbCCjjg
GGNLhfDMVcVrcGsT
jSJQFjHbwPFSvQSHwZFvHSHrqCCrrTsqBwNBrcBNsVTsqq
QjZSjZJZPvNRZJQPnSZbJZRWLfnmgDlmhdhWgWLdMdfmhM
CgGnzPNggCJtNTgTZTPZzZZvvcDcDDdqDFcJssJDHDqvHq
jhhrrLVlmLRRnRflfVbFHHHqdVsDqcvbHVDb
jWfWwrlmRRnQmPzZNGZPBNCQTB
NzDDhwNmhvtrGmNCvWRVbcRRVTcHHcVFTbwV
LgsPlLsQgQdJsLdldtpgFFTMbnFqTcMbHqFcPncq
dgsJsLLLggljrhtGNNtSjvGm
ptzSrZtzhsmmtPrhLFRFnjnnLMsnfLRL
HvwVDHwWWgGDGdHgqVDWDMnRnTjFNTNjfLJvRRRRRR
DwDgWgQbDDDHwBBBWdwQGVHhlhlZZSSmztfcppSBhzZcZp
CWmWRzlMJqWDWqCJbqDlCBBVLMQHVMGrfMVtQZrsLL
SnhPdFFPNZsBBdHtVQ
SSPcFFgnwnSpwvcSjwzCqRzTmJbpJCRBmbbD
wQbqGWWSqwrbGWWWGjbNMJPfgfnnDmPnPNLfjN
tJFztRZCvVRCztZFZRVgmMhmgNLfRfnmDPNPhm
BFCVZzpVFlHCdbQqcTcGlJbbSG
tttfLPZZQZTlZPHHPWgMVvBnjmvjnjgGBQ
FzcNDDDrNzprrrshprhFJtVGVnjtjGvnhvVnnjnjGM
RDqJNszDPfdqPtlT
QCJdMjCQbdBjSbTHDsbWDDwHTP
zlvlmqzqGfgdNzLldrHwwPGpWDrPGZWprr
gfVfRczVqcRzmdcSQMjQSQCSjQCQ
RhhCGhRBShjjRfpwppFTfFHZHZZD
qzdqzlnPPctPdmtPdTZbwQvvwqvHHvZpwZ
nVTVTcsWmWSRhhRVrGVB
GmshRMnzqRGsPNwMwcrrpcVV
CDCbFCLvCgfDSFLslgDpwpLtTwwcPtNNtTTprt
JvSFbSbbFllJlgDvlJbgdRhRdqzBGnzshZnRRRnHBZ
ShJhtcsvvvQbnnsccVTLVTppWqddpVnLWp
NdzPrPZgPMNNrmzpTzpTCjWfzCpzVL
dZgHmZRPPZRlZmrPDtDRccvbtQQbJbRS
wqjLjwhznhBLqLWGfvSlvcmlrJsqrtJTJJ
PwbpFPQDRCDrDJTrTmvs
gbZVFbZHgwHbCdpCRMnffNLhWnnzMdzLLW
RVVGSNTTRlNqHblBNB
JfwJMvLLZwLsMJwWMJfwLHBqzFlvzpBQcqzblFbBqblq
wMCZJsgJCCCnsMHrgLLjSPSVTgShtRjTPhRRmt
lmQSSWdMHHLWgWqD
ZZtVGGGJrJvGVCwfgHNLccmNFFcqtc
vrCGPhvrTPdRBnsRTmmp
dDMDDjzCQjwCCcDgjSLLLsLNlmpplN
FqrHFTFRLCLVFBmS
JhHJhHRThrfPZPvhnTZZbWdwdwDDWtDzJDtbMtCW
ghwDzJRDwHmPthncSPncLLsPcvnv
MWCrNTCHrMVjQQMQcSdnpTLnFFdTcnTc
qbWMfWfNrWVQWfbjVBbqMfwDtqzmhmRRzGhtHhHhRwZh
fmSmnjTjrlzGlTzJdH
BrhRRQMrgQvgFFhQQbwpFvGGdZqZJqpJqHVpJGJLHdLJ
ggbDwQMsvsMQrFMFcWSPSCPmSsPfnnmP
cmNVbMrrrjcHDRcvfW
wQGdFfSThFsLhhHWvDCWDCJRCCjd
LtpStGhqrrpnfnpp
bvcccTqbgvpGndJtgdsgNd
wDQwQhtQhQRmSmjsJndJdBBJBJnlLS
hwhmRrzFVjtwzDmrVFrvPCcCMVPPvfqpCCTVVb
jRrRNPNRWjPRWPRQNjQjThTCzBBzDCFBGzgDFGGQ
dnppLwmwCnvtlqltvtnTGBThGhdFZhgzDzGccD
MvnqpLlMqCqCHMjWPPHMSHSs
NNpNNvpvBdtTrMFFMhSSwzjzchzwhzwL
VVndHqflQZZZgHSLLhjzRSmZRhcR
glGgnqbQlngnWCGJpJprtrtFrdPPGs
WqwRjzGtRzZZRRGjWBJzjwmfMTHGGssTTDsrLmmmQLMD
SNdvSdFlSNNhSPFFcPFclbQQslHmfHTDsTQMLgDTmHQQ
CNcCFvpdnWpjWwJf
PVPnVHcnRncGZqbVzHVPnnLbSMjwrzWMjSwDtWwWtwWhwDWz
pTfsQCshCllpglWWSjBMSQSrMrjM
hvpvppggCpJTvTmshgfsmZRRHqbcLPHZmPLRnmPZ
LQbhVZZmZhZjBdbGmgHqnHTmvqgnnWHr
SzCfDFFNRfsSFFMFfvprvpWzqzgqTwHTvp
CDNDFJgMDSQhjVdPJLQG
plpdLdpjjrrHJJjLrrHLFdbzzCcvzgFgcwggzPMFvvcMhM
GRtSBQNsQlMPRzRlzw
ZSTtsmBlmjLLpnpH
hglGNVSdNSghzSgCBhDFLBMBtFMMFtHtbtLL
frQZccRcqGFmFHrJ
nvfGZwvTwGTfQwvfTwfgnCSlpdnzgzslppCsCV
snTSPbQnTTnQgbmsTJsLfZwjffhpLnGRjpGfjL
dcNWcNHHlNtWHHlCtltWNFNMLZwjpGfpmrZfrFprrRGpwZfp
HmdNWCmDMVvQPDgqJs
GGFtSngQLfnSnQffgPnRgFRGRwmRJvwbBbJDwjvTbjrwhJvJ
WHClslcNNWcqNWlCZdcHsVrThBwBjbhDTDBhrvDZJTwm
NWVqqcHHNpsNcNVdVlhCMlHQQMQQzLfzQPttFGPMLSLgtF"""

puzzle_input_2 = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

class Solution:
    def __init__(self, rucksacks, group_count, split_value):
        self.rucksacks = rucksacks.split('\n')
        self.group_count = group_count
        self.split_value = split_value


    def split(self, rucksack):
        ret = []
        length = len(rucksack)
        split_index = length // self.split_value
        start_index = 0
        end_index = split_index
        characters = ''

        while start_index < length:
            if start_index >= end_index:
                end_index += split_index
                ret.append(characters)
                characters = ''
            char = rucksack[start_index]
            characters += char
            start_index += 1

        if characters:
            ret.append(characters)

        return ret


    def get_common(self, compartments):
        if not compartments:
            return ''
        tmp_compartment = compartments.pop()
        while compartments:
            common_characters = []
            compartment = compartments.pop()
            for char in tmp_compartment:
                if char in compartment:
                    common_characters.append(char)
            tmp_compartment = common_characters
        return tmp_compartment[0]


    def get_priority(self, char):
        if not char:
            return 0
        subtrahend = 38 if char.isupper() else 96
        return ord(char) - subtrahend


    def calculate_priority_sum(self, group, initial_value = 0):
        common = self.get_common(group)
        priority = self.get_priority(common)
        return initial_value + priority


    def get_answer(self):
        ret = 0
        group = []
        for i in range(len(self.rucksacks)):
            if len(group) == self.group_count:
                priority_sum = self.calculate_priority_sum(group)
                ret += priority_sum
                group = []
            rucksack = self.rucksacks[i]
            group.append(rucksack)

        priority_sum = self.calculate_priority_sum(group)
        return ret + priority_sum


solution = Solution(puzzle_input, 3, 1)
answer = solution.get_answer()
print(answer) # 2510
