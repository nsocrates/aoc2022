"""
--- Day 7: No Space Left On Device ---
You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?

The device the Elves gave you has problems with more than just its communication system. You try to run a system update:

$ system-update --please --pretty-please-with-sugar-on-top
Error: No space left on device
Perhaps you can delete some files to make space for the update?

You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input). For example:

$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.

Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:

cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
cd / switches the current directory to the outermost directory, /.
ls means list. It prints out all of the files and directories immediately contained by the current directory:
123 abc means that the current directory contains a file named abc with size 123.
dir xyz means that the current directory contains a directory named xyz.
Given the commands and output in the example above, you can determine that the filesystem looks visually like this:

- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
Here, there are four directories: / (the outermost directory), a and d (which are in /), and e (which is in a). These directories also contain files of various sizes.

Since the disk is full, your first step should probably be to find directories that are good candidates for deletion. To do this, you need to determine the total size of each directory. The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)

The total sizes of the directories above can be found as follows:

The total size of directory e is 584 because it contains a single file i of size 584 and no other directories.
The directory a has total size 94853 because it contains files f (size 29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a contains e which contains i).
Directory d has total size 24933642.
As the outermost directory, / contains every file. Its total size is 48381165, the sum of the size of every file.
To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)

Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

Your puzzle answer was 1792222.

--- Part Two ---
Now, you're ready to choose a directory to delete.

The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. You need to find a directory you can delete that will free up enough space to run the update.

In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update. Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.

To achieve this, you have the following options:

Delete directory e, which would increase unused space by 584.
Delete directory a, which would increase unused space by 94853.
Delete directory d, which would increase unused space by 24933642.
Delete directory /, which would increase unused space by 48381165.
Directories e and a are both too small; deleting them would not free up enough space. However, directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.

Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?

Your puzzle answer was 1112963.
"""

example_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

puzzle_input = """$ cd /
$ ls
246027 gldg.jrd
dir qffvbf
dir qjjgh
dir vpjqpqfm
$ cd qffvbf
$ ls
dir dcqf
dir grcj
dir hwllqcd
76103 jrhp.hgg
253696 nscv.wvb
dir stnrzs
dir vzgpfd
$ cd dcqf
$ ls
dir gcjmpnsl
$ cd gcjmpnsl
$ ls
198360 gldg.jrd
$ cd ..
$ cd ..
$ cd grcj
$ ls
56512 grgtnhn.zdn
$ cd ..
$ cd hwllqcd
$ ls
100505 frzf.mzc
209030 gldg.jrd
9330 jjtjjlsr.dnl
191034 mfmps.vjt
82405 nscv.wvb
$ cd ..
$ cd stnrzs
$ ls
dir gmtmfpmb
dir jrhp
dir rhf
dir wzjtd
$ cd gmtmfpmb
$ ls
279472 hswhjhmj
81339 rsgsrn
$ cd ..
$ cd jrhp
$ ls
dir fpmnp
99771 grcj.scb
dir hjglg
dir hwvzv
$ cd fpmnp
$ ls
33215 grcj.tcj
$ cd ..
$ cd hjglg
$ ls
206893 tctfwpf.jhv
$ cd ..
$ cd hwvzv
$ ls
dir mfmps
$ cd mfmps
$ ls
46252 rjrmbqwr.wbj
$ cd ..
$ cd ..
$ cd ..
$ cd rhf
$ ls
222859 dcgvw
41140 grcj.qzh
dir zcjh
217515 zgqjbf
$ cd zcjh
$ ls
92243 prqhbzl.hls
$ cd ..
$ cd ..
$ cd wzjtd
$ ls
dir bnjj
dir dhhpf
dir grcj
dir jqmnp
16602 mfmps.dht
dir mrgh
112236 rsgsrn
dir wqwwwfd
243851 zgqjbf.bjh
$ cd bnjj
$ ls
158778 zjdvggcz.fhr
$ cd ..
$ cd dhhpf
$ ls
228680 gldg.jrd
18523 wcfpqqp.tcf
$ cd ..
$ cd grcj
$ ls
dir bcbspw
dir mpq
dir pjzw
$ cd bcbspw
$ ls
5449 rsgsrn
$ cd ..
$ cd mpq
$ ls
135338 mfmps
$ cd ..
$ cd pjzw
$ ls
dir cpffwn
$ cd cpffwn
$ ls
131835 rnwqngz
$ cd ..
$ cd ..
$ cd ..
$ cd jqmnp
$ ls
281939 nscv.wvb
103834 rsgsrn
34528 wcfpqqp.tcf
$ cd ..
$ cd mrgh
$ ls
dir grcj
$ cd grcj
$ ls
211470 bbzm.sbq
$ cd ..
$ cd ..
$ cd wqwwwfd
$ ls
59532 blfr.lqh
$ cd ..
$ cd ..
$ cd ..
$ cd vzgpfd
$ ls
dir grcj
dir lvhfqr
dir zgvjpnf
$ cd grcj
$ ls
160936 jbfsbsnn.sgj
dir mfmps
dir mfqjssr
dir vzgpfd
dir zgqjbf
$ cd mfmps
$ ls
176441 dcgvw
9961 grcj.sdl
dir mfmps
181303 nscv.wvb
273550 zfjhqtp
$ cd mfmps
$ ls
dir ndqjhlhp
$ cd ndqjhlhp
$ ls
43593 wcfpqqp.tcf
$ cd ..
$ cd ..
$ cd ..
$ cd mfqjssr
$ ls
137211 gldg.jrd
254301 grcj.rgv
$ cd ..
$ cd vzgpfd
$ ls
dir hqnfwtj
dir mtqzh
215717 thd.cgt
dir vgtvctd
dir vzgpfd
64282 zgqjbf
$ cd hqnfwtj
$ ls
155738 cjpqzq
128579 cnsm.mdt
150972 fpmjd
54851 rsgsrn
$ cd ..
$ cd mtqzh
$ ls
288824 bjnhtwg
209838 gldg.jrd
87464 jgdhm.wrb
dir nbnzfc
$ cd nbnzfc
$ ls
dir rtrbhtb
267378 wcfpqqp.tcf
152165 wsww.gdd
$ cd rtrbhtb
$ ls
264454 dcgvw
221078 jrhp.fsj
dir sgm
$ cd sgm
$ ls
dir tzzfc
$ cd tzzfc
$ ls
207888 cdmht.jjn
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd vgtvctd
$ ls
dir dtm
dir gghjmgqs
dir grcj
dir lcpmlcpn
57113 njpnzq.phl
279566 rsgsrn
59404 tzl
221164 vcpzw.qsh
$ cd dtm
$ ls
dir pmsvz
dir zdzv
$ cd pmsvz
$ ls
dir qctt
$ cd qctt
$ ls
285640 wzh.hwv
$ cd ..
$ cd ..
$ cd zdzv
$ ls
178732 fdvth.rvs
dir jjslblcb
dir tvq
dir zgqjbf
$ cd jjslblcb
$ ls
dir grcj
$ cd grcj
$ ls
186485 wcfpqqp.tcf
$ cd ..
$ cd ..
$ cd tvq
$ ls
48035 jrhp.qnf
$ cd ..
$ cd zgqjbf
$ ls
276537 gldg.jrd
$ cd ..
$ cd ..
$ cd ..
$ cd gghjmgqs
$ ls
238068 qqczbf
$ cd ..
$ cd grcj
$ ls
dir qnn
$ cd qnn
$ ls
117284 jmst.mld
$ cd ..
$ cd ..
$ cd lcpmlcpn
$ ls
dir cbzpzsj
53036 frzslwl.qgd
82430 grcj
273768 pvzslpsn.ztw
67092 rsgsrn
$ cd cbzpzsj
$ ls
36456 gldg.jrd
95656 mfmps.cfl
2578 qpl.jhn
225756 sqt.njp
$ cd ..
$ cd ..
$ cd ..
$ cd vzgpfd
$ ls
266582 cgvcwrfn.jjq
230770 dcgvw
266361 gqqcqtp.hvq
dir lnn
86659 pzft.smj
180519 qfszrvm.gnq
dir rwrt
dir thrthq
dir zgqjbf
$ cd lnn
$ ls
13294 dqqvbcf
268614 mczrlg.vmz
dir wqccmlvq
dir zgqjbf
$ cd wqccmlvq
$ ls
dir grcj
$ cd grcj
$ ls
55504 gldg.jrd
6925 jbqzth.rcj
168475 jqzmc.sfm
$ cd ..
$ cd ..
$ cd zgqjbf
$ ls
172255 nptpqjd.hzz
$ cd ..
$ cd ..
$ cd rwrt
$ ls
78039 jrhp.cmf
237632 mfmps
$ cd ..
$ cd thrthq
$ ls
122514 jrhp.fcj
$ cd ..
$ cd zgqjbf
$ ls
dir dpbnq
dir mfmps
dir rbnzhhn
$ cd dpbnq
$ ls
dir vzgpfd
$ cd vzgpfd
$ ls
278947 bhdtwf
$ cd ..
$ cd ..
$ cd mfmps
$ ls
118315 mfmps.lbq
$ cd ..
$ cd rbnzhhn
$ ls
96386 svwv.ldj
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd zgqjbf
$ ls
196735 cmrdgjl.hbd
$ cd ..
$ cd ..
$ cd lvhfqr
$ ls
dir njzv
dir sgwzscp
dir zgqjbf
$ cd njzv
$ ls
60680 bmqh.snz
129703 wcfpqqp.tcf
$ cd ..
$ cd sgwzscp
$ ls
dir rnjrj
1799 vzgpfd
37203 zgqjbf.jwf
25768 zjh
$ cd rnjrj
$ ls
242223 blrzc
63563 plb.dlq
$ cd ..
$ cd ..
$ cd zgqjbf
$ ls
91151 cmn.gcw
235818 llsnw.phb
$ cd ..
$ cd ..
$ cd zgvjpnf
$ ls
158932 nscv.wvb
110912 wzm
$ cd ..
$ cd ..
$ cd ..
$ cd qjjgh
$ ls
dir cwslqsb
34405 dcgvw
dir fvmmd
dir jrhp
dir vflhljrl
239915 vzgpfd
$ cd cwslqsb
$ ls
49934 mqzfncgb.jbf
$ cd ..
$ cd fvmmd
$ ls
dir grcj
dir jrhp
dir sqmbncp
dir vzgpfd
$ cd grcj
$ ls
32276 bjgc
211068 mfmps
$ cd ..
$ cd jrhp
$ ls
218633 wpqh.jfl
$ cd ..
$ cd sqmbncp
$ ls
137187 tzqqm.jqr
$ cd ..
$ cd vzgpfd
$ ls
258286 hqg.qzn
dir mvqgb
236455 vqdtns
255724 wrnhw.mzf
192529 zgqjbf.zzb
$ cd mvqgb
$ ls
dir vzgpfd
$ cd vzgpfd
$ ls
200955 grcj.wwl
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd jrhp
$ ls
86368 dcgvw
16512 vzgpfd
245341 wcfpqqp.tcf
$ cd ..
$ cd vflhljrl
$ ls
82670 gldg.jrd
228251 nscv.wvb
$ cd ..
$ cd ..
$ cd vpjqpqfm
$ ls
246705 gfff
dir grcj
dir hjdwrt
dir mfmps
dir plrrsmph
dir rgqtzc
175555 rsgsrn
142983 wjpbr.hdr
dir zlv
$ cd grcj
$ ls
dir grcj
dir mdvcmm
285341 mfmps
89089 nscv.wvb
$ cd grcj
$ ls
dir fcdz
dir fswpmd
dir gvjjjp
dir jrhp
$ cd fcdz
$ ls
dir dpwvm
dir rmmw
$ cd dpwvm
$ ls
dir chjbpb
118852 dcgvw
dir dsc
7271 fclhnmz.cbp
$ cd chjbpb
$ ls
41211 pzr
$ cd ..
$ cd dsc
$ ls
217960 nscv.wvb
$ cd ..
$ cd ..
$ cd rmmw
$ ls
dir cqzvcv
dir hld
99687 jrhp.nnb
dir pfvthfw
97451 qjmfdjwz.phc
$ cd cqzvcv
$ ls
dir zgqjbf
$ cd zgqjbf
$ ls
204153 nscv.wvb
$ cd ..
$ cd ..
$ cd hld
$ ls
113905 pwqs
244609 wfsgg.jgp
$ cd ..
$ cd pfvthfw
$ ls
dir grcj
$ cd grcj
$ ls
207441 jrhp
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd fswpmd
$ ls
99446 gldg.jrd
$ cd ..
$ cd gvjjjp
$ ls
dir pvzz
279071 wdmm.vjv
$ cd pvzz
$ ls
196937 nqfzj
273491 nscv.wvb
dir qthbl
$ cd qthbl
$ ls
204553 dcgvw
$ cd ..
$ cd ..
$ cd ..
$ cd jrhp
$ ls
175979 fct.dcg
$ cd ..
$ cd ..
$ cd mdvcmm
$ ls
dir crscnnh
109461 dcdtm.tvp
279544 ftzvrpcw.pff
124059 nnc
274104 nscv.wvb
dir ssvd
dir zvvhlw
$ cd crscnnh
$ ls
dir tzbjl
$ cd tzbjl
$ ls
112219 wcfpqqp.tcf
$ cd ..
$ cd ..
$ cd ssvd
$ ls
227906 bsqhzw
$ cd ..
$ cd zvvhlw
$ ls
166628 gldg.jrd
$ cd ..
$ cd ..
$ cd ..
$ cd hjdwrt
$ ls
59644 jrhp.fjj
dir rpsrm
221706 rsgsrn
dir rzn
14344 tvlmvr.flr
dir vlbrnq
dir vrcns
39113 wcfpqqp.tcf
dir zhwm
$ cd rpsrm
$ ls
282957 wmpnpjzd
$ cd ..
$ cd rzn
$ ls
142973 wcfpqqp.tcf
$ cd ..
$ cd vlbrnq
$ ls
79661 ccznjt.fqr
$ cd ..
$ cd vrcns
$ ls
262645 dcnnnhn.vhg
$ cd ..
$ cd zhwm
$ ls
dir glgs
dir grcj
dir jrhp
$ cd glgs
$ ls
282326 tcw.qnb
$ cd ..
$ cd grcj
$ ls
43293 qnqb.jqg
$ cd ..
$ cd jrhp
$ ls
197274 pgf.ltc
$ cd ..
$ cd ..
$ cd ..
$ cd mfmps
$ ls
dir dcm
47902 mrcn.wtb
8444 mzdgdh.ctn
$ cd dcm
$ ls
72397 mnrvqg.vmm
$ cd ..
$ cd ..
$ cd plrrsmph
$ ls
216816 gldg.jrd
148190 jzbswh
120319 wcfpqqp.tcf
dir zgqjbf
$ cd zgqjbf
$ ls
dir cfdr
dir hdsnc
$ cd cfdr
$ ls
34272 bzctmbvt.qzr
$ cd ..
$ cd hdsnc
$ ls
43772 ccds.vlz
$ cd ..
$ cd ..
$ cd ..
$ cd rgqtzc
$ ls
dir dblznh
dir lfpdqm
dir lmnmthm
dir mfmps
dir pcplzs
dir pvfbjm
dir rnl
dir wqgp
dir zgqjbf
$ cd dblznh
$ ls
65168 tdv.mwq
$ cd ..
$ cd lfpdqm
$ ls
dir cgvnspv
dir dthhvrln
dir jrhp
dir vzgpfd
$ cd cgvnspv
$ ls
dir qnmg
$ cd qnmg
$ ls
dir grcj
70937 jbvrp.psn
207093 vfgds.tjv
282330 vtlzgq.dfd
251235 zbvgc.whr
$ cd grcj
$ ls
dir pbn
$ cd pbn
$ ls
22094 dqt.dtv
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd dthhvrln
$ ls
206159 wvvczgd.wzs
$ cd ..
$ cd jrhp
$ ls
dir bqf
5738 rgpwf
dir zjhw
$ cd bqf
$ ls
dir clgjfn
58416 fcr
216467 mcdqnw.prv
288978 zthdgfhl.lqq
$ cd clgjfn
$ ls
274929 lwnpggm.mfp
$ cd ..
$ cd ..
$ cd zjhw
$ ls
dir cbwrrzwh
dir fdz
dir grcj
219439 grcj.szv
285756 mfmps
113288 mmg.cpr
236059 nmq
dir pbnfdq
74013 tvmswr
dir zgqjbf
$ cd cbwrrzwh
$ ls
223425 zgqjbf.ffm
$ cd ..
$ cd fdz
$ ls
dir wbtzsr
$ cd wbtzsr
$ ls
257781 hzf
$ cd ..
$ cd ..
$ cd grcj
$ ls
58266 dcgvw
dir rhncgdll
dir vzgpfd
12503 zgv.ndt
$ cd rhncgdll
$ ls
dir vnmbhbhc
$ cd vnmbhbhc
$ ls
10019 lfcggd.ccw
$ cd ..
$ cd ..
$ cd vzgpfd
$ ls
134965 zdsp.tzg
78684 zmjjvf.glv
$ cd ..
$ cd ..
$ cd pbnfdq
$ ls
173729 frqdqhw
dir fvjc
41055 svwd
106934 tngzpl.lml
dir zqhjjjd
$ cd fvjc
$ ls
88907 pcvcpptp.dsr
133102 tszsbtjp.lfl
$ cd ..
$ cd zqhjjjd
$ ls
61260 mpdlcjl
dir wfw
$ cd wfw
$ ls
dir jrhp
dir lwg
226393 rndnc
dir zhrtj
$ cd jrhp
$ ls
276912 dcgvw
dir pwrjq
dir zmnv
$ cd pwrjq
$ ls
198180 vclfmjf.tfp
$ cd ..
$ cd zmnv
$ ls
84228 mfmps.wzw
$ cd ..
$ cd ..
$ cd lwg
$ ls
dir jrhp
50562 lwcfwjh.dtm
145174 vnl
$ cd jrhp
$ ls
86877 dcgvw
$ cd ..
$ cd ..
$ cd zhrtj
$ ls
284728 rsgsrn
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd zgqjbf
$ ls
202268 zqpvm
$ cd ..
$ cd ..
$ cd ..
$ cd vzgpfd
$ ls
138188 djqqfrbn.cps
$ cd ..
$ cd ..
$ cd lmnmthm
$ ls
2715 fqdm.bvm
37482 jdsn.zpr
255467 nscv.wvb
175914 stvscbg
$ cd ..
$ cd mfmps
$ ls
288712 gldg.jrd
182389 jrhp
dir lvjg
41815 nscv.wvb
dir vzgpfd
dir zgqjbf
dir zvpnq
$ cd lvjg
$ ls
184529 wcfpqqp.tcf
$ cd ..
$ cd vzgpfd
$ ls
265556 hjqng.glq
$ cd ..
$ cd zgqjbf
$ ls
dir dqmbmlrf
dir grcj
dir hlsr
$ cd dqmbmlrf
$ ls
dir bdvhvwct
254123 bzhhm.rqp
172950 fgqbj.bcb
7417 fjfq.qbv
188707 hfvvlvqg.sqh
78273 ppljtfjr.hpm
dir zgqjbf
$ cd bdvhvwct
$ ls
76840 gldg.jrd
dir grcj
$ cd grcj
$ ls
dir vzgpfd
$ cd vzgpfd
$ ls
73163 mfmps.tnr
$ cd ..
$ cd ..
$ cd ..
$ cd zgqjbf
$ ls
62316 lpzsww
$ cd ..
$ cd ..
$ cd grcj
$ ls
160721 bwvgdqdr
$ cd ..
$ cd hlsr
$ ls
214688 vzgpfd
$ cd ..
$ cd ..
$ cd zvpnq
$ ls
34940 gjbzp.nqg
165326 mfmps.gfp
dir rwddqchj
dir ssw
dir zgqjbf
$ cd rwddqchj
$ ls
dir gnsndln
$ cd gnsndln
$ ls
223320 zgqjbf.wlm
$ cd ..
$ cd ..
$ cd ssw
$ ls
dir grcj
$ cd grcj
$ ls
251146 gldg.jrd
$ cd ..
$ cd ..
$ cd zgqjbf
$ ls
45732 vzgpfd.nbz
86126 zdnv.sss
$ cd ..
$ cd ..
$ cd ..
$ cd pcplzs
$ ls
90287 grcj
99213 rsgsrn
dir shmsp
156357 tgc.lzp
dir thbznt
dir vtqlszrs
dir vzgpfd
$ cd shmsp
$ ls
dir jrhp
$ cd jrhp
$ ls
132784 tmlntm
$ cd ..
$ cd ..
$ cd thbznt
$ ls
190697 mdj.lll
270626 wcfpqqp.tcf
$ cd ..
$ cd vtqlszrs
$ ls
44292 dcgvw
$ cd ..
$ cd vzgpfd
$ ls
13921 hccgnjqh.cdl
dir jrhp
23850 jvq
113952 mfmps
dir ppdfjqbr
dir vdpvzhrs
190631 vzgpfd
128060 wclfwhv.chh
dir wghzqb
$ cd jrhp
$ ls
237755 bgbmnpq
19551 dcgvw
$ cd ..
$ cd ppdfjqbr
$ ls
1458 dcgvw
563 gldg.jrd
155487 glhjmpm.sjt
dir vthf
dir vzgpfd
81314 zgqjbf.scm
$ cd vthf
$ ls
205316 vzgpfd.qlg
$ cd ..
$ cd vzgpfd
$ ls
46597 mfmps.zsq
$ cd ..
$ cd ..
$ cd vdpvzhrs
$ ls
13302 vcwrr.jvb
$ cd ..
$ cd wghzqb
$ ls
dir grcj
dir hbngsg
112293 jzvh.pvf
282888 smrq.lvp
$ cd grcj
$ ls
258764 nscv.wvb
230478 qpqgf
$ cd ..
$ cd hbngsg
$ ls
101699 bzwnwz.tgj
144196 hwjrgtt.pdm
dir mthnljv
$ cd mthnljv
$ ls
1397 jrhp.rvp
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd pvfbjm
$ ls
251602 nscv.wvb
$ cd ..
$ cd rnl
$ ls
233954 dqlncnds.dfn
dir nswpmqdd
$ cd nswpmqdd
$ ls
261883 rtpbgm.gbf
$ cd ..
$ cd ..
$ cd wqgp
$ ls
23813 pdfcfc
$ cd ..
$ cd zgqjbf
$ ls
15126 bvlbrq.pdj
dir jnjqhzh
dir smrzsq
dir vzgpfd
$ cd jnjqhzh
$ ls
243919 htdqwdc.nsr
254015 ppclcr.rms
234928 zmjr.hnt
$ cd ..
$ cd smrzsq
$ ls
dir ljvbmm
$ cd ljvbmm
$ ls
235241 jmcbrbdl.ccr
$ cd ..
$ cd ..
$ cd vzgpfd
$ ls
dir bhwd
38855 dcgvw
dir hdcqm
dir swcvhtmp
dir zgqjbf
118104 zhtlsdb.ncw
$ cd bhwd
$ ls
122018 gldg.jrd
dir lmjr
dir mfmps
$ cd lmjr
$ ls
40588 dcgvw
$ cd ..
$ cd mfmps
$ ls
dir grcj
$ cd grcj
$ ls
165840 zwbvbfj
$ cd ..
$ cd ..
$ cd ..
$ cd hdcqm
$ ls
156543 qfb.vhv
$ cd ..
$ cd swcvhtmp
$ ls
227964 rrfnsqw.rvh
$ cd ..
$ cd zgqjbf
$ ls
94269 mfmps.jsq
266360 rsgsrn
252761 zlz
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd zlv
$ ls
127388 nscv.wvb"""

import re

class Solution:
    def __init__(self, terminal_outputs, size_limit, total_space_available, minimum_space):
        self.terminal_outputs = re.split('\n', terminal_outputs)
        self.size_limit = size_limit
        self.total_space_available = total_space_available
        self.minimum_space = minimum_space
        self.current_path = []
        self.directory_map = {}

    def get_or_create_directory(self, directory_name = None):
        directory = self.directory_map
        for path in self.current_path:
            if path not in directory:
                directory[path] = {'name': path}
            directory = directory[path]
        if directory_name:
            if directory_name not in directory:
                directory[directory_name] = {'name': directory_name}
            directory = directory[directory_name]
        return directory

    def map_directory(self, terminal_output):
        p = re.compile(r'(?<=cd\W).+')
        search = p.search(terminal_output)
        if search is None:
            return
        directory_name = search.group(0)
        if directory_name == '..':
            self.current_path.pop()
        else:
            self.current_path.append(directory_name)
        self.get_or_create_directory()

    def map_contents(self, start_index):
        size = 0
        for i in range(start_index, len(self.terminal_outputs)):
            terminal_output = self.terminal_outputs[i]
            if terminal_output[0] == '$':
                break
            if 'dir' in terminal_output:
                p = re.compile(r'(?<=dir\W).+')
                directory_name = p.search(terminal_output).group(0)
                self.get_or_create_directory(directory_name)
            else:
                p = re.compile(r'^\d+')
                search = p.search(terminal_output)
                if search is not None:
                    file_size = int(search.group(0))
                    size += file_size
        current_directory = self.get_or_create_directory()
        current_directory['current_size'] = size

    def build_map(self):
        for i in range(len(self.terminal_outputs)):
            terminal_output = self.terminal_outputs[i]
            if terminal_output[0] == '$':
                if 'cd' in terminal_output:
                    self.map_directory(terminal_output)
                if 'ls' in terminal_output:
                    self.map_contents(i + 1)

    def build_total_size(self, directory_map = None):
        directory_map = directory_map or self.directory_map
        total_size = directory_map.get('current_size', 0)
        for key in directory_map:
            value = directory_map[key]
            if isinstance(value, dict):
                child_size = self.build_total_size(value)
                total_size += child_size
        directory_map['total_size'] = total_size
        return total_size

    def get_sum_total_within_limit(self, directory_map = None):
        directory_map = directory_map or self.directory_map['/']
        total_size = directory_map.get('total_size', 0)
        sum_total = 0
        if total_size <= self.size_limit:
            sum_total = total_size
        for key in directory_map:
            value = directory_map[key]
            if isinstance(value, dict):
                child_total = self.get_sum_total_within_limit(value)
                sum_total += child_total
        return sum_total

    def find_candidates_to_delete(self, directory_map = None):
        ret = []
        directory_map = directory_map or self.directory_map['/']
        current_size = self.total_space_available - self.directory_map['/']['total_size']
        size_to_remove = self.minimum_space - current_size
        if size_to_remove <= directory_map['total_size']:
            ret.append({'name': directory_map['name'], 'total_size': directory_map['total_size']})
        for key in directory_map:
            value = directory_map[key]
            if isinstance(value, dict):
                candidates = self.find_candidates_to_delete(value)
                ret.extend(candidates)
        return ret

    def get_smallest_size_to_delete(self):
        directory_size = float('inf')
        candidates = self.find_candidates_to_delete()
        for candidate in candidates:
            if candidate['total_size'] < directory_size:
                directory_size = candidate['total_size']
        return directory_size

    def get_answer(self):
        self.build_map()
        self.build_total_size()
        return self.get_smallest_size_to_delete()
        # return self.get_sum_total_within_limit()


solution = Solution(puzzle_input, 100000, 70000000, 30000000)
print(solution.get_answer())
