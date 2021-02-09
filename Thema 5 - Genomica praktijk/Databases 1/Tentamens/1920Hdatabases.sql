/*
This database contains information about the expression of genes
as determined by single cell RNA sequencing.
*/

drop table if exists gene_expressions;
drop table if exists cells;
drop table if exists genes;

create table genes
(   id              int             not null unique,
    gene_symbol     varchar(255),
    primary key(id)
);

-- information cell type on position of the cell in the sequencer
-- lane contains data on the chip identifier + lane location
-- sample contains the identifier for the donor the cell originated from
create table cells
(   id              int             auto_increment,
    x_coord         int             not null,
    y_coord         int             not null,
    cell_type       varchar(255),
    stimulated      varchar(255)    not null,
    sample          varchar(255)    not null,
    lane            varchar(255),
    primary key(id)
);

create table gene_expressions
(   id              int             auto_increment,
    cell            int             not null,
    gene            int             not null,
    expression_value    float       not null,
    primary key(id),
    foreign key(gene) references genes(id),
    foreign key(cell) references cells(id)
);

insert into genes values (1,'>lcl|MAL1P4.01');
insert into genes values (2,'>gi|124505647 MAL1P4.02');
insert into genes values (3,'>gi|124505649 MAL1P4.03');
insert into genes values (4,'>gi|124505651 MAL1P4.04');
insert into genes values (5,'>gi|124505653 MAL1P4.06');
insert into genes values (6,'>gi|124505655 MAL1P4.06b');
insert into genes values (7,'>gi|124505657 MAL1P4.07');
insert into genes values (8,'>gi|124505659 MAL1P4.08');
insert into genes values (9,'>gi|124505661 MAL1P1.9aa');
insert into genes values (10,'>gi|124505663 MAL1P1.9a');

insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(754, 688, 'liver', 1, 'MFEBGUNW@P', 'chip: NRJWGT@ONLL  lane: EEJ@ME?JQYF');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(333, 297, 'liver', 0, 'PKJGUJWGY@', 'chip: RWYONOWLOEP  lane: PKVIGVTGDD@');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(410, 186, 'blood', 1, 'EPMTGMP@TH', 'chip: BBYJDSUADYC  lane: LSL?KFQNU?K');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(68, 409, 'muscle', 1, '?CHU?BCEMR', 'chip: QS?WMMGYL@V  lane: SJXHMJEKN?H');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(72, 362, 'blood', 0, 'EQ@IAXNMAJ', 'chip: HNOHXBKQYTK   lane: FVJHGHR@XYN');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(746, 996, 'blood', 0, 'IIS@QHEFGV', 'chip: DHP?DDIMCWR  lane: QUKET?BDBIB');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(139, 71, 'muscle', 1, 'X@TOR@NJQW', 'chip: PPVMGHQE@IX  lane: RJCVFQVPVPW');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(428, 288, 'blood', 0, 'TAJSSDAXHI', 'chip: LPORPCC@APY  lane: FNIAYWFXODW');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(461, 724, 'blood', 1, 'YSGCDRUQNV', 'chip: MRGPJFBKKV?  lane: UVYBOWCYDIN');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(690, 145, 'blood', 0, 'XH?PGEXEFX', 'chip: CULLII@MUMS  lane: PD?TUORMQE@');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(158, 619, 'blood', 0, 'VDDUQAIJVO', 'chip: @Y@CPOJRVSL  lane: ?LIYVBPXWNB');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(299, 185, 'brain', 1, 'GCEFHRSOUU', 'chip: DVBYIAOWGWL  lane: AWETGWIPMXE');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(681, 255, 'blood', 0, 'GWHMACE?RF', 'chip: OUOWEP@U?OQ  lane: OYXPABXNVER');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(838, 612, 'liver', 1, '@PBWLTINNK', 'chip: VACPXTYFSJ@  lane: PHIIB@HDHRI');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(941, 859, 'brain', 0, 'KUQF?S@@VL', 'chip: ?BEPAWSGGGD  lane: QBV@PHSCBM@');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(374, 625, 'liver', 1, '@DFQEHLHLV', 'chip: @B@BPEHPPAH  lane: SNR@FWWT?@L');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(372, 483, 'liver', 0, 'LSJ@OSDGQA', 'chip: HUNW?QYGPRR  lane: AWOOOJFFCMF');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(721, 129, 'brain', 1, 'HG@XUKWEXF', 'chip: NKAKRSSVTVW  lane: BK@?OLJOMTX');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(249, 788, 'liver', 1, 'ROCJSXKSKF', 'chip: PDXPPOOEVAX  lane: INTWPAUO?YT');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(997, 526, 'brain', 1, 'JBEOAU?YBS', 'chip: ODRMEDUNUJE  lane: QGGFCNMRLPK');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(732, 502, 'blood', 0, 'BWQDRUQIKW', 'chip: VOHVGPBCHWX  lane: VQD?LIEOEQX');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(47, 600, 'blood', 1, 'VLCGSONKXP', 'chip: SAVGNI@TC@L   lane: @TBWYVO?YIH');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(454, 139, 'muscle', 0, 'DYX@EQIP?@', 'chip: IBVVX@ASMVJ lane: VQFIUPNNXQW');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(884, 691, 'liver', 0, 'LHGTIBIQ?J', 'chip: YLBDTXFODSC  lane: DCXQ?@SLQA?');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(751, 845, 'blood', 1, 'FDNPMNII@?', 'chip: AQPXYPLUDXV  lane: QUIQWBUAB@E');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(18, 434, 'liver', 0, 'OHBTHQEXE@', 'chip: JNN?F@VP@KL   lane: HVUGODDHEDS');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(916, 212, 'brain', 0, 'QHLXMPIKX@', 'chip: FUO@NQKJNA?  lane: MOBLLICX?JY');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(580, 51, 'brain', 1, '?VTTCMFWVS', 'chip: XQ??RHOSGQV   lane: I@XQWARBTIS');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(388, 757, 'brain', 1, 'T@AXJYVRSW', 'chip: CYASRBTGCPQ  lane: PMXNRRUHAPW');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(86, 510, 'liver', 1, 'ANFPFM@PXU', 'chip: YWHS?FFPYLM   lane: LCPJCXPK?VF');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(958, 768, 'brain', 0, 'CM?CYSIJVC', 'chip: OGHBNORSI@I  lane: CYD@SSUKXAF');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(275, 591, 'brain', 0, '?YNISWTHIG', 'chip: QJDJTUEPBBI  lane: GYSCMEITRTL');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(472, 498, 'blood', 0, 'KIHYCP@DOE', 'chip: QGGVPMSXEUN  lane: ?NANAXHKWON');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(253, 907, 'blood', 1, 'BTOTTKQGBE', 'chip: HCRGYEVHCWI  lane: HPHPQOV?BRW');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(976, 478, 'muscle', 0, 'WTJSRUWNNS', 'chip: PLKTPT?BD?V lane: LDFMKNABRTS');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(555, 597, 'brain', 1, 'QFSN@OXAJC', 'chip: RSRLAYTWTUY  lane: ACHLSPORXSW');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(713, 109, 'brain', 0, 'YAU?TEHWYS', 'chip: HXUTIYPGW@I  lane: ISLIRSGCDQV');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(200, 462, 'brain', 0, '@LSMPH?@TR', 'chip: MRAQYMUOBIC  lane: WIXJUPAOTJU');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(451, 867, 'liver', 1, 'LBY??JUKEC', 'chip: LAU@LDQEFXO  lane: NFHWCPEVRJN');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(360, 218, 'liver', 1, 'AVCI@YTODG', 'chip: ?@UHVBH@EVC  lane: IHJWEBIFTI?');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(629, 201, 'muscle', 0, 'FHJFJANDNG', 'chip: NDYRWQBTPQO lane: DSN?LDSQ@EN');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(297, 733, 'liver', 1, 'KCM??PWG@U', 'chip: AALIQ@TKMET  lane: HIGCA?S@?CJ');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(372, 986, 'brain', 1, 'UWIHMEGJLO', 'chip: TTQKWXXSOIN  lane: IGFKVWMDDAR');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(732, 303, 'blood', 1, 'SVUASDPCUD', 'chip: DVNFACWPQB?  lane: DMMHYVA??XN');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(904, 642, 'muscle', 1, '?P@NNYJMRU', 'chip: IYJUGTYTQSK lane: OPHQ@HBSOJX');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(62, 360, 'brain', 0, 'INCBVH@NFT', 'chip: IHSDQXESCWY   lane: SPLEIISTXMW');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(479, 158, 'blood', 1, 'OVCAEIYIXE', 'chip: B?LHA@DSCJM  lane: XCJPJBRRUTY');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(176, 902, 'blood', 1, 'HQYMKSLTYB', 'chip: KG@X@QBPSVG  lane: SVTBLA@DBFY');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(494, 654, 'liver', 1, '?DLOCOMKBD', 'chip: CCCGQIVFIVV  lane: UPHAXF?XWDH');
insert into cells(x_coord, y_coord, cell_type, stimulated, sample, lane) values(697, 974, 'muscle', 0, 'I?WXLQC?C@', 'chip: B@AUWJWAJKT lane: ?MHFMDTVPSC');


insert into gene_expressions(cell, gene, expression_value) values(42, 2, 71.54793579543336);
insert into gene_expressions(cell, gene, expression_value) values(19, 1, 9.020183334907783);
insert into gene_expressions(cell, gene, expression_value) values(41, 6, 55.26210727544776);
insert into gene_expressions(cell, gene, expression_value) values(21, 2, 19.03217466360444);
insert into gene_expressions(cell, gene, expression_value) values(16, 6, 15.26274083100676);
insert into gene_expressions(cell, gene, expression_value) values(22, 9, 90.32922283624147);
insert into gene_expressions(cell, gene, expression_value) values(43, 7, 38.63279031984613);
insert into gene_expressions(cell, gene, expression_value) values(1, 8, 90.35363992962353);
insert into gene_expressions(cell, gene, expression_value) values(27, 5, 82.29387186054464);
insert into gene_expressions(cell, gene, expression_value) values(29, 8, 23.244710434039373);
insert into gene_expressions(cell, gene, expression_value) values(47, 6, 88.87714500727222);
insert into gene_expressions(cell, gene, expression_value) values(45, 1, 18.58472699680005);
insert into gene_expressions(cell, gene, expression_value) values(49, 2, 2.6986239351923014);
insert into gene_expressions(cell, gene, expression_value) values(31, 9, 11.815005880156592);
insert into gene_expressions(cell, gene, expression_value) values(12, 8, 1.1220101070129496);
insert into gene_expressions(cell, gene, expression_value) values(5, 7, 82.28228338251313);
insert into gene_expressions(cell, gene, expression_value) values(46, 3, 18.031309008305506);
insert into gene_expressions(cell, gene, expression_value) values(27, 6, 68.321570807999);
insert into gene_expressions(cell, gene, expression_value) values(13, 1, 8.880883050485721);
insert into gene_expressions(cell, gene, expression_value) values(26, 5, 47.03013229479218);
insert into gene_expressions(cell, gene, expression_value) values(20, 8, 8.557351873225993);
insert into gene_expressions(cell, gene, expression_value) values(6, 7, 30.35110433425099);
insert into gene_expressions(cell, gene, expression_value) values(31, 3, 87.22678009409536);
insert into gene_expressions(cell, gene, expression_value) values(50, 1, 25.532134691404163);
insert into gene_expressions(cell, gene, expression_value) values(26, 1, 51.643029383302355);
insert into gene_expressions(cell, gene, expression_value) values(5, 8, 26.044793413787794);
insert into gene_expressions(cell, gene, expression_value) values(21, 6, 13.32795461736811);
insert into gene_expressions(cell, gene, expression_value) values(8, 7, 53.1141666527165);
insert into gene_expressions(cell, gene, expression_value) values(29, 6, 51.130813198924606);
insert into gene_expressions(cell, gene, expression_value) values(15, 5, 80.00477418723511);
insert into gene_expressions(cell, gene, expression_value) values(11, 4, 47.593686424798875);
insert into gene_expressions(cell, gene, expression_value) values(7, 9, 21.813367932473792);
insert into gene_expressions(cell, gene, expression_value) values(34, 1, 3.3156204479953266);
insert into gene_expressions(cell, gene, expression_value) values(7, 7, 69.48483470875672);
insert into gene_expressions(cell, gene, expression_value) values(48, 2, 0.46175801850896203);
insert into gene_expressions(cell, gene, expression_value) values(17, 4, 53.308055198520265);
insert into gene_expressions(cell, gene, expression_value) values(20, 4, 91.39982620777694);
insert into gene_expressions(cell, gene, expression_value) values(44, 1, 26.08314099954362);
insert into gene_expressions(cell, gene, expression_value) values(34, 4, 71.829777656319);
insert into gene_expressions(cell, gene, expression_value) values(24, 7, 89.2836434279745);
insert into gene_expressions(cell, gene, expression_value) values(3, 8, 0.36156480005018476);
insert into gene_expressions(cell, gene, expression_value) values(9, 6, 75.9652601976469);
insert into gene_expressions(cell, gene, expression_value) values(41, 5, 87.02702985436213);
insert into gene_expressions(cell, gene, expression_value) values(36, 9, 69.89838303870387);
insert into gene_expressions(cell, gene, expression_value) values(20, 7, 14.32031938403895);
insert into gene_expressions(cell, gene, expression_value) values(40, 5, 69.53078295479898);
insert into gene_expressions(cell, gene, expression_value) values(34, 6, 70.92989169623979);
insert into gene_expressions(cell, gene, expression_value) values(11, 8, 92.26632686656006);
insert into gene_expressions(cell, gene, expression_value) values(2, 3, 27.6186340504853);
insert into gene_expressions(cell, gene, expression_value) values(31, 2, 94.34212420344744);
insert into gene_expressions(cell, gene, expression_value) values(46, 1, 25.186255729339813);
insert into gene_expressions(cell, gene, expression_value) values(37, 5, 51.37382578088785);
insert into gene_expressions(cell, gene, expression_value) values(13, 8, 27.69114555443448);
insert into gene_expressions(cell, gene, expression_value) values(1, 3, 54.770756301270126);
insert into gene_expressions(cell, gene, expression_value) values(34, 9, 35.00807726668651);
insert into gene_expressions(cell, gene, expression_value) values(9, 3, 0.16921923545042405);
insert into gene_expressions(cell, gene, expression_value) values(46, 7, 5.929527413847602);
insert into gene_expressions(cell, gene, expression_value) values(39, 2, 24.196211762083507);
insert into gene_expressions(cell, gene, expression_value) values(50, 5, 14.360596760186105);
insert into gene_expressions(cell, gene, expression_value) values(12, 3, 39.06299197062392);
insert into gene_expressions(cell, gene, expression_value) values(7, 8, 59.864683064046666);
insert into gene_expressions(cell, gene, expression_value) values(42, 7, 55.06281879557119);
insert into gene_expressions(cell, gene, expression_value) values(41, 4, 80.5464789604833);
insert into gene_expressions(cell, gene, expression_value) values(20, 6, 20.794146589102425);
insert into gene_expressions(cell, gene, expression_value) values(37, 5, 47.49999379409152);
insert into gene_expressions(cell, gene, expression_value) values(44, 7, 30.293905258125243);
insert into gene_expressions(cell, gene, expression_value) values(10, 5, 72.0133822190433);
insert into gene_expressions(cell, gene, expression_value) values(48, 2, 71.01488299519984);
insert into gene_expressions(cell, gene, expression_value) values(14, 8, 57.54709447811857);
insert into gene_expressions(cell, gene, expression_value) values(19, 1, 16.679753376756633);
insert into gene_expressions(cell, gene, expression_value) values(46, 7, 92.73832503544031);
insert into gene_expressions(cell, gene, expression_value) values(44, 5, 2.118114626426437);
insert into gene_expressions(cell, gene, expression_value) values(27, 3, 75.55538729019362);
insert into gene_expressions(cell, gene, expression_value) values(23, 3, 82.57090289928693);
insert into gene_expressions(cell, gene, expression_value) values(42, 1, 12.067460113819406);
insert into gene_expressions(cell, gene, expression_value) values(29, 9, 36.35840962880905);
insert into gene_expressions(cell, gene, expression_value) values(1, 2, 12.95552402157294);
insert into gene_expressions(cell, gene, expression_value) values(21, 7, 1.589822107486727);
insert into gene_expressions(cell, gene, expression_value) values(4, 6, 19.137194696075667);
insert into gene_expressions(cell, gene, expression_value) values(44, 5, 85.196703035696);
insert into gene_expressions(cell, gene, expression_value) values(37, 6, 70.28907085540362);
insert into gene_expressions(cell, gene, expression_value) values(21, 6, 0.0031454941490705046);
insert into gene_expressions(cell, gene, expression_value) values(16, 7, 11.722192788619612);
insert into gene_expressions(cell, gene, expression_value) values(39, 8, 22.676222437692328);
insert into gene_expressions(cell, gene, expression_value) values(10, 6, 59.75499810951066);
insert into gene_expressions(cell, gene, expression_value) values(12, 4, 45.71279759299527);
insert into gene_expressions(cell, gene, expression_value) values(39, 6, 51.66042857023141);
insert into gene_expressions(cell, gene, expression_value) values(34, 9, 17.621811086843064);
insert into gene_expressions(cell, gene, expression_value) values(38, 2, 89.56487919595658);
insert into gene_expressions(cell, gene, expression_value) values(5, 8, 75.11035369698172);
insert into gene_expressions(cell, gene, expression_value) values(46, 8, 23.51002964670974);
insert into gene_expressions(cell, gene, expression_value) values(44, 3, 63.089797349395695);
insert into gene_expressions(cell, gene, expression_value) values(17, 1, 2.884642062208631);
insert into gene_expressions(cell, gene, expression_value) values(30, 5, 63.249398725207605);
insert into gene_expressions(cell, gene, expression_value) values(19, 9, 97.64393316272314);
insert into gene_expressions(cell, gene, expression_value) values(35, 2, 57.956652134907515);
insert into gene_expressions(cell, gene, expression_value) values(36, 2, 69.97228633920354);
insert into gene_expressions(cell, gene, expression_value) values(4, 8, 22.39186587787153);
insert into gene_expressions(cell, gene, expression_value) values(22, 6, 48.80286197873668);
insert into gene_expressions(cell, gene, expression_value) values(26, 8, 77.72030525366543);
