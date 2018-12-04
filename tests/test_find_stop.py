"""Tests to find stops."""
import pytest
import pyogt


stops = [
    'abborreberg',
    'abisko-centrum',
    'aby-centrum',
    'agetomta',
    'akerliden',
    'aleryds-sjukhem',
    'alerydsvagen-vastra',
    'algbosatter',
    'alvan',
    'alvastra-vagkors',
    'anders-ljungstedts-gymnasium',
    'angen-gardesrum',
    'anggardsskolan',
    'anggardsvagen',
    'arkosund-3',
    'asby',
    'aselstad',
    'askeby-affar',
    'asks-kyrka',
    'aspeliden',
    'aspnaset-linkoping',
    'aspnasvagen',
    'attetorp',
    'atvidabergs-resecentrum',
    'banergatan',
    'bankekind-affaren',
    'bankekinds-vagkors',
    'barnhemsgatan',
    'berga-centrum',
    'berga-soderleden',
    'bergdalagatan-13',
    'bergdalagatan-5',
    'bergdalsgatan-linkoping',
    'bestorp',
    'bilprovningen-linkoping',
    'bjarka-saby',
    'bjorkbacken-svartinge',
    'bjorkebergs-by',
    'bjorkhult-gammalkil',
    'bjorsaters-kyrka',
    'blasvadret',
    'boet',
    'borensbergs-bussterminal',
    'borggard-station',
    'borggarden',
    'bostallsgatan',
    'boxholms-station',
    'branntorp-horn',
    'braskens-bro',
    'braviken',
    'breviksvagen-61',
    'brokinds-vagkors',
    'brunneby-motala',
    'busstationen-ulrika',
    'busstationen-valdemarsvik',
    'bussterminalen-osterbymo',
    'butbro-vagkors',
    'bygardesgatan',
    'carl-cederstroms-gata',
    'centrum-atvidaberg',
    'cloetta',
    'dackmansgatan',
    'dalamon',
    'dalviksgatan',
    'degeron',
    'djakneparksskolan',
    'djuron',
    'doverstorp',
    'drabantgatan',
    'drottningplan',
    'drottningtorget',
    'duseborgsvagen',
    'egelstorp-tjallmo',
    'ekdalsvagen',
    'eke-ostra-ryd',
    'ekhaga-linkoping',
    'ekholmen-brokindsleden',
    'ekholmens-centrum',
    'ekholmens-vardcentral',
    'ekholmsskolan',
    'eksatter',
    'eksjo-station',
    'ektunavagen',
    'eskadern',
    'evalundsvagen',
    'fagelogatan',
    'fagelsangsvagen',
    'fagelsta-skola',
    'fagottgatan',
    'falerum-buss',
    'fanjunkaregatan',
    'farbacksvagen',
    'farhagsvagen',
    'farmek',
    'farsaxvagen',
    'farullsvagen',
    'finspang-station',
    'fivelstad-kvarn',
    'fivelstad-kyrka',
    'flasbjorke',
    'flistad-brunn',
    'flygvapenmuseum',
    'foi',
    'folkets-park-motala',
    'folkets-park-norrkoping',
    'folkungavallen',
    'fonvindsvagen-ostra',
    'fonvindsvagen-vastra',
    'fornasa',
    'forskningsbyn',
    'forsnas-station',
    'fridvalla',
    'frostorpsgatan',
    'g-janzens-gata',
    'galoppgatan',
    'galstad-lundby',
    'gamla-linkoping',
    'gammalkils-kyrka',
    'gardesgatan-linkoping',
    'garstad',
    'gistad-skiffervagen',
    'godegards-affar',
    'gottlosa',
    'graversfors-2',
    'grebo-affar',
    'grimstorp',
    'gryt',
    'grytgols-centrum',
    'gullringsvagen',
    'gunnarsdal',
    'gusums-centrum',
    'hackefors',
    'hackefors-sodra',
    'hagaskolan',
    'hageby-centrum',
    'haggebo-nykil',
    'hagvagen-berg',
    'halan-vastra',
    'halans-vagkors',
    'hallestad-kyrka',
    'haradstorp',
    'haraldsbo',
    'harnegatans-vandplats',
    'harseby',
    'harstenagatan',
    'hasslegatan',
    'hastholmen',
    'hattorp',
    'havla-affar',
    'heda',
    'hejla',
    'herrbeta-by',
    'herstadberg',
    'hestra',
    'hjulsbro-skola',
    'hockerstad-gard',
    'hoghultsvagen',
    'hoglycke',
    'hogstad',
    'horns-torg',
    'horsalsparken',
    'hultsbruk',
    'humlegatan',
    'huvklintsvagen-lotorp',
    'hycklinge-kvarn',
    'hylingekorset',
    'igelfors-skola',
    'ikea',
    'industrivagen',
    'infanterivagen',
    'isberget',
    'jagarvallsvagen',
    'jakobsdal',
    'jardalavagen-50',
    'johannelunds-centrum',
    'jonsbergs-kyrka',
    'kaga-kyrka',
    'karlslunds-skola',
    'karna-kors',
    'karna-skola',
    'karnabrunnsgatan',
    'kaserngatan',
    'kattinge',
    'kimstad-kyrka',
    'kimstad-station',
    'kisa-station',
    'kiselgatan',
    'klarinettgatan',
    'klockaretorpet',
    'klockrike',
    'klostergatan',
    'konungsund-vgk',
    'kopmansgrand',
    'koppargatan-30',
    'kristinagatan',
    'kristinebergsgatan',
    'kuddby',
    'kulla-kisa',
    'kullborg',
    'kungsgatan-linkoping',
    'kungshogaskolan-mjolby',
    'kvarn-norra',
    'kvarnberget',
    'kvarsebo',
    'kvinnebyvagen-12',
    'kvinnebyvagen-95',
    'lagno-vandplats',
    'landbogatan',
    'landerydsvagen',
    'lansmuseet',
    'lansstyrelsen',
    'lasarettet-entren-motala',
    'ledbergs-vagkors',
    'lektorshagen',
    'lillgardsgatan',
    'lillsjovagen-jursla',
    'lindaliden',
    'linghems-station',
    'linkoping-arena',
    'linkopings-resecentrum',
    'ljunghagsvagen',
    'ljungsbro-busstation',
    'ljusfors-bruk',
    'lofstad-slott',
    'loftgatan',
    'lotgatan',
    'lovbergsvagen-ljunga',
    'lovsbergsvagen-linkoping',
    'luddingsbo',
    'malmenvakten',
    'mantorps-centrum',
    'mariebergs-vardcentral',
    'mariedalsgatan',
    'masshallen',
    'master-mattias-vag',
    'masugnen',
    'medevi',
    'middagsgatan',
    'mjardevi-center',
    'mjardevi-linkoping',
    'mjolby-resecentrum',
    'mogata-kyrka',
    'morgongatan',
    'morkullevagen',
    'motala-central',
    'munkhagsgatan-140',
    'nedre-johannelund',
    'nobymalmsvagen',
    'normstorp',
    'norr-tull',
    'norrledens-vandp',
    'norsholms-centrum',
    'nya-strombron',
    'nykils-kyrka',
    'nykyrka-skola',
    'odegardsgatan-11',
    'odegardsgatan-24',
    'odeshog-torget',
    'orkanvagen',
    'ortagsvagen',
    'ortgatan',
    'ortomta',
    'ostantorp',
    'osterstad-allevagen',
    'ostra-husby-centrum',
    'ostra-ryds-centrum',
    'ostra-stenby-vgk',
    'ovre-johannelund',
    'parkgatan-linkoping',
    'pionjargatan',
    'platinagatan',
    'poleraregatan',
    'prastkop',
    'pumphuset-ljusfallshammar',
    'raberga-bro',
    'radhuset-norrkoping',
    'raknestickan',
    'rambodal',
    'ramfall',
    'rappestad-skola',
    'rattaregatan',
    'regementsgatan-linkoping',
    'rejmyre-vandplats',
    'resedan',
    'rimforsa-riksvag-34',
    'rimforsa-station',
    'ring',
    'ringarums-centrum',
    'ringdansen-c',
    'ringstorp',
    'risbrinksgatan',
    'risinge-kyrka',
    'rokglaset',
    'rosendalstorget',
    'roshagsvagen',
    'rotegatan',
    'roxtuna',
    'runstensgatan',
    'ryd-centrum',
    'rydbergsgatan-rydsnas',
    'rydsvagens-andhallplats',
    'saab-civila-porten',
    'saab-norra-porten',
    'sandgardsgatan',
    'sandviken-krokek',
    'sidvindsvagen',
    'siemens-kontor',
    'simonstorp-station',
    'skaggetorp-centrum',
    'skallviks-kyrka',
    'skanninge-station',
    'skarkind-kyrka',
    'skarkinds-vagkors',
    'skarpa',
    'skeda',
    'skeda-udde',
    'skeda-udde-riksvag-34',
    'skeppstad',
    'skogsfrid-linkoping',
    'skonnarbo-vandplats',
    'slagget',
    'slestadsskolan',
    'smedsby-skola',
    'snovagen',
    'soder-tull',
    'soderkopings-resecentrum',
    'sodra-handelo',
    'sodra-ullstamma',
    'spangerum',
    'spangsholms-bruk',
    'sparvstigen',
    'spiran',
    'sporthallen-motala',
    'st-anna',
    'staby-bro',
    'stationen-vadstena',
    'stationsgatan',
    'stenaldersgatan',
    'stenbacksvagen',
    'stiglotsgatan',
    'stora-aby',
    'stora-torget-linkoping',
    'stora-torget-motala',
    'stormarknaden-norrkoping',
    'stragatan',
    'stralsnas-station',
    'strandangsvagen',
    'stromporten',
    'stromsfors-vagkors',
    'studstorp',
    'sturefors-centrum',
    'sya-station',
    'tallberga',
    'tallboda-centrum',
    'tallboda-skola',
    'tannefors-center',
    'tegelbruksgatan',
    'tegskiftesgatan',
    'teknikhuset',
    'teknikringen',
    'tenndosan',
    'tenngatan-norrkoping',
    'tingstad-by',
    'tinnerbacksbadet',
    'tinnerbacksgrand',
    'tokarps-skola',
    'tolskepps-vagkors',
    'torgvagen-lotorp',
    'tornhagen',
    'torshag',
    'tradgardstorget',
    'tranas-station',
    'trehorna-kyrka',
    'ullstamma-by',
    'universitetet-golfbanan',
    'universitetssjukhuset-norra-entren',
    'universitetssjukhuset-sodra-entren',
    'vaderstad-kyrka',
    'vadstugan',
    'vallaplan',
    'vanga',
    'vardsbergsvagen',
    'vaster-tull',
    'vastra-husby-skola',
    'vaxelgatan',
    'vetegatan-linkoping',
    'vickergatan',
    'vidablick',
    'vijvagen',
    'vikingstad-skola',
    'vikingstad-vagkors',
    'vildmarkshotellet',
    'vimarkagatan',
    'vimmerby-resecentrum',
    'vinkannaren',
    'vistinge',
    'vreta-kloster-skola',
    'vreta-klosters-kyrka',
    'vrinnevisjukhuset',
    'vti',
    'wernersgatan',
    'westmansgatan-66',
    'ycke',
    'yrkesvagen',

]
stops = sorted(set(stops))


@pytest.mark.parametrize('name', stops)
def test_find_stop_by_name(name):
    """Find known stops and check that they exist."""
    stop = pyogt.find_stop(name)
    assert stop.get_name() == name
    assert stop.get_id() != -1


@pytest.mark.parametrize('name', stops)
def test_find_stop_by_id(name):
    """Find known stops and check that they exist."""
    stop = pyogt.find_stop(name)
    id_ = stop.get_id()
    stop = pyogt.find_stop_by_id(id_)
    assert stop.get_name() == name
    assert stop.get_id() == id_
