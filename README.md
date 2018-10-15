# prot_align_GUI

Graphic user interface that aligns two protein sequences with the selected
substitution matrix using a simplified version of the needleman-wunsch
algorithm.
It is based on my [prot_align script](https://github.com/alfonsosaera/prot_align)

<p align="center">
<img src=img/app_empty.png height="500">
</p>

# Usage

To launch the application in __windows__, open a Command prompt window in the folder of the frontend.py file and type:
```
py frontend.py
```
To lauch the application in __linux__, open a terminal in the folder of the frontend.py file and type:
```
python3 frontend.py
```
or (make sure you made frontend_unix.py executable with `chmod`)

```
./frontend_unix.py
```

```
Alignment score is: 1165

GHR-II  MA--AAL-------------T--LLFCLYILTSSALE--SA--SEQV--H-----PQRDPHLTGCVSANMETFRCRWNVGTLQNLSKPGE  62
        ||                  |  ||  |  | || |   |   |  |  |     |   || | | |   ||||| |  |   ||| ||
GHR-I   MAVFSSSSSSSSSSSSSSSSTSNLLL-L-LLVSS-LDWLSTRGSVFVMDHMTSSAPV-GPHFTECISREQETFRCWWSPGGFHNLSSPGA  86

GHR-II  LRLFYINKLSPLDPPKEWTECPHYS-IDRPNECFFNKNHTSVWTPYKVQLRSRDESTLY-DEN-TFTVDAIVQPDPPVDLTWTTLNESLS  149
        || ||  | ||     || ||| ||   |  ||||  |||||| ||  |||     | | ||   |||  || ||||| | || || | |

GHR-I   LRVFYLKKDSP-N--SEWKECPEYSHLKR--ECFFDVNHTSVWIPYCMQLRGQNNVT-YLDEDYCFTVENIVRPDPPVSLNWTLLNISPS  170

GHR-II  GTYYDIILSWKPPQSADVAMGWMTLQYEVQY--RSASSDLWHAVE--PVTVTQRSLFGLKHNVNHEVRVRCKMLAG-KEFGEFSDSIF--  232
        |  ||    | || ||||  |||   || ||  |      | | |  |   ||    ||      ||  || | |  | ||||||| |
GHR-I   GLSYDVMVNWEPPPSADVGAGWMRIEYEIQYTERN-TTN-WEALEMQP-H-TQQTIYGLQIGKEYEVHIRCRMQAFVK-FGEFSDSVFIQ  255

GHR-II  V-HIPAKVSSFPV-VALLLFGALCLVAILMLVI-ISQQEKLMFILLPPVPGPKIRGIDPELLKKGKLRELTSIL-GGPPN-LR---PELY  314
        |  ||   | ||   ||  || |    || | | ||||  || ||||||| ||| |||||||||||| ||  || ||    |    |  |
GHR-I   VTEIPSQDSNFPFKLALI-FGVLGIL-ILILLIGISQQPRLMMILLPPVPAPKIKGIDPELLKKGKLDELNFILSGGGMGGLSTYAPDFY  343

GHR-II  NNDPWVEFIDLDIEE-QS-DKLTDL--DTDCLMH--RSLSS--N--CTPVSIGFRDDDSGRASCCDPDLPSDPEASPFHP-LIPNQTLSK  393
           ||||||  | |      |      ||  |       |   |  |      | ||||||||| ||||  |         | | |
GHR-I   QDEPWVEFIEVDAEDADAAEKEENQGSDTQRLLDPPQPVSHHMNTGCAN-AVSFPDDDSGRASCYDPDL-HDQDTLMLMATLLPGQPEDG  431

GHR-II  EVS--C-QTAS--EPSS-P-VQSPASGEPPFAALGREAMYTQVSEVRSSGKVLLSPEEQTEV-EKTTG-KD-TEKDIM-AE--KEKAKKE  470
        | |      |   | |  | ||    | |    |     | ||| |  || | |||  |    | |    |   |     |   ||  ||
GHR-I   EDSFDVVERAPVIERSERPLVQTQTGG-PQ-TWLNTD-FYAQVSNVMPSGGVVLSPGQQLRFQESTSAAEDEAQKKGKGSEDSEEKTQKE  518

GHR-II  --FQLLVVNADHG-GYTSELNAGKMS-PRLSIGDQSEPGLTG-D-LSPLP-PASPYHESDTTAVSP--LP--P-----APV--YTVVEGV  542
          ||||||    | ||| | ||   | |  |      ||  |     | |    |         ||  ||  |     |||  ||||  |
GHR-I   LQFQLLVVDPE-GSGYTTESNARQISTPP-ST-PM--PG-SGYQTIHPQPVETKPAATAENNQ-SPYILPDSPQSQFFAPVADYTVVQEV  601

GHR-II  DRQNSLLLTP--NSTPAPQLII-P-KTMPT-PGGYLTPDLLGSITP  583
        | | |||| |     | | |   | |     | || ||||||   |
GHR-I   DSQHSLLLNPPPRQSPPPCLPHHPTKALAAMPVGYVTPDLLGNLSP  647
```
