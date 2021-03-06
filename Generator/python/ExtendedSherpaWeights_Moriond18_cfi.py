import FWCore.ParameterSet.Config as cms

SherpaWeightsBlock = cms.PSet(
    SherpaWeights = cms.vstring(
        'Weight',
        'MEWeight',
        'WeightNormalisation',
        'NTrials'
    ),
    SherpaVariationWeights = cms.vstring(*(
            'MUR0.5_MUF0.5_PDF261000',
            'MUR0.5_MUF1_PDF261000',
            'MUR1_MUF0.5_PDF261000',
            'MUR1_MUF2_PDF261000',
            'MUR2_MUF1_PDF261000',
            'MUR2_MUF2_PDF261000',
            'MUR1_MUF1_PDF261000',
            'MUR1_MUF1_PDF261001',
            'MUR1_MUF1_PDF261002',
            'MUR1_MUF1_PDF261003',
            'MUR1_MUF1_PDF261004',
            'MUR1_MUF1_PDF261005',
            'MUR1_MUF1_PDF261006',
            'MUR1_MUF1_PDF261007',
            'MUR1_MUF1_PDF261008',
            'MUR1_MUF1_PDF261009',
            'MUR1_MUF1_PDF261010',
            'MUR1_MUF1_PDF261011',
            'MUR1_MUF1_PDF261012',
            'MUR1_MUF1_PDF261013',
            'MUR1_MUF1_PDF261014',
            'MUR1_MUF1_PDF261015',
            'MUR1_MUF1_PDF261016',
            'MUR1_MUF1_PDF261017',
            'MUR1_MUF1_PDF261018',
            'MUR1_MUF1_PDF261019',
            'MUR1_MUF1_PDF261020',
            'MUR1_MUF1_PDF261021',
            'MUR1_MUF1_PDF261022',
            'MUR1_MUF1_PDF261023',
            'MUR1_MUF1_PDF261024',
            'MUR1_MUF1_PDF261025',
            'MUR1_MUF1_PDF261026',
            'MUR1_MUF1_PDF261027',
            'MUR1_MUF1_PDF261028',
            'MUR1_MUF1_PDF261029',
            'MUR1_MUF1_PDF261030',
            'MUR1_MUF1_PDF261031',
            'MUR1_MUF1_PDF261032',
            'MUR1_MUF1_PDF261033',
            'MUR1_MUF1_PDF261034',
            'MUR1_MUF1_PDF261035',
            'MUR1_MUF1_PDF261036',
            'MUR1_MUF1_PDF261037',
            'MUR1_MUF1_PDF261038',
            'MUR1_MUF1_PDF261039',
            'MUR1_MUF1_PDF261040',
            'MUR1_MUF1_PDF261041',
            'MUR1_MUF1_PDF261042',
            'MUR1_MUF1_PDF261043',
            'MUR1_MUF1_PDF261044',
            'MUR1_MUF1_PDF261045',
            'MUR1_MUF1_PDF261046',
            'MUR1_MUF1_PDF261047',
            'MUR1_MUF1_PDF261048',
            'MUR1_MUF1_PDF261049',
            'MUR1_MUF1_PDF261050',
            'MUR1_MUF1_PDF261051',
            'MUR1_MUF1_PDF261052',
            'MUR1_MUF1_PDF261053',
            'MUR1_MUF1_PDF261054',
            'MUR1_MUF1_PDF261055',
            'MUR1_MUF1_PDF261056',
            'MUR1_MUF1_PDF261057',
            'MUR1_MUF1_PDF261058',
            'MUR1_MUF1_PDF261059',
            'MUR1_MUF1_PDF261060',
            'MUR1_MUF1_PDF261061',
            'MUR1_MUF1_PDF261062',
            'MUR1_MUF1_PDF261063',
            'MUR1_MUF1_PDF261064',
            'MUR1_MUF1_PDF261065',
            'MUR1_MUF1_PDF261066',
            'MUR1_MUF1_PDF261067',
            'MUR1_MUF1_PDF261068',
            'MUR1_MUF1_PDF261069',
            'MUR1_MUF1_PDF261070',
            'MUR1_MUF1_PDF261071',
            'MUR1_MUF1_PDF261072',
            'MUR1_MUF1_PDF261073',
            'MUR1_MUF1_PDF261074',
            'MUR1_MUF1_PDF261075',
            'MUR1_MUF1_PDF261076',
            'MUR1_MUF1_PDF261077',
            'MUR1_MUF1_PDF261078',
            'MUR1_MUF1_PDF261079',
            'MUR1_MUF1_PDF261080',
            'MUR1_MUF1_PDF261081',
            'MUR1_MUF1_PDF261082',
            'MUR1_MUF1_PDF261083',
            'MUR1_MUF1_PDF261084',
            'MUR1_MUF1_PDF261085',
            'MUR1_MUF1_PDF261086',
            'MUR1_MUF1_PDF261087',
            'MUR1_MUF1_PDF261088',
            'MUR1_MUF1_PDF261089',
            'MUR1_MUF1_PDF261090',
            'MUR1_MUF1_PDF261091',
            'MUR1_MUF1_PDF261092',
            'MUR1_MUF1_PDF261093',
            'MUR1_MUF1_PDF261094',
            'MUR1_MUF1_PDF261095',
            'MUR1_MUF1_PDF261096',
            'MUR1_MUF1_PDF261097',
            'MUR1_MUF1_PDF261098',
            'MUR1_MUF1_PDF261099',
            'MUR1_MUF1_PDF261100',
            'MUR1_MUF1_PDF306000',
            'MUR1_MUF1_PDF306001',
            'MUR1_MUF1_PDF306002',
            'MUR1_MUF1_PDF306003',
            'MUR1_MUF1_PDF306004',
            'MUR1_MUF1_PDF306005',
            'MUR1_MUF1_PDF306006',
            'MUR1_MUF1_PDF306007',
            'MUR1_MUF1_PDF306008',
            'MUR1_MUF1_PDF306009',
            'MUR1_MUF1_PDF306010',
            'MUR1_MUF1_PDF306011',
            'MUR1_MUF1_PDF306012',
            'MUR1_MUF1_PDF306013',
            'MUR1_MUF1_PDF306014',
            'MUR1_MUF1_PDF306015',
            'MUR1_MUF1_PDF306016',
            'MUR1_MUF1_PDF306017',
            'MUR1_MUF1_PDF306018',
            'MUR1_MUF1_PDF306019',
            'MUR1_MUF1_PDF306020',
            'MUR1_MUF1_PDF306021',
            'MUR1_MUF1_PDF306022',
            'MUR1_MUF1_PDF306023',
            'MUR1_MUF1_PDF306024',
            'MUR1_MUF1_PDF306025',
            'MUR1_MUF1_PDF306026',
            'MUR1_MUF1_PDF306027',
            'MUR1_MUF1_PDF306028',
            'MUR1_MUF1_PDF306029',
            'MUR1_MUF1_PDF306030',
            'MUR1_MUF1_PDF306031',
            'MUR1_MUF1_PDF306032',
            'MUR1_MUF1_PDF306033',
            'MUR1_MUF1_PDF306034',
            'MUR1_MUF1_PDF306035',
            'MUR1_MUF1_PDF306036',
            'MUR1_MUF1_PDF306037',
            'MUR1_MUF1_PDF306038',
            'MUR1_MUF1_PDF306039',
            'MUR1_MUF1_PDF306040',
            'MUR1_MUF1_PDF306041',
            'MUR1_MUF1_PDF306042',
            'MUR1_MUF1_PDF306043',
            'MUR1_MUF1_PDF306044',
            'MUR1_MUF1_PDF306045',
            'MUR1_MUF1_PDF306046',
            'MUR1_MUF1_PDF306047',
            'MUR1_MUF1_PDF306048',
            'MUR1_MUF1_PDF306049',
            'MUR1_MUF1_PDF306050',
            'MUR1_MUF1_PDF306051',
            'MUR1_MUF1_PDF306052',
            'MUR1_MUF1_PDF306053',
            'MUR1_MUF1_PDF306054',
            'MUR1_MUF1_PDF306055',
            'MUR1_MUF1_PDF306056',
            'MUR1_MUF1_PDF306057',
            'MUR1_MUF1_PDF306058',
            'MUR1_MUF1_PDF306059',
            'MUR1_MUF1_PDF306060',
            'MUR1_MUF1_PDF306061',
            'MUR1_MUF1_PDF306062',
            'MUR1_MUF1_PDF306063',
            'MUR1_MUF1_PDF306064',
            'MUR1_MUF1_PDF306065',
            'MUR1_MUF1_PDF306066',
            'MUR1_MUF1_PDF306067',
            'MUR1_MUF1_PDF306068',
            'MUR1_MUF1_PDF306069',
            'MUR1_MUF1_PDF306070',
            'MUR1_MUF1_PDF306071',
            'MUR1_MUF1_PDF306072',
            'MUR1_MUF1_PDF306073',
            'MUR1_MUF1_PDF306074',
            'MUR1_MUF1_PDF306075',
            'MUR1_MUF1_PDF306076',
            'MUR1_MUF1_PDF306077',
            'MUR1_MUF1_PDF306078',
            'MUR1_MUF1_PDF306079',
            'MUR1_MUF1_PDF306080',
            'MUR1_MUF1_PDF306081',
            'MUR1_MUF1_PDF306082',
            'MUR1_MUF1_PDF306083',
            'MUR1_MUF1_PDF306084',
            'MUR1_MUF1_PDF306085',
            'MUR1_MUF1_PDF306086',
            'MUR1_MUF1_PDF306087',
            'MUR1_MUF1_PDF306088',
            'MUR1_MUF1_PDF306089',
            'MUR1_MUF1_PDF306090',
            'MUR1_MUF1_PDF306091',
            'MUR1_MUF1_PDF306092',
            'MUR1_MUF1_PDF306093',
            'MUR1_MUF1_PDF306094',
            'MUR1_MUF1_PDF306095',
            'MUR1_MUF1_PDF306096',
            'MUR1_MUF1_PDF306097',
            'MUR1_MUF1_PDF306098',
            'MUR1_MUF1_PDF306099',
            'MUR1_MUF1_PDF306100',
            'MUR1_MUF1_PDF306101',
            'MUR1_MUF1_PDF306102',
            'MUR1_MUF1_PDF305800',
            'MUR1_MUF1_PDF305801',
            'MUR1_MUF1_PDF305802',
            'MUR1_MUF1_PDF305803',
            'MUR1_MUF1_PDF305804',
            'MUR1_MUF1_PDF305805',
            'MUR1_MUF1_PDF305806',
            'MUR1_MUF1_PDF305807',
            'MUR1_MUF1_PDF305808',
            'MUR1_MUF1_PDF305809',
            'MUR1_MUF1_PDF305810',
            'MUR1_MUF1_PDF305811',
            'MUR1_MUF1_PDF305812',
            'MUR1_MUF1_PDF305813',
            'MUR1_MUF1_PDF305814',
            'MUR1_MUF1_PDF305815',
            'MUR1_MUF1_PDF305816',
            'MUR1_MUF1_PDF305817',
            'MUR1_MUF1_PDF305818',
            'MUR1_MUF1_PDF305819',
            'MUR1_MUF1_PDF305820',
            'MUR1_MUF1_PDF305821',
            'MUR1_MUF1_PDF305822',
            'MUR1_MUF1_PDF305823',
            'MUR1_MUF1_PDF305824',
            'MUR1_MUF1_PDF305825',
            'MUR1_MUF1_PDF305826',
            'MUR1_MUF1_PDF305827',
            'MUR1_MUF1_PDF305828',
            'MUR1_MUF1_PDF305829',
            'MUR1_MUF1_PDF305830',
            'MUR1_MUF1_PDF305831',
            'MUR1_MUF1_PDF305832',
            'MUR1_MUF1_PDF305833',
            'MUR1_MUF1_PDF305834',
            'MUR1_MUF1_PDF305835',
            'MUR1_MUF1_PDF305836',
            'MUR1_MUF1_PDF305837',
            'MUR1_MUF1_PDF305838',
            'MUR1_MUF1_PDF305839',
            'MUR1_MUF1_PDF305840',
            'MUR1_MUF1_PDF305841',
            'MUR1_MUF1_PDF305842',
            'MUR1_MUF1_PDF305843',
            'MUR1_MUF1_PDF305844',
            'MUR1_MUF1_PDF305845',
            'MUR1_MUF1_PDF305846',
            'MUR1_MUF1_PDF305847',
            'MUR1_MUF1_PDF305848',
            'MUR1_MUF1_PDF305849',
            'MUR1_MUF1_PDF305850',
            'MUR1_MUF1_PDF305851',
            'MUR1_MUF1_PDF305852',
            'MUR1_MUF1_PDF305853',
            'MUR1_MUF1_PDF305854',
            'MUR1_MUF1_PDF305855',
            'MUR1_MUF1_PDF305856',
            'MUR1_MUF1_PDF305857',
            'MUR1_MUF1_PDF305858',
            'MUR1_MUF1_PDF305859',
            'MUR1_MUF1_PDF305860',
            'MUR1_MUF1_PDF305861',
            'MUR1_MUF1_PDF305862',
            'MUR1_MUF1_PDF305863',
            'MUR1_MUF1_PDF305864',
            'MUR1_MUF1_PDF305865',
            'MUR1_MUF1_PDF305866',
            'MUR1_MUF1_PDF305867',
            'MUR1_MUF1_PDF305868',
            'MUR1_MUF1_PDF305869',
            'MUR1_MUF1_PDF305870',
            'MUR1_MUF1_PDF305871',
            'MUR1_MUF1_PDF305872',
            'MUR1_MUF1_PDF305873',
            'MUR1_MUF1_PDF305874',
            'MUR1_MUF1_PDF305875',
            'MUR1_MUF1_PDF305876',
            'MUR1_MUF1_PDF305877',
            'MUR1_MUF1_PDF305878',
            'MUR1_MUF1_PDF305879',
            'MUR1_MUF1_PDF305880',
            'MUR1_MUF1_PDF305881',
            'MUR1_MUF1_PDF305882',
            'MUR1_MUF1_PDF305883',
            'MUR1_MUF1_PDF305884',
            'MUR1_MUF1_PDF305885',
            'MUR1_MUF1_PDF305886',
            'MUR1_MUF1_PDF305887',
            'MUR1_MUF1_PDF305888',
            'MUR1_MUF1_PDF305889',
            'MUR1_MUF1_PDF305890',
            'MUR1_MUF1_PDF305891',
            'MUR1_MUF1_PDF305892',
            'MUR1_MUF1_PDF305893',
            'MUR1_MUF1_PDF305894',
            'MUR1_MUF1_PDF305895',
            'MUR1_MUF1_PDF305896',
            'MUR1_MUF1_PDF305897',
            'MUR1_MUF1_PDF305898',
            'MUR1_MUF1_PDF305899',
            'MUR1_MUF1_PDF305900',
            'MUR1_MUF1_PDF305901',
            'MUR1_MUF1_PDF305902',
            'MUR1_MUF1_PDF315000',
            'MUR1_MUF1_PDF292200',
            'MUR1_MUF1_PDF292600',
            'MUR1_MUF1_PDF13100',
            'MUR1_MUF1_PDF13101',
            'MUR1_MUF1_PDF13102',
            'MUR1_MUF1_PDF13103',
            'MUR1_MUF1_PDF13104',
            'MUR1_MUF1_PDF13105',
            'MUR1_MUF1_PDF13106',
            'MUR1_MUF1_PDF13107',
            'MUR1_MUF1_PDF13108',
            'MUR1_MUF1_PDF13109',
            'MUR1_MUF1_PDF13110',
            'MUR1_MUF1_PDF13111',
            'MUR1_MUF1_PDF13112',
            'MUR1_MUF1_PDF13113',
            'MUR1_MUF1_PDF13114',
            'MUR1_MUF1_PDF13115',
            'MUR1_MUF1_PDF13116',
            'MUR1_MUF1_PDF13117',
            'MUR1_MUF1_PDF13118',
            'MUR1_MUF1_PDF13119',
            'MUR1_MUF1_PDF13120',
            'MUR1_MUF1_PDF13121',
            'MUR1_MUF1_PDF13122',
            'MUR1_MUF1_PDF13123',
            'MUR1_MUF1_PDF13124',
            'MUR1_MUF1_PDF13125',
            'MUR1_MUF1_PDF13126',
            'MUR1_MUF1_PDF13127',
            'MUR1_MUF1_PDF13128',
            'MUR1_MUF1_PDF13129',
            'MUR1_MUF1_PDF13130',
            'MUR1_MUF1_PDF13131',
            'MUR1_MUF1_PDF13132',
            'MUR1_MUF1_PDF13133',
            'MUR1_MUF1_PDF13134',
            'MUR1_MUF1_PDF13135',
            'MUR1_MUF1_PDF13136',
            'MUR1_MUF1_PDF13137',
            'MUR1_MUF1_PDF13138',
            'MUR1_MUF1_PDF13139',
            'MUR1_MUF1_PDF13140',
            'MUR1_MUF1_PDF13141',
            'MUR1_MUF1_PDF13142',
            'MUR1_MUF1_PDF13143',
            'MUR1_MUF1_PDF13144',
            'MUR1_MUF1_PDF13145',
            'MUR1_MUF1_PDF13146',
            'MUR1_MUF1_PDF13147',
            'MUR1_MUF1_PDF13148',
            'MUR1_MUF1_PDF13149',
            'MUR1_MUF1_PDF13150',
            'MUR1_MUF1_PDF13151',
            'MUR1_MUF1_PDF13152',
            'MUR1_MUF1_PDF13153',
            'MUR1_MUF1_PDF13154',
            'MUR1_MUF1_PDF13155',
            'MUR1_MUF1_PDF13156',
            'MUR1_MUF1_PDF13163',
            'MUR1_MUF1_PDF13167',
            'MUR1_MUF1_PDF13000',
            'MUR1_MUF1_PDF13001',
            'MUR1_MUF1_PDF13002',
            'MUR1_MUF1_PDF13003',
            'MUR1_MUF1_PDF13004',
            'MUR1_MUF1_PDF13005',
            'MUR1_MUF1_PDF13006',
            'MUR1_MUF1_PDF13007',
            'MUR1_MUF1_PDF13008',
            'MUR1_MUF1_PDF13009',
            'MUR1_MUF1_PDF13010',
            'MUR1_MUF1_PDF13011',
            'MUR1_MUF1_PDF13012',
            'MUR1_MUF1_PDF13013',
            'MUR1_MUF1_PDF13014',
            'MUR1_MUF1_PDF13015',
            'MUR1_MUF1_PDF13016',
            'MUR1_MUF1_PDF13017',
            'MUR1_MUF1_PDF13018',
            'MUR1_MUF1_PDF13019',
            'MUR1_MUF1_PDF13020',
            'MUR1_MUF1_PDF13021',
            'MUR1_MUF1_PDF13022',
            'MUR1_MUF1_PDF13023',
            'MUR1_MUF1_PDF13024',
            'MUR1_MUF1_PDF13025',
            'MUR1_MUF1_PDF13026',
            'MUR1_MUF1_PDF13027',
            'MUR1_MUF1_PDF13028',
            'MUR1_MUF1_PDF13029',
            'MUR1_MUF1_PDF13030',
            'MUR1_MUF1_PDF13031',
            'MUR1_MUF1_PDF13032',
            'MUR1_MUF1_PDF13033',
            'MUR1_MUF1_PDF13034',
            'MUR1_MUF1_PDF13035',
            'MUR1_MUF1_PDF13036',
            'MUR1_MUF1_PDF13037',
            'MUR1_MUF1_PDF13038',
            'MUR1_MUF1_PDF13039',
            'MUR1_MUF1_PDF13040',
            'MUR1_MUF1_PDF13041',
            'MUR1_MUF1_PDF13042',
            'MUR1_MUF1_PDF13043',
            'MUR1_MUF1_PDF13044',
            'MUR1_MUF1_PDF13045',
            'MUR1_MUF1_PDF13046',
            'MUR1_MUF1_PDF13047',
            'MUR1_MUF1_PDF13048',
            'MUR1_MUF1_PDF13049',
            'MUR1_MUF1_PDF13050',
            'MUR1_MUF1_PDF13051',
            'MUR1_MUF1_PDF13052',
            'MUR1_MUF1_PDF13053',
            'MUR1_MUF1_PDF13054',
            'MUR1_MUF1_PDF13055',
            'MUR1_MUF1_PDF13056',
            'MUR1_MUF1_PDF13065',
            'MUR1_MUF1_PDF13069',
            'MUR1_MUF1_PDF13200',
            'MUR1_MUF1_PDF25200',
            'MUR1_MUF1_PDF25201',
            'MUR1_MUF1_PDF25202',
            'MUR1_MUF1_PDF25203',
            'MUR1_MUF1_PDF25204',
            'MUR1_MUF1_PDF25205',
            'MUR1_MUF1_PDF25206',
            'MUR1_MUF1_PDF25207',
            'MUR1_MUF1_PDF25208',
            'MUR1_MUF1_PDF25209',
            'MUR1_MUF1_PDF25210',
            'MUR1_MUF1_PDF25211',
            'MUR1_MUF1_PDF25212',
            'MUR1_MUF1_PDF25213',
            'MUR1_MUF1_PDF25214',
            'MUR1_MUF1_PDF25215',
            'MUR1_MUF1_PDF25216',
            'MUR1_MUF1_PDF25217',
            'MUR1_MUF1_PDF25218',
            'MUR1_MUF1_PDF25219',
            'MUR1_MUF1_PDF25220',
            'MUR1_MUF1_PDF25221',
            'MUR1_MUF1_PDF25222',
            'MUR1_MUF1_PDF25223',
            'MUR1_MUF1_PDF25224',
            'MUR1_MUF1_PDF25225',
            'MUR1_MUF1_PDF25226',
            'MUR1_MUF1_PDF25227',
            'MUR1_MUF1_PDF25228',
            'MUR1_MUF1_PDF25229',
            'MUR1_MUF1_PDF25230',
            'MUR1_MUF1_PDF25231',
            'MUR1_MUF1_PDF25232',
            'MUR1_MUF1_PDF25233',
            'MUR1_MUF1_PDF25234',
            'MUR1_MUF1_PDF25235',
            'MUR1_MUF1_PDF25236',
            'MUR1_MUF1_PDF25237',
            'MUR1_MUF1_PDF25238',
            'MUR1_MUF1_PDF25239',
            'MUR1_MUF1_PDF25240',
            'MUR1_MUF1_PDF25241',
            'MUR1_MUF1_PDF25242',
            'MUR1_MUF1_PDF25243',
            'MUR1_MUF1_PDF25244',
            'MUR1_MUF1_PDF25245',
            'MUR1_MUF1_PDF25246',
            'MUR1_MUF1_PDF25247',
            'MUR1_MUF1_PDF25248',
            'MUR1_MUF1_PDF25249',
            'MUR1_MUF1_PDF25250',
            'MUR1_MUF1_PDF25300',
            'MUR1_MUF1_PDF25301',
            'MUR1_MUF1_PDF25302',
            'MUR1_MUF1_PDF25303',
            'MUR1_MUF1_PDF25304',
            'MUR1_MUF1_PDF25305',
            'MUR1_MUF1_PDF25306',
            'MUR1_MUF1_PDF25307',
            'MUR1_MUF1_PDF25308',
            'MUR1_MUF1_PDF25309',
            'MUR1_MUF1_PDF25310',
            'MUR1_MUF1_PDF25311',
            'MUR1_MUF1_PDF25312',
            'MUR1_MUF1_PDF25313',
            'MUR1_MUF1_PDF25314',
            'MUR1_MUF1_PDF25315',
            'MUR1_MUF1_PDF25316',
            'MUR1_MUF1_PDF25317',
            'MUR1_MUF1_PDF25318',
            'MUR1_MUF1_PDF25319',
            'MUR1_MUF1_PDF25320',
            'MUR1_MUF1_PDF25321',
            'MUR1_MUF1_PDF25322',
            'MUR1_MUF1_PDF25323',
            'MUR1_MUF1_PDF25324',
            'MUR1_MUF1_PDF25325',
            'MUR1_MUF1_PDF25326',
            'MUR1_MUF1_PDF25327',
            'MUR1_MUF1_PDF25328',
            'MUR1_MUF1_PDF25329',
            'MUR1_MUF1_PDF25330',
            'MUR1_MUF1_PDF25331',
            'MUR1_MUF1_PDF25332',
            'MUR1_MUF1_PDF25333',
            'MUR1_MUF1_PDF25334',
            'MUR1_MUF1_PDF25335',
            'MUR1_MUF1_PDF25336',
            'MUR1_MUF1_PDF25337',
            'MUR1_MUF1_PDF25338',
            'MUR1_MUF1_PDF25339',
            'MUR1_MUF1_PDF25340',
            'MUR1_MUF1_PDF25341',
            'MUR1_MUF1_PDF25342',
            'MUR1_MUF1_PDF25343',
            'MUR1_MUF1_PDF25344',
            'MUR1_MUF1_PDF25345',
            'MUR1_MUF1_PDF25346',
            'MUR1_MUF1_PDF25347',
            'MUR1_MUF1_PDF25348',
            'MUR1_MUF1_PDF25349',
            'MUR1_MUF1_PDF25350',
            'MUR1_MUF1_PDF25000',
            'MUR1_MUF1_PDF42400',
            'MUR1_MUF1_PDF42401',
            'MUR1_MUF1_PDF42402',
            'MUR1_MUF1_PDF42403',
            'MUR1_MUF1_PDF42404',
            'MUR1_MUF1_PDF42405',
            'MUR1_MUF1_PDF42406',
            'MUR1_MUF1_PDF42407',
            'MUR1_MUF1_PDF42408',
            'MUR1_MUF1_PDF42409',
            'MUR1_MUF1_PDF42410',
            'MUR1_MUF1_PDF42411',
            'MUR1_MUF1_PDF42412',
            'MUR1_MUF1_PDF42413',
            'MUR1_MUF1_PDF42414',
            'MUR1_MUF1_PDF42415',
            'MUR1_MUF1_PDF42416',
            'MUR1_MUF1_PDF42417',
            'MUR1_MUF1_PDF42418',
            'MUR1_MUF1_PDF42419',
            'MUR1_MUF1_PDF42420',
            'MUR1_MUF1_PDF42421',
            'MUR1_MUF1_PDF42422',
            'MUR1_MUF1_PDF42423',
            'MUR1_MUF1_PDF42424',
            'MUR1_MUF1_PDF42425',
            'MUR1_MUF1_PDF42426',
            'MUR1_MUF1_PDF42427',
            'MUR1_MUF1_PDF42428',
            'MUR1_MUF1_PDF42780',
            'MUR1_MUF1_PDF42781',
            'MUR1_MUF1_PDF42782',
            'MUR1_MUF1_PDF42783',
            'MUR1_MUF1_PDF42784',
            'MUR1_MUF1_PDF42785',
            'MUR1_MUF1_PDF42786',
            'MUR1_MUF1_PDF42787',
            'MUR1_MUF1_PDF42788',
            'MUR1_MUF1_PDF42789',
            'MUR1_MUF1_PDF42790',
            'MUR1_MUF1_PDF42791',
            'MUR1_MUF1_PDF42792',
            'MUR1_MUF1_PDF42793',
            'MUR1_MUF1_PDF42794',
            'MUR1_MUF1_PDF42795',
            'MUR1_MUF1_PDF42796',
            'MUR1_MUF1_PDF42797',
            'MUR1_MUF1_PDF42798',
            'MUR1_MUF1_PDF42799',
            'MUR1_MUF1_PDF42800',
            'MUR1_MUF1_PDF42801',
            'MUR1_MUF1_PDF42802',
            'MUR1_MUF1_PDF42803',
            'MUR1_MUF1_PDF42804',
            'MUR1_MUF1_PDF42805',
            'MUR1_MUF1_PDF42806',
            'MUR1_MUF1_PDF42807',
            'MUR1_MUF1_PDF42808',
            'MUR1_MUF1_PDF42809',
            'MUR1_MUF1_PDF90200',
            'MUR1_MUF1_PDF90201',
            'MUR1_MUF1_PDF90202',
            'MUR1_MUF1_PDF90203',
            'MUR1_MUF1_PDF90204',
            'MUR1_MUF1_PDF90205',
            'MUR1_MUF1_PDF90206',
            'MUR1_MUF1_PDF90207',
            'MUR1_MUF1_PDF90208',
            'MUR1_MUF1_PDF90209',
            'MUR1_MUF1_PDF90210',
            'MUR1_MUF1_PDF90211',
            'MUR1_MUF1_PDF90212',
            'MUR1_MUF1_PDF90213',
            'MUR1_MUF1_PDF90214',
            'MUR1_MUF1_PDF90215',
            'MUR1_MUF1_PDF90216',
            'MUR1_MUF1_PDF90217',
            'MUR1_MUF1_PDF90218',
            'MUR1_MUF1_PDF90219',
            'MUR1_MUF1_PDF90220',
            'MUR1_MUF1_PDF90221',
            'MUR1_MUF1_PDF90222',
            'MUR1_MUF1_PDF90223',
            'MUR1_MUF1_PDF90224',
            'MUR1_MUF1_PDF90225',
            'MUR1_MUF1_PDF90226',
            'MUR1_MUF1_PDF90227',
            'MUR1_MUF1_PDF90228',
            'MUR1_MUF1_PDF90229',
            'MUR1_MUF1_PDF90230',
            'MUR1_MUF1_PDF90231',
            'MUR1_MUF1_PDF90232',
            'MUR1_MUF1_PDF90233',
            'MUR1_MUF1_PDF90234',
            'MUR1_MUF1_PDF90235',
            'MUR1_MUF1_PDF90236',
            'MUR1_MUF1_PDF90237',
            'MUR1_MUF1_PDF90238',
            'MUR1_MUF1_PDF90239',
            'MUR1_MUF1_PDF90240',
            'MUR1_MUF1_PDF90241',
            'MUR1_MUF1_PDF90242',
            'MUR1_MUF1_PDF90243',
            'MUR1_MUF1_PDF90244',
            'MUR1_MUF1_PDF90245',
            'MUR1_MUF1_PDF90246',
            'MUR1_MUF1_PDF90247',
            'MUR1_MUF1_PDF90248',
            'MUR1_MUF1_PDF90249',
            'MUR1_MUF1_PDF90250',
            'MUR1_MUF1_PDF90251',
            'MUR1_MUF1_PDF90252',
            'MUR1_MUF1_PDF90253',
            'MUR1_MUF1_PDF90254',
            'MUR1_MUF1_PDF90255',
            'MUR1_MUF1_PDF90256',
            'MUR1_MUF1_PDF90257',
            'MUR1_MUF1_PDF90258',
            'MUR1_MUF1_PDF90259',
            'MUR1_MUF1_PDF90260',
            'MUR1_MUF1_PDF90261',
            'MUR1_MUF1_PDF90262',
            'MUR1_MUF1_PDF90263',
            'MUR1_MUF1_PDF90264',
            'MUR1_MUF1_PDF90265',
            'MUR1_MUF1_PDF90266',
            'MUR1_MUF1_PDF90267',
            'MUR1_MUF1_PDF90268',
            'MUR1_MUF1_PDF90269',
            'MUR1_MUF1_PDF90270',
            'MUR1_MUF1_PDF90271',
            'MUR1_MUF1_PDF90272',
            'MUR1_MUF1_PDF90273',
            'MUR1_MUF1_PDF90274',
            'MUR1_MUF1_PDF90275',
            'MUR1_MUF1_PDF90276',
            'MUR1_MUF1_PDF90277',
            'MUR1_MUF1_PDF90278',
            'MUR1_MUF1_PDF90279',
            'MUR1_MUF1_PDF90280',
            'MUR1_MUF1_PDF90281',
            'MUR1_MUF1_PDF90282',
            'MUR1_MUF1_PDF90283',
            'MUR1_MUF1_PDF90284',
            'MUR1_MUF1_PDF90285',
            'MUR1_MUF1_PDF90286',
            'MUR1_MUF1_PDF90287',
            'MUR1_MUF1_PDF90288',
            'MUR1_MUF1_PDF90289',
            'MUR1_MUF1_PDF90290',
            'MUR1_MUF1_PDF90291',
            'MUR1_MUF1_PDF90292',
            'MUR1_MUF1_PDF90293',
            'MUR1_MUF1_PDF90294',
            'MUR1_MUF1_PDF90295',
            'MUR1_MUF1_PDF90296',
            'MUR1_MUF1_PDF90297',
            'MUR1_MUF1_PDF90298',
            'MUR1_MUF1_PDF90299',
            'MUR1_MUF1_PDF90300',
            'MUR1_MUF1_PDF90301',
            'MUR1_MUF1_PDF90302',
            'MUR1_MUF1_PDF91200',
            'MUR1_MUF1_PDF91201',
            'MUR1_MUF1_PDF91202',
            'MUR1_MUF1_PDF91203',
            'MUR1_MUF1_PDF91204',
            'MUR1_MUF1_PDF91205',
            'MUR1_MUF1_PDF91206',
            'MUR1_MUF1_PDF91207',
            'MUR1_MUF1_PDF91208',
            'MUR1_MUF1_PDF91209',
            'MUR1_MUF1_PDF91210',
            'MUR1_MUF1_PDF91211',
            'MUR1_MUF1_PDF91212',
            'MUR1_MUF1_PDF91213',
            'MUR1_MUF1_PDF91214',
            'MUR1_MUF1_PDF91215',
            'MUR1_MUF1_PDF91216',
            'MUR1_MUF1_PDF91217',
            'MUR1_MUF1_PDF91218',
            'MUR1_MUF1_PDF91219',
            'MUR1_MUF1_PDF91220',
            'MUR1_MUF1_PDF91221',
            'MUR1_MUF1_PDF91222',
            'MUR1_MUF1_PDF91223',
            'MUR1_MUF1_PDF91224',
            'MUR1_MUF1_PDF91225',
            'MUR1_MUF1_PDF91226',
            'MUR1_MUF1_PDF91227',
            'MUR1_MUF1_PDF91228',
            'MUR1_MUF1_PDF91229',
            'MUR1_MUF1_PDF91230',
            'MUR1_MUF1_PDF91231',
            'MUR1_MUF1_PDF91232',
            'MUR1_MUF1_PDF91233',
            'MUR1_MUF1_PDF91234',
            'MUR1_MUF1_PDF91235',
            'MUR1_MUF1_PDF91236',
            'MUR1_MUF1_PDF91237',
            'MUR1_MUF1_PDF91238',
            'MUR1_MUF1_PDF91239',
            'MUR1_MUF1_PDF91240',
            'MUR1_MUF1_PDF91241',
            'MUR1_MUF1_PDF91242',
            'MUR1_MUF1_PDF91243',
            'MUR1_MUF1_PDF91244',
            'MUR1_MUF1_PDF91245',
            'MUR1_MUF1_PDF91246',
            'MUR1_MUF1_PDF91247',
            'MUR1_MUF1_PDF91248',
            'MUR1_MUF1_PDF91249',
            'MUR1_MUF1_PDF91250',
            'MUR1_MUF1_PDF91251',
            'MUR1_MUF1_PDF91252',
            'MUR1_MUF1_PDF91253',
            'MUR1_MUF1_PDF91254',
            'MUR1_MUF1_PDF91255',
            'MUR1_MUF1_PDF91256',
            'MUR1_MUF1_PDF91257',
            'MUR1_MUF1_PDF91258',
            'MUR1_MUF1_PDF91259',
            'MUR1_MUF1_PDF91260',
            'MUR1_MUF1_PDF91261',
            'MUR1_MUF1_PDF91262',
            'MUR1_MUF1_PDF91263',
            'MUR1_MUF1_PDF91264',
            'MUR1_MUF1_PDF91265',
            'MUR1_MUF1_PDF91266',
            'MUR1_MUF1_PDF91267',
            'MUR1_MUF1_PDF91268',
            'MUR1_MUF1_PDF91269',
            'MUR1_MUF1_PDF91270',
            'MUR1_MUF1_PDF91271',
            'MUR1_MUF1_PDF91272',
            'MUR1_MUF1_PDF91273',
            'MUR1_MUF1_PDF91274',
            'MUR1_MUF1_PDF91275',
            'MUR1_MUF1_PDF91276',
            'MUR1_MUF1_PDF91277',
            'MUR1_MUF1_PDF91278',
            'MUR1_MUF1_PDF91279',
            'MUR1_MUF1_PDF91280',
            'MUR1_MUF1_PDF91281',
            'MUR1_MUF1_PDF91282',
            'MUR1_MUF1_PDF91283',
            'MUR1_MUF1_PDF91284',
            'MUR1_MUF1_PDF91285',
            'MUR1_MUF1_PDF91286',
            'MUR1_MUF1_PDF91287',
            'MUR1_MUF1_PDF91288',
            'MUR1_MUF1_PDF91289',
            'MUR1_MUF1_PDF91290',
            'MUR1_MUF1_PDF91291',
            'MUR1_MUF1_PDF91292',
            'MUR1_MUF1_PDF91293',
            'MUR1_MUF1_PDF91294',
            'MUR1_MUF1_PDF91295',
            'MUR1_MUF1_PDF91296',
            'MUR1_MUF1_PDF91297',
            'MUR1_MUF1_PDF91298',
            'MUR1_MUF1_PDF91299',
            'MUR1_MUF1_PDF91300',
            'MUR1_MUF1_PDF91301',
            'MUR1_MUF1_PDF91302',
            'MUR1_MUF1_PDF90400',
            'MUR1_MUF1_PDF90401',
            'MUR1_MUF1_PDF90402',
            'MUR1_MUF1_PDF90403',
            'MUR1_MUF1_PDF90404',
            'MUR1_MUF1_PDF90405',
            'MUR1_MUF1_PDF90406',
            'MUR1_MUF1_PDF90407',
            'MUR1_MUF1_PDF90408',
            'MUR1_MUF1_PDF90409',
            'MUR1_MUF1_PDF90410',
            'MUR1_MUF1_PDF90411',
            'MUR1_MUF1_PDF90412',
            'MUR1_MUF1_PDF90413',
            'MUR1_MUF1_PDF90414',
            'MUR1_MUF1_PDF90415',
            'MUR1_MUF1_PDF90416',
            'MUR1_MUF1_PDF90417',
            'MUR1_MUF1_PDF90418',
            'MUR1_MUF1_PDF90419',
            'MUR1_MUF1_PDF90420',
            'MUR1_MUF1_PDF90421',
            'MUR1_MUF1_PDF90422',
            'MUR1_MUF1_PDF90423',
            'MUR1_MUF1_PDF90424',
            'MUR1_MUF1_PDF90425',
            'MUR1_MUF1_PDF90426',
            'MUR1_MUF1_PDF90427',
            'MUR1_MUF1_PDF90428',
            'MUR1_MUF1_PDF90429',
            'MUR1_MUF1_PDF90430',
            'MUR1_MUF1_PDF90431',
            'MUR1_MUF1_PDF90432',
            'MUR1_MUF1_PDF91400',
            'MUR1_MUF1_PDF91401',
            'MUR1_MUF1_PDF91402',
            'MUR1_MUF1_PDF91403',
            'MUR1_MUF1_PDF91404',
            'MUR1_MUF1_PDF91405',
            'MUR1_MUF1_PDF91406',
            'MUR1_MUF1_PDF91407',
            'MUR1_MUF1_PDF91408',
            'MUR1_MUF1_PDF91409',
            'MUR1_MUF1_PDF91410',
            'MUR1_MUF1_PDF91411',
            'MUR1_MUF1_PDF91412',
            'MUR1_MUF1_PDF91413',
            'MUR1_MUF1_PDF91414',
            'MUR1_MUF1_PDF91415',
            'MUR1_MUF1_PDF91416',
            'MUR1_MUF1_PDF91417',
            'MUR1_MUF1_PDF91418',
            'MUR1_MUF1_PDF91419',
            'MUR1_MUF1_PDF91420',
            'MUR1_MUF1_PDF91421',
            'MUR1_MUF1_PDF91422',
            'MUR1_MUF1_PDF91423',
            'MUR1_MUF1_PDF91424',
            'MUR1_MUF1_PDF91425',
            'MUR1_MUF1_PDF91426',
            'MUR1_MUF1_PDF91427',
            'MUR1_MUF1_PDF91428',
            'MUR1_MUF1_PDF91429',
            'MUR1_MUF1_PDF91430',
            'MUR1_MUF1_PDF91431',
            'MUR1_MUF1_PDF91432',
            'MUR1_MUF1_PDF61100',
            'MUR1_MUF1_PDF61101',
            'MUR1_MUF1_PDF61102',
            'MUR1_MUF1_PDF61103',
            'MUR1_MUF1_PDF61104',
            'MUR1_MUF1_PDF61105',
            'MUR1_MUF1_PDF61106',
            'MUR1_MUF1_PDF61107',
            'MUR1_MUF1_PDF61108',
            'MUR1_MUF1_PDF61109',
            'MUR1_MUF1_PDF61110',
            'MUR1_MUF1_PDF61111',
            'MUR1_MUF1_PDF61112',
            'MUR1_MUF1_PDF61113',
            'MUR1_MUF1_PDF61114',
            'MUR1_MUF1_PDF61115',
            'MUR1_MUF1_PDF61116',
            'MUR1_MUF1_PDF61117',
            'MUR1_MUF1_PDF61118',
            'MUR1_MUF1_PDF61119',
            'MUR1_MUF1_PDF61120',
            'MUR1_MUF1_PDF61121',
            'MUR1_MUF1_PDF61122',
            'MUR1_MUF1_PDF61123',
            'MUR1_MUF1_PDF61124',
            'MUR1_MUF1_PDF61125',
            'MUR1_MUF1_PDF61126',
            'MUR1_MUF1_PDF61127',
            'MUR1_MUF1_PDF61128',
            'MUR1_MUF1_PDF61130',
            'MUR1_MUF1_PDF61131',
            'MUR1_MUF1_PDF61132',
            'MUR1_MUF1_PDF61133',
            'MUR1_MUF1_PDF61134',
            'MUR1_MUF1_PDF61135',
            'MUR1_MUF1_PDF61136',
            'MUR1_MUF1_PDF61137',
            'MUR1_MUF1_PDF61138',
            'MUR1_MUF1_PDF61139',
            'MUR1_MUF1_PDF61140',
            'MUR1_MUF1_PDF61141',
            'MUR1_MUF1_PDF61142',
            'MUR1_MUF1_PDF61143',
            'MUR1_MUF1_PDF61200',
            'MUR1_MUF1_PDF61201',
            'MUR1_MUF1_PDF61202',
            'MUR1_MUF1_PDF61203',
            'MUR1_MUF1_PDF61204',
            'MUR1_MUF1_PDF61205',
            'MUR1_MUF1_PDF61206',
            'MUR1_MUF1_PDF61207',
            'MUR1_MUF1_PDF61208',
            'MUR1_MUF1_PDF61209',
            'MUR1_MUF1_PDF61210',
            'MUR1_MUF1_PDF61211',
            'MUR1_MUF1_PDF61212',
            'MUR1_MUF1_PDF61213',
            'MUR1_MUF1_PDF61214',
            'MUR1_MUF1_PDF61215',
            'MUR1_MUF1_PDF61216',
            'MUR1_MUF1_PDF61217',
            'MUR1_MUF1_PDF61218',
            'MUR1_MUF1_PDF61219',
            'MUR1_MUF1_PDF61220',
            'MUR1_MUF1_PDF61221',
            'MUR1_MUF1_PDF61222',
            'MUR1_MUF1_PDF61223',
            'MUR1_MUF1_PDF61224',
            'MUR1_MUF1_PDF61225',
            'MUR1_MUF1_PDF61226',
            'MUR1_MUF1_PDF61227',
            'MUR1_MUF1_PDF61228',
            'MUR1_MUF1_PDF61230',
            'MUR1_MUF1_PDF61231',
            'MUR1_MUF1_PDF61232',
            'MUR1_MUF1_PDF61233',
            'MUR1_MUF1_PDF61234',
            'MUR1_MUF1_PDF61235',
            'MUR1_MUF1_PDF61236',
            'MUR1_MUF1_PDF61237',
            'MUR1_MUF1_PDF61238',
            'MUR1_MUF1_PDF61239',
            'MUR1_MUF1_PDF61240',
            'MUR1_MUF1_PDF61241',
            'MUR1_MUF1_PDF61242',
            'MUR1_MUF1_PDF61243',
            'MUR1_MUF1_PDF13400',
            'MUR1_MUF1_PDF13401',
            'MUR1_MUF1_PDF13402',
            'MUR1_MUF1_PDF13403',
            'MUR1_MUF1_PDF13404',
            'MUR1_MUF1_PDF13405',
            'MUR1_MUF1_PDF13406',
            'MUR1_MUF1_PDF13407',
            'MUR1_MUF1_PDF13408',
            'MUR1_MUF1_PDF13409',
            'MUR1_MUF1_PDF13410',
            'MUR1_MUF1_PDF13411',
            'MUR1_MUF1_PDF13412',
            'MUR1_MUF1_PDF13413',
            'MUR1_MUF1_PDF13414',
            'MUR1_MUF1_PDF13415',
            'MUR1_MUF1_PDF13416',
            'MUR1_MUF1_PDF13417',
            'MUR1_MUF1_PDF13418',
            'MUR1_MUF1_PDF13419',
            'MUR1_MUF1_PDF13420',
            'MUR1_MUF1_PDF13421',
            'MUR1_MUF1_PDF13422',
            'MUR1_MUF1_PDF13423',
            'MUR1_MUF1_PDF13424',
            'MUR1_MUF1_PDF13425',
            'MUR1_MUF1_PDF13426',
            'MUR1_MUF1_PDF13427',
            'MUR1_MUF1_PDF13428',
            'MUR1_MUF1_PDF13429',
            'MUR1_MUF1_PDF13430',
            'MUR1_MUF1_PDF82000',
            'MUR1_MUF1_PDF82001',
            'MUR1_MUF1_PDF82002',
            'MUR1_MUF1_PDF82003',
            'MUR1_MUF1_PDF82004',
            'MUR1_MUF1_PDF82005',
            'MUR1_MUF1_PDF82006',
            'MUR1_MUF1_PDF82007',
            'MUR1_MUF1_PDF82008',
            'MUR1_MUF1_PDF82009',
            'MUR1_MUF1_PDF82010',
            'MUR1_MUF1_PDF82011',
            'MUR1_MUF1_PDF82012',
            'MUR1_MUF1_PDF82013',
            'MUR1_MUF1_PDF82014',
            'MUR1_MUF1_PDF82015',
            'MUR1_MUF1_PDF82016',
            'MUR1_MUF1_PDF82017',
            'MUR1_MUF1_PDF82018',
            'MUR1_MUF1_PDF82019',
            'MUR1_MUF1_PDF82020',
            'MUR1_MUF1_PDF82021',
            'MUR1_MUF1_PDF82022',
            'MUR1_MUF1_PDF82023',
            'MUR1_MUF1_PDF82024',
            'MUR1_MUF1_PDF82025',
            'MUR1_MUF1_PDF82026',
            'MUR1_MUF1_PDF82027',
            'MUR1_MUF1_PDF82028',
            'MUR1_MUF1_PDF82029',
            'MUR1_MUF1_PDF82030',
            'MUR1_MUF1_PDF82031',
            'MUR1_MUF1_PDF82032',
            'MUR1_MUF1_PDF82033',
            'MUR1_MUF1_PDF82034',
            'MUR1_MUF1_PDF82035',
            'MUR1_MUF1_PDF82036',
            'MUR1_MUF1_PDF82037',
            'MUR1_MUF1_PDF82038',
            'MUR1_MUF1_PDF82039',
            'MUR1_MUF1_PDF82040',
            'MUR1_MUF1_PDF82041',
            'MUR1_MUF1_PDF82042',
            'MUR1_MUF1_PDF82043',
            'MUR1_MUF1_PDF82044',
            'MUR1_MUF1_PDF82045',
            'MUR1_MUF1_PDF82046',
            'MUR1_MUF1_PDF82047',
            'MUR1_MUF1_PDF82048',
            'MUR1_MUF1_PDF82049',
            'MUR1_MUF1_PDF82050',
            'MUR1_MUF1_PDF82051',
            'MUR1_MUF1_PDF82052',
            'MUR1_MUF1_PDF82053',
            'MUR1_MUF1_PDF82054',
            'MUR1_MUF1_PDF82055',
            'MUR1_MUF1_PDF82056',
            'MUR1_MUF1_PDF82057',
            'MUR1_MUF1_PDF82058',
            'MUR1_MUF1_PDF82059',
            'MUR1_MUF1_PDF82060',
            'MUR1_MUF1_PDF82061',
            'MUR1_MUF1_PDF82062',
            'MUR1_MUF1_PDF82063',
            'MUR1_MUF1_PDF82064',
            'MUR1_MUF1_PDF82065',
            'MUR1_MUF1_PDF82066',
            'MUR1_MUF1_PDF82067',
            'MUR1_MUF1_PDF82068',
            'MUR1_MUF1_PDF82069',
            'MUR1_MUF1_PDF82070',
            'MUR1_MUF1_PDF82071',
            'MUR1_MUF1_PDF82072',
            'MUR1_MUF1_PDF82073',
            'MUR1_MUF1_PDF82074',
            'MUR1_MUF1_PDF82075',
            'MUR1_MUF1_PDF82076',
            'MUR1_MUF1_PDF82077',
            'MUR1_MUF1_PDF82078',
            'MUR1_MUF1_PDF82079',
            'MUR1_MUF1_PDF82080',
            'MUR1_MUF1_PDF82081',
            'MUR1_MUF1_PDF82082',
            'MUR1_MUF1_PDF82083',
            'MUR1_MUF1_PDF82084',
            'MUR1_MUF1_PDF82085',
            'MUR1_MUF1_PDF82086',
            'MUR1_MUF1_PDF82087',
            'MUR1_MUF1_PDF82088',
            'MUR1_MUF1_PDF82089',
            'MUR1_MUF1_PDF82090',
            'MUR1_MUF1_PDF82091',
            'MUR1_MUF1_PDF82092',
            'MUR1_MUF1_PDF82093',
            'MUR1_MUF1_PDF82094',
            'MUR1_MUF1_PDF82095',
            'MUR1_MUF1_PDF82096',
            'MUR1_MUF1_PDF82097',
            'MUR1_MUF1_PDF82098',
            'MUR1_MUF1_PDF82099',
            'MUR1_MUF1_PDF82100',
            'MUR1_MUF1_PDF82101',
            'MUR1_MUF1_PDF82102',
            'MUR1_MUF1_PDF82103',
            'MUR1_MUF1_PDF82104',
            'MUR1_MUF1_PDF82105',
            'MUR1_MUF1_PDF82106',
            'MUR1_MUF1_PDF82107',
    )),
)
